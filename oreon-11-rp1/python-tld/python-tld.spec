%global source0_hash 2328b2153b521abfd228793ff45b58717e1e4683880e7825f41eee21fe459164

%global pypi_name tld
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.13.2
Release:        1%{?dist}
Summary:        Extract the top level domain from the URL given

License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later
URL:            https://github.com/barseghyanartur/tld
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Extract the top level domain (TLD) from the URL given. List of TLD names is
taken from Mozilla.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with network}
BuildRequires: python3-coverage
BuildRequires: python3-factory-boy
BuildRequires: python3-faker
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-runner
BuildRequires: python3-tox
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Extract the top level domain (TLD) from the URL given. List of TLD names is
taken from Mozilla.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n %{name}-doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Upstream removed this file, but their tox configuration still references it.
touch requirements/testing.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with network}
%check
# Don't test the CLI part
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v --pyargs tld.tests \
 -k "not test_1_update_tld_names_command and not test_1_update_tld_names_mozilla_command and not test_18_update_tld_names_cli" 
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst CREDITS.rst README.rst
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt LICENSE_MPL_1.1.txt
%{_bindir}/update-tld-names
%exclude %{python3_sitelib}/%{pypi_name}/tests/

%files -n %{name}-doc
%doc html
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt LICENSE_MPL_1.1.txt

%changelog
%autochangelog
