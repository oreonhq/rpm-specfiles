%global source0_hash 827797d8eced3dec1ddb2555506bc412ec22a88d2f0e6fe9db9b889090c807fa
Name:           home-assistant-cli
Version:        1.0.0
Release:        1%{?dist}
Summary:        Command-line tool for Home Assistant
License:        Apache-2.0
URL:            https://github.com/home-assistant/home-assistant-cli
Source0:        https://github.com/home-assistant/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Patch0:          %{url}/pull/403.patch
Patch1:          %{url}/commit/edb0af38fbf1c2533e87745dbb7d75ce3aed6cb5.patch
Patch2:          %{url}/pull/426.patch
Patch3:          %{url}/pull/412.patch
# oreon:deps
BuildRequires:  python3-aiohttp
BuildRequires:  python3-click
BuildRequires:  python3-click-log
BuildRequires:  python3-dateparser
BuildRequires:  python3-devel
BuildRequires:  python3-jsonpath-ng
BuildRequires:  python3-mypy
BuildRequires:  python3-netdisco
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-sugar
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-regex
BuildRequires:  python3-requests-mock
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-tabulate
# /oreon:deps
%description
The Home Assistant Command-line interface (hass-cli) allows one to work with
a local or a remote Home Assistant instance directly from the command-line.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
sed -i "/>=0.3.2,<0.4/d" setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%check

PYTHONPATH=%{buildroot}/%{python3_sitelib}/ pytest-%{python3_version} -v tests \
  -k "not test_commands_loads[template]"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
