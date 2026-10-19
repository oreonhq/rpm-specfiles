%global source0_hash 67fb03bf6ca3e0bdbd98d374dfb5b1651a07d17ae6c23e11a81b4b084447e7c6
%undefine __cmake_in_source_build
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global docs 1
Name:            polkit-qt
Version:         0.112.0
Release:        1%{?dist}
Summary:        Qt bindings for PolicyKit
License:         GPL-2.0-or-later
URL:             https://projects.kde.org/projects/kdesupport/polkit-qt-1 
Source0:        http://download.kde.org/stable/apps/KDE4.x/admin/polkit-qt-1-%{version}.tar.bz2
Source1:         Doxyfile
Patch0:          polkit-qt-0.95.1-install-cmake-find.patch
Patch1: 0001-do-not-use-global-static-systembus-instance.patch
Patch2: 0002-fix-build-with-Qt4-which-doesn-t-have-QStringLiteral.patch
Patch3: 0003-Fix-QDBusArgument-assertion.patch
Patch5: 0005-Add-wrapper-for-polkit_system_bus_name_get_user_sync.patch
Patch6: 0006-Drop-use-of-deprecated-Qt-functions.patch
Patch7: 0007-Fix-compilation-with-Qt5.6.patch
Patch8: 0008-Allow-compilation-with-older-polkit-versions.patch
Source10:        macros.polkit-qt
%if 0%{?docs}
%endif
Obsoletes:       polkit-qt-examples < 0.10
# oreon:deps
BuildRequires:  automoc4
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtXml)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
# /oreon:deps
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
%global oreon_srcdir %{name}-1-%{version}
%oreon_prep
%build

%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DUSE_QT4:BOOL=ON -DUSE_QT5:BOOL=OFF \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DDATA_INSTALL_DIR:PATH=%{_datadir}
%cmake_build
%if 0%{?docs}
doxygen %{SOURCE1}
rm -fv html/installdox
%endif
%install
%cmake_install
install -p -m644 -D %{SOURCE10} %{buildroot}%{rpm_macros_dir}/macros.polkit-qt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n polkit-qt-devel -f %{oreon_filedir}/polkit-qt-devel.list
%files -n polkit-qt-doc -f %{oreon_filedir}/polkit-qt-doc.list

%changelog

%autochangelog
