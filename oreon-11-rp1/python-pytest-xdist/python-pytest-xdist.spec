%global source0_hash 7e578125ec9bc6050861aa93f2d59f1d8d085595d6551c2c90b6f4fad8d3a9f1
%global pypi_name pytest_xdist

Name:           python-pytest-xdist
Version:        3.8.0
Release:        %autorelease
Summary:        pytest plugin for distributed testing and loop-on-failing modes

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch:          44f4bea.patch
Patch:          0c98447.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:	python3dist(execnet) >= 2.1
BuildRequires:	python3dist(setproctitle)
BuildRequires:	python3dist(tox-current-env) >= 0.0.16

%global _description %{expand:
The pytest-xdist plugin extends pytest with new test execution modes,
the most used being distributing tests across multiple CPUs
to speed up test execution:

    pytest -n auto

With this call, pytest will spawn a number of workers processes equal
to the number of available CPUs, and distribute the tests randomly across them.}

%description %_description

%package -n     python3-pytest-xdist
Summary:        %{summary}

%description -n python3-pytest-xdist %_description

%pyproject_extras_subpkg -n python3-pytest-xdist psutil setproctitle

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires -t -x testing -x psutil -x setproctitle

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l xdist

%check
%tox

%files -n python3-pytest-xdist -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
