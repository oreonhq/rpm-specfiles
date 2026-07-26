%global source0_hash 4fdbe67c5dfaf89405639e18599f4eae77978073ffa54f3c78c368ab54bd12f6

%define _hardened_build 1

Name:           atop
Version:        2.12.1
Release:        3%{?dist}
Summary:        An advanced interactive monitor to view the load on system and process level

License:        GPL-2.0-or-later
URL:            https://www.atoptool.nl
Source0:        https://www.atoptool.nl/download/%{name}-%{version}.tar.gz
Source1:        atop.d

Patch0:         atop-sysconfig.patch

BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  ncurses-devel
BuildRequires:  glib2-devel
BuildRequires:  systemd
BuildRequires:  make

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
An advanced interactive monitor for Linux-systems to view the load on 
system-level and process-level.
The command atop has some major advantages compared to other
performance-monitors: 
   - Resource consumption by all processes
   - Utilization of all relevant resources
   - Permanent logging of resource utilization
   - Highlight critical resources
   - Watch activity only
   - Watch deviations only
   - Accumulated process activity per user
   - Accumulated process activity per program
 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p0 -b .sysconfig

# Correct unit file path
sed -i "s|/etc/default/atop|/etc/sysconfig/atop|g" atop.service

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS $(pkg-config --cflags glib-2.0) -I. -std=gnu17"

%install
install -Dp -m 0755 atop $RPM_BUILD_ROOT%{_bindir}/atop
install -Dp -m 0755 atopconvert $RPM_BUILD_ROOT%{_bindir}/atopconvert
ln -s atop $RPM_BUILD_ROOT%{_bindir}/atopsar
install -Dp -m 0644 man/atop.1 $RPM_BUILD_ROOT%{_mandir}/man1/atop.1
install -Dp -m 0644 man/atopsar.1 $RPM_BUILD_ROOT%{_mandir}/man1/atopsar.1
install -Dp -m 0644 man/atopacctd.8 $RPM_BUILD_ROOT%{_mandir}/man8/atopacctd.8
install -Dp -m 0755 atop.daily $RPM_BUILD_ROOT%{_datadir}/atop/atop.daily
install -Dp -m 0644 atop.default $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/atop
install -Dp -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/atopd
install -Dp -m 0644 atop.service $RPM_BUILD_ROOT%{_unitdir}/atop.service
install -d $RPM_BUILD_ROOT%{_localstatedir}/log/atop
install -Dp -m 0755 atopacctd $RPM_BUILD_ROOT%{_sbindir}/atopacctd
install -Dp -m 0644 atopacct.service $RPM_BUILD_ROOT%{_unitdir}/atopacct.service
#%%if 0%%{?rhel} >= 8 || 0%%{?fedora}
#install -Dp -m 0755 atopgpud $RPM_BUILD_ROOT%%{_sbindir}/atopgpud
#install -Dp -m 0644 atopgpu.service $RPM_BUILD_ROOT%%{_unitdir}/atopgpu.service
#%%endif
install -Dp -m 0644 atop-rotate.* $RPM_BUILD_ROOT%{_unitdir}/

%post
%systemd_post atop.service atopacct.service atop-rotate.timer
#%%if 0%%{?rhel} >= 8 || 0%%{?fedora}
#%%systemd_post atopgpu.service
#%%endif

%preun
%systemd_preun atop.service atopacct.service atop-rotate.timer
#%%if 0%%{?rhel} >= 8 || 0%%{?fedora}
#%%systemd_preun atopgpu.service
#%%endif

%postun
%systemd_postun_with_restart atop.service atopacct.service atop-rotate.timer
#%%if 0%%{?rhel} >= 8 || 0%%{?fedora}
#%%systemd_postun_with_restart atopgpu.service
#%%endif

%files
%if 0%{?rhel}
%doc COPYING
%else
%license COPYING
%endif
%doc README*
%config(noreplace) %{_sysconfdir}/sysconfig/atop
%{_bindir}/atopsar
%{_bindir}/atop
%{_bindir}/atopd
%{_bindir}/atopconvert
%{_mandir}/man1/atop.1.gz
%{_mandir}/man1/atopsar.1.gz
%{_mandir}/man8/atopacctd.8.gz
%attr(0755,root,root) %dir %{_localstatedir}/log/atop
%{_unitdir}/atop*.service
%{_unitdir}/atop*.timer
%{_datadir}/atop/atop.daily
%{_sbindir}/atopacctd
#%%if 0%%{?rhel} >= 8 || 0%%{?fedora}
#%%{_sbindir}/atopgpud
#%%endif

%changelog
%autochangelog
