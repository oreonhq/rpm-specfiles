# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b6991bc77fe8fe7322a0dee7ff45ec6ed562fcee773e74e1f009f17e1766dc2f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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

%if 0%{?fedora} >= 41 || 0%{?rhel}
ExcludeArch: %{ix86}
%endif

%define debug_package %{nil}

%description
Cockpit component for managing software updates for ostree based systems.

%prep
%oreon_verify_sources
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
