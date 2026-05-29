%global source0_hash none

# Bug: https://bugzilla.redhat.com/show_bug.cgi?id=2061194
%define _lto_cflags %{nil}

%global qt_module qtdeclarative

# definition borrowed from qtbase
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9

#global bootstrap 1

Summary: Qt5 - QtDeclarative component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/official_releases/qt/%{qt5_version}/submodules/qtdeclarative-everywhere-opensource-src-%{qt5_version}.tar.xz
# header file to workaround multilib issue
# https://bugzilla.redhat.com/show_bug.cgi?id=1441343
Source5: qv4global_p-multilib.h

## upstream patches
## repo: https://invent.kde.org/qt/qt/qtdeclarative
## branch: kde/5.15
## git format-patch v5.15.18-lts-lgpl
Patch0:  0001-Remove-unused-QPointer-QQuickPointerMask.patch
Patch1:  0002-QQmlDelegateModel-Refresh-the-view-when-a-column-is-.patch
Patch2:  0003-Fix-TapHandler-so-that-it-actually-registers-a-tap.patch
Patch3:  0004-Revert-Fix-TapHandler-so-that-it-actually-registers-.patch
Patch4:  0005-Make-sure-QQuickWidget-and-its-offscreen-window-s-sc.patch
Patch5:  0006-Don-t-convert-QByteArray-in-startDrag.patch
Patch6:  0007-Fix-build-after-95290f66b806a307b8da1f72f8fc2c698019.patch
Patch7:  0008-Implement-accessibility-for-QQuickWidget.patch
Patch8:  0009-Send-ObjectShow-event-for-visible-components-after-i.patch
Patch9:  0010-QQuickItem-avoid-emitting-signals-during-destruction.patch
Patch10: 0011-a11y-track-item-enabled-state.patch
Patch11: 0012-Make-QaccessibleQuickWidget-private-API.patch
Patch12: 0013-QQmlImportDatabase-Make-sure-the-newly-added-import-.patch
Patch13: 0014-Models-Avoid-crashes-when-deleting-cache-items.patch
Patch14: 0015-qv4function-Fix-crash-due-to-reference-being-invalid.patch
Patch15: 0016-Quick-Animations-Fix-crash.patch
Patch16: 0017-Prevent-crash-when-destroying-asynchronous-Loader.patch
Patch17: 0018-QQuickItem-Fix-effective-visibility-for-items-withou.patch
Patch18: 0019-Revert-QQuickItem-Fix-effective-visibility-for-items.patch
Patch19: 0020-QML-Fortify-qmlExecuteDeferred-some-more.patch
Patch20: 0021-QtQml-Clean-up-QQmlData-ctor.patch
Patch21: 0022-Avoid-undefined-behavior-in-the-JIT.patch


## upstreamable patches
Patch100: %{name}-gcc11.patch
# https://pagure.io/fedora-kde/SIG/issue/82
Patch101: qtdeclarative-5.15.0-FixMaxXMaxYExtent.patch

# filter qml provides
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$

Obsoletes: qt5-qtjsbackend < 5.2.0
Obsoletes: qt5-qtdeclarative-render2d < 5.7.1-10

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: python%{python3_pkgversion}

%if 0%{?bootstrap}
Obsoletes: %{name}-examples < %{version}-%{release}
%global no_examples CONFIG-=compile_examples
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
Obsoletes: qt5-qtjsbackend-devel < 5.2.0
Obsoletes: qt5-qtdeclarative-render2d-devel < 5.7.1-10
Provides:  %{name}-private-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build

# HACK so calls to "python" get what we want
ln -s %{__python3} python
export PATH=`pwd`:$PATH

%qmake_qt5

%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

%ifarch %{multilib_archs}
# multilib: qv4global_p.h
  mv %{buildroot}%{_qt5_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p.h \
     %{buildroot}%{_qt5_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt5_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p.h
%endif

# hardlink files to %{_bindir}, add -qt5 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt5_bindir}
for i in * ; do
  case "${i}" in
    # qt4 conflicts
    qmlplugindump|qmlprofiler)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt5
      ln -sv ${i} ${i}-qt5
      ;;
    # qtchooser stuff
    qml|qmlbundle|qmlmin|qmlscene)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt5
      ln -sv ${i} ${i}-qt5
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  rm -fv "$(basename ${prl_file} .prl).la"
  sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
done
popd


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt5_libdir}
make sub-tests-all %{?_smp_mflags}
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make check -k -C tests ||:
%endif


%ldconfig_scriptlets

%files
%license LICENSE.LGPL*
%{_qt5_libdir}/libQt5Qml.so.5*
%{_qt5_libdir}/libQt5QmlModels.so.5*
%{_qt5_libdir}/libQt5QmlWorkerScript.so.5*
%{_qt5_libdir}/libQt5Quick.so.5*
%{_qt5_libdir}/libQt5QuickWidgets.so.5*
%{_qt5_libdir}/libQt5QuickParticles.so.5*
%{_qt5_libdir}/libQt5QuickShapes.so.5*
%{_qt5_libdir}/libQt5QuickTest.so.5*
%{_qt5_plugindir}/qmltooling/
%{_qt5_archdatadir}/qml/Qt*
%{_qt5_archdatadir}/qml/builtins.qmltypes

%files devel
%{_bindir}/qml*
%{_qt5_bindir}/qml*
%{_qt5_headerdir}/Qt*/
%{_qt5_libdir}/libQt5Qml.so
%{_qt5_libdir}/libQt5Qml.prl
%{_qt5_libdir}/libQt5QmlModels.so
%{_qt5_libdir}/libQt5QmlModels.prl
%{_qt5_libdir}/libQt5QmlWorkerScript.so
%{_qt5_libdir}/libQt5QmlWorkerScript.prl
%{_qt5_libdir}/libQt5Quick*.so
%{_qt5_libdir}/libQt5Quick*.prl
%dir %{_qt5_libdir}/cmake/Qt5Quick*/
%{_qt5_libdir}/cmake/Qt5*/Qt5*Config*.cmake
%{_qt5_libdir}/metatypes/qt5*_metatypes.json
%{_qt5_libdir}/pkgconfig/Qt5*.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_archdatadir}/mkspecs/features/*.prf
%dir %{_qt5_libdir}/cmake/Qt5Qml/
%{_qt5_libdir}/cmake/Qt5Qml/Qt5Qml_*Factory.cmake
%{_qt5_libdir}/cmake/Qt5QmlImportScanner/

%files static
%{_qt5_libdir}/libQt5QmlDevTools.a
%{_qt5_libdir}/libQt5QmlDevTools.prl
%{_qt5_libdir}/libQt5PacketProtocol.a
%{_qt5_libdir}/libQt5PacketProtocol.prl
%{_qt5_libdir}/libQt5QmlDebug.a
%{_qt5_libdir}/libQt5QmlDebug.prl

%if ! 0%{?no_examples:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
