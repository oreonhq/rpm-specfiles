%global source0_hash none
Name:           wsl-setup
Version:        1.0.1
Release:        1%{?dist}
Summary:        Windows Subsystem for Linux setup script and configuration
License:        MIT
URL:            https://src.fedoraproject.org/rpms/wsl-setup
BuildArch:      noarch
Source1:        LICENSE
Source2:        wsl.conf
Source3:        wsl-distribution.conf
Source4:        wsl-oobe.sh
Source5:        firstboot-override.conf
Source6:        wsl-setup-tmpfiles.conf
Source7:        wsl-setup-user-tmpfiles.conf
Source8:        wsl-setup
Requires:       system-logos
Requires:       shadow-utils
Requires:       systemd
# oreon:deps
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Provides WSL specific configuration files and first-time setup script.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

%install
install -pm 0644 %{SOURCE1} LICENSE
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/ %{SOURCE2}
install -Dpm0644 -T %{SOURCE3} %{buildroot}%{_datarootdir}/wsl-setup/wsl-distribution.conf.template
install -Dpm0755 -T %{SOURCE4} %{buildroot}%{_libexecdir}/wsl/oobe.sh
install -Dpm0755 -T %{SOURCE8} %{buildroot}%{_bindir}/wsl-setup
ln -s ..%{_prefix}/lib/wsl-distribution.conf %{buildroot}%{_sysconfdir}/wsl-distribution.conf
install -Dpm0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dpm0644 %{SOURCE7} %{buildroot}%{_user_tmpfilesdir}/%{name}.conf
install -Dpm0644 %{SOURCE5} %{buildroot}%{_unitdir}/systemd-firstboot.service.d/override.conf
%oreon_autofiles main

%post

%{_bindir}/wsl-setup
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-1
- Prepare for Oreon 11 (RP1)
