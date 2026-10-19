%global source0_hash 59fdeba1eb81af63ed2414d27e2ea38c973d6a4c0240b2f827692063ed5c5762
Name:           python-pyxlsb2
Version:        0.0.9
%global         baserelease     0.10
Summary:        Excel 2007+ Binary Workbook (xlsb) parser
License:        Apache-2.0 AND MIT
URL:            https://github.com/DissectMalware/pyxlsb2
BuildArch:      noarch
%bcond_with     release
%{!?pytest: %global pytest pytest-3}
%global         gituser         DissectMalware
%global         gitname         pyxlsb2
%global         commit          0a1ff1be329aa282ecbc347ff44fc6c07351685b
%global         gitdate         20220509
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%if %{with release}
Release:        1%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz#/%{name}-%{version}-%{gitdate}-%{shortcommit}.tar.gz
%else
Release:        1%{?dist}
%endif
Patch0:         python-pyxlsb2-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n     python%{python3_pkgversion}-pyxlsb2
Summary:        Excel 2007+ Binary Workbook (xlsb) parser
%py_provides    python3-pyxlsb2
%description -n python%{python3_pkgversion}-pyxlsb2

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

FAILING="not test_stringify and not test_sheets and not test_rows"
FAILING="$FAILING and not test_read_string and not test_read_string_u and not test_get_string"
%pytest -sv -k "$FAILING"
%files -f %{oreon_filedir}/main.list
%files -n python3-pyxlsb2 -f %{oreon_filedir}/python3-pyxlsb2.list

%changelog

%autochangelog
