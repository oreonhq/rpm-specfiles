%global source0_hash cf0e3cf56142039133628b5acffe8ef0c12bc902d2aadd3e0fe5878dc08d1050

%global pypi_name openpyxl
%global sum Python library to read/write Excel 2010 xlsx/xlsm files
%global desc openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.\
\
It was born from lack of existing library to read/write natively from Python the\
Office Open XML format.

Name:           python-%{pypi_name}
Version:        3.1.5
Release:        5%{?dist}
Summary:        %{sum}

# Automatically converted from old format: MIT and Python - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Python
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source

BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
Requires:       python3dist(numpy)

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

# No tests

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS.rst
%license LICENCE.rst

%changelog
%autochangelog
