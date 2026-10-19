%global source0_hash 1ffbdb6fee656914c9184a8e6553c4716aee38524f0f00c57a041f35861eacdc
%define _hardened_build 1
Summary:        TCP port reservation utility
Name: portreserve
Version: 0.0.5
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://cyberelk.net/tim/portreserve/
Source0:        http://cyberelk.net/tim/data/portreserve/stable/%{name}-%{version}.tar.bz2
Source1: portreserve.service
Patch1: portreserve-pid-file.patch
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-sysv
Obsoletes: portreserve-selinux < 0.0.3-3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-units
BuildRequires:  xmlto
# /oreon:deps
%description
The portreserve program aims to help services with well-known ports that
lie in the portmap range.  It prevents portmap from a real service's port
by occupying it itself, until the real service tells it to release the
port (generally in the init script).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# Avoid a race during start-up if there are no configured ports (bug #1034139).
%patch -P1 -p1 -b .pid-file

%build

%configure --sbindir=%_sbindir
make
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_rundir}/portreserve
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}/portreserve.service
mkdir -p %{buildroot}%{_sysconfdir}/portreserve
mkdir -p %{buildroot}%{_tmpfilesdir}
cat <<EOF > %{buildroot}%{_tmpfilesdir}/portreserve.conf
d %{_rundir}/portreserve 0755 root root 10d
EOF
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%triggerun -- portreserve < 0.0.5-3

%{_bindir}/systemd-sysv-convert --save portreserve >/dev/null 2>&1 ||:
/sbin/chkconfig --del portreserve >/dev/null 2>&1 || :
/bin/systemctl try-restart portreserve.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.5-40
- Prepare for Oreon 11 (RP1)
