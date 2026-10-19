%global source0_hash e176991785a61a1a06810dca96080858b1c0ca965803c42990dec044c8a3a0fb
Name:       distgen
Summary:        Templating system/generator for distributions
Version:    2.4
Release:        1%{?dist}
License:    GPL-2.0-or-later AND Apache-2.0
URL:        https://github.com/devexp-db/distgen
BuildArch:  noarch
Source0:        https://pypi.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-distgen = %{version}-%{release}
# /oreon:deps
%description
Based on given template specification (configuration for template), template
file and preexisting distribution metadata generate output file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest tests/unittests/
%files

%changelog

%autochangelog
