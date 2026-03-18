Name:       iso-codes
Summary:    ISO code lists and translations
Version:    4.20.1
Release:    3%{?dist}
License:    LGPL-2.1-or-later
URL:        https://salsa.debian.org/iso-codes-team/iso-codes
Source0:    https://salsa.debian.org/iso-codes-team/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: gettext
BuildRequires: python3
BuildRequires: meson
BuildArch: noarch

# for /usr/share/xml
Requires: xml-common

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
%autosetup -n %{name}-v%{version}

# The '&' character is not getting parsed using xmllint
# Change it to "and" word
sed -i 's/ & / and /g' data/iso_3166-2.json

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%license LICENSES/LGPL-2.1-or-later.txt
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml
%{_datadir}/iso-codes

%files devel
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.20.1-3
- Prepare for Oreon 11 (RP1)
