%global debug_package %{nil}

Name:    kf6
# This version MUST remain in sync with KF6 versions!
Version: 6.24.0
Release: 13%{?dist}
Summary: Filesystem and RPM macros for KDE Frameworks 6
License: BSD-3-Clause
URL:     http://www.kde.org
Source0: macros.kf6
Source1: LICENSE

%description
Filesystem and RPM macros for KDE Frameworks 6

%package filesystem
Summary: Filesystem for KDE Frameworks 6
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires: kde-filesystem >= 5
%endif
%{?_qt6_version:Requires: qt6-qtbase >= %{_qt6_version}}
%description filesystem
Filesystem for KDE Frameworks 6.

%package rpm-macros
Summary: RPM macros for KDE Frameworks 6
Requires: cmake >= 3
Requires: qt6-rpm-macros >= 6
# misc build environment dependencies
Requires: gcc-c++
# Optional qdoc stack (qt6-doc-devel, kde-qdoc-common, clang-devel, cmake(Qt6ToolsTools))
Recommends: doxygen
Recommends: qt6-doc-devel
Recommends: kde-qdoc-common
Recommends: cmake(Qt6ToolsTools)
Recommends: clang-devel
BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 6 packages.
%%cmake_kf6 sets KDE install paths. %%cmake_build_kf6 is a single cmake ``--build`` pass
(not %%cmake_build from qt6-rpm-macros, which adds ``-t prepare_docs``). %%cmake_install_kf6
runs only ``cmake --install`` (not %%cmake_install from qt6, which can run
``install_html_docs`` and fail if qdoc output was never built). Oreon kf6-* framework specs
also inline the build one-liner in %%build where needed.

%install
# See macros.kf6 where the directories are specified
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt6/plugins/kf6/
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt6/qml/org/kde/
mkdir -p %{buildroot}%{_includedir}/kf6
mkdir -p %{buildroot}%{_includedir}/KF6
mkdir -p %{buildroot}%{_datadir}/{kf6,kservices6,kservicetypes6}
mkdir -p %{buildroot}%{_datadir}/kio/servicemenus
mkdir -p %{buildroot}%{_datadir}/qlogging-categories6/
mkdir -p %{buildroot}%{_docdir}/qt6
mkdir -p %{buildroot}%{_libexecdir}/kf6
mkdir -p %{buildroot}%{_datadir}/kf6/
mkdir -p %{buildroot}%{_datadir}/locale/tok
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p %{buildroot}%{_datadir}/{config.kcfg,kconf_update}
mkdir -p %{buildroot}%{_datadir}/kpackage/{genericqml,kcms}
mkdir -p %{buildroot}%{_datadir}/knsrcfiles/
mkdir -p %{buildroot}%{_datadir}/solid/{actions,devices}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}
%endif

# macros.zz-kf6 sorts after macros.qt6 so %%cmake_build_kf6 is not overwritten by qt6-rpm-macros.
install -Dpm644 %{_sourcedir}/macros.kf6 %{buildroot}%{_rpmconfigdir}/macros.d/macros.zz-kf6
install -Dpm644 %{_sourcedir}/LICENSE %{buildroot}%{_datadir}/kf6/LICENSE
sed -i \
  -e "s|@@kf6_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.zz-kf6

%files filesystem
%{_datadir}/kf6/
%{_datadir}/kio/
%{_datadir}/kservices6/
%{_datadir}/kservicetypes6/
%{_datadir}/qlogging-categories6/
%{_docdir}/qt6/
%{_includedir}/kf6/
%{_includedir}/KF6/
%{_libexecdir}/kf6/
%{_prefix}/%{_lib}/qt6/plugins/kf6/
%{_prefix}/lib/qt6/plugins/kf6/
%{_prefix}/%{_lib}/qt6/qml/org/kde/
%{_prefix}/lib/qt6/qml/org/kde/
%{_datadir}/locale/tok
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%{_datadir}/config.kcfg/
%{_datadir}/kconf_update/
%{_datadir}/knsrcfiles/
%{_datadir}/kpackage/
%{_datadir}/solid/
%{_prefix}/%{_lib}/kconf_update_bin/
%{_prefix}/lib/kconf_update_bin/
%{_sysconfdir}/xdg/plasma-workspace/
%endif

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.zz-kf6

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-13
- %%cmake_install_kf6: plain cmake --install (avoid qt6 %%cmake_install install_html_docs)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-12
- docs: note framework specs inline cmake --build alongside macros.zz-kf6

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-11
- rpm-macros: install as macros.zz-kf6 so definitions load after qt6 (fix prepare_docs override)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-10
- macros: %%cmake_build_kf6 avoids qt6 %%cmake_build extra prepare_docs pass (qdoc SIGSEGV)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-9
- macros: drop -DQDOC_BIN=/bin/true so real qdoc runs with patched qt6-qttools (QTBUG-142742)

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-8
- macros: use -DQDOC_BIN=/bin/true instead of ECM patch (works with any unpatched ECM)

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-6
- rpm-macros: restore qdoc deps, require clang-devel, set LLVM_INSTALL_DIR and QT_QPA_PLATFORM for mock

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-5
- rpm-macros: stop requiring qt6-doc-devel and qdoc stack (ECM skips qdoc targets without it)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
