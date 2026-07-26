%global source0_hash 7384d2bd30e55e8929c7ad113fa7b83c5aa8aef86116e9359e680178c587e75a

Name: libcdson
Version: 1.0.0
Release: 10%{?dist}
Summary: Pure C parsing/serialization for the DSON data format, for humans
License: MPL-2.0
URL: https://github.com/frozencemetery/cdson
Source0: https://github.com/frozencemetery/cdson/releases/download/v%{version}/cdson-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: git
BuildRequires: meson

Patch0001: 0001-tests-fix-build-on-legacy-32-bit-machines.patch
Patch0002: 0002-build-version-the-shared-objects.patch

%global desc \
A pure C parsing and serialization library for the DSON data serialization \
format, for humans. cdson is believed to have complete spec coverage, though \
as with any project, there may still be bugs. \
%{nil}
%description %{desc}

%package devel
Summary: Development headers for libcdson
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am -n cdson-%{version}

%build
CFLAGS="%{build_cflags} -Wno-error=unused-result"
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
%autochangelog
