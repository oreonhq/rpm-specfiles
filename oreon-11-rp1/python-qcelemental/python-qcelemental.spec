%global source0_hash 3571b9bc6c67faba8ea9d988948fd8efc593bf3b5d533486f84ee2e423d60c1e

# Whether to run the tests; disabled till the tests are ported to pydantic v2
%bcond tests 0

Name:           python-qcelemental
Version:        0.29.0
Release:        7%{?dist}
Summary:        Periodic table, physical constants, and molecule parsing for quantum chemistry
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/MolSSI/QCElemental
Source0:        https://github.com/MolSSI/QCElemental/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
BuildRequires:  python3-pint
BuildRequires:  python3-pydantic
BuildRequires:  python3-networkx

%description
QCElemental is a resource module for quantum chemistry containing
physical constants and periodic table data from NIST and molecule
handlers.

Periodic Table and Physical Constants data are pulled from NIST srd144
and srd121, respectively (details) in a renewable manner (class around
NIST-published JSON file).

This project also contains a generator, validator, and translator for
Molecule QCSchema.

%package -n     python3-qcelemental
Summary:        %{summary}
%{?python_provide:%python_provide python3-qcelemental}
# For some reason, these dependencies aren't picked up automatically
Requires: python3-numpy
Requires: python3-pint
Requires: python3-pydantic
Requires: python3-networkx

%description -n python3-qcelemental
QCElemental is a resource module for quantum chemistry containing
physical constants and periodic table data from NIST and molecule
handlers.

Periodic Table and Physical Constants data are pulled from NIST srd144
and srd121, respectively (details) in a renewable manner (class around
NIST-published JSON file).

This project also contains a generator, validator, and translator for
Molecule QCSchema.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n QCElemental-%{version}
# Remove bundled egg-info
rm -rf QCElemental.*-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
%pytest qcelemental
%endif

%files -n python3-qcelemental
%license LICENSE
%doc README.md
%{python3_sitelib}/qcelemental
%{python3_sitelib}/qcelemental-%{version}.dist-info

%changelog
%autochangelog
