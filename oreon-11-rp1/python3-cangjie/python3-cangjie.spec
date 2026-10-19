%global source0_hash 07f1e3f5ffe176a824da7f4885860eb51008a1512baaa5acd80e7d841e2d26d8
%global module_name cangjie
%global forgeurl https://gitlab.freedesktop.org/cangjie/pycangjie
%global archiveext tar.xz
Name:             python3-%{module_name}
Summary:        Python bindings to libcangjie
Version:          1.5.0
Release:        1%{?dist}
%forgemeta
License:          LGPL-3.0-only
URL:              https://gitlab.freedesktop.org/cangjie/pycangjie
Source0:        %{forgeurl}/-/archive/%{version}/py%{module_name}-%{version}.%{archiveext}
%forgemeta
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcangjie-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
# /oreon:deps
%description
Python bindings to libcangjie, the library implementing Cangjie and Quick
input methods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pycangjie-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f '{}' \;
%oreon_autofiles main

%check

export CANGJIE_DB=/usr/share/libcangjie/cangjie.db
%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
