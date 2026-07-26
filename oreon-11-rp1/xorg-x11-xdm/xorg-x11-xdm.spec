%global source0_hash 9494aef0911a031c53670725b5c8c9bb9d3f7c5ea7318b1f72ddd9dcbbeceb6a

%global pkgname xdm

Summary: X.Org X11 xdm - X Display Manager
Name: xorg-x11-%{pkgname}
Version: 1.1.17
Release: 3%{?dist}
# NOTE: Remove Epoch line if/when the package ever gets renamed.
Epoch: 1
License: MIT
URL: http://www.x.org

Source0: https://ftp.x.org/pub/individual/app/xdm-%{version}.tar.xz

Source1: Xsetup_0
Source10: xdm.init
Source11: xdm.pamd

# Following are Fedora specific patches
Patch1: xdm-1.0.5-sessreg-utmp-fix-bug177890.patch

# send a USER_LOGIN event like other login programs do.
Patch2: xdm-1.1.14-add-audit-events.patch

# systemd unit file update
Patch3: xdm-1.1.14-xdm-systemd-unit.patch

# set -nolisten tcp
Patch4: xdm-1.1.14-add-nolisten-tcp-option.patch

# FIXME: Temporary build dependencies for autotool dependence.
BuildRequires: make
BuildRequires: autoconf, automake, libtool

BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-xtrans-devel
BuildRequires: libXaw-devel
BuildRequires: libXmu-devel
BuildRequires: libXt-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXext-devel
BuildRequires: libXpm-devel
BuildRequires: libX11-devel
BuildRequires: libxcrypt-devel
# FIXME: There's no autotool dep on libXdmcp currently, but it fails with the
# following:
# configure: error: Library requirements (xdmcp) not met; consider adjusting
# the PKG_CONFIG_PATH environment variable if your libraries are in a
# nonstandard prefix so pkg-config can find them.
BuildRequires: libXdmcp-devel
# FIXME: There's no autotool specified dep on this currently, but everything
# explodes looking for X11/Xauth.h without it:
BuildRequires: libXau-devel
BuildRequires: libXinerama-devel
BuildRequires: pam-devel
# Add TrueType support (resolves bug #551908)
BuildRequires: libXft-devel
# Add libaudit support
BuildRequires: audit-libs-devel
# systemd support
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Provides: xdm = %{version}-%{release}

Requires: pam

# We want to use the system Xsession script
Requires: xorg-x11-xinit
Requires: sessreg

%description
X.Org X11 xdm - X Display Manager

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%patch -P 1 -p0 -b .redhat-sessreg-utmp-fix-bug177890
%patch -P 2 -p1 -b .add-audit-events
%patch -P 3 -p1 -b .systemd-unit
%patch -P 4 -p1 -b .nolisten

%build
autoreconf -v --install
%configure \
	--disable-static \
	--with-libaudit \
	--with-xdmlibdir=%{_libexecdir} \
	--with-xdmconfigdir=%{_sysconfdir}/X11/xdm \
	--with-xdmscriptdir=%{_sysconfdir}/X11/xdm \
	--with-pixmapdir=%{_datadir}/xdm/pixmaps \
	--enable-xdmshell

%make_build

%install
echo looking for xdmshell
find . -name \*xdmshell\*
%make_install
echo looking for xdmshell
find %{buildroot} -name \*xdmshell\*

find %{buildroot} -name '*.la' -exec rm -f {} ';'

install -p -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xdm/Xsetup_0

# Install pam xdm config files
{
   mkdir -p %{buildroot}%{_sysconfdir}/pam.d
   install -p -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/xdm
}

rm -f %{buildroot}%{_sysconfdir}/X11/xdm/Xsession
(cd %{buildroot}%{_sysconfdir}/X11/xdm; ln -sf ../xinit/Xsession .)

# we need to create /var/lib/xdm to make authorization work (bug
# 500704)
mkdir -p %{buildroot}%{_sharedstatedir}/xdm

%post
%systemd_post xdm.service

%preun
%systemd_preun xdm.service

%postun
%systemd_postun xdm.service

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/xdm
%{_bindir}/xdmshell
%dir %{_sysconfdir}/X11/xdm

# NOTE: The Xaccess file from our "xinitrc" package had no customizations,
# and was out of sync with upstream, so we ship the upstream one now.
%config(noreplace) %{_sysconfdir}/X11/xdm/Xaccess
%config(noreplace) %{_sysconfdir}/X11/xdm/Xresources
%config(noreplace) %{_sysconfdir}/X11/xdm/Xservers
%config(noreplace) %{_sysconfdir}/X11/xdm/xdm-config
%config(noreplace) %{_sysconfdir}/X11/xdm/Xsession

%{_sysconfdir}/X11/xdm/Xreset
%{_sysconfdir}/X11/xdm/Xsetup_0
%{_sysconfdir}/X11/xdm/Xstartup
%{_sysconfdir}/X11/xdm/Xwilling

%{_sysconfdir}/X11/xdm/GiveConsole
%{_sysconfdir}/X11/xdm/TakeConsole

# NOTE: For security, upgrades of this package will install the new pam.d
# files and make backup copies by default.  'noreplace' is intentionally avoided
# here.
%config(noreplace) %{_sysconfdir}/pam.d/xdm

# NOTE: We intentionally default to OS supplied file being favoured here on
# OS upgrades.
%{_datadir}/X11/app-defaults/Chooser
%dir %{_datadir}/xdm
%dir %{_datadir}/xdm/pixmaps
%{_datadir}/xdm/pixmaps/xorg-bw.xpm
%{_datadir}/xdm/pixmaps/xorg.xpm
%dir %{_sharedstatedir}/xdm
%{_libexecdir}/chooser
%{_libexecdir}/libXdmGreet.so
%{_mandir}/man8/*.8*
# systemd unit file
%{_unitdir}/xdm.service

%changelog
%autochangelog
