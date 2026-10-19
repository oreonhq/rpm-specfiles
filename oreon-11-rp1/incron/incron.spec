%global source0_hash cce80bd723bafce59f35464f2f851d02707e32efa102e2b941ed0e42bdd38f91
Summary:        Inotify cron system
Name:        incron
Version:     0.5.12
Release:        1%{?dist}
License:     GPL-2.0-only
URL:         https://github.com/ar-/incron
Source0:        https://github.com/ar-/%{name}/archive/%{version}.tar.gz
Source1:     incrond.service
Patch0:      incron-0.5.10-gcc.patch
Patch1:      incron-0.5.12-prevent-zombies.patch
Patch2:      56.patch
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
This program is an "inotify cron" system.
It consists of a daemon and a table manipulator.
You can use it a similar way as the regular cron.
The difference is that the inotify cron handles
filesystem events rather than time periods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc
%patch -P1 -p1
%patch -P2 -p1

%build

make %{?_smp_mflags} CXXFLAGS="%{optflags} -std=c++14" LDFLAGS="%{__global_ldflags}"
%install
install -D -p incrond %{buildroot}%{_sbindir}/incrond
install -D -p -m 4755 incrontab %{buildroot}%{_bindir}/incrontab
install -d %{buildroot}%{_localstatedir}/spool/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}.d
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/incrond.service
install -D -p -m 0644 incron.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf
make install-man MANPATH="%{buildroot}%{_mandir}" INSTALL="install -D -p"
%oreon_autofiles main

%post

%systemd_post incrond.service
%preun

%systemd_preun incrond.service
%postun

%systemd_postun_with_restart incrond.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
