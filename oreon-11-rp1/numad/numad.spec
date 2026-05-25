Name: numad
Version: 0.5
Release: 50.20251104git%{?dist}
Summary: NUMA user daemon

License: LGPL-2.1-only
URL: https://pagure.io/numad
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#   git clone https://pagure.io/numad.git numad-0.5git
#   tar --exclude-vcs -cJf numad-0.5git.tar.xz numad-0.5git/
Source0: %{name}-%{version}git.tar.xz

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-rpm-macros

%description
Numad, a daemon for NUMA (Non-Uniform Memory Architecture) systems,
that monitors NUMA characteristics and manages placement of processes
and memory to minimize memory latency and thus provide optimum performance.

%prep
%autosetup -n %{name}-%{version}git

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
