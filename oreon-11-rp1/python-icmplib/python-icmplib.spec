%global source0_hash 4bb59ab4ed202b2139f3e9e6d8d62baa9bdca0f185ba648c5a08304a9d958fb6
Name:           python-icmplib
Version:        3.0.4
Release:        1%{?dist}
Summary:        An implementation of the ICMP protocol in Python
License:        LGPL-3.0-or-later
URL:            https://github.com/ValentinBELYN/icmplib
Source0:        https://github.com/ValentinBELYN/icmplib/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-icmplib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-icmplib
Summary:        An implementation of the ICMP protocol in Python
%description -n python3-icmplib

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir icmplib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-icmplib usr/lib/python3*/site-packages/icmplib* usr/lib64/python3*/site-packages/icmplib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/icmplib* usr/lib64/python3*/site-packages/icmplib* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-icmplib -f %{oreon_filedir}/python3-icmplib.list

%changelog

%autochangelog
