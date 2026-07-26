%global source0_hash aac1bff39aea88e45aea3bcaf2425a2f75e30308dfa173aa96c97f2c433ac845

%global         sum Spreadsheet python library
%global         commit 98ab3e962ef31c04bba684c82888354eafb243a5
%global         git_tag 1.3.0
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-xlwt
Version:        1.3.0
Release:        19%{?dist}
Summary:        %{sum}

                # Utils.py is LPGL2.0+
# Automatically converted from old format: LGPLv2+ and BSD and BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising
URL:            http://pypi.python.org/pypi/xlwt
                # See also https://github.com/python-excel/xlwt
Source0:        https://github.com/python-excel/xlwt/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement
is Python 2.6 or later.

%package -n python3-xlwt
Summary:      %{sum}
              # https://github.com/python-excel/xlwt/issues/73
Provides:     bundled(antlr) = 2.7.7
%{?python_provide:%python_provide python3-xlwt}

%description -n python3-xlwt
A library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement
is Python 2.6 or later.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n xlwt-%{commit}
sed -i "s|tests/python.bmp|python.bmp|g" tests/test_bitmaps.py

%build
%py3_build

%check
cd tests
PYTHONPATH=.. %{__python3} -m unittest discover

%install
%py3_install
mkdir tmp_docs
cp -ar examples docs tmp_docs

%files -n python3-xlwt
%license docs/licenses.rst
%doc README.rst tmp_docs/*
%{python3_sitelib}/xlwt
%{python3_sitelib}/*.egg-info

%changelog
%autochangelog
