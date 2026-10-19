%global source0_hash 66fd881f6c68171a1940a73b02a7b687f80e6621dc66a2a3c14fc699b05c92a0
%global forgeurl https://gitlab.freedesktop.org/cangjie/libcangjie
%global archiveext tar.xz
Name:             libcangjie
Summary:        Cangjie Input Method Library
Version:          1.4.0
Release:        1%{?dist}
License:          LGPL-3.0-or-later
URL:              http://cangjians.github.io/projects/%{name}
Source0:        %{forgeurl}/-/archive/v%{version}/%{name}-%{version}.%{archiveext}
Requires:         %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Library implementing the Cangjie input method.

%package data
Summary:          Database for %{name}
BuildArch:        noarch
%description data
Database for %{name}.

%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{_isa} = %{version}-%{release}
Requires:         sqlite-devel
%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f '{}' \;
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libcangjie-data -f %{oreon_filedir}/libcangjie-data.list
%files -n libcangjie-devel -f %{oreon_filedir}/libcangjie-devel.list

%changelog

%autochangelog
