%global source0_hash 90a24f8d46574513b3d334b473e128c456e7eddaec6e3dd198d7e5ad69ddc12f
Summary:        Linux scheduler python bindings
Name: python-schedutils
Version: 0.6
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://rt.wiki.kernel.org/index.php/Tuna
Source0:        https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-schedutils
Summary: %summary
%{?python_provide:%python_provide python3-schedutils}
%description -n python3-schedutils

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-schedutils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-schedutils -f %{oreon_filedir}/python3-schedutils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-30
- Prepare for Oreon 11 (RP1)
