%global source0_hash ccc169b8e240828b36965dfd84fa1478957dec2028ffeba553ae97e542e15120
%global branch 1.28
Name:          eom
Version:       %{branch}.1
Release:        1%{?dist}
Summary:        Eye of MATE image viewer
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ 
URL:           http://mate-desktop.org 
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1:        eom_0001-configure-Only-use-girepository-2.0-if-libpeas-uses-.patch
Requires:      mate-desktop-libs
Requires:      libpeas-loader-python3
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  desktop-file-utils
BuildRequires:  exempi-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  lcms2-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpeas1-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Eye of MATE (eom) is the official image viewer for the
MATE desktop. It can view single image files in a variety of formats, as
well as large image collections.
Eye of Mate is extensible through a plugin system.

%package devel
Summary:  Support for developing plugins for the eom image viewer
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for eom

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Patch1 + generating autotools files
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
   --with-x \
   --disable-schemas-compile \
   --enable-introspection=yes \
   --enable-thumbnailer \
   --without-gdk-pixbuf-thumbnailer
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                               \
  --delete-original                                \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
$RPM_BUILD_ROOT%{_datadir}/applications/eom.desktop
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n eom-devel -f %{oreon_filedir}/eom-devel.list

%changelog

%autochangelog
