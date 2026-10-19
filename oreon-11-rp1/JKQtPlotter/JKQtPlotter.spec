%global source0_hash 1a5cd3e84493f969bfaea5e761e28b128b978cb8a18df8c83240f39922e82825
%global gitcommit d243218119b1632987df26baea0d4bc6ccdee533
%global gitdate 20251013
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%bcond_without qt5
Name:           JKQtPlotter
Version:        5.0.0~beta2
Release:        1%{?dist}
Summary:        An extensive Qt6 Plotter framework
License:        LGPL-2.1-or-later AND OFL-1.1
URL:            https://github.com/jkriege2/JKQtPlotter
Source0:        https://github.com/jkriege2/%{name}/archive/%{gitcommit}.tar.gz
Requires:       %{name}-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  CImg-devel
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
Extensive Qt6 Plotter framework
(including a feature-rich plotter widget,
a speed-optimized, but limited variant and
a LaTeX equation renderer!), written fully
in C/C++ and without external dependencies.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with qt5}
%package        -n %{name}-qt5
Summary:        An extensive Qt5 Plotter framework
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
Requires:       %{name}-doc = %{version}-%{release}
%description    -n %{name}-qt5
Extensive Qt5 Plotter framework
(including a feature-rich plotter widget,
a speed-optimized, but limited variant and
a LaTeX equation renderer!), written fully
in C/C++ and without external dependencies.

%package        -n %{name}-qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
%description    -n %{name}-qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name}-qt5.
%endif

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
Contains documentation files for the usage of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qc

%if %{with qt5}
cp -a %{name}-%{gitcommit} %{name}-qt5-%{gitcommit}
cp -p %{name}-%{gitcommit}/lib/jkqtmathtext/resources/firaMath/LICENSE \
      %{name}-%{gitcommit}/lib/jkqtmathtext/resources/firaMath/LICENSE-firaMath
%endif

%build

pushd %{name}-%{gitcommit}
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
       -DCMAKE_PREFIX_PATH:PATH=/usr/%{_lib}/cmake/Qt6 \
       -DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF
%cmake_build
popd
%if %{with qt5}
pushd %{name}-qt5-%{gitcommit}
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
       -DCMAKE_PREFIX_PATH:PATH=/usr/%{_lib}/cmake/Qt5 \
       -DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF
%cmake_build
popd
%endif
%install
pushd %{name}-%{gitcommit}
%cmake_install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/
rm -rf %{buildroot}%{_bindir}
popd
%if %{with qt5}
pushd %{name}-qt5-%{gitcommit}
%cmake_install
mkdir -p %{buildroot}%{_libexecdir}/%{name}-qt5
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}-qt5/
rm -rf %{buildroot}%{_bindir}
popd
%oreon_autofiles JKQtPlotter-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles JKQtPlotter-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles JKQtPlotter-qt5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles JKQtPlotter-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

pushd %{name}-%{gitcommit}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest -V -E test_jkqtpdatastore
popd
%if %{with qt5}
pushd %{name}-qt5-%{gitcommit}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest -V -E test_jkqtpdatastore
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n JKQtPlotter-devel -f %{oreon_filedir}/JKQtPlotter-devel.list
%files -n JKQtPlotter-qt5 -f %{oreon_filedir}/JKQtPlotter-qt5.list
%files -n JKQtPlotter-qt5-devel -f %{oreon_filedir}/JKQtPlotter-qt5-devel.list
%files -n JKQtPlotter-doc -f %{oreon_filedir}/JKQtPlotter-doc.list

%changelog

%autochangelog
