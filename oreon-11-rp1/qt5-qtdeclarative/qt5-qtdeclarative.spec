%global source0_hash 876f20c476f07a07c53756b84c8ede7162d455ee0927b995acceb7c64e5c17a7
%define _lto_cflags %{nil}
%global qt_module qtdeclarative
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
Summary:        Qt5 - QtDeclarative component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Source5: qv4global_p-multilib.h
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
Patch100: %{name}-gcc11.patch
Patch101: qtdeclarative-5.15.0-FixMaxXMaxYExtent.patch
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$
Obsoletes: qt5-qtjsbackend < 5.2.0
Obsoletes: qt5-qtdeclarative-render2d < 5.7.1-10
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%if 0%{?bootstrap}
Obsoletes: %{name}-examples < %{version}-%{release}
%global no_examples CONFIG-=compile_examples
%endif
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  dbus-x11
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  python3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-rpm-macros
BuildRequires:  time
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

%build

ln -s %{__python3} python
export PATH=`pwd`:$PATH
%qmake_qt5
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%ifarch %{multilib_archs}
  mv %{buildroot}%{_qt5_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p.h \
     %{buildroot}%{_qt5_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt5_headerdir}/QtQml/%{version}/QtQml/private/qv4global_p.h
%endif
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt5_bindir}
for i in * ; do
  case "${i}" in
    qmlplugindump|qmlprofiler)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt5
      ln -sv ${i} ${i}-qt5
      ;;
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
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  rm -fv "$(basename ${prl_file} .prl).la"
  sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
done
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n qt5-qtdeclarative-devel -f %{oreon_filedir}/qt5-qtdeclarative-devel.list
%files -n qt5-qtdeclarative-static -f %{oreon_filedir}/qt5-qtdeclarative-static.list
%files -n qt5-qtdeclarative-examples -f %{oreon_filedir}/qt5-qtdeclarative-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
