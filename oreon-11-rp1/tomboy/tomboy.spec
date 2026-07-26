%global source0_hash 78d0a5f33db9b1077115773ad3291ecaf6e656f58545859b77a2ae7440abb248

Name:           tomboy
Version:        1.15.9
Release:        25%{?dist}
Summary:        Note-taking application
# Automatically converted from old format: LGPLv2+ and GPLv2+ and MIT - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND LicenseRef-Callaway-MIT
# Tomboy itself is LGPLv2+
# libtomboy contains GPL+ code
# Mono.Addins is MIT
URL:            http://projects.gnome.org/tomboy/
Source0:        http://download.gnome.org/sources/%{name}/1.15/%{name}-%{version}.tar.xz
Patch0:         tomboy-1.15.9-fix-help-fr_po.patch

BuildRequires: make
BuildRequires:  pkgconfig(atk) >= 1.2.4
BuildRequires:  pkgconfig(gconf-sharp-2.0)
BuildRequires:  pkgconfig(gdk-2.0) >= 2.6.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.14.0
BuildRequires:  pkgconfig(gtk-sharp-2.0) >= 2.10.1
BuildRequires:  pkgconfig(gtkspell-2.0) >= 2.0.9
BuildRequires:  pkgconfig(mono) >= 1.9.1
BuildRequires:  pkgconfig(mono-addins) >= 0.3
BuildRequires:  pkgconfig(mono-addins-gui) >= 0.3
BuildRequires:  pkgconfig(mono-addins-setup) >= 0.3
BuildRequires:  pkgconfig(dbus-sharp-2.0) >= 0.4
BuildRequires:  pkgconfig(dbus-sharp-glib-2.0) >= 0.3
BuildRequires:  mono(Mono.Cairo)
BuildRequires:  mono(mcs)
BuildRequires:  GConf2
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  /usr/bin/xmllint
BuildRequires:  intltool
BuildRequires:  libX11-devel
BuildRequires:  gcc

Requires: gtkspell
Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

# Mono only available on these:
ExclusiveArch: %{mono_arches}

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
# parallel builds currently not supported
make

%install
%{make_install}

find %{buildroot} -name '*.la' -delete

chmod a+x %{buildroot}%{_libdir}/%{name}/*.exe
chmod a+x %{buildroot}%{_libdir}/%{name}/addins/*.dll

# fix shebang
sed -i -e '1 s,^#!.*,#!%{_bindir}/bash,' %{buildroot}%{_bindir}/tomboy

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
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

%post
%gconf_schema_upgrade tomboy

%pre
%gconf_schema_prepare tomboy

%preun
%gconf_schema_remove tomboy

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%dir %{_libdir}/%{name}
%{_bindir}/tomboy
%{_libdir}/tomboy/*
%{_datadir}/dbus-1/services/org.gnome.Tomboy.service
%{_mandir}/man1/tomboy.1.gz
%{_datadir}/tomboy
%{_datadir}/icons/hicolor/*/apps/tomboy.*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/tomboy.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/tomboy.desktop
%{_sysconfdir}/gconf/schemas/tomboy.schemas

%files devel
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
