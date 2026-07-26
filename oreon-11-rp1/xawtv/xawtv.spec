%global source0_hash c53bea63c155e5bc52821e1772cdae2da06a948be45544c7015277a02207b714

%bcond_with	quicktime

Summary: TV applications for video4linux compliant devices
Name: xawtv
Version: 3.107
Release: 17%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://linuxtv.org/wiki/index.php/Xawtv

Source0: http://linuxtv.org/downloads/xawtv/%{name}-%{version}.tar.bz2
Patch0: xawtv-strsignal.patch
Patch1: xawtv-3.107-XawListChange.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: mesa-libGL-devel, libXaw-devel, libXext-devel
BuildRequires: libXft-devel, libXinerama-devel
BuildRequires: libXpm-devel, libXrandr-devel, libXt-devel
BuildRequires: libXxf86dga-devel, libXv-devel
BuildRequires: motif-devel
%{?with_quicktime:BuildRequires: libquicktime-devel}

BuildRequires: ncurses-devel, coreutils, libjpeg-devel, libpng-devel
BuildRequires: alsa-lib-devel
%ifnarch s390 s390x
BuildRequires: libdv-devel
%endif
BuildRequires: zvbi-devel, aalib-devel
BuildRequires: gpm-devel, slang-devel
BuildRequires: ImageMagick desktop-file-utils libappstream-glib
BuildRequires: libv4l-devel
BuildRequires: perl-interpreter

Requires: polkit xorg-x11-fonts-misc hicolor-icon-theme

%description
Xawtv is a simple xaw-based TV program which uses the bttv driver or
video4linux. Xawtv contains various command-line utilities for
grabbing images and .avi movies, for tuning in to TV stations, etc.
Xawtv also includes a grabber driver for vic.

%package motv
Summary: MoTV Analog Television Viewer
Requires: %{name} = %{version}-%{release}

%description motv
Motif UI version of the xawtv analog television viewer.

%package mtt
Summary: Analog TV Teletext viewing application
Requires: %{name} = %{version}-%{release}

%description mtt
Easy to use Motif UI for viewing analog tv teletext on video4linux devices
which support teletext.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -fcommon"
%configure %{!?_with_quicktime: --disable-quicktime}
make %{?_smp_mflags} verbose=yes

%install
make DESTDIR=$RPM_BUILD_ROOT SUID_ROOT="" install

%if %{without quicktime}
rm -f $RPM_BUILD_ROOT%{_bindir}/showqt
%endif

for i in 16x16 32x32 48x48; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$i/apps
  convert contrib/%{name}$i.xpm \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$i/apps/%{name}.png
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
for i in xawtv motv mtt; do
   desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
       contrib/$i.desktop
   install -p -m 0644 contrib/$i.*.xml $RPM_BUILD_ROOT%{_datadir}/appdata
   appstream-util validate-relax --nonet \
       $RPM_BUILD_ROOT%{_datadir}/appdata/$i.*.xml
done

#   v4l-conf  stuff

mkdir -p $RPM_BUILD_ROOT%{_libexecdir} $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

mv $RPM_BUILD_ROOT%{_bindir}/v4l-conf $RPM_BUILD_ROOT%{_libexecdir}/

cat >v4l-conf.sh <<EOF
#!/bin/sh
exec %{_bindir}/pkexec %{_libexecdir}/v4l-conf
EOF
install -p -m 755 v4l-conf.sh $RPM_BUILD_ROOT%{_bindir}/v4l-conf

cat >v4l-conf.policy <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE policyconfig PUBLIC
 "-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
 "http://www.freedesktop.org/standards/PolicyKit/1.0/policyconfig.dtd">
<policyconfig>

  <vendor>XawTV Project</vendor>
  <vendor_url>%{url}</vendor_url>

  <action id="org.fedoraproject.v4l.conf.pkexec.run">

    <description>Run v4l-conf with privileges required</description>
    <message>Authentication is required for privileged operations of v4l-conf</message>
    <defaults>
      <allow_any>no</allow_any>
      <allow_inactive>no</allow_inactive>
      <allow_active>yes</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">%{_libexecdir}/v4l-conf</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
  </action>

</policyconfig>
EOF
install -p -m 644 v4l-conf.policy $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions/org.fedoraproject.v4l.conf.policy

%files
%doc README TODO contrib/frequencies*
%license COPYING
%{_bindir}/*
%exclude %{_bindir}/motv
%exclude %{_bindir}/mtt
%{_libexecdir}/*
%{_libdir}/xawtv
%{_datadir}/xawtv
%{_datadir}/X11/app-defaults/Xawtv
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/*
%{_mandir}/man?/*
%exclude %{_mandir}/man1/motv.1*
%exclude %{_mandir}/man1/mtt.1*
%lang(es) %{_mandir}/es/*/*
%lang(fr) %{_mandir}/fr/*/*

%files motv
%{_bindir}/motv
%{_mandir}/man1/motv.1*
%{_datadir}/X11/app-defaults/MoTV*
%lang(de) %{_datadir}/X11/de_DE.UTF-8/app-defaults/MoTV*
%lang(fr) %{_datadir}/X11/fr_FR.UTF-8/app-defaults/MoTV*
%lang(it) %{_datadir}/X11/it_IT.UTF-8/app-defaults/MoTV*
%{_datadir}/appdata/motv.metainfo.xml
%{_datadir}/applications/motv.desktop

%files mtt
%{_bindir}/mtt
%{_mandir}/man1/mtt.1*
%{_datadir}/X11/app-defaults/mtt*
%{_datadir}/appdata/mtt.metainfo.xml
%{_datadir}/applications/mtt.desktop

%changelog
%autochangelog
