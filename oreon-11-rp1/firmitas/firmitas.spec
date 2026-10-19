%global source0_hash 912569a3152d90b0fa7cfc091cd6cc66dc62296ac9c6685e2a9151f38d397462
Name:           firmitas
Version:        0.1.4
Release:        1%{?dist}
Summary:        Simple notification service for X.509-standard TLS certificate statuses
License:        GPL-3.0-or-later
Url:            https://gitlab.com/t0xic0der/firmitas
Source0:        https://files.pythonhosted.org/packages/source/f/firmitas/firmitas-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-firmitas = %{version}-%{release}
# /oreon:deps
%description
Simple notification service for X.509-standard TLS certificate statuses

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
