%global source0_hash 311f3a2603e1973bb59baef9dfa740a376de713157d4782ee043681e889c9260
%global qt_module qtdeclarative
%define _lto_cflags %{nil}
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
Summary:        Qt6 - QtDeclarative component
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
Source5:        qv4global_p-multilib.h
%global __provides_exclude_from ^%{_qt6_qmldir}/.*\\.so$
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%if 0%{?tests}
%endif
Obsoletes:     qt6-qtquickcontrols2 < 6.2.0~beta3-1
Provides:      qt6-qtquickcontrols2 = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-x11
BuildRequires:  gcc-c++
BuildRequires:  mesa-dri-drivers
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtlanguageserver-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  time
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Provides:  %{name}-private-devel = %{version}-%{release}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  qt6-qtbase-devel%{?_isa}
Obsoletes: qt6-qtquickcontrols2-devel < 6.2.0~beta3-1
Provides:  qt6-qtquickcontrols2-devel = %{version}-%{release}
%description devel
%{summary}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Obsoletes: qt6-qtquickcontrols2-examples < 6.2.0~beta3-1
Provides:  qt6-qtquickcontrols2-examples = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

%build

ln -s %{__python3} python
export PATH=`pwd`:$PATH
%cmake_qt6 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}
%cmake_build
%install
%cmake_install
%ifarch %{multilib_archs}
  mv %{buildroot}%{_qt6_headerdir}/QtQml/%{qt_version}/QtQml/private/qv4global_p.h \
     %{buildroot}%{_qt6_headerdir}/QtQml/%{qt_version}/QtQml/private/qv4global_p-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt6_headerdir}/QtQml/%{qt_version}/QtQml/private/qv4global_p.h
%endif
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qmlcachegen|qmlleasing|qmlformat|qmleasing|qmlimportscanner|qmllint| \
    qmlpreview|qmlscene|qmltestrunner|qmltyperegistrar|qmlplugindump| \
    qmlprofiler|qml|qmlbundle|qmlmin|qmltime)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  rm -fv "$(basename ${prl_file} .prl).la"
  sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
done
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt6_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt6_libdir}
make sub-tests-all %{?_smp_mflags}
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make check -k -C tests ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n qt6-qtdeclarative-devel -f %{oreon_filedir}/qt6-qtdeclarative-devel.list
%files -n qt6-qtdeclarative-static -f %{oreon_filedir}/qt6-qtdeclarative-static.list
%files -n qt6-qtdeclarative-examples -f %{oreon_filedir}/qt6-qtdeclarative-examples.list

%changelog

%autochangelog
