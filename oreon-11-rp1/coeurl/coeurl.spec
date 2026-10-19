%global source0_hash 84c1d76116bd118ee2c3a1c7913e2f2f7b20fff34628d09bd86eb349bfdaf1a7
%bcond check 1
Name: coeurl
Version: 0.3.2
Release:        1%{?dist}
License: MIT
URL: https://nheko.im/nheko-reborn/%{name}
Summary:        Simple async wrapper around CURL for C++
Source0:        https://nheko.im/nheko-reborn/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libevent-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openssl
BuildRequires:  python3dist(flask)
BuildRequires:  spdlog-devel
# /oreon:deps
%description
Simple library to do http requests asynchronously via CURL in C++.

Based on the CURL-libevent example.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson \
    -Dwerror=false \
%if %{with check}
    -Dtests=true \
%else
    -Dtests=false \
%endif
    -Dexamples=false
%meson_build
%install
%meson_install
%oreon_autofiles coeurl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

scripts/run_testserver.sh &
scripts/run_tls_testserver.sh &
sleep 5
%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n coeurl-devel -f %{oreon_filedir}/coeurl-devel.list

%changelog

%autochangelog
