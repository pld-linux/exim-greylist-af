Summary:	Greylisting for Exim
Summary(pl):	Obs³uga "szarych list" dla Exima
Name:		exim-greylist-af
Version:	0.02
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://andrew-ford.com/exim/%{name}-%{version}.tar.gz
Patch0:		%{name}-dlopen.patch
URL:		http://andrew-ford.com/exim/
BuildRequires:	exim-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
Requires:	exim >= 2:4.52-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Greylisting for exim.

%description -l pl
Obs³uga "szarych list" dla Exima.

%prep
%setup -q
%patch0 -p1

%build
rm -f local_scan.h
%{__cc} -Wall -DDLOPEN_LOCAL_SCAN=1 %{rpmcflags} %{rpmldflags} -fPIC \
        -I%{_includedir}/exim -I%{_includedir}/mysql -I%{_includedir}/openssl \
        -lmysqlclient -lcrypto \
        -shared local_scan.c -o %{name}.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/mail,%{_libdir}/exim}

install %{name}.so $RPM_BUILD_ROOT%{_libdir}/exim/%{name}.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc greylisting-localscan.txt *.sql
%attr(755,root,root) %{_libdir}/exim/%{name}.so
