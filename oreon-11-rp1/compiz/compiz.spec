%global source0_hash e87018b2d6c9ab3da87d910b117a7ae35f64328eea485e6c2a532501b361144c
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with bootstrap
%global    core_plugins    blur clone cube decoration fade ini inotify minimize move place png regex resize rotate scale screenshot switcher water wobbly zoom fs obs commands wall annotate svg matecompat
%global    plugins         core,dbus,decoration,fade,minimize,move,obs,place,png,resize,scale,screenshot,svg,switcher,wall
Name:           compiz
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Version:        0.8.18
Release:        1%{?dist}
Epoch:          1
Summary:        OpenGL window and compositing manager
URL:            https://gitlab.com/compiz/compiz-core
Source0:        https://gitlab.com/%{name}/%{name}-core/-/archive/v%{version}/%{name}-core-v%{version}.tar.bz2
Patch0:        compiz-0.8.18-fedora-logo.patch
Patch1:        compiz-0.8.18-rsvg2-2.52-fix.patch
Patch2:        compiz-0.8.18-gcc-14-fix.patch
Patch3:        compiz-0.8.18-libxml-2.12-fix.patch
%if %{without bootstrap}
%endif
Requires:      glx-utils
Obsoletes: %{name}-xfce < %{epoch}:%{version}-%{release}
Obsoletes: %{name}-lxde < %{epoch}:%{version}-%{release}
Obsoletes: %{name}-mate < %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fuse-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtool
BuildRequires:  libwnck3-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  marco-devel
BuildRequires:  mesa-libGLU-devel
# /oreon:deps
%description
Compiz is one of the first OpenGL-accelerated compositing window
managers for the X Window System. The integration allows it to perform
compositing effects in window management, such as a minimization
effect and a cube work space. Compiz is an OpenGL compositing manager
that use Compiz use EXT_texture_from_pixmap OpenGL extension for
binding redirected top-level windows to texture objects.

%package devel
Summary: Development packages for compiz
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
Requires: libXcomposite-devel libXfixes-devel libXdamage-devel libXrandr-devel
Requires: libXinerama-devel libICE-devel libSM-devel libxml2-devel
Requires: libxslt-devel startup-notification-devel
%description devel
The compiz-devel package includes the header files,
and developer docs for the compiz package.
Install compiz-devel if you want to develop plugins for the compiz
windows and compositing manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir compiz-core-v%{version}
%oreon_prep
%build

./autogen.sh
%configure \
    --with-gtk=3.0 \
    --enable-librsvg \
    --enable-gtk \
    --enable-marco \
    --enable-menu-entries \
    --with-default-plugins=%{plugins}
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                              \
    --delete-original                             \
    --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%find_lang %{name}
cat %{name}.lang > core-files.txt
for f in %{core_plugins}; do
  echo %{_libdir}/compiz/lib$f.so
  echo %{_datadir}/compiz/$f.xml
done >> core-files.txt
mkdir -p %{buildroot}%{_datadir}/compiz/icons/hicolor/{scalable/{apps,\
categories},22x22/{categories,devices,mimetypes}}
%ldconfig_scriptlets
%oreon_autofiles compiz-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n compiz-devel -f %{oreon_filedir}/compiz-devel.list

%changelog

%autochangelog
