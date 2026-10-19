%global source0_hash 8b584da74a0c4488ad5e31c3d740a1813c35d28bc003fef8854963d17058c9e0
%global framework kirigami2
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        QtQuick plugins to build user interfaces based on the KDE UX guidelines
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND GPL-2.1-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND LGPL-2.1-or-later
URL:     https://techbase.kde.org/Kirigami
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$
%if 0%{?tests}
%endif
Requires:      qt5-qtquickcontrols%{?_isa}
Requires:      qt5-qtquickcontrols2%{?_isa}
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtsvg-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang_kf5 libkirigami2plugin_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export QT_XCB_FORCE_SOFTWARE_OPENGL=1
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
  make test ARGS="--output-on-failure --timeout 30" -C %{_vpath_builddir} ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n kf5-kirigami2-devel -f %{oreon_filedir}/kf5-kirigami2-devel.list

%changelog

%autochangelog
