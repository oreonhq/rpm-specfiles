%global source0_hash 22914e48ef48f894bb5143c5efc3d01ab96e0a0cde80de11058d3b4301377d34

Name:           dia
Version:        0.97.3
Release:        32%{?dist}
Epoch:          1
Summary:        Diagram drawing program
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Dia
Source0:        https://download.gnome.org/sources/dia/0.97/%{name}-%{version}.tar.xz
# Upstream from https://gitlab.gnome.org/GNOME/dia/-/commit/baa2df853f9fb770eedcf3d94c7f5becebc90bb9
Patch0:         https://gitlab.gnome.org/GNOME/dia/-/commit/baa2df853f9fb770eedcf3d94c7f5becebc90bb9.patch#/dia-0.97.3-cve-2019-19451.patch
# Downstream patch
Patch1:         dia-configure-c99.patch
# Backport from https://gitlab.gnome.org/GNOME/dia/-/commit/f57ea2685034ddbafc19f35d9b525a12283d7c24
Patch2:         dia-0.97.3-get_data_size.patch
# Upstream from https://gitlab.gnome.org/GNOME/dia/-/commit/e5557aa1d396bc3ca80240f7b5c0a1831a5cf209
Patch3:         https://gitlab.gnome.org/GNOME/dia/-/commit/e5557aa1d396bc3ca80240f7b5c0a1831a5cf209.patch#/dia-0.97.3-const-ft_vector.patch
# Backport from https://gitlab.gnome.org/GNOME/dia/-/commit/caddfcab250fe677ecf294fad835b71e6b10cf26
Patch4:         dia-0.97.3-g_test_add_data_func_1.patch
# Backport from https://gitlab.gnome.org/GNOME/dia/-/commit/9c481f649414190bf8d6741cbca1777e9766756b
Patch5:         dia-0.97.3-g_test_add_data_func_2.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libart-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  freetype-devel
BuildRequires:  intltool
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
The Dia drawing program can be used to draw different types of diagrams,
and includes support for UML static structure diagrams (class diagrams),
entity relationship modeling, and network diagrams.  Dia can load and
save diagrams to a custom XML format and export diagrams to formats like
EPS, SVG, XFIG, PDF, PNG and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i 's|libdia_la_LDFLAGS = -avoid-version|libdia_la_LDFLAGS = -avoid-version $(shell pkg-config --libs gtk+-2.0 libxml-2.0 libart-2.0)|' \
  lib/Makefile.*
chmod -x `find objects/AADL -type f`
iconv -f WINDOWS-1252 -t UTF8 doc/en/usage-layers.xml > usage-layers.xml.UTF-8
mv usage-layers.xml.UTF-8 doc/en/usage-layers.xml

# run in single window mode (--integrated) by default (#910275)
sed -i 's|Exec=dia|Exec=dia --integrated|' dia.desktop.in.in

%build
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
# gtk2 GtkItemFactoryCallback is not compatible with latest C
export CFLAGS="$CFLAGS -std=gnu17"
%endif

%configure --enable-db2html --disable-silent-rules
%make_build

%install
%make_install
%find_lang %{name} --with-man

# below is the desktop file and icon stuff.
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  --remove-category Application                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -f samples/Makefile*

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=710955
SentUpstream: 2013-10-27
-->
<application>
  <id type="desktop">dia.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Dia is a GTK+ based diagram creation program</summary>
  <description>
    <p>
      Dia is roughly inspired by the commercial Windows program 'Visio,' though
      more geared towards informal diagrams for casual use.
      It can be used to draw many different kinds of diagrams.
      It currently has special objects to help draw entity relationship diagrams,
      UML diagrams, flowcharts, network diagrams, and many other diagrams.
      It is also possible to add support for new shapes by writing simple XML files,
      using a subset of SVG to draw the shape.
    </p>
    <p>
      It can load and save diagrams to a custom XML format (gzipped by default,
      to save space), can export diagrams to a number of formats, including EPS,
      SVG, XFIG, WMF and PNG, and can print diagrams (including ones that span
      multiple pages).
    </p>
  </description>
  <url type="homepage">https://wiki.gnome.org/Apps/Dia</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/dia/a.png</screenshot>
  </screenshots>
  <updatecontact>dia-list@gnome.org</updatecontact>
</application>
EOF

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog KNOWN_BUGS NEWS README THANKS
%doc doc/custom-shapes doc/diagram.dtd doc/shape.dtd doc/sheet.dtd samples/
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime-info/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
%autochangelog
