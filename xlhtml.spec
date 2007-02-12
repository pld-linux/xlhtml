Summary:	Excel 95/97 and PowerPoint to HTML converter
Summary(pl.UTF-8):	Konwerter z Excela 95/97 oraz PowerPointa do HTML
Name:		xlhtml
Version:	0.5.1
Release:	5
License:	GPL
Group:		Applications/Text
#Source0:	http://dl.sourceforge.net/chicago/%{name}.%{version}.tgz
Source0:	%{name}.%{version}.tgz
# Source0-md5:	deeb108545e1848fce5dcb8d84d8a48e
Patch0:		%{name}-shared.patch
Patch1:		%{name}-colors.patch
URL:		http://chicago.sourceforge.net/xlhtml/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	xlHtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xlhtml program will take an Excel 95, or 97 file as input and
convert it to HTML. The output is via standard out so it can be
re-directed to files or piped to filters or used as a gateway to the
internet. pptHtml program converts PowerPoint files to HTML.

%description -l pl.UTF-8
Program xlhtml przyjmuje na wejście pliki Excela 95 lub 97 i
konwertuje je do HTML, wyrzucając na standardowe wyjście - które może
być przekierowane do innego filtru. Program pptHtml konwertuje pliki
PowerPointa do HTML.

%package devel
Summary:	Excel 95/97 to HTML converter development resources
Summary(pl.UTF-8):	Zasoby programistyczne xlhtml
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
Obsoletes:	xlHtml-devel

%description devel
Excel 95/97 to HTML converter development resources.

%description devel -l pl.UTF-8
Zasoby programistyczne konwertera Excela 95/97 do HTML.

%package static
Summary:	Excel 95/97 to HTML converter static libraries
Summary(pl.UTF-8):	Statyczne biblioteki xlhtml
Group:		Applications/Text
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	xlHtml-static

%description static
Excel 95/97 to HTML converter static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki konwertera Excela 95/97 do HTML.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install cole/cole-config $RPM_BUILD_ROOT%{_bindir}

#install -d $RPM_BUILD_ROOT%{_mandir}/man1
#install xlhtml/xlhtml.1 ppthtml/ppthtml.1 $RPM_BUILD_ROOT%{_mandir}/man1

rm -rf xlhtml/contrib/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xlhtml/contrib xlhtml/{README,THANKS,TODO}
%attr(755,root,root) %{_bindir}/nsopen
%attr(755,root,root) %{_bindir}/nsxlview
%attr(755,root,root) %{_bindir}/nspptview
%attr(755,root,root) %{_bindir}/xlhtml
%attr(755,root,root) %{_bindir}/ppthtml
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc xlhtml/ChangeLog
%attr(755,root,root) %{_bindir}/cole-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cole

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
