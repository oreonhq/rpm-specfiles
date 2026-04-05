%global framework extra-cmake-modules
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    extra-cmake-modules
Summary: Additional modules for CMake build system
Version: 6.24.0
Release:	7%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://api.kde.org/ecm/
Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
BuildArch:      noarch

## upstreamable patches
# do not unconditionally link in base/core libpoppler library
Patch2: extra-cmake-modules-5.39.0-poppler_overlinking.patch

## downstream patches
# qdoc targets must not run on default "all" (cmake --build); matches ECM docs and avoids qdoc crashes
Patch3: extra-cmake-modules-ECMGenerateQDoc-exclude-from-all.patch

BuildRequires: kf6-rpm-macros
BuildRequires: make
# qcollectiongenerator
BuildRequires: qt5-qttools-devel
# sphinx-build
BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-qthelp
%global sphinx_build -DSphinx_BUILD_EXECUTABLE:PATH=%{_bindir}/sphinx-build-3

# Qt5Core is needed for tests to run properly (As-of 5.246.1).
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt6Core)
%if 0%{?fedora} || 0%{?rhel} < 10
Requires: (kf5-rpm-macros if qt5-qtbase-devel)
%endif
Requires: (kf6-rpm-macros if qt6-qtbase-devel)
Recommends: appstream

%description
Additional modules for CMake build system needed by KDE Frameworks.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6 \
  -DBUILD_MAN_DOCS:BOOL=OFF \
  -DBUILD_HTML_DOCS:BOOL=OFF \
  -DBUILD_QTHELP_DOCS:BOOL=ON \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  %{?sphinx_build}
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
# move to qt6 docdir so it shows up in Qt Creator by default
mkdir %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_kf6_docdir}/ECM/*.qch %{buildroot}%{_qt6_docdir}/

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_vpath_builddir} ||:
%endif

%files
%doc README.rst
%license LICENSES/*.txt
%{_datadir}/ECM/

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-6
- Patch ECMGenerateQDoc: EXCLUDE_FROM_ALL on prepare_docs and related targets (default build skips qdoc)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-5
- Note: kf6-rpm-macros no longer stubs QDOC_BIN, rely on patched qt6-qttools qdoc

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-4
- Drop ECM_ENABLE_QDOC_TARGETS patch, not needed (QDOC_BIN=/bin/true in kf6-rpm-macros works with any ECM)

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-3
- Add ECM_ENABLE_QDOC_TARGETS option (Patch3, upstreamable) for distro qdoc disable

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-2
- Prefer skipping qdoc by not requiring doc tools on kf6-rpm-macros (no ECM patch)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
