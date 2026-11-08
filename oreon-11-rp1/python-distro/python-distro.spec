# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6ede051357868ed427ea71d16fc27f4d63cc0d9c8a32788aa11c450ecefcc76f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global pypi_name distro

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        1%{?dist}
Summary:        Linux Distribution - a Linux OS platform information API

License:        Apache-2.0
URL:            https://github.com/python-distro/distro
Source0:        https://github.com/python-distro/distro/archive/v%{version}/distro-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  oreon-rpm-macros
 
%global _description \
The distro (for: Linux Distribution) package provides information about the\
Linux distribution it runs on, such as a reliable machine-readable ID, or\
version information.\
\
It is a renewed alternative implementation for Python's original\
platform.linux_distribution function, but it also provides much more\
functionality. An alternative implementation became necessary because\
Python 3.5 deprecated this function, and Python 3.7 is expected to remove it\
altogether. Its predecessor function platform.dist was already deprecated since\
Python 2.6 and is also expected to be removed in Python 3.7. Still, there are\
many cases in which access to that information is needed. See Python issue 1322\
for more information.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Suggests:       /usr/bin/lsb_release

%description -n python3-%{pypi_name} %{_description}

%prep
%oreon_sha256

%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc CHANGELOG.md CONTRIBUTORS.md README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%{_bindir}/distro

%check
%pytest

