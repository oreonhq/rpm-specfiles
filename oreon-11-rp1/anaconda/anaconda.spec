%global source0_hash a5360cf49e09c85961651b9cb3bf1b3687ca28b71a80f89b2d0ec3c2eb9f0793
Summary:        Graphical system installer
Name:    anaconda
Version: 45.28
Release:        1%{?dist}
ExcludeArch: %{ix86}
License: GPL-2.0-or-later
URL:     http://fedoraproject.org/wiki/Anaconda
Source0:        https://github.com/rhinstaller/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
%bcond glade %[%{undefined rhel} && %{undefined eln}]
%bcond live %[%{defined fedora} || %{defined eln}]
%define dasbusver 1.3
%define dbusver 1.2.3
%define dnfver 5.2.15.0-1
%define dracutver 102-3
%define fcoeutilsver 1.0.12-3.20100323git
%define gettextver 0.19.8
%define gtk3ver 3.22.17
%define isomd5sumver 1.0.10
%define langtablever 0.0.60
%define libarchivever 3.0.4
%define libblockdevver 2.1
%define libreportanacondaver 2.0.21-1
%define mehver 0.23-1
%define nmver 1.0
%define pykickstartver 3.65-1
%define pypartedver 2.5-2
%define pythonblivetver 1:3.13.0-1
%define rpmver 4.15.0
%define simplelinever 1.9.0-1
%define subscriptionmanagerver 1.29.31
%define utillinuxver 2.15.1
%define rpmostreever 2023.2
%define s390utilscorever 2.31.0
%if %{with glade}
%endif
%ifarch s390 s390x
%endif
Requires: anaconda-gui = %{version}-%{release}
Requires: anaconda-tui = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext-devel
BuildRequires:  glade-devel
BuildRequires:  glib2-devel
BuildRequires:  glib2-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  gtk3-devel-docs
BuildRequires:  libarchive-devel
BuildRequires:  libtool
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
License: GPL-2.0-or-later AND MIT
Requires: python3-libs
Requires: python3-libdnf5 >= %{dnfver}
Requires: python3-blivet >= %{pythonblivetver}
Requires: python3-blockdev >= %{libblockdevver}
Requires: python3-meh >= %{mehver}
Requires: python3-iso639
Requires: python3-libselinux
Requires: python3-rpm >= %{rpmver}
Requires: python3-pyparted >= %{pypartedver}
Requires: python3-requests
Requires: python3-requests-file
Requires: python3-requests-ftp
Requires: python3-kickstart >= %{pykickstartver}
Requires: python3-langtable >= %{langtablever}
Requires: util-linux >= %{utillinuxver}
Requires: python3-gobject-base
Requires: python3-pwquality
Requires: python3-systemd
Requires: python3-productmd
Requires: python3-dasbus >= %{dasbusver}
Requires: python3-xkbregistry
Requires: flatpak
Requires: flatpak-libs
Requires: cracklib-dicts
%ifarch s390 s390x
Requires: openssh
Requires: s390utils-core >= %{s390utilscorever}
Requires: dracut-network >= %{dracutver}
%endif
Requires: NetworkManager >= %{nmver}
Requires: NetworkManager-libnm >= %{nmver}
Requires: kbd
Requires: chrony
Requires: systemd
Requires: systemd-pam
Requires: python3-pid
Requires: crypto-policies
Requires: crypto-policies-scripts
%ifnarch s390 s390x
Requires: grub2-common >= 2.12-37
%endif
Requires: anaconda-tui = %{version}-%{release}
Requires: (glibc-langpack-en or glibc-all-langpacks)
Requires: dbus-daemon
Requires: /usr/bin/date
Conflicts: grubby < 8.40-10
Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
%description core
The anaconda-core package contains the program which was used to install your
system.

%if %{with live}
# do not provide the live subpackage on RHEL

%package live
Summary: Live installation specific files and dependencies
BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: zenity
Recommends: xhost
Requires: python3-dbus-next
%description live
The anaconda-live package contains scripts, data and dependencies required
for live installations.

%endif

%package install-env-deps
Summary: Installation environment specific dependencies
Requires: udisks2-iscsi
Requires: libblockdev-plugins-all >= %{libblockdevver}
Requires: libblockdev-tools
Requires: libblockdev-lvm-dbus
Requires: realmd
Requires: isomd5sum >= %{isomd5sumver}
%ifarch x86_64
Recommends: fcoe-utils >= %{fcoeutilsver}
%endif
%ifarch x86_64
%endif
%ifnarch riscv64
Requires: kexec-tools
%endif
Requires: tmux
Requires: gdb
Requires: rsync
Recommends: kdump-anaconda-addon
Requires: xfsprogs
Requires: dosfstools
Requires: e2fsprogs
Recommends: nvme-cli
%description install-env-deps
The anaconda-install-env-deps metapackage lists all installation environment
dependencies. This makes it possible for packages (such as Initial Setup) to
depend on the main Anaconda package without pulling in all the install time
dependencies as well.

%package install-img-deps
Summary: Installation image specific dependencies
Requires: anaconda-install-env-deps = %{version}-%{release}
%ifarch x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: device-mapper-multipath
Requires: kdump-anaconda-addon
Requires: zram-generator
Requires: createrepo_c
Requires: gsettings-desktop-schemas
Requires: nm-connection-editor
Requires: librsvg2
Requires: gnome-kiosk
Requires: gnome-remote-desktop
Requires: openssl
Requires: mesa-dri-drivers
Requires: brltty
Requires: python3-pam
Requires: rpm-ostree >= %{rpmostreever}
Requires: ostree
Requires: skopeo
Requires: nvme-cli
Requires: podman
Requires: bootc
Requires: bootupd
Requires: dnsconfd
Requires: dnsconfd-dracut
Requires: selinux-policy
Requires: libselinux-utils
Requires: selinux-policy-targeted
Requires: policycoreutils-python-utils
Requires: fonts-filesystem
Requires: liberation-fonts
%description install-img-deps
The anaconda-install-img-deps metapackage lists all boot.iso installation
image dependencies. Add this package to an image build (eg. with lorax) to
ensure all Anaconda capabilities are supported in the resulting image.

%package gui
Summary: Graphical user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release}
Requires: anaconda-widgets = %{version}-%{release}
Requires: python3-meh-gui >= %{mehver}
Requires: adwaita-icon-theme
Requires: tecla
Requires: nm-connection-editor
%ifnarch s390 s390x
Requires: NetworkManager-wifi
%endif
Requires: system-logos
BuildRequires: gsettings-desktop-schemas
BuildRequires: glib2-devel
%description gui
This package contains graphical user interface for the Anaconda installer.

%package tui
Summary: Textual user interface for the Anaconda installer
Requires: anaconda-core = %{version}-%{release}
Requires: python3-simpleline >= %{simplelinever}
%description tui
This package contains textual user interface for the Anaconda installer.

%package widgets
Summary: A set of custom GTK+ widgets for use with anaconda
Requires: %{__python3}
%description widgets
This package contains a set of custom GTK+ widgets used by the anaconda
installer.

%package widgets-devel
Summary: Development files for anaconda-widgets
%if %{with glade}
Requires: glade
%endif
Requires: %{name}-widgets%{?_isa} = %{version}-%{release}
%description widgets-devel
This package contains libraries and header files needed for writing the
anaconda installer.  It also contains Python and Glade support files,
as well as documentation for working with this library.

%package dracut
Summary: The anaconda dracut module
Requires: dracut >= %{dracutver}
Requires: dracut-network
Requires: dracut-live
Requires: xz
Requires: python3-kickstart
Requires: iputils
Requires: dnsconfd-dracut
Requires: dnsconfd
%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{!?with_glade:export ANACONDA_DISABLE_GLADE=yes}
autoreconf -vfi
%configure ANACONDA_RELEASE=%{release} %{!?with_glade:--disable-glade}
%{__make} %{?_smp_mflags}
%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}
mkdir %{buildroot}%{_datadir}/anaconda/addons
mkdir %{buildroot}%{_datadir}/anaconda/post-scripts
%if %{with live}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%else
rm -rf \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/liveinst-setup.desktop \
  %{buildroot}/%{_bindir}/liveinst \
  %{buildroot}/%{_libexecdir}/liveinst-setup.sh \
  %{buildroot}/%{_libexecdir}/locale1-x11-sync \
  %{buildroot}/%{_userunitdir}/locale1-x11-sync.service \
  %{buildroot}/%{_datadir}/anaconda/gnome \
  %{buildroot}/%{_datadir}/anaconda/gnome/fedora-welcome \
  %{buildroot}/%{_datadir}/anaconda/gnome/org.fedoraproject.welcome-screen.desktop \
  %{buildroot}/%{_datadir}/polkit-1/actions/* \
  %{buildroot}/%{_datadir}/applications/liveinst.desktop
%endif
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n anaconda-core -f %{oreon_filedir}/anaconda-core.list
%files -n anaconda-live -f %{oreon_filedir}/anaconda-live.list
%files -n anaconda-install-env-deps -f %{oreon_filedir}/anaconda-install-env-deps.list
%files -n anaconda-install-img-deps -f %{oreon_filedir}/anaconda-install-img-deps.list
%files -n anaconda-gui -f %{oreon_filedir}/anaconda-gui.list
%files -n anaconda-tui -f %{oreon_filedir}/anaconda-tui.list
%files -n anaconda-widgets -f %{oreon_filedir}/anaconda-widgets.list
%files -n anaconda-widgets-devel -f %{oreon_filedir}/anaconda-widgets-devel.list
%files -n anaconda-dracut -f %{oreon_filedir}/anaconda-dracut.list

%changelog

%autochangelog
