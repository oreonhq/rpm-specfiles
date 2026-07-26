%global source0_hash 3c4fd64f453e8f40cf862420a70da95a71b6487ace75e8e0cf85d73707db6065

%global pypi_name ephem

Name:           python-%{pypi_name}
Version:        4.2
Release:        7%{?dist}
Summary:        Compute positions of the planets and stars

License:        MIT
URL:            http://rhodesmill.org/pyephem/
Source0:        %{pypi_source}
# Build libastro with -Wl,-Bsymbolic, to prevent symbol collision with range from netcdf
# https://stackoverflow.com/questions/6538501/linking-two-shared-libraries-with-some-of-the-same-symbols
Patch0:         ephem_bsymbolic.patch

BuildRequires:  gcc

%description
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{pypi_name}
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy application.

%package -n python-%{pypi_name}-doc
Summary:        The %{pypi_name} documentation
BuildArch:      noarch
BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 ephem/doc html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
cd %{buildroot}%{python3_sitearch}/%{pypi_name}
# One test has an AttributeError
# test_constellation is temporarily disabled because ephem is not compatible with
# Python 3.10 yet.
# For more info see: https://bugzilla.redhat.com/show_bug.cgi?id=1891793
%pytest -v tests -k "not JPLTest and not test_github_25 and not test_constellation"
# Remove left-overs from the tests
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}/{.benchmarks,.hypothesis,.pytest_cache}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
