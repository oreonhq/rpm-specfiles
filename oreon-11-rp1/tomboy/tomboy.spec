%global source0_hash 78d0a5f33db9b1077115773ad3291ecaf6e656f58545859b77a2ae7440abb248
Name:           tomboy
Version:        1.15.9
Release:        1%{?dist}
Summary:        Note-taking application
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://projects.gnome.org/tomboy/
Source0:        http://download.gnome.org/sources/%{name}/1.15/%{name}-%{version}.tar.xz
Patch0:         tomboy-1.15.9-fix-help-fr_po.patch
Requires: gtkspell
Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2
ExclusiveArch: %{mono_arches}
# oreon:deps
BuildRequires:  /usr/bin/xmllint
BuildRequires:  GConf2
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  mono(Mono.Cairo)
BuildRequires:  mono(mcs)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dbus-sharp-2.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-2.0)
BuildRequires:  pkgconfig(gconf-sharp-2.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(mono-addins-gui)
BuildRequires:  pkgconfig(mono-addins-setup)
# /oreon:deps
%description
Tomboy is a desktop note-taking application which is simple and easy to use.
It lets you organise your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects.

%package devel
Summary: Support for developing addings for tomboy
Requires: %{name} = %{version}-%{release}
%description devel
Tomboy is a desktop note-taking application. This package allows you
to develop addins that add new functionality to tomboy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# dbus2
sed -i configure configure.ac \
 -e "s#dbus-sharp-1.0#dbus-sharp-2.0#g" \
 -e "s#dbus-sharp-glib-1.0#dbus-sharp-glib-2.0#g"

# Convert to utf-8
for file in ChangeLog ; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build

%configure --disable-schemas-install \
           --disable-update-mimedb \
           --disable-silent-rules
make
%install
%{make_install}
find %{buildroot} -name '*.la' -delete
chmod a+x %{buildroot}%{_libdir}/%{name}/*.exe
chmod a+x %{buildroot}%{_libdir}/%{name}/addins/*.dll
sed -i -e '1 s,^#!.*,#!%{_bindir}/bash,' %{buildroot}%{_bindir}/tomboy
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=736869
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">tomboy.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Tomboy is a desktop note-taking application for GNU/Linux, Unix, Windows, and
      Mac OS X.
      Simple and easy to use, but with potential to help you organize the ideas and
      information you deal with every day.
    </p>
    <p>
      Have you ever felt the frustration at not being able to locate a website you
      wanted to check out, or find an email you found interesting, or remember an idea
      about the direction of the political landscape in post-industrial Australia?
      Or are you one of those desperate souls with home-made, buggy, or not-quite-perfect
      notes systems?
      Time for Tomboy.
    </p>
    <p>
      We bet you'll be surprised at how well a little application can make life less
      cluttered and run more smoothly.
    </p>
  </description>
  <url type="homepage">https://projects.gnome.org/tomboy/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tomboy/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/tomboy.desktop
%find_lang %name --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%gconf_schema_upgrade tomboy
%pre

%gconf_schema_prepare tomboy
%preun

%gconf_schema_remove tomboy
%files -f %{oreon_filedir}/main.list
%files -n tomboy-devel -f %{oreon_filedir}/tomboy-devel.list

%changelog

%autochangelog
