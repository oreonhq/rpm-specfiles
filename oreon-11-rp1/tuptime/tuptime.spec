%global source0_hash a4dfeac8221688be1452273458d69075c83a2ecad0dc8a27f973e8456737ec48

Name:		tuptime
Version:	5.2.5
Release:	2%{?dist}
Summary:	Report historical system real time

License:	GPL-2.0-or-later
BuildArch:	noarch
URL:		https://github.com/rfmoz/tuptime/
Source0:	https://github.com/rfmoz/tuptime/archive/%{version}.tar.gz

%{?systemd_requires}
# Check for EPEL Python (python34, python36)
%if 0%{?python3_pkgversion}
BuildRequires:	python%{python3_pkgversion}-devel
%else
BuildRequires:	python3-devel
%endif
BuildRequires:	systemd-rpm-macros
Requires:	systemd

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

%files
%{_unitdir}/tuptime.service
%{_unitdir}/tuptime-sync.service
%{_unitdir}/tuptime-sync.timer
%{_sysusersdir}/tuptime.conf
%attr(0755, root, root) %{_bindir}/tuptime
%dir %attr(0755, _tuptime, _tuptime) %{_sharedstatedir}/tuptime/
%doc tuptime-manual.txt
%doc CHANGELOG README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/tuptime.1.*

%changelog
%autochangelog
