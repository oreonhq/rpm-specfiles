%global source0_hash 9b97d556b0c4e61154614879d804c98202dbde64ad352fbcab2b6f5e54b5b517

%undefine __cmake_in_source_build
%global framework kjsembed

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 5.116.0
Release: 9%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon for binding JS objects to QObjects

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/v%{version}/%{framework}-v%{version}.tar.gz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kjs-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-static

%description
KSJEmbed provides a method of binding JavaScript objects to QObjects, so you
can script your applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kjs-devel >= %{majmin}
Requires:       kf5-ki18n-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-v%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-man

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license COPYING.LIB
%{_kf5_bindir}/kjscmd5
%{_kf5_bindir}/kjsconsole
%{_kf5_libdir}/libKF5JsEmbed.so.*
%{_kf5_datadir}/man/man1/*

%files devel
%{_kf5_libdir}/libKF5JsEmbed.so
%{_kf5_libdir}/cmake/KF5JsEmbed/
%{_kf5_includedir}/KJsEmbed/
%{_kf5_archdatadir}/mkspecs/modules/qt_KJsEmbed.pri

%changelog
%autochangelog
