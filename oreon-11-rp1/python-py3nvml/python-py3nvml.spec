%global source0_hash 55cdd578973b1cad706bf28dc18c40902dae35acefea49d89f94a3053f5c3dec

%global pypi_name py3nvml

Name:           python-%{pypi_name}
Version:        0.2.7
Release:        17%{?dist}
Summary:        Python 3 Bindings for the NVIDIA Management Library

License:        BSD-3-Clause
URL:            https://github.com/fbcotter/py3nvml
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description \
Python 3 compatible bindings to the NVIDIA Management Library. Can be used to \
query the state of the GPUs on your system.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(xmltodict)
%description -n python3-%{pypi_name} %{_description}

%package -n     python3-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python3-%{pypi_name}-doc %{_description}

This package contains the documentation for %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/py3smi

%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
