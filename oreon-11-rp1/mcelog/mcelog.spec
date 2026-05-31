%global source0_hash ed25a39bb20178e79e18cc5d3202b198868986ec3e964b6285f6a7bac8469fdf

Summary:	Tool to translate x86-64 CPU Machine Check Exception data
Name:		mcelog
Version:	175
Release:	14%{?dist}
Epoch:		3
License:	GPL-2.0-only
URL:		https://github.com/andikleen/mcelog
Source0:        https://github.com/andikleen/mcelog/archive/v175/mcelog-175.tar.gz
# note that this source OVERRIDES the one on the tarball above!
Source1:	mcelog.conf
ExclusiveArch:	i686 x86_64
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires:  gcc
BuildRequires: systemd

%description
mcelog is a utility that collects and decodes Machine Check Exception data
on x86-32 and x86-64 systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -fpie -pie"

%install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man{5,8}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog/triggers
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -p -m755 mcelog $RPM_BUILD_ROOT/%{_sbindir}/mcelog
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog/mcelog.conf
install -p -m755 triggers/cache-error-trigger $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog/triggers/cache-error-trigger
install -p -m755 triggers/dimm-error-trigger $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog/triggers/dimm-error-trigger
install -p -m755 triggers/page-error-trigger $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog/triggers/page-error-trigger
install -p -m755 triggers/socket-memory-error-trigger $RPM_BUILD_ROOT/%{_sysconfdir}/mcelog/triggers/socket-memory-error-trigger
install -p -m644 mcelog.service $RPM_BUILD_ROOT%{_unitdir}/mcelog.service
install -p -m644 mcelog*.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install -p -m644 mcelog*.5 $RPM_BUILD_ROOT/%{_mandir}/man5/

%post
%systemd_post mcelog.service

%preun
%systemd_preun mcelog.service

%postun
%systemd_postun_with_restart mcelog.service

%files
%{_sbindir}/mcelog
%dir %{_sysconfdir}/mcelog
%{_sysconfdir}/mcelog/triggers
%config(noreplace) %{_sysconfdir}/mcelog/mcelog.conf
%{_unitdir}/mcelog.service
%{_mandir}/*/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3:175-14
- Import
