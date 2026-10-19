%global source0_hash 7a053dbc7dea1fdc3c13e6bcc2dc19b4c74786174196742db7c449e965cdb856
Name: numad
Version: 0.5
Release:        1%{?dist}
Summary:        NUMA user daemon
License: LGPL-2.1-only
URL: https://pagure.io/numad
%global numad_commit ff1507f
Source0:        https://deb.debian.org/debian/pool/main/n/numad/numad_0.5+20251104.orig.tar.xz#/numad-0.5git.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Numad, a daemon for NUMA (Non-Uniform Memory Architecture) systems,
that monitors NUMA characteristics and manages placement of processes
and memory to minimize memory latency and thus provide optimum performance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir numad-0.5+20251104
%oreon_prep
%build

%make_build CFLAGS="$CFLAGS"
%install
install -D -p -m 644 {,%{buildroot}%{_unitdir}/}numad.service
install -D -p -m 644 {,%{buildroot}%{_sysconfdir}/logrotate.d/%{name}/}numad.logrotate
%make_install prefix=%{buildroot}/usr
%oreon_autofiles main

%post

%systemd_post numad.service
%preun

%systemd_preun numad.service
%postun

%systemd_postun numad.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5-50.20251104git
- Import
