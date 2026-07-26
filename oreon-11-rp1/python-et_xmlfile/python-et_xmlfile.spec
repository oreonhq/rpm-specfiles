%global source0_hash b710736febf4b4589805f1cc0ccea41781353fc4550466c472649f8518bed4b5

%global pypi_name et_xmlfile
%global sum An implementation of lxml.xmlfile for the standard library
%global desc et_xmlfile is a low memory library for creating large XML files.\
\
It is based upon the xmlfile module from lxml with the aim of allowing code to\
be developed that will work with both libraries. It was developed initially for\
the openpyxl project but is now a standalone module.

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        7%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://foss.heptapod.net/openpyxl/et_xmlfile/-/archive/2.0.0/et_xmlfile-2.0.0.tar.gz
Patch:          Differentiate-assertion-based-on-Python-version.patch

BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist lxml
Requires:       %py3_dist lxml

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst doc/
%license LICENCE.rst

%changelog
%autochangelog
