%global source0_hash 90a24f8d46574513b3d334b473e128c456e7eddaec6e3dd198d7e5ad69ddc12f

Summary: Linux scheduler python bindings
Name: python-schedutils
Version: 0.6
Release: 30%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://rt.wiki.kernel.org/index.php/Tuna
Source:        https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: gcc


%global _description\
Python interface for the Linux scheduler sched_{get,set}{affinity,scheduler}\
functions and friends.

%description %_description

%package -n python3-schedutils
Summary: %summary
%{?python_provide:%python_provide python3-schedutils}

%description -n python3-schedutils %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files -n python3-schedutils
%license COPYING
%{_bindir}/pchrt
%{_bindir}/ptaskset
%{_mandir}/man1/pchrt.1*
%{_mandir}/man1/ptaskset.1*
%{python3_sitearch}/schedutils*.so
%{python3_sitearch}/*.egg-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-30
- Prepare for Oreon 11 (RP1)
