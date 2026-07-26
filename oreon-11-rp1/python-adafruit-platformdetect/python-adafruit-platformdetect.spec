%global source0_hash 485fce8671db80443954fc47767a042284aeeab48d93e2125846febf7d22f21f

%global pypi_name adafruit-platformdetect

Name:           python-%{pypi_name}
Version:        3.81.0
Release:        %autorelease

Summary:        Platform detection module

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PlatformDetect
Source0:        %{pypi_source adafruit_platformdetect}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)

%global _description %{expand:
This library provides best-guess platform detection for a range of
single-board computers and (potentially) other platforms.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        Documentation for adafruit-platformdetect

BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for adafruit-platformdetect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n adafruit_platformdetect-%{version}

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%pyproject_save_files adafruit_platformdetect

%ifarch %{arm} %{arm64}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
