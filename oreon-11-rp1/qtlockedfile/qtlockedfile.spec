%global source0_hash 0d0349e58f180719909768e11d909c96c9b7bbdf6bd98cd21a77ec6470f3580c
%global commit0	   5a07df503a6f01280f493cbcc2aace462b9dee57
%global commitdate 20150629
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Summary:        QFile extension with advisory locking functions
Name:		qtlockedfile
Version:	2.4
Release:        1%{?dist}
License:	BSD-3-Clause AND (GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1)
URL:		http://doc.qt.digia.com/solutions/4/qtlockedfile/qtlockedfile.html
Source0:        https://github.com/qtproject/qt-solutions/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Source1:	qtlockedfile.prf.in
Source2:	LICENSE.LGPL
Source3:	LGPL_EXCEPTION
Source4:	LICENSE.GPL3
%{?_with_qt4:BuildRequires:	qt4-devel}
# oreon:deps
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_libdir}
cp -ap lib/* %{buildroot}%{_libdir}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if 0%{?_with_qt4}
%files -f %{oreon_filedir}/main.list
%files -n qtlockedfile-qt5 -f %{oreon_filedir}/qtlockedfile-qt5.list
%files -n qtlockedfile-qt5-devel -f %{oreon_filedir}/qtlockedfile-qt5-devel.list
%files -n qtlockedfile-qt6 -f %{oreon_filedir}/qtlockedfile-qt6.list
%files -n qtlockedfile-qt6-devel -f %{oreon_filedir}/qtlockedfile-qt6-devel.list

%changelog

%autochangelog
%endif
