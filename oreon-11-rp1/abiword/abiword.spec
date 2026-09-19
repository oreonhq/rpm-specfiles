%global source0_hash ef2fdc2cb66a54a58185e7008bd349ce858e59648e18571913d5a3e2b43abf37

%define bigversion 3.0

%global forgeurl https://gitlab.gnome.org/World/AbiWord

Name: abiword
Version: 3.0.8
Release: 2%{?dist}
%global tag release-%{version}
%forgemeta

Epoch: 1
Summary: Word processing program
License: GPL-2.0-or-later
URL: %{forgeurl}

Source0: %{forgesource}
Source11: abiword.mime
Source12: abiword.keys
Source13: abiword.xml

ExcludeArch:    %{ix86}

Patch0: abiword-2.6.0-windowshelppaths.patch
Patch1: abiword-2.8.3-desktop.patch
Patch2: abiword-2.6.0-boolean.patch
Patch4: abiword-3.0.2-explicit-python.patch
Patch5: abiword-3.0.4-pygobject.patch
Patch6: boost-includes.patch

BuildRequires: aiksaurus-devel
BuildRequires: aiksaurus-gtk-devel
BuildRequires: asio-devel
# Needed while explicit-python.patch touches gi-overrides/Makefile.am
BuildRequires: automake autoconf libtool autoconf-archive
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: flex
BuildRequires: fribidi-devel
BuildRequires: gcc-c++
BuildRequires: gobject-introspection-devel
BuildRequires: goffice-devel
BuildRequires: gtk3-devel
# Probably because it's gtk2 based
#BuildRequires: gtkmathview-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgsf-devel
BuildRequires: libpng-devel
BuildRequires: librevenge-devel
BuildRequires: librsvg2-devel
BuildRequires: libsoup-devel
BuildRequires: libwmf-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: libxslt-devel
BuildRequires: link-grammar-devel
BuildRequires: loudmouth-devel
BuildRequires: ots-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: pkgconfig(libwps-0.4)
BuildRequires: poppler-devel
BuildRequires: popt-devel
BuildRequires: python3-gobject
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: readline-devel
BuildRequires: t1lib-devel
BuildRequires: telepathy-glib-devel
BuildRequires: wv-devel
BuildRequires: zlib-devel
BuildRequires: make
BuildRequires: libappstream-glib

Requires: libabiword = %{epoch}:%{version}-%{release}
Requires: python3-gobject-base

%description
AbiWord is a cross-platform Open Source word processor. It is full-featured,
while still remaining lean.

%package -n libabiword
Summary: Library for developing applications based on AbiWord's core

%description -n libabiword
Library for developing applications based on AbiWord's core.

%package -n libabiword-devel
Summary: Files for developing with libabiword
Requires: libabiword = %{epoch}:%{version}-%{release}

%description -n libabiword-devel
Includes and definitions for developing with libabiword.

%package -n python3-abiword
%{?python_provide:%python_provide python3-abiword}
Summary: Python bindings for developing with libabiword
Requires: libabiword = %{epoch}:%{version}-%{release}

%description -n python3-abiword
Python bindings for developing with libabiword

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# setup abiword
%setup -qn AbiWord-release-%{version}

# patch abiword
%patch -P 1 -p1 -b .desktop
%patch -P 2 -p1 -b .boolean
%patch -P 4 -p1 -b .explicit_python
%patch -P 5 -p1 -b .pygo
%patch -P 6 -p0 -b .boost

%build
# Needed while explicit-python.patch touches gi-overrides/Makefile.am
./autogen.sh

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS -DASIO_ENABLE_BOOST"
%configure \
  --enable-plugins --enable-clipart --enable-templates --enable-introspection \
  --with-gir-dir=%{_datadir}/gir-1.0 --with-typelib-dir=%{_libdir}/girepository-1.0 \
  --enable-maintainer-mode
%{make_build} V=1

%install
%{make_install} overridesdir=%{python3_sitelib}/gi/overrides

install -p -m 0644 -D %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/mime-info/abiword.mime
install -p -m 0644 -D %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/mime-info/abiword.keys
install -p -m 0644 -D %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/mime/packages/abiword.xml

# Remove libtool archives and static libs
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

mv %{buildroot}%{_datadir}/applications/abiword.desktop %{buildroot}%{_datadir}/applications/com.abisource.AbiWord.desktop

mkdir -p %{buildroot}%{_metainfodir}/
mv %{buildroot}%{_datadir}/appdata/abiword.appdata.xml %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/abiword.appdata.xml

%ldconfig_scriptlets -n libabiword

%files
%{_bindir}/abiword
%{_metainfodir}/abiword.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/mime-info/abiword.mime
%{_datadir}/mime-info/abiword.keys
%{_datadir}/mime/packages/abiword.xml
%{_datadir}/icons/hicolor/*/apps/abiword.png
%{_datadir}/icons/hicolor/scalable/apps/abiword.svg
%{_mandir}/man1/abiword.1*

%files -n libabiword
%license COPYING COPYRIGHT.TXT
%{_libdir}/libabiword-%{bigversion}.so
%{_libdir}/libAiksaurusGtk3*
%{_libdir}/%{name}-%{bigversion}
%{_libdir}/girepository-1.0/Abi-3.0.typelib
%{_datadir}/%{name}-%{bigversion}
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%{_datadir}/telepathy/clients/AbiCollab.client

%files -n libabiword-devel
%{_includedir}/%{name}-%{bigversion}
%{_libdir}/pkgconfig/%{name}-%{bigversion}.pc
%{_datadir}/gir-1.0/Abi-3.0.gir

%files -n python3-abiword
%pycached %{python3_sitelib}/gi/overrides/Abi.py

%changelog
%autochangelog
