%global source0_hash 9661817a61ab212cea229c6d36b5305cae01a904afce3f88730780335a2e008e

%global srcname virtualenv-clone

Name:             python-virtualenv-clone
Version:          0.5.7
Release:          18%{?dist}
Summary:          Script to clone Python virtual environments

License:          MIT
URL:              https://github.com/edwardgeorge/virtualenv-clone
# Use GitHub source archive rather than the one on PyPI since the latter omits
# the tests/ directory and tox.ini file.
Source0:          %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Allow the current Python version in tests
# Extend the hardcoded list of Python versions with sys.version_info
Patch:            https://github.com/edwardgeorge/virtualenv-clone/pull/76.patch

BuildArch:        noarch
BuildRequires:    python3-devel

%global _description %{expand:
A script for cloning a non-relocatable Python virtual environment.

Virtualenv provides a way to make a virtual environment relocatable which could
then be copied as we wanted. However, making a virtualenv relocatable this way
breaks the no-site-packages isolation of the virtualenv as well as other
aspects that come with relative paths and '/usr/bin/env' shebangs that may be
undesirable. Also, the '.pth' and '.egg-link' rewriting doesn't seem to work as
intended.

Virtualenv-clone attempts to overcome these issues and provide a way to easily
clone an existing virtualenv.}

%description %_description

%package -n python3-virtualenv-clone
Summary:          %{summary}
Requires:         python3-virtualenv

%description -n python3-virtualenv-clone %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files clonevirtualenv

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/virtualenv-clone

%changelog
%autochangelog
