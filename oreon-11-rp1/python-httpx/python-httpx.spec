# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 61fe412dd34b6d95197feb9dbfb6a6e2c749197b67287b2f75925ec257bb41ae
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond tests 0
%else
%bcond tests 1
%endif

Name:           python-httpx
Version:        0.28.1
Release:        %{autorelease}
Summary:        Next-generation HTTP client for Python

License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
Source0:        %{url}/archive/%{version}/httpx-%{version}.tar.gz
Patch:          %{url}/pull/3773.patch
BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist chardet}
BuildRequires:  %{py3_dist cryptography}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist trustme}
BuildRequires:  %{py3_dist uvicorn}
BuildRequires:  %{py3_dist zstandard}
%endif
BuildRequires:  help2man

%global _description %{expand:
HTTPX is a fully featured HTTP client library for Python 3. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2, and
provides both sync and async APIs.}

%description %{_description}

%package -n     python3-httpx
Summary:        %{summary}

%description -n python3-httpx %{_description}
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%pyproject_extras_subpkg -n python3-httpx brotli http2 socks

%pyproject_extras_subpkg -n python3-httpx cli
%{_bindir}/httpx
%{_mandir}/man1/httpx.1*

%prep
%oreon_sha256
%autosetup -n httpx-%{version} -p1
sed -i 's/rich>=10,<14/rich>=10/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x brotli,cli,http2,socks

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l httpx
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    PATH="${PATH-}:%{buildroot}%{_bindir}" \
    PYTHONDONTWRITEBYTECODE=1 \
    help2man --no-info --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/httpx.1' httpx

%check
%pyproject_check_import
%if %{with tests}
k="${k-}${k+ and }not client"
k="${k-}${k+ and }not test_api"
k="${k-}${k+ and }not test_config"
k="${k-}${k+ and }not test_exceptions"
k="${k-}${k+ and }not test_main"
k="${k-}${k+ and }not test_timeouts"
k="${k-}${k+ and }not test_utils"
%pytest -m 'not network' -k "${k-}" -v
%endif

%files -n python3-httpx -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
