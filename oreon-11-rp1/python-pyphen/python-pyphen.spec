%global source0_hash 1ef18f4adb1f4592d87c0074d6816452aa52472aa496535b2112de04f7858eee

%global srcname Pyphen
%global modname pyphen

Name:           python-pyphen
Version:        0.18.1
Release:        1%{?dist}
Summary:        Pure Python module to hyphenate text
# Automatically converted from old format: GPLv2+ or LGPLv2+ or MPLv1.1 - review is highly recommended.
License:        GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR LicenseRef-Callaway-MPLv1.1
URL:            https://github.com/Kozea/Pyphen
Source0:        https://github.com/Kozea/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch1:         %{name}-strip-optional-dependencies.patch

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros

%description
Pyphen is a pure Python module to hyphenate text using existing
hyphenation dictionaries, e.g., from Libreoffice language packs.

%package -n python3-pyphen
Summary:        Pure Python module to hyphenate text

%description -n python3-pyphen
Pyphen is a pure Python module to hyphenate text using existing
hyphenation dictionaries, e.g., from Libreoffice language packs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-pyphen
%license LICENSE COPYING.GPL COPYING.LGPL COPYING.MPL
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}.dist-info/

%changelog
%autochangelog
