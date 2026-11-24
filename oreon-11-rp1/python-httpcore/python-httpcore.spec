# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash eb542a99b37a2d6307dcbbd8b3da3b798ef9c20e82ce2e976d8ec7444cd0472c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name httpcore

%if 0%{?oreon}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           python-%{pypi_name}
Version:        1.0.9
Release:        %{autorelease}
Summary:        Minimal low-level HTTP client

License:        BSD-3-Clause
URL:            https://github.com/encode/httpcore
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-trio
BuildRequires:  python3-pytest-httpbin
%endif

%description -n python3-%{pypi_name}
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%pyproject_extras_subpkg -n python3-httpcore http2,socks,trio,asyncio

%prep
%oreon_sha256
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x http2,socks,trio,asyncio

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%if %{with tests}
%pytest -Wdefault
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
