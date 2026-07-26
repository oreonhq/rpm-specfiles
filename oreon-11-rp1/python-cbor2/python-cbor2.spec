%global source0_hash b682820677ee1dbba45f7da11898d2720f92e06be36acec290867d5ebf3d7e09

%global pypi_name cbor2

Name:           python-%{pypi_name}
Version:        5.6.5
Release:        7%{?dist}
Summary:        Python CBOR (de)serializer with extensive tag support

License:        MIT
URL:            https://github.com/agronholm/cbor2
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 7049) serialization format.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 7049) serialization format.

%package -n python-%{pypi_name}-doc
Summary:        cbor2 documentation
BuildArch:      noarch
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)

%description -n python-%{pypi_name}-doc
Documentation for cbor2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{python3_sitearch}/_%{pypi_name}%{python3_ext_suffix}
%{_bindir}/%{pypi_name}

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
%autochangelog
