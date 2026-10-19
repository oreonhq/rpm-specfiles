%global source0_hash 83f00d2b83bc9badd18add6e9c650c41f2aeb6483eb19013dbdae21e4d7bf81d
%global qt_module qtwayland
Summary:        Qt5 - Wayland platform support and QtCompositor module
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch1:  0001-Client-Announce-an-output-after-receiving-more-compl.patch
Patch2:  0002-Fix-issue-with-repeated-window-size-changes.patch
Patch3:  0003-Client-Connect-drags-being-accepted-to-updating-the-.patch
Patch4:  0004-Client-Disconnect-registry-listener-on-destruction.patch
Patch5:  0005-Client-Set-XdgShell-size-hints-before-the-first-comm.patch
Patch6:  0006-Fix-build.patch
Patch7:  0007-Fix-remove-listener.patch
Patch8:  0008-Hook-up-queryKeyboardModifers.patch
Patch9:  0009-Correctly-detect-if-image-format-is-supported-by-QIm.patch
Patch10: 0010-Client-Don-t-always-recreate-frame-callbacks.patch
Patch11: 0011-Client-Always-destroy-frame-callback-in-the-actual-c.patch
Patch12: 0012-Wayland-client-use-wl_keyboard-to-determine-active-s.patch
Patch13: 0013-Client-do-not-empty-clipboard-when-a-new-popup-windo.patch
Patch14: 0014-Client-Implement-DataDeviceV3.patch
Patch15: 0015-Client-Delay-deletion-of-QDrag-object-until-after-we.patch
Patch16: 0016-Client-Avoid-processing-of-events-when-showing-windo.patch
Patch17: 0017-Handle-registry_global-out-of-constructor.patch
Patch18: 0018-Connect-flushRequest-after-forceRoundTrip.patch
Patch19: 0019-Move-the-wayland-socket-polling-to-a-separate-event-.patch
Patch20: 0020-Client-Remove-mWaitingForUpdateDelivery.patch
Patch21: 0021-client-Simplify-round-trip-behavior.patch
Patch22: 0022-Client-Fix-opaque-region-setter.patch
Patch23: 0023-Use-proper-dependencies-in-compile-tests.patch
Patch24: 0024-Revert-Client-Remove-mWaitingForUpdateDelivery.patch
Patch25: 0025-Fix-race-condition-on-mWaitingForUpdateDelivery.patch
Patch26: 0026-use-poll-2-when-reading-from-clipboard.patch
Patch27: 0027-Reduce-memory-leakage.patch
Patch28: 0028-Only-close-popup-in-the-the-hierchary.patch
Patch29: 0029-Check-pointer-for-null-before-use-in-ASSERT.patch
Patch30: 0030-Use-wl_surface.damage_buffer-on-the-client-side.patch
Patch31: 0031-Client-clear-focus-on-touch-cancel.patch
Patch32: 0032-Guard-mResizeDirty-by-the-correctMutex.patch
Patch33: 0033-Fix-compile-tests.patch
Patch34: 0034-Call-finishDrag-in-QWaylandDataDevice-dragSourceCanc.patch
Patch35: 0035-Hold-surface-read-lock-throughout-QWaylandEglWindow-.patch
Patch36: 0036-Keep-toplevel-windows-in-the-top-left-corner-of-the-.patch
Patch37: 0037-Client-Add-F_SEAL_SHRINK-seal-to-shm-backing-file.patch
Patch38: 0038-Client-Call-wl_output_release-upon-QWaylandScreen-de.patch
Patch39: 0039-Client-Bump-wl_output-version.patch
Patch40: 0040-Fix-frame-sync-related-to-unprotected-multithread-ac.patch
Patch41: 0041-Client-Handle-zwp_primary_selection_device_manager_v.patch
Patch42: 0042-Fixes-the-build-on-CentOS.patch
Patch43: 0043-client-Avoid-protocol-error-with-invalid-min-max-siz.patch
Patch44: 0044-Client-Fix-handling-of-Qt-BlankCursor.patch
Patch45: 0045-client-Force-a-roundtrip-when-an-XdgOutput-is-not-re.patch
Patch46: 0046-Destroy-frame-queue-before-display.patch
Patch47: 0047-client-Fix-crash-on-dnd-updates-after-client-facing-.patch
Patch48: 0048-Convert-cursor-bitmap-to-supported-format.patch
Patch49: 0049-Replace-scale-with-devicePixelRatio-for-non-integer-.patch
Patch50: 0050-Client-Fix-buffer-damage.patch
Patch51: 0051-Client-Commit-the-initial-surface-state-explicitly.patch
Patch52: 0052-tests-Fix-tst_xdgshell-minMaxSize.patch
Patch53: 0053-Client-Remove-some-surface-commits.patch
Patch54: 0054-Client-Avoid-locking-resizing-in-QWaylandShmBackingS.patch
Patch55: 0055-bradient-Use-QWaylandWindow-actual-window-title.patch
Patch100: qtwayland-use-adwaita-decorations-by-default.patch
Patch101: qtwayland-decoration-support-backports-from-qt6.patch
Patch102: qtwayland-client-fix-window-margin-calculation.patch
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  libXext-devel
BuildRequires:  make
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

%build

%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtwayland-devel -f %{oreon_filedir}/qt5-qtwayland-devel.list
%files -n qt5-qtwayland-examples -f %{oreon_filedir}/qt5-qtwayland-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
