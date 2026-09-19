%global source0_hash fbd7e759541ac725c29c506612003de393249b94310ea78ae44cb1d04b220095

%global pypi_name pydyf

Name:           python-pydyf
Version:        0.12.1
Release:        2%{?dist}
Summary:        Low-level PDF creator
# The test suite is released under the AGPL but we are not shipping any test
# code in the "binary" (noarch) RPM so we can just use the 3-clause BSD.
License:        BSD-3-Clause
URL:            https://www.courtbouillon.org/pydyf
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# used as "build-backend" in pyproject.toml but not detected by Fedora's
# macros to generate build requirements
BuildRequires:  python3dist(flit-core)
# test suite calls the "gs" binary to verify outputs, not detectable by
# Fedora's macros
BuildRequires:  ghostscript

%description
pydyf is a low-level PDF generator written in Python and based on PDF
specification 1.7.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
pydyf is a low-level PDF generator written in Python and based on PDF
specification 1.7.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n  python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
