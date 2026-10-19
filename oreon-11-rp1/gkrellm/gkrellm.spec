%global source0_hash 089e3c1ed398482e682c9900b504ea166a6144a6c9fa041e70c5bbca6b177e63
Name:           gkrellm
Version:        2.5.1
Release:        1%{?dist}
Summary:        Multiple stacked system monitors in one process
License:        GPL-3.0-or-later
URL:            https://gkrellm.srcbox.net/
Source0:        https://gkrellm.srcbox.net/releases/%{name}-%{version}.tar.bz2
Source5:        make-git-snapshot.sh
Patch1:         gkrellm-2.4.0-config.patch
Patch3:         gkrellm-2.4.0-width.patch
Requires:       gdk-pixbuf2-modules-extra%{?_isa}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libSM-devel
BuildRequires:  libappstream-glib
BuildRequires:  libntlm-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd
# /oreon:deps
%description
GKrellM charts CPU, load, Disk, and all active net interfaces
automatically.  An on/off button and online timer for the PPP
interface is provided, as well as monitors for memory and swap usage,
file system, internet connections, APM laptop battery, mbox style
mailboxes, and temperature sensors on supported systems.  Also
included is an uptime monitor, a hostname label, and a clock/calendar.
Additional features are:

  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * A gui popup for configuration of chart sizes and resolutions.

%package daemon
Summary:        The GNU Krell Monitors Server
BuildRequires:  systemd >= 186
BuildRequires: make
Requires(pre):  systemd
Requires(post,preun,postun): systemd
%description daemon
gkrellmd listens for connections from gkrellm clients. When a gkrellm
client connects to a gkrellmd server all builtin monitors collect their
data from the server.

%package        devel
Summary:        Development files for the GNU Krell Monitors
Requires:       gtk2-devel%{?_isa}
%description devel
Development files for the GNU Krell Monitors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

for i in gkrellmd.1 gkrellm.1 README Changelog.OLD Changelog-plugins.html \
    src/gkrellm.h server/gkrellmd.h; do
   sed -i -e "s@/usr/lib/gkrellm2*/plugins@%{_libdir}/gkrellm2/plugins@" $i
   sed -i -e "s@/usr/local/lib/gkrellm2*/plugins@/usr/local/%{_lib}/gkrellm2/plugins@" $i
done

# Create a sysusers.d config file
cat >gkrellm.sysusers.conf <<EOF
u gkrellmd - 'GNU Krell daemon' - -
EOF

%build

make %{?_smp_mflags} PREFIX=%{_prefix} \
    PKGCONFIGDIR=%{_libdir}/pkgconfig \
    INCLUDEDIR=%{_includedir} \
    SINSTALLDIR=%{_sbindir} \
    CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -Wno-error=incompatible-pointer-types" \
    LDFLAGS="$RPM_LD_FLAGS"
%install
mkdir -p %{buildroot}%{_datadir}/gkrellm2/themes
mkdir -p %{buildroot}%{_libdir}/gkrellm2/plugins
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    LOCALEDIR=%{buildroot}%{_datadir}/locale \
    INSTALLDIR=%{buildroot}%{_bindir} \
    SINSTALLDIR=%{buildroot}%{_sbindir} \
    MANDIR=%{buildroot}%{_mandir}/man1 \
    PKGCONFIGDIR=%{buildroot}%{_libdir}/pkgconfig \
    INCLUDEDIR=%{buildroot}%{_includedir} \
    CFGDIR=%{buildroot}%{_sysconfdir}
%find_lang %name
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
install -m0644 -D gkrellm.sysusers.conf %{buildroot}%{_sysusersdir}/gkrellm.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post daemon

%systemd_post gkrellmd.service
%preun daemon

%systemd_preun gkrellmd.service
%postun daemon

%systemd_postun_with_restart gkrellmd.service
%files -f %{oreon_filedir}/main.list
%files -n gkrellm-daemon -f %{oreon_filedir}/gkrellm-daemon.list
%files -n gkrellm-devel -f %{oreon_filedir}/gkrellm-devel.list

%changelog

%autochangelog
