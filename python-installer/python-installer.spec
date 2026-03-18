Name:           python-installer
Version:        0.7.0
Release:        14%{?dist}
Summary:        A library for installing Python wheels

# SPDX
License:        MIT
URL:            https://github.com/pypa/installer
Source:         %{pypi_source installer}

# Fix the build with Python 3.13 - merged upstream
# https://github.com/pypa/installer/commit/b23f89b10cf5
Patch:          Fix-removed-importlib.resources.read_binary-in-Pytho.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3-pytest

%global _description %{expand:
This is a low-level library for installing a Python package from
a wheel distribution. It provides basic functionality and abstractions
for handling wheels and installing packages from wheels.}


%description %_description

%package -n     python3-installer
Summary:        %{summary}

%description -n python3-installer %_description


%prep
%autosetup -p1 -n installer-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files installer


%check
%pyproject_check_import
%pytest


%files -n python3-installer -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTING.md README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-14
- Prepare for Oreon 11 (RP1)
