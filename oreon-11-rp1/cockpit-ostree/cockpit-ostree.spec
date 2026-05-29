%global source0_hash b6991bc77fe8fe7322a0dee7ff45ec6ed562fcee773e74e1f009f17e1766dc2f

Name: cockpit-ostree
Epoch: 1
Version: 222
Release: 1%{?dist}
BuildArch: noarch
Summary: Cockpit user interface for rpm-ostree
License: LGPL-2.1-or-later
BuildRequires: make
Requires: cockpit-bridge >= 125
Requires: cockpit-system >= 125
Requires: rpm-ostree

Source:        https://github.com/cockpit-project/cockpit-ostree/releases/download/222/cockpit-ostree-222.tar.xz

%if 0%{?fedora} >= 41 || 0%{?rhel}
ExcludeArch: %{ix86}
%endif

%define debug_package %{nil}

%description
Cockpit component for managing software updates for ostree based systems.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -n cockpit-ostree

%install
%make_install PREFIX=/usr

%files
%doc README.md
%license LICENSE dist/ostree.js.LEGAL.txt
%{_datadir}/cockpit/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 222-1
- Prepare for Oreon 11 (RP1)
