%global source0_hash e7a1b695f037f87e309856c6678d8ee74d20ba3f1e4d2c1311b9982d612ba725
Name:		tuptime
Version:	5.2.6
Release:        1%{?dist}
Summary:        Report historical system real time
License:	GPL-2.0-or-later
BuildArch:	noarch
URL:		https://github.com/rfmoz/tuptime/
Source0:        https://github.com/rfmoz/tuptime/archive/%{version}.tar.gz
%{?systemd_requires}
%if 0%{?python3_pkgversion}
%else
%endif
Requires:	systemd
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Tuptime track and report historical and statistical real time of the
system, keeping the uptime and downtime between shutdowns.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix python shebang
%py3_shebang_fix src/tuptime

%build

%install
install -d %{buildroot}%{_bindir}/
install -d %{buildroot}%{_unitdir}/
install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_sharedstatedir}/tuptime/
install -d %{buildroot}%{_sysusersdir}/
cp src/tuptime %{buildroot}%{_bindir}/
cp src/systemd/tuptime.service %{buildroot}%{_unitdir}/
cp src/systemd/tuptime-sync.service %{buildroot}%{_unitdir}/
cp src/systemd/tuptime-sync.timer %{buildroot}%{_unitdir}/
cp src/systemd/sysusers.d/tuptime.conf %{buildroot}%{_sysusersdir}/
cp src/man/tuptime.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%post

%systemd_post tuptime.service
%systemd_post tuptime-sync.service
%systemd_post tuptime-sync.timer
%preun

%systemd_preun tuptime.service
%systemd_preun tuptime-sync.service
%systemd_preun tuptime-sync.timer
%postun

%systemd_postun_with_restart tuptime.service
%systemd_postun_with_restart tuptime-sync.service
%systemd_postun_with_restart tuptime-sync.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
