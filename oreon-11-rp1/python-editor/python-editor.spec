%global source0_hash 61a4758919668b8ffe5eb389a86a4c2e8c2f789c02b9c6aee0ddf3c4ebfe3fd3

%global pypi_name python-editor

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-editor
Version:        1.0.4
Release:        27%{?dist}
Summary:        Programmatically open an editor, capture the result

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/fmoo/python-editor
Source:         https://github.com/fmoo/python-editor/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Programmatically open an editor, capture the result.

%package -n python3-editor
Summary:        Programmatically open an editor, capture the result.
%{?python_provide:%python_provide python3-editor}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-editor
Programmatically open an editor, capture the result.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{upstream_version}
rm -rf %{pypi_name}.egg-info
# Change shebang according to Python version
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' editor.py

%build
%py3_build

%install
%py3_install
chmod a+x $RPM_BUILD_ROOT%{python3_sitelib}/editor.py

%files -n python3-editor
%doc README.md
%license LICENSE
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/editor.py*
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog
