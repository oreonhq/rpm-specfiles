%global source0_hash d1f2d8b5edec827fd386c22d6f9151377ec7c194dca4d293e3abad9df9974209
Name:           libsfdo
Version:        0.1.3
Release:        1%{?dist}
Summary:        A collection of libraries implementing freedesktop.org specifications
License:        BSD-2-Clause
URL:            https://gitlab.freedesktop.org/vyivel/libsfdo
Source0:        https://gitlab.freedesktop.org/vyivel/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libsfdo-devel -f %{oreon_filedir}/libsfdo-devel.list

%changelog

%autochangelog
