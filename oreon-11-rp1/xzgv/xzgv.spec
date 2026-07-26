%global source0_hash 25a240bb8c4a85c3979ce1a39c81c859724b490c1fd83dd4e3ef1db053ee819e

Summary:         Picture viewer
Name:            xzgv
Version:         0.9.2
Release:         24%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
URL:             http://sourceforge.net/projects/xzgv/
Source0:         http://downloads.sourceforge.net/xzgv/xzgv-%{version}.tar.gz
Patch0:          xzgv-0.9-fix-doc-install.patch
Patch1:          xzgv-0.9-fix-thumbnail-generation.patch
Patch2:          0001-Fix-xzgv-man-page-so-it-is-valid-nroff.patch
BuildRequires:   desktop-file-utils
BuildRequires:   gcc
BuildRequires:   gtk2-devel
BuildRequires:   libexif-devel
BuildRequires:   libpng-devel
BuildRequires:   make
BuildRequires:   texinfo
Requires:        gdk-pixbuf2-modules-extra
Requires:        gnome-icon-theme
Requires:        xterm
%description 
A picture viewer with a thumbnail-based file selector.  Many file
formats are supported, and the thumbnails used are compatible with xv,
zgv and the Gimp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for f in ChangeLog NEWS; do
  iconv -f iso8859-1 -t utf8 $f -o $f.txt
  touch -r $f.txt $f
  mv $f.txt $f
done

%build
sed -i 's|^CFLAGS.*|CFLAGS=%{optflags} -std=gnu17|' config.mk
make %{?_smp_flags}
make info

cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=xzgv Image Viewer
Comment=View different types of images
Exec=xzgv
Icon=xzgv
Terminal=false
Type=Application
Categories=GTK;Graphics;RasterGraphics;Viewer;
EOF

%install
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -d -m 0755 %{buildroot}%{_datadir}/pixmaps

make PREFIX=%{buildroot}/%{_prefix} \
     MANDIR=%{buildroot}/%{_mandir}/man1 \
     INFODIR=%{buildroot}/%{_infodir} \
     DESKTOPDIR2=%{buildroot}%{_datadir}/applications \
     install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}/%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/xzgv/feature-requests/5/
-->
<application>
  <id type="desktop">xzgv.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Simple image viewer</summary>
  <description>
    <p>
      xzgv is a simple image editor, with a focus on controlling all actions
      using keyboard input.
      It has a simple, two pane layout, with all the thumbnails of the current
      directory listed in the left pane, and the image viewed in the main pane.
      The menu in xzgv can be viewed in a context menu that is shown by
      right-clicking on the main image pane.
      This context menu also lists all the keyboard shortcuts if you are new to
      xzgv and need to know them.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/xzgv/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/xzgv/a.png</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc AUTHORS NEWS README TODO ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_infodir}/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/xzgv.xpm

%changelog
%autochangelog
