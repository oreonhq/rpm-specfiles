%global source0_hash 0c0e96974250008c28ce854c2e0bad7ef75690c9c50f2c4ffeafb2f1ce4876b7

%global pypi_name textfsm

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python module for parsing semi-structured text into python tables

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/textfsm
Source0:        https://github.com/google/textfsm/archive/v%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2291946
# with apologies to the Sex Pistols, drop 'future' dep from setup.py
# because it's never used
# not upstreamed because upstream has a *much* larger fix pending for
# 2.0.0: https://github.com/google/textfsm/pull/121
Patch:          textfsm-1.1.3-no-future.patch
BuildArch:      noarch

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest
Requires:       python3-six

%description -n python3-%{pypi_name}
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Fix version in __init__.py, this was fixed in the repo in
# https://github.com/google/textfsm/commit/ca3755dcb8b1b043857d63f1d1352d62030f0d2d
 # (post-1.1.3 release)
sed -i 's/1.1.2/1.1.3/' textfsm/__init__.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license COPYING
%exclude %{python3_sitelib}/testdata
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/textfsm

%changelog
%autochangelog
