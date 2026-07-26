%global source0_hash 67fb03bf6ca3e0bdbd98d374dfb5b1651a07d17ae6c23e11a81b4b084447e7c6

%undefine __cmake_in_source_build

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%global docs 1

Name:            polkit-qt
Version:         0.112.0
Release:         34%{?dist}
Summary:         Qt bindings for PolicyKit

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
URL:             https://projects.kde.org/projects/kdesupport/polkit-qt-1 
Source0:         http://download.kde.org/stable/apps/KDE4.x/admin/polkit-qt-1-%{version}.tar.bz2 
Source1:         Doxyfile

# temporary patch - installs FindPolkitQt-1.cmake until we decide how to deal with cmake
# module installation
Patch0:          polkit-qt-0.95.1-install-cmake-find.patch

## upstream patches
Patch1: 0001-do-not-use-global-static-systembus-instance.patch
Patch2: 0002-fix-build-with-Qt4-which-doesn-t-have-QStringLiteral.patch
Patch3: 0003-Fix-QDBusArgument-assertion.patch
Patch5: 0005-Add-wrapper-for-polkit_system_bus_name_get_user_sync.patch
Patch6: 0006-Drop-use-of-deprecated-Qt-functions.patch
Patch7: 0007-Fix-compilation-with-Qt5.6.patch
Patch8: 0008-Allow-compilation-with-older-polkit-versions.patch

Source10:        macros.polkit-qt

BuildRequires:   automoc4
BuildRequires:   cmake
%if 0%{?docs}
BuildRequires:   doxygen
%endif
BuildRequires:   gcc-c++
BuildRequires:   pkgconfig(polkit-agent-1) pkgconfig(polkit-gobject-1)
BuildRequires:   pkgconfig(QtDBus) pkgconfig(QtGui) pkgconfig(QtXml)

Obsoletes:       polkit-qt-examples < 0.10

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package devel
Summary: Development files for PolicyKit Qt bindings
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Doxygen documentation for the PolkitQt API
BuildArch: noarch
%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-1-%{version} -p1

%build
%cmake \
  -DUSE_QT4:BOOL=ON -DUSE_QT5:BOOL=OFF \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DDATA_INSTALL_DIR:PATH=%{_datadir}

%cmake_build

%if 0%{?docs}
## build docs
doxygen %{SOURCE1}
# Remove installdox file - it is not necessary here
rm -fv html/installdox
%endif

%install
%cmake_install

install -p -m644 -D %{SOURCE10} %{buildroot}%{rpm_macros_dir}/macros.polkit-qt

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README
%license COPYING
%{_libdir}/libpolkit-qt-core-1.so.1*
%{_libdir}/libpolkit-qt-gui-1.so.1*
%{_libdir}/libpolkit-qt-agent-1.so.1*

%files devel
%{rpm_macros_dir}/macros.polkit-qt
%{_includedir}/polkit-qt-1/
%{_libdir}/libpolkit-qt-core-1.so
%{_libdir}/libpolkit-qt-gui-1.so
%{_libdir}/libpolkit-qt-agent-1.so
%{_libdir}/pkgconfig/polkit-qt-1.pc
%{_libdir}/pkgconfig/polkit-qt-core-1.pc
%{_libdir}/pkgconfig/polkit-qt-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt-agent-1.pc
%{_libdir}/cmake/PolkitQt-1/
%{_datadir}/cmake/Modules/*.cmake

%if 0%{?docs}
%files doc
%doc html/*
%endif

%changelog
%autochangelog
