%global source0_hash 2e8b145669afa0e93833e4064b657677abc9413e4007fa5ddc91397c9bddc295

Summary: Multimedia framework api for Qt4
Name:    phonon-qt4
Version: 4.10.3
Release: 29%{?dist}
License: LGPL-2.0-or-later
URL:     https://community.kde.org/Phonon

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/phonon/%{version}/phonon-%{version}.tar.xz

## upstream patches

## upstreamable patches
# avoid rpath
Patch10: phonon-rpath_use_link_path.patch
# avoid gcc errors/warnings about use of deprecated _BSD_SOURCE (use _DEFAULT_SOURCE instead) 
Patch11: phonon-DEFAULT_SOURCE.patch

Patch12: phonon-qt4-fix_cmake.patch

# filter plugins
%global __provides_exclude_from ^(%{_qt4_plugindir}/.*\\.so)$

BuildRequires: make
BuildRequires: automoc4 >= 0.9.86
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kde4-macros(api)
BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpulse-mainloop-glib) > 0.9.15
BuildRequires: pkgconfig(libxml-2.0)
# Qt4
BuildRequires: pkgconfig(QtDBus)
BuildRequires: pkgconfig(QtDesigner)
BuildRequires: pkgconfig(QtOpenGL)
# added explict dep, despite qt-devel already depending on it
BuildRequires: gcc-c++

Requires: kde-filesystem
Recommends: phonon-qt4-backend-gstreamer%{?_isa}

# phonon -> phonon-qt4 transition
Obsoletes: phonon < 4.10.3-10
Provides:  phonon = %{version}-%{release}
Provides:  phonon%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package devel
Summary: Developer files for phonon
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: phonon-devel < 4.10.3-10
Provides:  phonon-devel = %{version}-%{release}
Provides:  phonon-devel%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n phonon-%{version}

%patch -P10 -p1 -b .10
%patch -P11 -p1 -b .11
%patch -P12 -p1 -b .12


%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DCMAKE_DISABLE_FIND_PACKAGE_QZeitgeist:BOOL=ON \
  -DPHONON_BUILD_DECLARATIVE_PLUGIN:BOOL=OFF \
  -DPHONON_INSTALL_QT_COMPAT_HEADERS:BOOL=ON \
  -DPHONON_QT_IMPORTS_INSTALL_DIR=%{_qt4_importdir} \
  -DPHONON_QT_MKSPECS_INSTALL_DIR=%{_qt4_datadir}/mkspecs/modules \
  -DPHONON_QT_PLUGIN_INSTALL_DIR=%{_qt4_plugindir}/designer

%cmake_build


%install
%cmake_install

# own these dirs
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/plugins/phonon_backend/
mkdir -p %{buildroot}%{_kde4_datadir}/kde4/services/phononbackends/
mkdir -p %{buildroot}%{_qt5_plugindir}/phonon4qt5_backend


%check
export PKG_CONFIG_PATH="%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig${PKG_CONFIG_PATH:+:}${PKG_CONFIG_PATH}"
test "$(pkg-config --modversion phonon)" = "%{version}"

%files
%license COPYING.LIB
%{_libdir}/libphonon.so.4*
%{_libdir}/libphononexperimental.so.4*
%{_qt4_plugindir}/designer/libphononwidgets.so
%dir %{_datadir}/phonon/
%dir %{_kde4_libdir}/kde4/plugins/phonon_backend/
%dir %{_kde4_datadir}/kde4/services/phononbackends/

# https://bugzilla.redhat.com/show_bug.cgi?id=1223956
# replacing symlink with a dir
%pretrans devel -p <lua>
path = "%{_includedir}/phonon/Phonon"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files devel
%license %{_datadir}/phonon/buildsystem/COPYING-CMAKE-SCRIPTS
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%{_datadir}/phonon/buildsystem/
%{_libdir}/cmake/phonon/
%dir %{_includedir}/KDE
%{_includedir}/KDE/Phonon/
%{_includedir}/phonon/
%{_libdir}/pkgconfig/phonon.pc
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_qt4_datadir}/mkspecs/modules/qt_phonon.pri

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.10.3-29
- Prepare for Oreon 11 (RP1)
