%global source0_hash 0e7b7094a02550dd80b7243bcffc3671550b0f1d8ba625e4dff52517827d5d23
%global debug_package %{nil}
Name:           tllist
Version:        1.1.0
Release:        8%{?dist}
Summary:        C header file only implementation of a typed linked list
License:        MIT
URL:            https://codeberg.org/dnkl/%{name}
Source0:        https://codeberg.org/dnkl/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n tllist-devel -f %{oreon_filedir}/tllist-devel.list

%changelog

%autochangelog
