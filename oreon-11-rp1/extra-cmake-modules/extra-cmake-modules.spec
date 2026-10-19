%global source1_hash 16d5993d3acb6c2fe4e85da0ca7cbd7bbab3c6ae6bf4f48b297363f2ffef0392
%global source0_hash 22c9f7ff930dae7329faebf2942d2424f4a298c43bb3f11e217be6b12f227f6e
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
%global framework extra-cmake-modules
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    extra-cmake-modules
Summary:        Additional modules for CMake build system
Version: 6.30.0
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL:     https://api.kde.org/ecm/
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
BuildArch:      noarch
Patch2: extra-cmake-modules-5.39.0-poppler_overlinking.patch
%global sphinx_build -DSphinx_BUILD_EXECUTABLE:PATH=%{_bindir}/sphinx-build
Requires: (kf6-rpm-macros if qt6-qtbase-devel)
Recommends: appstream
# oreon:deps
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-qthelp
BuildRequires:  qt5-qttools-devel
# /oreon:deps
%description
Additional modules for CMake build system needed by KDE Frameworks.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 \
  -DBUILD_MAN_DOCS:BOOL=OFF \
  -DBUILD_HTML_DOCS:BOOL=OFF \
  -DBUILD_QTHELP_DOCS:BOOL=ON \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  %{?sphinx_build}
%cmake_build
%install
%cmake_install
mkdir %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_kf6_docdir}/ECM/*.qch %{buildroot}%{_qt6_docdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_vpath_builddir} ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n extra-cmake-modules-doc -f %{oreon_filedir}/extra-cmake-modules-doc.list

%changelog

%autochangelog
