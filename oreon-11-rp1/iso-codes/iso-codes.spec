%global source0_hash 2d7d9f6084ab9ce6c534ce71a3dd5144b6e474f3c97616459a88f73f44a64bff
Name:       iso-codes
Summary:        ISO code lists and translations
Version:    4.20.1
Release:        1%{?dist}
License:    LGPL-2.1-or-later
URL:        https://salsa.debian.org/iso-codes-team/iso-codes
Source0:        https://salsa.debian.org/iso-codes-team/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch: noarch
Requires: xml-common
# oreon:deps
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  python3
# /oreon:deps
%description
This package provides the ISO 639 Language code list, the ISO 4217
Currency code list, the ISO 3166 Territory code list, and ISO 3166-2
sub-territory lists, and all their translations in gettext format.

%package devel
Summary: Files for development using %{name}
Requires: %{name} = %{version}-%{release}
%description devel
This package contains the pkg-config files for development
when building programs that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-v%{version}

# The '&' character is not getting parsed using xmllint
# Change it to "and" word
sed -i 's/ & / and /g' data/iso_3166-2.json

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%find_lang %{name} --all-name
%files -f %{oreon_filedir}/main.list
%files -n iso-codes-devel -f %{oreon_filedir}/iso-codes-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.20.1-3
- Prepare for Oreon 11 (RP1)
