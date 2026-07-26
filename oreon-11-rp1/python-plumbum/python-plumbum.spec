%global source0_hash f8cbf0ecec0b73ff4e349398b65112a9e3f9300e7dc019001217dcc148d5c97c

%global pypi_name plumbum

Name:           python-%{pypi_name}
Version:        1.10.0
Release:        3%{?dist}
Summary:        Shell combinators library

License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source0:        %{pypi_source}
# Upstream, but not released: https://github.com/tomerfiliba/plumbum/issues/761.
Patch0:         0001-fix-test-on-prerelease-of-3.15.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Needed for tests:
BuildRequires:  openssh-clients
BuildRequires:  procps-ng
BuildRequires:  python-unversioned-command
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-timeout)

%global _description %{expand:
Ever wished the wrist-handiness of shell scripts be put into a real programming
language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead,
which was used to create pipes back in the day) is a small yet feature-rich
library for shell script-like programs in Python. The motto of the library is
"Never write shell scripts again", and thus it attempts to mimic the shell
syntax ("shell combinators") where it makes sense, while keeping it all
pythonic and cross-platform.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        Shell combinators library

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l plumbum

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc LICENSE README.rst

%changelog
%autochangelog
