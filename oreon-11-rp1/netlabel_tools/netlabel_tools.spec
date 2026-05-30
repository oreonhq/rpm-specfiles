%global source0_hash 6192e9715b45b34136f90e7505d4416028e32aa296e12f72f9d7245bcb9e1d59

Summary: Tools to manage the Linux NetLabel subsystem
Name: netlabel_tools
Version: 0.30.0
Release: 22%{?dist}
License: GPL-2.0-only
URL: https://github.com/netlabel/netlabel_tools
Source:        https://github.com/netlabel/netlabel_tools/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0: rhbz1683434.patch

Requires: libnl3
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires:  gcc
BuildRequires: kernel-headers
BuildRequires: libnl3-devel
BuildRequires: doxygen
BuildRequires: systemd

%description
NetLabel is a kernel subsystem which implements explicit packet labeling
protocols such as CIPSO for Linux.  Packet labeling is used in secure networks
to mark packets with the security attributes of the data they contain.  This
package provides the necessary user space tools to query and configure the
kernel subsystem.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1

%build
%configure
make V=1 %{?_smp_mflags}

%install
rm -rf "%{buildroot}"
mkdir -p "%{buildroot}/etc"
mkdir -p "%{buildroot}/%{_sbindir}"
mkdir -p "%{buildroot}/%{_unitdir}"
mkdir -p "%{buildroot}/%{_mandir}"
make V=1 DESTDIR="%{buildroot}" install

# NOTE: disable since the tests require messing with the running kernel
#%check
#make V=1 check

%preun
%systemd_preun netlabel.service

%postun
%systemd_postun netlabel.service

%post
%systemd_post netlabel.service

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README
%doc CHANGELOG
%doc SUBMITTING_PATCHES
%attr(0644,root,root) %{_mandir}/man8/*
%attr(0755,root,root) %{_sbindir}/netlabelctl
%attr(0755,root,root) %{_sbindir}/netlabel-config
%attr(0644,root,root) %{_unitdir}/netlabel.service
%attr(0644,root,root) %config(noreplace) /etc/netlabel.rules

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30.0-22
- Prepare for Oreon 11 (RP1)
