%global source0_hash 78b05bfac92bef099209aa56fdf4ca4558172583752f6736450fc0368bde01df

%?mingw_package_header

%global qt_module qtquickcontrols
#global pre beta

#global commit 9f085b889524a80d4064d6ac01dbdc817bb31060
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        2%{?dist}
Summary:        Qt5 for Windows - QtQuickControls component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}
BuildRequires:  mingw32-qt5-qmldevtools-devel = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}
BuildRequires:  mingw64-qt5-qmldevtools-devel = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls component
Requires:       mingw32-qt5-qtdeclarative

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-static
Summary:       Static version of the mingw32-qt5-qtquickcontrols library
Requires:      mingw32-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw32-qt5-qtbase-static
Requires:      mingw32-qt5-qtdeclarative-static

%description -n mingw32-qt5-%{qt_module}-static
Static version of the mingw32-qt5-qtquickcontrols library.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls component
Requires:       mingw64-qt5-qtdeclarative

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-static
Summary:       Static version of the mingw64-qt5-qtquickcontrols library
Requires:      mingw64-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw64-qt5-qtbase-static
Requires:      mingw64-qt5-qtdeclarative-static

%description -n mingw64-qt5-%{qt_module}-static
Static version of the mingw64-qt5-qtquickcontrols library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif

%build
MINGW_BUILDDIR_SUFFIX=_static %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=static
MINGW_BUILDDIR_SUFFIX=_static %mingw_make_build

MINGW_BUILDDIR_SUFFIX=_shared %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=shared
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_build

%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make install INSTALL_ROOT=%{buildroot}
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make install INSTALL_ROOT=%{buildroot}

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%dir %{mingw32_libdir}/qt5/qml/QtQuick/
%{mingw32_libdir}/qt5/qml/QtQuick/Controls/
%{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/
%{mingw32_libdir}/qt5/qml/QtQuick/Extras/
%{mingw32_libdir}/qt5/qml/QtQuick/PrivateWidgets/
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

%files -n mingw32-qt5-%{qt_module}-static
%{mingw32_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%dir %{mingw64_libdir}/qt5/qml/QtQuick/
%{mingw64_libdir}/qt5/qml/QtQuick/Controls/
%{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/
%{mingw64_libdir}/qt5/qml/QtQuick/Extras/
%{mingw64_libdir}/qt5/qml/QtQuick/PrivateWidgets/
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

%files -n mingw64-qt5-%{qt_module}-static
%{mingw64_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

%changelog
%autochangelog
