%global source0_hash 72abbe49820d4e44e998bf8d9f55d6825191f1d20331cf9a0a5f3a324d035fbe

Name:       generic-logos
Version:    18.0.0
Release:    27%{?dist}
Summary:    Icons and pictures

URL:        https://pagure.io/generic-logos
Source0:    https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
#The KDE Logo is under a LGPL license (no version statement)
# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License:    GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
BuildArch:  noarch

Obsoletes:  redhat-logos
Obsoletes:  generic-logos < 17.0.0-5
Provides:   redhat-logos = %{version}-%{release}
Provides:   system-logos = %{version}-%{release}

Conflicts:  fedora-logos
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
BuildRequires: make
BuildRequires: fdupes
# For _kde4_* macros:
BuildRequires: kde4-filesystem
# For generating the EFI icon
BuildRequires: libicns-utils
Requires(post): coreutils

%description
The generic-logos package contains various image files which can be
used by the bootloader, anaconda, and other related tools. It can
be used as a replacement for the fedora-logos package, if you are
unable for any reason to abide by the trademark restrictions on the
fedora-logos or fedora-remix-logos package.

%package httpd
Summary: Fedora-related icons and pictures used by httpd
Provides: system-logos-httpd = %{version}-%{release}
Provides: system-logos(httpd-logo-ng)
Conflicts: fedora-logos-httpd
Obsoletes:  generic-logos < 17.0.0-5
BuildArch: noarch

%description httpd
The generic-logos-httpd package contains image files which can be used by
httpd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/firstboot/themes/generic
for i in firstboot/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/firstboot/themes/generic
done

mkdir -p %{buildroot}%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora.icns %{buildroot}%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora.vol %{buildroot}%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora-media.vol  %{buildroot}%{_datadir}/pixmaps/bootloader

mkdir -p %{buildroot}%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps/splash
done

mkdir -p %{buildroot}%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps
done

for size in scalable ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  ln -s ../../../hicolor/$size/apps/fedora-logo-icon.svg icon-panel-menu.svg
  ln -s ../../../hicolor/$size/apps/fedora-logo-icon.svg gnome-main-menu.svg
  ln -s ../../../hicolor/$size/apps/fedora-logo-icon.svg kmenu.svg
  ln -s ../../../hicolor/$size/apps/fedora-logo-icon.svg start-here.svg
  install -p -m 644 pixmaps/fedora-logo-sprite.svg %{buildroot}%{_datadir}/icons/hicolor/$size/apps/fedora-logo-icon.svg
done

mkdir -p %{buildroot}%{_kde4_iconsdir}/oxygen/48x48/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_kde4_iconsdir}/oxygen/48x48/apps/
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536
install -p -m 644 ksplash/SolarComet-kde.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png

mkdir -p %{buildroot}%{_datadir}/plymouth/themes/charge/
for i in plymouth/charge/* ; do
    install -p -m 644 $i %{buildroot}%{_datadir}/plymouth/themes/charge/
done

# File or directory names do not count as trademark infringement
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install	-p -m 644 icons/Fedora/scalable/apps/* %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -p -m 644 pixmaps/fedora-logo-sprite.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 pixmaps/fedora-logo-sprite.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/start-here.svg

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/places/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/places/
ln -s ../apps/start-here.svg .
popd

(cd anaconda; make DESTDIR=%{buildroot} install)

# save some dup'd icons
%fdupes %{buildroot}/

%post
touch --no-create %{_datadir}/icons/hicolor || :
touch --no-create %{_kde4_iconsdir}/oxygen ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor || :
touch --no-create %{_kde4_iconsdir}/oxygen ||:
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  if [ -f %{_datadir}/icons/hicolor/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
  fi
  if [ -f %{_kde4_iconsdir}/Fedora-KDE/index.theme ]; then
    gtk-update-icon-cache --quiet %{_kde4_iconsdir}/Fedora-KDE/index.theme || :
  fi
fi
fi

%posttrans
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  if [ -f %{_datadir}/icons/Fedora/index.theme ]; then
    gtk-update-icon-cache --quiet %{_datadir}/icons/Fedora || :
  fi
  if [ -f %{_kde4_iconsdir}/oxygen/index.theme ]; then
    gtk-update-icon-cache --quiet %{_kde4_iconsdir}/oxygen/index.theme || :
  fi
fi

%files
%license COPYING COPYING-kde-logo
%doc README
%{_datadir}/firstboot/themes/*
%{_datadir}/anaconda/boot/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/plymouth/themes/charge/*
%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png
%{_kde4_iconsdir}/oxygen/

%files httpd
%license COPYING
%{_datadir}/pixmaps/poweredby.png

%changelog
%autochangelog
