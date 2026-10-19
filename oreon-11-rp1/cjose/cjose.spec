%global source0_hash 2de8652b23ee3e15398176e8b2aaa513aa89635368f2748fbc304f8aefe910a4
Name:           cjose
Version:        0.6.2.2
Release:        10%{?dist}
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)
License:        MIT
URL:            https://github.com/OpenIDC/cjose
Source0:        https://github.com/OpenIDC/cjose/releases/download/v%{version}/cjose-%{version}.tar.gz
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Implementation of JOSE for C/C++

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure
%make_build
%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles cjose-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check || (cat test/test-suite.log; exit 1)
%files -f %{oreon_filedir}/main.list
%files -n cjose-devel -f %{oreon_filedir}/cjose-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2.2-10
- Prepare for Oreon 11 (RP1)
