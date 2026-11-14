# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9aee407f92c7d51a2ce50f3b78291a9094e334e34bd68e82bf60020795fa2c94
%global pypi_name inotify

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python3-inotify
Version:        0.2.12
Release:        1%{?dist}
Summary:        An adapter to Linux kernel support for inotify
License:        GPL-2.0-only
URL:            https://github.com/dsoprea/PyInotify
Source0:        https://files.pythonhosted.org/packages/f7/e1/9eb0047d6808ab1bb8930ac4d508f663fd94cfaea4bc905f62c199b64872/inotify-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

Requires:       python3

Provides:       python3dist(inotify) = %{version}
Provides:       python-%{pypi_name} = %{version}-%{release}

%description
Python bindings / adapter for the Linux inotify subsystem.

%prep
%oreon_sha256
%autosetup -n inotify-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -q tests

%files -f %{_builddir}/%{name}.files
%license LICENSE
%doc README.md

%changelog
%autochangelog
