%global source0_hash 0df60157b052f0e774ade8a8bac59d6e8d4b464058cc55f9208d72e41156811f
Name:           liboauth
Version:        1.0.3
Release:        1%{?dist}
Summary:        OAuth library functions
License:        MIT
URL:            http://liboauth.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%if 0%{?el5}
%endif
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nss-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liboauth-devel -f %{oreon_filedir}/liboauth-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-28
- Import
