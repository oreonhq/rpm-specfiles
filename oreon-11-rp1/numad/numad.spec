%global source0_hash none

Name: numad
Version: 0.5
Release: 50.20251104git%{?dist}
Summary: NUMA user daemon

License: LGPL-2.1-only
URL: https://pagure.io/numad
%global numad_commit ff1507f
Source0:        https://deb.debian.org/debian/pool/main/n/numad/numad_0.5+20251104.orig.tar.xz#/numad-0.5git.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-rpm-macros

%description
Numad, a daemon for NUMA (Non-Uniform Memory Architecture) systems,
that monitors NUMA characteristics and manages placement of processes
and memory to minimize memory latency and thus provide optimum performance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n numad-0.5+20251104

%build
%make_build CFLAGS="$CFLAGS"

%install
install -D -p -m 644 {,%{buildroot}%{_unitdir}/}numad.service
install -D -p -m 644 {,%{buildroot}%{_sysconfdir}/logrotate.d/%{name}/}numad.logrotate
%make_install prefix=%{buildroot}/usr

%files
%config(noreplace) %{_sysconfdir}/logrotate.d/numad
%{_bindir}/numad
%{_mandir}/man8/numad.8.*
%{_unitdir}/numad.service

%post
%systemd_post numad.service

%preun
%systemd_preun numad.service

%postun
%systemd_postun numad.service

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5-50.20251104git
- Import
