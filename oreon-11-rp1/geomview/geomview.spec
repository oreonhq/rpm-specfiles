%global source0_hash fa46920e7d06d5f14bf889711fb5977f7827a2e4993f71a4f225723a795f43d9
%global commit  1d6759ec9771fbc6bdc71ec79b7a5a28711cd9fd
%global date    20190630
%global forgeurl https://github.com/geomview/geomview
%global __brp_compress %{nil}
Name:           geomview
Summary:        Interactive 3D viewing program
Version:        1.9.5
%forgemeta
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Release:        1%{?dist}
URL:            http://www.geomview.org/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        org.geomview.geomview.desktop
Source2:        org.geomview.geomview.metainfo.xml
Source10:       application_x-geomview.xml
Source20:       hi16-app-geomview.png
Source21:       hi22-app-geomview.png
Source22:       hi32-app-geomview.png
Source23:       hi48-app-geomview.png
Source24:       hi64-app-geomview.png
Source25:       hi128-app-geomview.png
Source26:       hisc-app-geomview.svg
Patch:          %{forgeurl}/pull/2.patch
Patch:          %{forgeurl}/pull/3.patch
Patch:          %{forgeurl}/pull/4.patch
Patch:          %{forgeurl}/pull/5.patch
Patch:          %{name}-zlib-ng.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gzip
Requires:       netpbm-progs
Requires:       xdg-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  motif-devel
BuildRequires:  netpbm-progs
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  xdg-utils
# /oreon:deps
%description
Geomview is an interactive 3D viewing program for Unix. It lets you view and
manipulate 3D objects: you use the mouse to rotate, translate, zoom in and out,
etc. It can be used as a standalone viewer for static objects or as a display
engine for other programs which produce dynamically changing geometry. It can
display objects described in a variety of file formats. It comes with a wide
selection of example objects, and you can create your own objects too.

%package        libs
Summary:        Geomview runtime libraries
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%conf
# Fix a shebang
sed -i '1s,:,#!%{_bindir}/perl,' src/bin/geomutil/hvectext/hvectext.in

# Generate the configure script
autoreconf -fi .

%build

%configure \
  --enable-shared \
  --disable-static \
  --with-htmlbrowser=xdg-open \
  --with-pdfviewer=xdg-open \
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/org.geomview.geomview.metainfo.xml
install -p -m644 -D %{SOURCE10} %{buildroot}%{_datadir}/mime/packages/x-geomview.xml
install -p -m644 -D %{SOURCE20} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/geomview.png
install -p -m644 -D %{SOURCE21} %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/geomview.png
install -p -m644 -D %{SOURCE22} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/geomview.png
install -p -m644 -D %{SOURCE23} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/geomview.png
install -p -m644 -D %{SOURCE24} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/geomview.png
install -p -m644 -D %{SOURCE25} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/geomview.png
install -p -m644 -D %{SOURCE26} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/geomview.svg
rm -fv %{buildroot}%{_infodir}/dir
for f in %{buildroot}%{_infodir}/geomview*; do
  mv $f $f.info
done
gzip -9v \
     %{buildroot}%{_infodir}/*.info \
     %{buildroot}%{_mandir}/man1/* \
     %{buildroot}%{_mandir}/man3/* \
     %{buildroot}%{_mandir}/man5/* \
%fdupes %{buildroot}%{_prefix}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n geomview-libs -f %{oreon_filedir}/geomview-libs.list
%files -n geomview-devel -f %{oreon_filedir}/geomview-devel.list

%changelog

%autochangelog
