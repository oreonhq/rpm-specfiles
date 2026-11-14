# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f288924cae4e29463698d6d60bc6a4da69c89185ad1e0bcc4104f584e960b9ed
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-requests
Version: 2.34.2
Release: 1%{?dist}
Summary: Python HTTP for Humans.
License: Apache-2.0
URL: https://pypi.org/project/requests/
Source0: https://files.pythonhosted.org/packages/ac/c3/e2a2b89f2d3e2179abd6d00ebd70bff6273f37fb3e0cc209f48b39d00cbf/requests-2.34.2.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-charset-normalizer
BuildRequires: python3-idna
BuildRequires: python3-urllib3
BuildRequires: python3-certifi
Requires: python3
Requires: python3-charset-normalizer
Requires: python3-idna
Requires: python3-urllib3
Requires: python3-certifi

%description
Python HTTP for Humans.

%prep
%oreon_sha256
%autosetup -n requests-2.34.2

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import requests'

%files -f %{_builddir}/%{name}.files
