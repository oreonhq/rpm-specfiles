%global source0_hash 0d0349e58f180719909768e11d909c96c9b7bbdf6bd98cd21a77ec6470f3580c

%if (0%{?fedora} || 0%{?rhel} < 8) && ! 0%{?flatpak}
%global _with_qt4      1
%endif

%global commit0	   5a07df503a6f01280f493cbcc2aace462b9dee57
%global commitdate 20150629

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:	QFile extension with advisory locking functions
Name:		qtlockedfile
Version:	2.4
Release:	46.%{commitdate}git%{shortcommit0}%{?dist}

# most files has BSD-3-Clause
# project declared license is GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1
License:	BSD-3-Clause AND (GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1)
URL:		http://doc.qt.digia.com/solutions/4/qtlockedfile/qtlockedfile.html
Source0:	https://github.com/qtproject/qt-solutions/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Source1:	qtlockedfile.prf.in
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source2:	LICENSE.LGPL
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source3:	LGPL_EXCEPTION
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source4:	LICENSE.GPL3
%{?_with_qt4:BuildRequires:	qt4-devel}
BuildRequires: make
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt6-qtbase-devel

%description
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.

%if 0%{?_with_qt4}
%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt4-devel

%description devel
This package contains libraries and header files for developing applications
that use QtLockedFile.
%endif

%package qt5
Summary:	QFile extension with advisory locking functions (Qt5)
Requires:	qt5-qtbase

%description qt5
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.
This is a special build against Qt5.

%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	qt5-qtbase-devel

%description qt5-devel
This package contains libraries and header files for developing applications
that use QtLockedFile with Qt5.

%package qt6
Summary:	QFile extension with advisory locking functions (Qt6)
Requires:	qt6-qtbase

%description qt6
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.
This is a special build against Qt6.

%package qt6-devel
Summary:	Development files for %{name}-qt6
Requires:	%{name}-qt6 = %{version}-%{release}
Requires:	qt6-qtbase-devel

%description qt6-devel
This package contains libraries and header files for developing applications
that use QtLockedFile with Qt6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn qt-solutions-%{commit0}/%{name}
# use versioned soname
sed -i s,head,%{version}, common.pri
# do not build example source
sed -i /example/d %{name}.pro
mkdir licenses
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} licenses

%build
# Does not use GNU configure
./configure -library
%if 0%{?_with_qt4}
%{qmake_qt4}
%make_build
sed -e 's|@QT_INCLUDEDIR@|%{_qt4_headerdir}|' %{SOURCE1} > qtlockedfile.prf
%endif
mkdir qt5
pushd qt5
%{qmake_qt5} ..
%make_build
sed -e 's|@QT_INCLUDEDIR@|%{_qt5_headerdir}|' %{SOURCE1} > qtlockedfile.prf
popd
mkdir qt6
pushd qt6
%{qmake_qt6} ..
%make_build
sed -e 's|@QT_INCLUDEDIR@|%{_qt6_headerdir}|' %{SOURCE1} > qtlockedfile.prf
popd

%install
# libraries
mkdir -p %{buildroot}%{_libdir}
cp -ap lib/* %{buildroot}%{_libdir}

# headers
%if 0%{?_with_qt4}
mkdir -p %{buildroot}%{_qt4_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt4_headerdir}/QtSolutions
install -p -D -m644 qtlockedfile.prf %{buildroot}%{_qt4_datadir}/mkspecs/features/qtlockedfile.prf
%endif
mkdir -p %{buildroot}%{_qt5_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt5_headerdir}/QtSolutions
install -p -D -m644 qt5/qtlockedfile.prf %{buildroot}%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf
mkdir -p %{buildroot}%{_qt6_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt6_headerdir}/QtSolutions
install -p -D -m644 qt6/qtlockedfile.prf %{buildroot}%{_qt6_archdatadir}/mkspecs/features/qtlockedfile.prf

%if 0%{?_with_qt4}
%files
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt4_libdir}/libQtSolutions_LockedFile*.so.*

%files devel
%doc doc/html/ example/
%{_qt4_headerdir}/QtSolutions/
%{_qt4_libdir}/libQtSolutions_LockedFile*.so
%{_qt4_datadir}/mkspecs/features/qtlockedfile.prf
%endif

%files qt5
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt5_libdir}/libQt5Solutions_LockedFile*.so.*

%files qt5-devel
%doc doc/html/ example/
%{_qt5_headerdir}/QtSolutions/
%{_qt5_libdir}/libQt5Solutions_LockedFile*.so
%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf

%files qt6
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt6_libdir}/libQt6Solutions_LockedFile*.so.*

%files qt6-devel
%doc doc/html/ example/
%{_qt6_headerdir}/QtSolutions/
%{_qt6_libdir}/libQt6Solutions_LockedFile*.so
%{_qt6_archdatadir}/mkspecs/features/qtlockedfile.prf

%changelog
%autochangelog
