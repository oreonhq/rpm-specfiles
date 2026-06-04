%global source0_hash ffedbec1a5acd46632e439d44b47ff725ee1c20d41f9415f98d49ca34f4e270e

%global have_xen 0

Summary:       Virtualization host metrics daemon
Name:          vhostmd
Version:       1.2
Release:       1%{?dist}
License:       LGPL-2.1-or-later

URL:           https://github.com/vhostmd/vhostmd

Source0:        https://github.com/vhostmd/vhostmd/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       vhostmd.conf

Patch0001:     0001-Add-channel_path-setting-to-daemon-config-file.patch
Patch0002:     0002-Support-libvirts-new-channel-path-naming-scheme.patch
Patch0003:     0003-Fix-parsing-of-vmstat-output.patch
ExcludeArch: %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: chrpath
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: libxml2-devel
BuildRequires: libvirt-devel
BuildRequires: autoconf, automake, libtool
BuildRequires: git
%{?systemd_requires}
BuildRequires: systemd

%if %{have_xen}
BuildRequires: xen-devel
%endif

# This is hopefully temporary, but required to run vhostmd.xml as
# currently written.  For more information see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1897130
Requires:      libvirt


%description 
vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.


%package -n    vm-dump-metrics
Summary:       Virtualization host metrics dump 


%description -n vm-dump-metrics
Executable to dump all available virtualization host metrics to stdout
or a file.


%package -n    vm-dump-metrics-devel
Summary:       Virtualization host metrics dump development 
Requires:      vm-dump-metrics = %{version}-%{release}
Requires:      pkgconfig


%description -n vm-dump-metrics-devel
Header and libraries necessary for metrics gathering development


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git


%build
autoreconf -i
%configure \
%if %{have_xen} == 0
  --without-xenstore \
%endif
  --with-init-script=systemd \
  --enable-shared --disable-static
make %{_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%{_libdir}/libmetrics.la

chrpath --delete $RPM_BUILD_ROOT%{_sbindir}/vm-dump-metrics

# Remove docdir - we'll make a proper one ourselves.
rm -r $RPM_BUILD_ROOT%{_docdir}/vhostmd

# Remove metric.dtd from /etc.
rm $RPM_BUILD_ROOT%{_sysconfdir}/vhostmd/metric.dtd

# The default configuration file is great for Xen, not so great
# for anyone else.  Replace it with one which is better for libvirt
# users.
rm $RPM_BUILD_ROOT%{_sysconfdir}/vhostmd/vhostmd.conf
cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/vhostmd/vhostmd.conf

%if 0%{?rhel} || (0%{?oreon} >= 11)
# Remove Perl script (https://bugzilla.redhat.com/show_bug.cgi?id=749875)
rm $RPM_BUILD_ROOT%{_datadir}/vhostmd/scripts/pagerate.pl
%endif


%pre
# UID:GID 112:112 reserved, see RHBZ#534109.
%sysusers_create_inline u vhostmd 112 "Virtual Host Metrics Daemon" %{_datadir}/vhostmd /sbin/nologin


%post
%systemd_post vhostmd.service


%preun
%systemd_preun vhostmd.service


%postun
%systemd_postun_with_restart vhostmd.service


%files
%doc AUTHORS ChangeLog COPYING README
%doc mdisk.xml metric.dtd vhostmd.dtd vhostmd.xml

%{_sbindir}/vhostmd

%dir %{_sysconfdir}/vhostmd
%config(noreplace) %{_sysconfdir}/vhostmd/vhostmd.conf
%config %{_sysconfdir}/vhostmd/vhostmd.dtd

%{_unitdir}/vhostmd.service

%dir %{_datadir}/vhostmd
%dir %{_datadir}/vhostmd/scripts
%if !0%{?rhel} || (0%{?oreon} >= 11)
%{_datadir}/vhostmd/scripts/pagerate.pl
%endif

%{_mandir}/man8/vhostmd.8.gz


%files -n vm-dump-metrics
%doc COPYING
%{_sbindir}/vm-dump-metrics
%{_libdir}/libmetrics.so.0
%{_libdir}/libmetrics.so.0.0.0
%{_mandir}/man1/vm-dump-metrics.1.gz


%files -n vm-dump-metrics-devel
%doc README
%{_libdir}/libmetrics.so
%dir %{_includedir}/vhostmd
%{_includedir}/vhostmd/libmetrics.h


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-1
- Import
