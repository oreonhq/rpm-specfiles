%global source1_hash f8d200b0b97e0c1650d119ab4a85039402b5ec5676a7fd10813638ba86491e43
%global source0_hash ca550826e30fee9d6ccfc621ddd0e4c430d440f51cdfcbebe623cedfe64fd805
%bcond thumbnailer %[0%{?fedora} >= 41]
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}
Summary:        Image browser and viewer
Name: geeqie
License: GPL-2.0-or-later
Version: 3.1
Release:        1%{?dist}
URL: https://www.geeqie.org
%if %{defined gitcommit}
Source0:        https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
%else
Source1: https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2: 91EC400226201276E2ADCEC7D0DA6F44C936D1DA.gpg
%endif
ExcludeArch: %{ix86}
%if %{with thumbnailer}
%endif
Requires:      exiv2
Requires:      fbida
Requires:      ImageMagick
Requires:      zenity
# oreon:deps
BuildRequires:  /usr/bin/xxd
BuildRequires:  ImageMagick
BuildRequires:  LibRaw-devel
BuildRequires:  cfitsio-devel
BuildRequires:  clutter-devel
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  evince
BuildRequires:  exiv2
BuildRequires:  exiv2-devel
BuildRequires:  fbida
BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnome-doc-utils
BuildRequires:  gnupg2
BuildRequires:  gspell-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  lcms2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel
BuildRequires:  libchamplain-devel
BuildRequires:  libheif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  lirc-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  openexr-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  webp-pixbuf-loader
BuildRequires:  yelp-tools
BuildRequires:  zenity
# /oreon:deps
%description
Geeqie has been forked from the GQview project with the goal of picking up
development and integrating patches. It is an image viewer for browsing
through graphics files. Its many features include single click file viewing,
support for external editors, previewing images using thumbnails, and zoom.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 %{?gitcommit:-n %{name}-%{gitcommit}}

%build

for f in exiftran exiv2 mogrify zenity ; do
    type $f || exit 1
done
export CXXFLAGS="$CXXFLAGS -Wno-deprecated-declarations -Wno-unused-variable -Wno-unused-but-set-variable -Wno-unused-parameter"
%meson %{!?with_thumbnailer: -Dvideothumbnailer=disabled}
%meson_build
%install
%meson_install
cp -av %{_vpath_builddir}/doc/html %{buildroot}%{_pkgdocdir}/
test -f %{buildroot}%{_pkgdocdir}/html/index.html
install -p -m 0644 COPYING NEWS README* \
    %{buildroot}%{_pkgdocdir}
ln -s NEWS %{buildroot}%{_pkgdocdir}/ChangeLog
desktop-file-install \
    --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/org.geeqie.Geeqie.desktop
%find_lang %name
mv %{buildroot}/usr/share/metainfo %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/org.geeqie.Geeqie.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
