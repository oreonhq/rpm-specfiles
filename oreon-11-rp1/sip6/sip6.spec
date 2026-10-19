%global source0_hash 4ead2ace2f48cd82f2c1c5aeb7a8d9b643371ce3a009a8e77a4aeca45c9f344f
%global pypi_name sip
Name:           sip6
Version:        6.16.1
Release:        1%{?dist}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip6
License:        BSD-2-Clause
URL:            https://github.com/Python-SIP/sip
Source0:        https://github.com/Python-SIP/sip/archive/refs/tags/6.16.1.tar.gz#/sip-6.15.1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(sip) < 7
BuildRequires:  python3dist(sip) >= 6
Requires:       python3-sip6 = %{version}-%{release}
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version} -p 1

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
