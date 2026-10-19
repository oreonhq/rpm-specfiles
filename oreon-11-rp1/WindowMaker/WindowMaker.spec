%global source0_hash 4fe130ba23cf4aa21c156ec8f01f748df537d0604ec06c6bbcec896df1926f6d
Summary:        A fast, feature rich Window Manager
Name:           WindowMaker
Version:        0.96.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.windowmaker.org 
Source0:        https://github.com/window-maker/wmaker/releases/download/wmaker-%{version}/%{name}-%{version}.tar.gz
Source3:        WindowMaker-WMRootMenu-fedora
Requires:       WINGs-libs = %{version}-%{release}
Requires:       desktop-backgrounds-compat
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  fontconfig-devel
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  git-core
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Window Maker is an X11 window manager designed to give additional
integration support to the GNUstep Desktop Environment. In every way
possible, it reproduces the elegant look and feel of the NEXTSTEP GUI.
It is fast, feature rich, easy to configure, and easy to use. In
addition, Window Maker works with GNOME and KDE, making it one of the
most useful and universal window managers available.

%package devel
Summary:        Development files for WindowMaker
Requires:       WindowMaker = %{version}-%{release}
Requires:       WINGs-devel = %{version}-%{release}
%description devel
Development files for WindowMaker.

%package -n WINGs-libs
Summary:        Widgets and image libraries needed for WindowMaker
%description -n WINGs-libs
Widgets and image libraries needed for WindowMaker.

%package -n WINGs-devel
Summary:        Development files for the WINGs library
Requires:       WINGs-libs = %{version}-%{release}
Requires:       libX11-devel
Requires:       xorg-x11-proto-devel
Requires:       libXinerama-devel
Requires:       libXrandr-devel
Requires:       libXext-devel
Requires:       libtiff-devel
Requires:       zlib-devel
Requires:       libXpm-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       giflib-devel
Requires:       libXft-devel
Requires:       fontconfig-devel
%description -n WINGs-devel
Development files for the WINGs library.

%package extra
Summary:        Extra themes and Icons for WindowMaker
Requires:       WindowMaker = %{version}-%{release}
BuildArch:      noarch
%description extra
This is the extra data package for Window Maker. For now it only contains some
icons and a few themes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

# cleanup menu entries
for i in WindowMaker/*menu*; do
echo $i
sed -i.old -e 's:/usr/local/:%{_prefix}/:g' \
  -e 's:/home/mawa:$(HOME):g' \
  -e 's:GNUstep/Applications/WPrefs.app:bin:g' $i
done

for i in util/wmgenmenu.c WindowMaker/Defaults/WindowMaker.in WPrefs.app/Paths.c; do
echo $i
sed -i.old -e  's:/usr/local/:%{_prefix}/:g'  $i
done

# fix utf8 issues
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

for i in doc/cs/geticonset.1 doc/cs/seticons.1 doc/cs/wdwrite.1 doc/cs/wmaker.1 \
 doc/cs/wmsetbg.1 doc doc/cs/wxcopy.1 doc/cs/wxpaste.1 doc/sk/geticonset.1 \
 doc/sk/seticons.1 doc/sk/wdwrite.1 doc/sk/wmaker.1 doc/sk/wmsetbg.1 \
 doc/sk/wxcopy.1 doc/sk/wxpaste.1; do
echo $i
iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i
done

autoreconf -vfi -I m4

%build

CFLAGS="$RPM_OPT_FLAGS -DNEWAPPICON"
LINGUAS=`(cd po ; echo *.po | sed 's/.po//g')`
NLSDIR="%{_datadir}/locale"
export CFLAGS LINGUAS NLSDIR
%configure \
 --disable-static \
 --enable-modelock \
 --enable-randr \
 --enable-xinerama \
 --enable-usermenu \
 --enable-pango \
 --enable-wmreplace \
 --x-includes=%{_includedir} \
 --x-libraries=%{_libdir}
%make_build
%install
%make_install NLSDIR=%{_datadir}/locale
%find_lang '\(WPrefs\|WindowMaker\|WINGs\|wmgenmenu\|WRaster\)'
install -D -m0644 -p %{SOURCE3} \
%{buildroot}%{_sysconfdir}/WindowMaker/WMRootMenu
sed -i \
  -e 's:WorkspaceBack = (solid:WorkspaceBack = (mpixmap, "/usr/share/backgrounds/default.png":' \
  %{buildroot}%{_sysconfdir}/WindowMaker/WindowMaker
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod 755 %{buildroot}%{_datadir}/WindowMaker/{autostart.sh,exitscript.sh}
chmod 644 util/wmiv.{c,h}
for f in wmaker wdwrite wdread getstyle setstyle convertfonts seticons \
    geticonset wmsetbg wmagnify wmgenmenu wmmenugen WPrefs \
    wmiv wxcopy wxpaste ; do
  chrpath --delete %{buildroot}%{_bindir}/$f
done
chrpath --delete %{buildroot}%{_libdir}/libWINGs.so.3.2.0
chrpath --delete %{buildroot}%{_libdir}/libwraster.so.6.1.0
chrpath --delete %{buildroot}%{_libdir}/libWMaker.so.1.0.1
%ldconfig_scriptlets
%ldconfig_scriptlets -n WINGs-libs
%oreon_autofiles WindowMaker-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles WINGs-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles WINGs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles WindowMaker-extra usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n WindowMaker-devel -f %{oreon_filedir}/WindowMaker-devel.list
%files -n WINGs-libs -f %{oreon_filedir}/WINGs-libs.list
%files -n WINGs-devel -f %{oreon_filedir}/WINGs-devel.list
%files -n WindowMaker-extra -f %{oreon_filedir}/WindowMaker-extra.list

%changelog

%autochangelog
