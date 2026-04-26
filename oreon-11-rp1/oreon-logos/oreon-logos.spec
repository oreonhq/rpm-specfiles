%global codename Horizon
# Package is only arch specific due to missing deps on arm
# Debuginfo package is useless.
%global debug_package %{nil}

Name:       oreon-logos
Version:    11
Release:    2%{?dist}
Summary:    Oreon-related icons and pictures

Group:      System Environment/Base
URL:        https://oreonhq.com
Source0:    %{name}-%{version}.tar.xz
License:    Licensed only for approved usage, see COPYING for details.

Obsoletes:  oreon-logos < 90.4-1
Provides:   system-logos = %{version}-%{release}
Provides:   redhat-logos = %{version}-%{release}

Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5

Requires(post): coreutils
BuildRequires: hardlink
BuildRequires: make

%description
Licensed only for approved usage, see COPYING for details.

%package httpd
Summary: Oreon-related icons and pictures used by httpd
Provides: system-logos-httpd = %{version}-%{release}
Provides: redhat-logos-httpd = %{version}-%{release}
Provides: system-logos(httpd-logo-ng)
BuildArch: noarch

%description httpd
Licensed only for approved usage, see COPYING for details.

%package ipa
Summary: Oreon-related icons and pictures used by ipa
Provides: system-logos-ipa = %{version}-%{release}
Provides: redhat-logos-ipa = %{version}-%{release}
BuildArch: noarch

%description ipa
Licensed only for approved usage, see COPYING for details.

%package -n oreon-backgrounds
Summary: Oreon-related desktop backgrounds
BuildArch: noarch

#Obsoletes: oreon-logos < 80.1-2
Provides:  system-backgrounds = %{version}-%{release}
Requires:  oreon-logos = %{version}-%{release}

%description -n oreon-backgrounds
Licensed only for approved usage, see COPYING for details.


%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/
for i in backgrounds/*.jpg backgrounds/*.xml; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.background.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.screensaver.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/desktop-backgrounds-default.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
for i in bootloader/*; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
done
pushd $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
ln -sf fedora.icns oreon.icns
ln -sf fedora.icns oreon-media.vol
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
for i in plymouth/charge/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
done

for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  done
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
pushd $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_datadir}/icons/hicolor/16x16/apps/fedora-logo-icon.png favicon.png
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/xfce4_xicon1.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/fedora-logo-icon.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/start-here.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/start-here.svg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
ln -s ../apps/start-here.svg .
popd

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a fedora/*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.png $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.jpg $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images

mkdir -p $RPM_BUILD_ROOT%{_datadir}/testpage
install -p -m 644 testpage/index.html $RPM_BUILD_ROOT%{_datadir}/testpage

# save some dup'd icons
# Except in /boot. Because some people think it is fun to use VFAT for /boot.
hardlink -v %{buildroot}/usr

%ifnarch x86_64 i686
rm -f $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/splash.lss
%endif

%post
touch --no-create %{_datadir}/icons/hicolor || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/favicon.png
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/firstboot/themes/fedora-%{codename}/
%{_datadir}/plymouth/themes/charge/

%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/anaconda/pixmaps/*
%ifarch x86_64 i686
%{_datadir}/anaconda/boot/splash.lss
%endif
%{_datadir}/anaconda/boot/syslinux-splash.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/%{name}/

# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/backgrounds
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/22x22/apps/
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/36x36/
%dir %{_datadir}/icons/hicolor/36x36/apps/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%dir %{_datadir}/icons/hicolor/96x96/
%dir %{_datadir}/icons/hicolor/96x96/apps/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%dir %{_datadir}/icons/hicolor/scalable/places/
%dir %{_datadir}/anaconda
%dir %{_datadir}/anaconda/boot/
%dir %{_datadir}/anaconda/pixmaps
%dir %{_datadir}/firstboot/
%dir %{_datadir}/firstboot/themes/
%dir %{_datadir}/plymouth/
%dir %{_datadir}/plymouth/themes/

%files httpd
%license COPYING
%{_datadir}/pixmaps/poweredby.png
%{_datadir}/testpage
%{_datadir}/testpage/index.html

%files ipa
%license COPYING
%{_datadir}/ipa/ui/images/*
# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/ipa
%dir %{_datadir}/ipa/ui
%dir %{_datadir}/ipa/ui/images

%files -n oreon-backgrounds
%license COPYING
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/*


%changelog
* Tue Apr 7 2026 Brandon Lester <blester@oreonhq.com> - 11-1
- Prepare for Oreon 11 (RP1)

* Fri Feb 20 2026 Brandon Lester <blester@oreonhq.com> - 10-3
- replace all brand mark logos with cleaner and properly sized logos

* Thu Mar 13 2025 Brandon Lester <blester@oreonproject.org> - 10-2
- Background change

* Sat Oct 26 2024 Brandon Lester <blester@oreonproject.org> - 10-1
- Prepare for Oreon 10
