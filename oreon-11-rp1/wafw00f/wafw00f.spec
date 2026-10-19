%global source0_hash e4a784b5c6f0632d129146e0a6a769495044e6faa7ab8b498d1f6d5b14744479
Name:           wafw00f
Version:        2.3.2
Release:        2%{?dist}
Summary:        Tool to identifies and fingerprints Web Application Firewall (WAF)
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sandrogauci/wafw00f
Source0:        https://github.com/sandrogauci/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wafw00f = %{version}-%{release}
# /oreon:deps
%description
WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' {wafw00f/*.py,wafw00f/*/*.py}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
