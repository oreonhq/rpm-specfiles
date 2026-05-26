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

Source: https://github.com/cockpit-project/%{name}/releases/download/%{version}/cockpit-ostree-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 b6991bc77fe8fe7322a0dee7ff45ec6ed562fcee773e74e1f009f17e1766dc2f
%global source0_file cockpit-ostree-222.tar.xz
# oreon url source checksums end

%if 0%{?fedora} >= 41 || 0%{?rhel}
ExcludeArch: %{ix86}
%endif

%define debug_package %{nil}

%description
Cockpit component for managing software updates for ostree based systems.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cockpit-ostree-222.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b6991bc77fe8fe7322a0dee7ff45ec6ed562fcee773e74e1f009f17e1766dc2f" || { echo "oreon: Source0 SHA256 mismatch for cockpit-ostree-222.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
