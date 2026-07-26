%global source0_hash 469b72cf5cac11fd1c71eb22b396fd8da862cf602ae3fb6115a97774d679cb55

%if (0%{?fedora} || 0%{?rhel} < 8) && ! 0%{?flatpak}
%global _with_qt4      1
%endif

%global commit0 ad9bc4600ce769a8b3ad10910803cd555811b70c

Summary:    Qt library to start applications only once per user
Name:       qtsingleapplication
Version:    2.6.1
Release:    53%{?dist}

# most files has BSD-3-Clause
# project declared license is GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1
License:	BSD-3-Clause AND (GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1)
URL:        http://doc.qt.digia.com/solutions/4/qtsingleapplication/qtsingleapplication.html
Source0:    https://github.com/qtproject/qt-solutions/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
# Proposed upstream in https://codereview.qt-project.org/#/c/92417/
Source1:    qtsingleapplication.prf.in
# Proposed upstream in https://codereview.qt-project.org/#/c/92416/
Source2:    qtsinglecoreapplication.prf.in
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source3:    LICENSE.GPL3
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source4:    LICENSE.LGPL
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source5:    LGPL_EXCEPTION

# Proposed upstream in https://codereview.qt-project.org/#/c/92416/
Patch0:     qtsingleapplication-build-qtsinglecoreapplication.patch
# Proposed upstream in https://codereview.qt-project.org/#/c/92415/
Patch1:     qtsingleapplication-remove-included-qtlockedfile.patch

# Features for unbundling in Qupzilla, https://github.com/QupZilla/qupzilla/issues/1503
Patch2:     qtsingleapplication-qupzilla.patch

%{?_with_qt4:BuildRequires: qt4-devel qtlockedfile-devel}
BuildRequires: make
BuildRequires: qt5-qtbase-devel qtlockedfile-qt5-devel
BuildRequires: qt6-qtbase-devel qtlockedfile-qt6-devel

%description
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.

%if 0%{?_with_qt4}
%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt4-devel

%description devel
This package contains libraries and header files for developing applications
that use QtSingleApplication.

%package -n qtsinglecoreapplication
Summary:    Qt library to start applications only once per user
Requires:   qt4

%description -n qtsinglecoreapplication
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

%package -n qtsinglecoreapplication-devel
Summary:    Development files for qtsinglecoreapplication
Requires:   qtsinglecoreapplication = %{version}-%{release}
Requires:   qt4-devel

%description -n qtsinglecoreapplication-devel
This package contains libraries and header files for developing applications
that use QtSingleCoreApplication.
%endif

%package qt5
Summary:    Qt5 library to start applications only once per user
Requires:   qt5-qtbase

%description qt5
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

This is a special build against Qt5.

%package qt5-devel
Summary:    Development files for %{name}-qt5
Requires:   %{name}-qt5 = %{version}-%{release}
Requires:   qt5-qtbase-devel

%description qt5-devel
This package contains libraries and header files for developing applications
that use QtSingleApplication with Qt5.

%package -n qtsinglecoreapplication-qt5
Summary:    Qt library to start applications only once per user (Qt5)
Requires:   qt5-qtbase

%description -n qtsinglecoreapplication-qt5
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

This is a special build against Qt5.

%package -n qtsinglecoreapplication-qt5-devel
Summary:    Development files for qtsinglecoreapplication-qt5
Requires:   qtsinglecoreapplication-qt5 = %{version}-%{release}
Requires:   qt5-qtbase-devel

%description -n qtsinglecoreapplication-qt5-devel
This package contains libraries and header files for developing applications
that use QtSingleCoreApplication.

%package qt6
Summary:    Qt6 library to start applications only once per user
Requires:   qt6-qtbase

%description qt6
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

This is a special build against Qt6.

%package qt6-devel
Summary:    Development files for %{name}-qt6
Requires:   %{name}-qt6 = %{version}-%{release}
Requires:   qt6-qtbase-devel

%description qt6-devel
This package contains libraries and header files for developing applications
that use QtSingleApplication with Qt6.

%package -n qtsinglecoreapplication-qt6
Summary:    Qt library to start applications only once per user (Qt6)
Requires:   qt6-qtbase

%description -n qtsinglecoreapplication-qt6
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

This is a special build against Qt6.

%package -n qtsinglecoreapplication-qt6-devel
Summary:    Development files for qtsinglecoreapplication-qt6
Requires:   qtsinglecoreapplication-qt6 = %{version}-%{release}
Requires:   qt6-qtbase-devel

%description -n qtsinglecoreapplication-qt6-devel
This package contains libraries and header files for developing applications
that use QtSingleCoreApplication.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qnqt-solutions-%{commit0}/%{name}
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1
# use versioned soname
sed -i "s,head,%(echo '%{version}' |sed -r 's,(.*)\..*,\1,'),g" common.pri

mkdir licenses
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} licenses

# We already disabled bundling this external library.
# But just to make sure:
rm -rf ../qtlockedfile/
rm src/{QtLocked,qtlocked}*

sed -e 's|@QT_INCLUDEDIR@|%{_qt4_headerdir}|' %{SOURCE1} > qtsingleapplication.prf
sed -e 's|@QT_INCLUDEDIR@|%{_qt4_headerdir}|' %{SOURCE2} > qtsinglecoreapplication.prf

mkdir qt5
sed -e 's|@QT_INCLUDEDIR@|%{_qt5_headerdir}|' %{SOURCE1} > qt5/qtsingleapplication.prf
sed -e 's|@QT_INCLUDEDIR@|%{_qt5_headerdir}|' %{SOURCE2} > qt5/qtsinglecoreapplication.prf

mkdir qt6
sed -e 's|@QT_INCLUDEDIR@|%{_qt6_headerdir}|' %{SOURCE1} > qt6/qtsingleapplication.prf
sed -e 's|@QT_INCLUDEDIR@|%{_qt6_headerdir}|' %{SOURCE2} > qt6/qtsinglecoreapplication.prf

%build
# Does not use GNU configure
./configure -library
%if 0%{?_with_qt4}
%{qmake_qt4}
%make_build
%endif

# Qt5
pushd qt5
%if 0%{?flatpak}
# qmake does not search mkspecs in /app
cat %{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf >> ../common.pri
%endif
# additional header needed for Qt5.5
sed -i -r 's,.include,\0 <QDataStream>\n\0,' ../src/qtlocalpeer.cpp
%{qmake_qt5} ..
%make_build
popd

# Qt6
pushd qt6
# additional header needed for Qt6
sed -i -r 's,.include,\0 <QRegularExpression>\n\0,' ../src/qtlocalpeer.cpp
sed -i 's,QRegExp,QRegularExpression,g' ../src/qtlocalpeer.cpp
%{qmake_qt6} ..
%make_build
popd

%install
# libraries
mkdir -p %{buildroot}%{_libdir}
cp -a lib/* %{buildroot}%{_libdir}
chmod 755 %{buildroot}%{_libdir}/*.so*

# headers
%if 0%{?_with_qt4}
mkdir -p %{buildroot}%{_qt4_headerdir}/QtSolutions  %{buildroot}%{_qt4_datadir}/mkspecs/features
cp -ap \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    %{buildroot}%{_qt4_headerdir}/QtSolutions
install -p -m644 *.prf %{buildroot}%{_qt4_datadir}/mkspecs/features
%endif
mkdir -p %{buildroot}%{_qt5_headerdir}/QtSolutions %{buildroot}%{_qt5_archdatadir}/mkspecs/features
cp -ap \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    %{buildroot}%{_qt5_headerdir}/QtSolutions
install -p -m644 qt5/*.prf %{buildroot}%{_qt5_archdatadir}/mkspecs/features

mkdir -p %{buildroot}%{_qt6_headerdir}/QtSolutions %{buildroot}%{_qt6_archdatadir}/mkspecs/features
cp -ap \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    %{buildroot}%{_qt6_headerdir}/QtSolutions
install -p -m644 qt6/*.prf %{buildroot}%{_qt6_archdatadir}/mkspecs/features

%if 0%{?_with_qt4}
%files
%license licenses/*
%doc README.TXT
# Caution! Unversioned .so file goes into -devel
%{_qt4_libdir}/libQtSolutions_SingleApplication*.so.*

%files devel
%doc doc/html/ examples/
%{_qt4_libdir}/libQtSolutions_SingleApplication*.so
%dir %{_qt4_headerdir}/QtSolutions/
%{_qt4_headerdir}/QtSolutions/QtSingleApplication
%{_qt4_headerdir}/QtSolutions/%{name}.h
%{_qt4_datadir}/mkspecs/features/qtsingleapplication.prf

%files -n qtsinglecoreapplication
%license licenses/*
# Caution! Unversioned .so file goes into -devel
%{_qt4_libdir}/libQtSolutions_SingleCoreApplication*.so.*

%files -n qtsinglecoreapplication-devel
%{_qt4_libdir}/libQtSolutions_SingleCoreApplication*.so
%dir %{_qt4_headerdir}/QtSolutions/
%{_qt4_headerdir}/QtSolutions/QtSingleCoreApplication
%{_qt4_headerdir}/QtSolutions/qtsinglecoreapplication.h
%{_qt4_datadir}/mkspecs/features/qtsinglecoreapplication.prf
%endif

%files qt5
%license licenses/*
%doc README.TXT
# Caution! Unversioned .so file goes into -devel
%{_qt5_libdir}/libQt5*SingleApplication*.so.*

%files qt5-devel
%doc doc/html/ examples/
%{_qt5_libdir}/libQt5*SingleApplication*.so
%dir %{_qt5_headerdir}/QtSolutions/
%{_qt5_headerdir}/QtSolutions/QtSingleApplication
%{_qt5_headerdir}/QtSolutions/%{name}.h
%{_qt5_archdatadir}/mkspecs/features/qtsingleapplication.prf

%files -n qtsinglecoreapplication-qt5
%license licenses/*
# Caution! Unversioned .so file goes into -devel
%{_qt5_libdir}/libQt5*SingleCoreApplication*.so.*

%files -n qtsinglecoreapplication-qt5-devel
%{_qt5_libdir}/libQt5*SingleCoreApplication*.so
%dir %{_qt5_headerdir}/QtSolutions/
%{_qt5_headerdir}/QtSolutions/QtSingleCoreApplication
%{_qt5_headerdir}/QtSolutions/qtsinglecoreapplication.h
%{_qt5_archdatadir}/mkspecs/features/qtsinglecoreapplication.prf

%files qt6
%license licenses/*
%doc README.TXT
# Caution! Unversioned .so file goes into -devel
%{_qt6_libdir}/libQt6*SingleApplication*.so.*

%files qt6-devel
%doc doc/html/ examples/
%{_qt6_libdir}/libQt6*SingleApplication*.so
%dir %{_qt6_headerdir}/QtSolutions/
%{_qt6_headerdir}/QtSolutions/QtSingleApplication
%{_qt6_headerdir}/QtSolutions/%{name}.h
%{_qt6_archdatadir}/mkspecs/features/qtsingleapplication.prf

%files -n qtsinglecoreapplication-qt6
%license licenses/*
# Caution! Unversioned .so file goes into -devel
%{_qt6_libdir}/libQt6*SingleCoreApplication*.so.*

%files -n qtsinglecoreapplication-qt6-devel
%{_qt6_libdir}/libQt6*SingleCoreApplication*.so
%dir %{_qt6_headerdir}/QtSolutions/
%{_qt6_headerdir}/QtSolutions/QtSingleCoreApplication
%{_qt6_headerdir}/QtSolutions/qtsinglecoreapplication.h
%{_qt6_archdatadir}/mkspecs/features/qtsinglecoreapplication.prf

%changelog
%autochangelog
