%global source0_hash 7f53cf55a007570c9de5a1c4f946ca7372fad5e057c8b1c9d7afc2176cc32cd3
Name: btrbk
Version: 0.32.7
Release:        1%{?dist}
Summary:        Tool for creating snapshots and remote backups of btrfs sub-volumes
License: GPL-3.0-or-later
URL: https://digint.ch/btrbk/
Source0:        https://digint.ch/download/%{name}/releases/%{name}-%{version}.tar.xz
Source1: btrbk-logrotate
BuildArch: noarch
Requires: btrfs-progs >= 4.12
Recommends: openssh-clients
Recommends: pv
Recommends: mbuffer
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
# /oreon:deps
%description
Backup tool for btrfs sub-volumes, using a configuration file, allows
creation of backups from multiple sources to multiple destinations,
with ssh and flexible retention policy support (hourly, daily,
weekly, monthly)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
%make_install
rm -rf %{buildroot}/%{_docdir}/%{name}
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%systemd_post %{name}.timer
%preun

%systemd_preun %{name}.service
%systemd_preun %{name}.timer
%postun

%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
