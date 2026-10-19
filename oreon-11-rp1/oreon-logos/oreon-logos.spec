%global source0_hash none
%global codename Horizon
%global debug_package %{nil}
Name:       oreon-logos
Version:    11
Release:        2%{?dist}
Summary:        Oreon-related icons and pictures
Group:      System Environment/Base
URL:        https://oreonhq.com
Source0:        %{name}-%{version}.tar.xz
License:    Licensed only for approved usage, see COPYING for details.
Obsoletes:  oreon-logos < 90.4-1
Provides:   system-logos = %{version}-%{release}
Provides:   redhat-logos = %{version}-%{release}
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
Requires(post): coreutils
# oreon:deps
BuildRequires:  hardlink
BuildRequires:  make
# /oreon:deps
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
Provides:  system-backgrounds = %{version}-%{release}
Requires:  oreon-logos = %{version}-%{release}
%description -n oreon-backgrounds
Licensed only for approved usage, see COPYING for details.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
hardlink -v %{buildroot}/usr
%ifnarch x86_64 i686
rm -f $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/splash.lss
%oreon_autofiles oreon-backgrounds usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
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
%files -f %{oreon_filedir}/main.list
%files -n oreon-logos-httpd -f %{oreon_filedir}/oreon-logos-httpd.list
%files -n oreon-logos-ipa -f %{oreon_filedir}/oreon-logos-ipa.list
%files -n oreon-backgrounds -f %{oreon_filedir}/oreon-backgrounds.list

%changelog

* Tue Apr 7 2026 Brandon Lester <blester@oreonhq.com> - 11-1
- Prepare for Oreon 11 (RP1)

* Fri Feb 20 2026 Brandon Lester <blester@oreonhq.com> - 10-3
- replace all brand mark logos with cleaner and properly sized logos

* Thu Mar 13 2025 Brandon Lester <blester@oreonproject.org> - 10-2
- Background change

* Sat Oct 26 2024 Brandon Lester <blester@oreonproject.org> - 10-1
- Prepare for Oreon 10
