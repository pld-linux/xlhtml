Summary:	Excel 95/97 and PowerPoint to html converter
Summary(pl):	Konwerter z Excela 95/97 oraz PowerPointa do HTML
Name:		xlhtml
Version:	0.5.1
Release:	2
License:	GPL
Group:		Applications/Text
Vendor:		Steve Grubb <linux_4ever@yahoo.com>
Source0:	http://chicago.sf.net/%{name}/%{name}.%{version}.tgz
URL:		http://chicago.sourceforge.net/xlhtml/
# project is continued at link above
#URL:		http://www.xlhtml.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Provides:	xlHtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xlHtml program will take an Excel 95, or 97 file as input and
convert it to html. The output is via standard out so it can be
re-directed to files or piped to filters or used as a gateway to the
internet. pptHtml program converts PowerPoint files to HTML.

%description -l pl
Program xlHtml przyjmuje na wej¶cie pliki Excela 95 lub 97 i
konwertuje je do HTML, wyrzucaj±c na standardowe wyj¶cie - które mo¿e
byæ przekierowane do innego filtru. Program pptHtml konwertuje pliki
PowerPointa do HTML.

%package devel
Summary:	Excel 95/97 to html converter development resources
Summary(pl):	Zasoby programistyczne xlHtml
Group:		Applications/Text
Requires:	%{name} = %{version}
Provides:	xlHtml-devel

%description devel
Excel 95/97 to html converter development resources.

%description devel -l pl
Zasoby programistyczne konwertera Excela 95/97 do HTML.

%package static
Summary:	Excel 95/97 to html converter static libraries
Summary(pl):	Statyczne biblioteki xlHtml
Group:		Applications/Text
Requires:	%{name}-devel = %{version}
Provides:	xlHtml-static

%description static
Excel 95/97 to html converter static libraries.

%description static -l pl
Statyczne biblioteki konwertera Excela 95/97 do HTML.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
aclocal
%{__autoconf}
rm -f missing
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	coleaclocaldir=%{_aclocaldir}

#install cole-config $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install xlhtml/xlhtml.1 ppthtml/ppthtml.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf xlhtml/{README,THANKS,TODO,ChangeLog}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xlHtml/contrib xlHtml/{README,THANKS,TODO}.gz
%attr(755,root,root) %{_bindir}/nsopen
%attr(755,root,root) %{_bindir}/nsxlview
%attr(755,root,root) %{_bindir}/nspptview
%attr(755,root,root) %{_bindir}/xlhtml
%attr(755,root,root) %{_bindir}/ppthtml
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc xlHtml/ChangeLog.gz
#%attr(755,root,root) %{_bindir}/cole-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/cole
%{_aclocaldir}/cole.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
