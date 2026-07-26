%global source0_hash 6677af0c486a4c9cfefe74a0951e85dad53435010031bf2b7fcdf9c5df6b3edd

%undefine __cmake_in_source_build
%global framework kirigami

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 1.1.0
Release: 28%{?dist}
Summary: QtQuick plugins to build user interfaces based on the KDE UX guidelines

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
#URL:    https://quickgit.kde.org/?p=%{framework}.git
URL:     https://techbase.kde.org/Kirigami
Source0: http://download.kde.org/stable/kirigami/%{framework}-%{version}.tar.xz

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires: make
BuildRequires: extra-cmake-modules
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-rpm-macros
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtsvg-devel

# upgrade path from OBS packages
Obsoletes: kirigami < 1.1.0
Provides:  kirigami = %{version}-%{release}

%if 0%{?tests}
%if 0%{?fedora}
BuildRequires: appstream
%endif
%endif

Requires:      kf5-filesystem >= %{version}
Requires:      qt5-qtquickcontrols%{?_isa}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
# upgrade path from OBS packages
Obsoletes:      kirigami-devel < 1.1.0
Provides:       kirigami-devel = %{version}-%{release}
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

%find_lang_kf5 libkirigamiplugin_qt

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f libkirigamiplugin_qt.lang
# README is currently only build instructions, omit for now
#doc README.md
%license LICENSE*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kirigami/

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_Kirigami.pri
%{_kf5_libdir}/cmake/KF5Kirigami/

%changelog
%autochangelog
