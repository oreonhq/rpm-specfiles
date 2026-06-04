%global source0_hash 0f48bb1e255bfa3379d9ab06cc675454c47480fbb2f2e59897faa2b43b631fff

%global libdnf_version 0.62.0

Name:           microdnf
Version:        3.10.1
Release:        4%{?dist}
Summary:        Lightweight implementation of DNF in C

License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/microdnf
Source0:        https://github.com/rpm-software-management/microdnf/archive/refs/tags/3.10.1.tar.gz#/microdnf-3.10.1.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.20.0
BuildRequires:  (pkgconfig(libdnf) >= %{libdnf_version} with pkgconfig(libdnf) < 5)
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  help2man

Requires:       libdnf%{?_isa} >= %{libdnf_version}
%if 0%{?rhel} > 8 || 0%{?fedora}
# Ensure DNF package manager configuration skeleton is installed
Requires:       /etc/dnf/dnf.conf
%endif

%description
Micro DNF is a lightweight C implementation of DNF, designed to be used
for doing simple packaging actions when you don't need full-blown DNF and
you want the tiniest useful environments possible.

That is, you don't want any interpreter stack and you want the most
minimal environment possible so you can build up to exactly what you need.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_mandir}/man8/microdnf.8*
%{_bindir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.1-4
- Prepare for Oreon 11 (RP1)
