%global source0_hash 5240f4a3475648773ba10af8b0ebe549cbfc5d6de00470a517330a80068a4f78
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_with	qt4
%bcond_without	qt5
%bcond_without	qt6
%else
%bcond_without	qt4
%bcond_without	qt5
%bcond_without	qt6
%endif
%bcond_without test
%global QUAZIP_LIB_VERSION %{version} 
%global QUAZIP_LIB_SOVERSION 1.7
Name:		quazip
Version:	1.7.2
Release:        1%{?dist}
Summary:        Qt/C++ wrapper for the minizip library
License:	GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+
URL:		https://github.com/stachenov/quazip
Source0:        https://github.com/stachenov/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	FindQuaZip.cmake
%if %{with qt4}
%endif
%if %{with qt5}
%endif
%if %{with qt6}
%endif
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%if %{with qt4}
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	bzip2-devel%{?_isa}
Requires:	qt4-devel%{?_isa}
Requires:	zlib-devel%{?_isa}
%description devel
The %{name}-devel package contains libraries, header files and documentation
for developing applications that use %{name}. 
%endif

%if %{with qt5}
%package qt5
Summary: Qt5 wrapper for the minizip library
%description qt5
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5%{?_isa} = %{version}-%{release}
Requires:	bzip2-devel%{?_isa}
Requires:	qt5-qtbase-devel%{?_isa}
Requires:	zlib-devel%{?_isa}
%description qt5-devel
The %{name}-qt5-devel package contains libraries, header files and documentation
for developing applications that use %{name}-qt5.
%endif

%if %{with qt6}
%package qt6
Summary: Qt6 wrapper for the minizip library
%description qt6
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package qt6-devel
Summary:	Development files for %{name}-qt6
Requires:	%{name}-qt6%{?_isa} = %{version}-%{release}
Requires:	bzip2-devel%{?_isa}
Requires:	qt6-qtbase-devel%{?_isa}
Requires:	qt6-qt5compat-devel%{?_isa}
Requires:	zlib-devel%{?_isa}
%description qt6-devel
The %{name}-qt6-devel package contains libraries, header files and documentation
for developing applications that use %{name}-qt6.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with qt4}
%global _vpath_builddir build-qt4
%cmake -DQUAZIP_QT_MAJOR_VERSION=4 -DQUAZIP_ENABLE_TESTS=ON
%cmake_build
%endif
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake -DQUAZIP_QT_MAJOR_VERSION=5 -DQUAZIP_ENABLE_TESTS=ON
%cmake_build
%endif
%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake -DQUAZIP_QT_MAJOR_VERSION=6 -DQUAZIP_ENABLE_TESTS=ON
%cmake_build
%endif
doxygen Doxyfile
for file in doc/html/*; do
	touch -r Doxyfile $file
done
%install
%if %{with qt4}
%global _vpath_builddir build-qt4
%cmake_install
%endif
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake_install
%endif
%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake_install
%endif
%if %{with qt4}
ln -s libquazip1-qt4.so %{buildroot}%{_libdir}/libquazip.so
install -d %{buildroot}%{_includedir}/quazip
pushd %{buildroot}%{_includedir}/QuaZip-Qt4-%{version}/quazip
for f in *; do
	ln -s ../QuaZip-Qt4-%{version}/quazip/$f %{buildroot}%{_includedir}/quazip/$f
done
popd
install -d %{buildroot}%{_datadir}/cmake/Modules
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/cmake/Modules/FindQuaZip.cmake
%endif
%if %{with qt5}
ln -s libquazip1-qt5.so %{buildroot}%{_libdir}/libquazip5.so
install -d %{buildroot}%{_includedir}/quazip5
pushd %{buildroot}%{_includedir}/QuaZip-Qt5-%{version}/quazip
for f in *; do
	ln -s ../QuaZip-Qt5-%{version}/quazip/$f %{buildroot}%{_includedir}/quazip5/$f
done
popd
install -d %{buildroot}%{_datadir}/cmake/Modules
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/cmake/Modules/FindQuaZip5.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if %{with test}
%check

export LC_ALL=C.UTF-8
export QT_ENABLE_REGEXP_JIT=0
%if %{with qt4}
%global _vpath_builddir build-qt4
%ctest
%endif
%if %{with qt5}
%global _vpath_builddir build-qt5
%ctest
%endif
%if %{with qt6}
%global _vpath_builddir build-qt6
%ctest
%endif
%endif
%if %{with qt4}
%files -f %{oreon_filedir}/main.list
%files -n quazip-devel -f %{oreon_filedir}/quazip-devel.list
%files -n quazip-qt5 -f %{oreon_filedir}/quazip-qt5.list
%files -n quazip-qt5-devel -f %{oreon_filedir}/quazip-qt5-devel.list
%files -n quazip-qt6 -f %{oreon_filedir}/quazip-qt6.list
%files -n quazip-qt6-devel -f %{oreon_filedir}/quazip-qt6-devel.list

%changelog

%autochangelog
%endif
