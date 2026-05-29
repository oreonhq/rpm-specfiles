%global source0_hash none

## uncomment to enable bootstrap mode
#global bootstrap 1

## currently includes no tests
%if !0%{?bootstrap}
# skip slower archs for now
%ifnarch %{arm}
%global tests 1
%endif
%endif

%global qt_module qtscript

Summary: Qt5 - QtScript component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/official_releases/qt/%{version}/submodules/qtscript-everywhere-opensource-src-%{version}.tar.xz
## upstream patches

## downstream patches
# add s390(x0 support to Platform.h (taken from webkit)
Patch100: qtscript-everywhere-src-5.12.1-s390.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

# qtwebkit version from 2011/01/27, probably has a lot of CVEs.
Provides: bundled(javascriptcore) = 0~snapshot110127

%if ! 0%{?bootstrap}
# extra examples
BuildRequires: pkgconfig(Qt5UiTools)
%endif

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: mesa-dri-drivers
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-private-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

#patch100 -p1 -b .s390


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

# workaround serious failures when building with f28's gcc8
# https://bugzilla.redhat.com/show_bug.cgi?id=1551246
# if 0%%{?fedora} > 27
%if 0
export CXXFLAGS="$RPM_OPT_FLAGS -O1"
%endif

%qmake_qt5

%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl file love (maybe consider just deleting these -- rex
# nuke dangling reference(s) to %%buildroot, excessive (.la-like) libs
sed -i \
  -e "/^QMAKE_PRL_BUILD_DIR/d" \
  -e "/^QMAKE_PRL_LIBS/d" \
  %{buildroot}%{_qt5_libdir}/*.prl

## unpackaged files
# .la files, die, die, die.
rm -fv %{buildroot}%{_qt5_libdir}/lib*.la


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt5_libdir}
## do in %%build ?
%make_build -k sub-tests-all ||:
timeout 180 \
xvfb-run -a \
time \
%make_build check -k -C tests ||:
if [ "$?" -eq "124" ]; then
echo 'make check timeout reached!'
exit 1
fi
%endif


%ldconfig_scriptlets

%files
%license LICENSE.LGPL*
%{_qt5_libdir}/libQt5Script.so.5*
%{_qt5_libdir}/libQt5ScriptTools.so.5*

%files devel
%{_qt5_headerdir}/Qt*/
%{_qt5_libdir}/libQt5Script.so
%{_qt5_libdir}/libQt5Script.prl
%{_qt5_libdir}/libQt5ScriptTools.so
%{_qt5_libdir}/libQt5ScriptTools.prl
%dir %{_qt5_libdir}/cmake/Qt5Script/
%{_qt5_libdir}/cmake/Qt5Script/Qt5ScriptConfig*.cmake
%dir %{_qt5_libdir}/cmake/Qt5ScriptTools/
%{_qt5_libdir}/cmake/Qt5ScriptTools/Qt5ScriptToolsConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5*.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%{_qt5_examplesdir}/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
