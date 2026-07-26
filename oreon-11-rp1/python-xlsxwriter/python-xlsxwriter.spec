%global source0_hash 254b1c37a368c444eac6e2f867405cc9e461b0ed97a3233b2ac1e574efb4140c

%global pypi_name xlsxwriter
%global src_name XlsxWriter

Name:		python-%{pypi_name}
Version:	3.2.9
Release:	2%{?dist}
Summary:	Python module for writing files in the Excel 2007+ XLSX file format
License:	BSD-2-Clause
URL:		https://pypi.python.org/pypi/XlsxWriter
Source0:	https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

%global common_desc\
XlsxWriter is a Python module for writing files in the Excel 2007+\
XLSX file format.\
\
XlsxWriter can be used to write text, numbers, formulas and hyperlinks\
to multiple worksheets and it supports features such as formatting and\
many more, including:\
\
	100% compatible Excel XLSX files.\
	Full formatting.\
	Merged cells.\
	Defined names.\
	Charts.\
	Autofilters.\
	Data validation and drop down lists.\
	Conditional formatting.\
	Worksheet PNG/JPEG images.\
	Rich multi-format strings.\
	Cell comments.\
	Integration with Pandas.\
	Textboxes.\
	Memory optimization mode for writing large files.\
\
It supports Python 2.7, 3.4+, Jython and PyPy and uses standard libraries only.

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:		Python 3 modules for writing files in the Excel 2007+ XLSX file format
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/vba_extract.py

%changelog
%autochangelog
