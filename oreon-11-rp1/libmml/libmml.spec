%global source0_hash c2a0cc9a2ea700620badb807ef4095bba9a2cff85aa8fa1cb8819332849fd280

%global commit c77c438c0992cd36f163a1abcc51181cc29a3322
%global gittag %{commit}
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global commitdate 20260127

%bcond_without qt6

%if 0%{?fedora} < 44
%bcond_without qt4
%else
%bcond_with qt4
%endif

Name:           libmml
Version:        2.4
Release:        27.%{commitdate}git%{shortcommit}%{?dist}
Summary:        MML Widget
License:        GPL-3.0-only OR LGPL-2.1-only WITH Qt-LGPL-exception-1.1
URL:            https://github.com/copasi/copasi-dependencies/tree/master/src/mml
Source0:        https://gitlab.com/anto.trande/mml/-/archive/%{commit}/mml-%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)

%description
The QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

############### QT6 ######################
%if %{with qt6}
%package        qt6
Summary:        Qt6/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Qwt6)
Buildrequires:  qt6-rpm-macros
Requires:       pkgconfig(Qt6)
Provides:       libqtmmlwidget-qt6%{?_isa} = %{version}-%{release}

%description    qt6
The Qt5 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}

%description    qt6-devel
The %{name}-qt6-devel package contains Qt6 libraries and header files for
developing applications that use %{name}.
%endif

############### QT5 ######################
%package        qt5
Summary:        Qt5/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qwt6)
Buildrequires:  qt5-rpm-macros, qt5-qtbase-devel
Requires:       pkgconfig(Qt5Core)
Provides:       libqtmmlwidget%{?_isa} = %{version}-%{release}

%description    qt5
The Qt5 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains Qt5 libraries and header files for
developing applications that use %{name}.

############### QT4 ######################
%if %{with qt4}
%package        qt4
Summary:        Qt4/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt)
BuildRequires:  pkgconfig(qwt5-qt4)
Requires:       pkgconfig(QtCore)
Provides:       libqtmmlwidget-qt4%{?_isa} = %{version}-%{release}

%description    qt4
The Qt4 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt4-devel
Summary:        Development files for %{name}-qt4
Requires:       %{name}-qt4%{?_isa} = %{version}-%{release}

%description    qt4-devel
The %{name}-qt4-devel package contains Qt4 libraries and header files for
developing applications that use %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc -n mml-%{commit}

mv mml-%{commit} qt5
%if %{with qt4}
cp -a qt5 qt4
%endif
%if %{with qt6}
cp -a qt5 qt6
%endif

%build
############### QT6 ######################
%if %{with qt6}
pushd qt6
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev \
 -DSELECT_QT=Qt6 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt6 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt) \
 -DQWT_LIBRARY:FILEPATH=%{_qt6_libdir}/libqwt.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt6_headerdir}/qwt \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt6_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt6_headerdir}/%{name}-qt6
%cmake_build
popd
%endif

############### QT5 ######################
pushd qt5
# -Werror=format-security/ flag prevents compilation
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev \
 -DSELECT_QT=Qt5 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt5 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt) \
 -DQWT_LIBRARY:FILEPATH=%{_qt5_libdir}/libqwt-qt5.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt5_headerdir}/qwt \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt5_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt5_headerdir}/%{name}-qt5
%cmake_build
popd

############### QT4 ######################
%if %{with qt4}
pushd qt4
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev \
 -DSELECT_QT=Qt4 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt4 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt5-qt4) \
 -DQWT_LIBRARY:FILEPATH=%{_qt4_libdir}/libqwt5-qt4.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt4_headerdir}/qwt5-qt4 \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt4_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt4_headerdir}/%{name}-qt4
%cmake_build
popd
%endif

%install
############### QT6 ######################
%if %{with qt6}
pushd qt6
%cmake_install
popd
%endif

############### QT5 ######################
pushd qt5
%cmake_install
popd

############### QT4 ######################
%if %{with qt4}
pushd qt4
%cmake_install
popd
%endif

############### QT6 ######################
%if %{with qt6}
%files qt6
%license qt6/LGPL_EXCEPTION.txt qt6/LICENSE.LGPL
%{_qt6_libdir}/%{name}-qt6.so.*

%files qt6-devel
%{_qt6_headerdir}/%{name}-qt6/
%{_qt6_libdir}/%{name}-qt6.so
%endif

############### QT5 ######################
%files qt5
%license qt5/LGPL_EXCEPTION.txt qt5/LICENSE.LGPL
%{_qt5_libdir}/%{name}.so.*

%files qt5-devel
%dir %{_qt5_headerdir}
%{_qt5_headerdir}/%{name}-qt5/
%{_qt5_libdir}/%{name}.so

############### QT4 ######################
%if %{with qt4}
%files qt4
%license qt4/LGPL_EXCEPTION.txt qt4/LICENSE.LGPL
%{_qt4_libdir}/%{name}-qt4.so.*

%files qt4-devel
%{_qt4_headerdir}/%{name}-qt4/
%{_qt4_libdir}/%{name}-qt4.so
%endif

%changelog
%autochangelog
