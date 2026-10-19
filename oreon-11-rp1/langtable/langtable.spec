%global source0_hash 725b94121856a3b76d2345e8596954b82ed1eda78513e55ac55fbe4a4823e66e
Name:           langtable
Version:        0.0.70
Release:        1%{?dist}
Summary:        Guessing reasonable defaults for locale, keyboard layout, territory, and language.
License:        GPL-3.0-or-later
URL:            https://github.com/mike-fabian/langtable
Source0:        https://github.com/mike-fabian/langtable/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-langtable = %{version}-%{release}
# /oreon:deps
%description
langtable is used to guess reasonable defaults for locale, keyboard layout,
territory, and language, if part of that information is already known. For
example, guess the territory and the keyboard layout if the language
is known or guess the language and keyboard layout if the territory is
already known.

%package -n python3-langtable
Summary:        Python module to query the langtable-data
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-data < %{version}-%{release}
Provides:       %{name}-data = %{version}-%{release}
%description -n python3-langtable
This package contains a Python module to query the data
from langtable-data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

perl -pi -e "s,_DATADIR = '(.*)',_DATADIR = '%{_datadir}/langtable'," langtable/langtable.py
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-langtable usr/lib/python3*/site-packages/langtable* usr/lib64/python3*/site-packages/langtable* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/langtable* usr/lib64/python3*/site-packages/langtable* usr/bin/*

%check

%pyproject_check_import
(cd $RPM_BUILD_DIR/%{name}-%{version}/langtable; %{__python3} langtable.py)
(cd $RPM_BUILD_DIR/%{name}-%{version}; %{__python3} test_cases.py)
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/keyboards.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/keyboards.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/languages.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/languages.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/territories.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/territories.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/timezoneidparts.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/timezoneidparts.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/timezones.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/timezones.xml.gz
%files
%files -n python3-langtable -f %{oreon_filedir}/python3-langtable.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.70-1
- Prepare for Oreon 11 (RP1)
