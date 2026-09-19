%global source0_hash 59fdeba1eb81af63ed2414d27e2ea38c973d6a4c0240b2f827692063ed5c5762

Name:           python-pyxlsb2
Version:        0.0.9
%global         baserelease     0.10
Summary:        Excel 2007+ Binary Workbook (xlsb) parser

# Project is released with the Apache-2.0 license
# it is based on original project pyxlsb released with MIT license
License:        Apache-2.0 AND MIT
URL:            https://github.com/DissectMalware/pyxlsb2
BuildArch:      noarch

# with release - build from official release, otherwise build from git
%bcond_with     release

# macro pytest is not defined on rhel7
%{!?pytest: %global pytest pytest-3}

%global _description %{expand:
pyxlsb2 (a variant of pyxlsb - is an Excel 2007+ Binary Workbook (xlsb) parser
written in Python. The pyxslb2 offers the following improvements/changes in
comparison to pyxlsb:
1. By default, keeps all data in memory instead of
creating temporary files. This is mainly to speed up the processing and also
not changing the local filesystem during the processing.
2. relies on both "xl\\workbook.bin" and "xl\_rels\workbook.bin.rels" to load
locate boundsheets. As a result, it can load all worksheets as well as all
macrosheets.
3. it extracts macro formulas:
- accurately shows the formulas
- supports A1 addressing
- supports external addressing (partially implemented))
4. extracts defined names such as auto_open
}

%global         gituser         DissectMalware
%global         gitname         pyxlsb2
%global         commit          0a1ff1be329aa282ecbc347ff44fc6c07351685b
%global         gitdate         20220509
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

%if %{with release}
Release:        %{baserelease}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/releases/download/%{gitname}_%{pkgver}/%{gitname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        %{baserelease}.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz#/%{name}-%{version}-%{gitdate}-%{shortcommit}.tar.gz
%endif
# Maintainers, please upstream
Patch0:         python-pyxlsb2-rm-python-mock-usage.diff

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

# Needed for the %%check
BuildRequires:  python%{python3_pkgversion}-pytest

%description %_description

%package -n     python%{python3_pkgversion}-pyxlsb2

Summary:        %{summary}
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-pyxlsb2 }
%else
%py_provides    python3-pyxlsb2
%endif

%description -n python%{python3_pkgversion}-pyxlsb2 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with release}
%autosetup -n pyxlsb2-%{version} -p1
%else
%autosetup -n pyxlsb2-%{commit} -p1
%endif
# Remove bundled egg-info
rm -rf pyxlsb2.egg-info

%build
%py3_build

%install
%py3_install

%check
# Known to be failing 20231026 - test_stringify, test_sheets, test_rows
FAILING="not test_stringify and not test_sheets and not test_rows"
# Failing on s390x platform
FAILING="$FAILING and not test_read_string and not test_read_string_u and not test_get_string"

%pytest -sv -k "$FAILING"

%files -n python%{python3_pkgversion}-pyxlsb2
%license LICENSE LICENSE_pyxlsb
%doc README.rst
%{python3_sitelib}/pyxlsb2
%{python3_sitelib}/pyxlsb2-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
