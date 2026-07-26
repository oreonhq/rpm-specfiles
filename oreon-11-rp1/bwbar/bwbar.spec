%global source0_hash d82f8ba7defbdb9ae6671cbd7a064597a2a717ee6eeb32df6093403e8a86d1c1

Summary: Generate a readout of the current bandwidth use
Name: bwbar
Version: 1.2.3
Release: 42%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://www.kernel.org/pub/software/web/bwbar/bwbar-1.2.3.tar.bz2
Source1: bwbar.systemd
Source2: bwbar.8
Patch0: bwbar.daemon.patch
Patch1: bwbar.debian-010_directory_option.patch
Patch2: bwbar.debian-020_proc_net_2.6.x_fix.patch
Patch3: bwbar.zlib.h.patch
URL: http://www.kernel.org/pub/software/web/bwbar/
BuildRequires:  gcc
BuildRequires: libpng-devel systemd-units
BuildRequires: make
Requires(post): systemd-units, systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
bwbar is a small program that generates a text and a graphical readout
of the current bandwidth use.  It is currently for Linux only.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man8
%{__mkdir_p} $RPM_BUILD_ROOT%{_initrddir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__install} -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%{__install} -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man8

%{__cat} >> $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/bwbar << END
#OPTIONS="eth0 100 -d /path/to/outdir"
END

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerun -- %{name} < 1.2.3-11
/usr/bin/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:
/bin/systemctl --no-reload enable %{name}.service >/dev/null 2>&1 ||:
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man8/*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
%autochangelog
