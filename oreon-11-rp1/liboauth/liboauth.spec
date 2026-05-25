Name:           liboauth
Version:        1.0.3
Release:        28%{?dist}
Summary:        OAuth library functions

License:        MIT
URL:            http://liboauth.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%if 0%{?el5}
%endif

BuildRequires:  gcc
BuildRequires:  curl-devel nss-devel
BuildRequires: make
#Requires:       

%description
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%if 0%{?el5}
Requires:       pkgconfig curl-devel nss-devel
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-nss
make %{?_smp_mflags}


%install
%if 0%{?el5}
rm -rf $RPM_BUILD_ROOT
%endif
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc AUTHORS COPYING.MIT README 
%{_libdir}/*.so.*

%files devel
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oauth.pc
%{_mandir}/man3/oauth.*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-28
- Import
