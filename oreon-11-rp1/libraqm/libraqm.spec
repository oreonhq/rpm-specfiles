%global source0_hash 3d0add115f7d4a9410d3377462ed3c05e86342193ef984183e4380e3787b2d4c
Name:           libraqm
Version:        0.11.0
Release:        1%{?dist}
License:        MIT
Summary:        Complex text layout library
URL:            https://github.com/HOST-Oman/libraqm
Source0:        https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.xz
# oreon:deps
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  harfbuzz-devel
BuildRequires:  meson
# /oreon:deps
%description
Library that encapsulates the logic for complex text layout and provides a
convenient API.

%package devel
Summary:        Development files for libraqm
Requires:       libraqm%{?_isa} = %{version}-%{release}
%description devel
Development files for libraqm.

%package docs
Summary:        Documentation for libraqm
BuildArch:      noarch
%description docs
Documentation for libraqm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir raqm-%{version}
%oreon_prep
%build

%meson -Ddocs=true
%meson_build
%check

export LC_ALL=C.UTF-8
%meson_test
%install
%meson_install
rm -f %{buildroot}%{_libdir}/*.{la,a}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libraqm-devel -f %{oreon_filedir}/libraqm-devel.list
%files -n libraqm-docs -f %{oreon_filedir}/libraqm-docs.list

%changelog

%autochangelog
