%global source0_hash 1f6fcd61b696608faaff92c7c14f70995de26b6c45c4463485ffb8105c902750
Name:           python-xlrd2
Version:        1.3.4
Release:        1%{?dist}
Summary:        Library to extract data from Microsoft Excel legacy spreadsheet files (xls)
License:        Apache-2.0 AND BSD-3-Clause AND BSD-Advertising-Acknowledgement
URL:            https://github.com/DissectMalware/xlrd2
Source0:        https://github.com/DissectMalware/xlrd2/releases/download/v%{version}/xlrd2-%{version}.tar.gz
Patch1:         https://patch-diff.githubusercontent.com/raw/python-excel/xlrd/pull/375.patch#/python-xlrd2-01-defusedxmliter.patch
Patch2:         https://github.com/DissectMalware/xlrd2/pull/14.patch#/python-xlrd2-02-rename.patch
BuildArch:      noarch
%global pypi_name xlrd2
%{!?pytest: %global pytest pytest-3}
%global common_description %{expand:
The xlrd2 module is an effort to extend [xlrd project]( which is no longer
maintained by its developers). The main goal is to make it suitable for
extracting necessary information from malicious xls documents.
**Xlrd Purpose**: Provide a library for developers to use to extract data
from Microsoft Excel (tm) spreadsheet files.
It is not an end-user tool.
}
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description %common_description

%package -n     python%{python3_pkgversion}-xlrd2
Summary:        Library to extract data from Microsoft Excel legacy spreadsheet files (xls)
%description -n python%{python3_pkgversion}-xlrd2 %common_description
%py_provides    python3-xlrd2

%package -n python-xlrd2-doc
Summary:        The documentation for python module xlrd2
%description -n python-xlrd2-doc
The Documentation for the python module xlrd2
%common_description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n xlrd2-%{version}
# Remove bundled egg-info
rm -rf .egg-info

# Fix CRLF ends of lines
echo "=== Fixing CRLF ends of lines for all text files"
find ./ -type f '!' '(' -name '*.xls' -o -name '*.xlsx' ')' -print -exec sed '-i' '-e' 's/\r$//' '{}' ';'

%build

%py3_build
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles python-xlrd2-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -sv -k "not test_names_demo"
%files -f %{oreon_filedir}/main.list
%files -n python3-xlrd2 -f %{oreon_filedir}/python3-xlrd2.list
%files -n python-xlrd2-doc -f %{oreon_filedir}/python-xlrd2-doc.list

%changelog

%autochangelog
