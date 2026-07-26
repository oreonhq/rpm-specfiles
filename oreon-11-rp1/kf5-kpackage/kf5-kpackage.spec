%global source0_hash 5705b185c72b09f19215fa659fc628dc74529bb7d3f649d1fc953ae5a7ebf1be

%undefine __cmake_in_source_build
%global framework kpackage

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:           kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary:        KDE Frameworks 5 Tier 2 library to load and install packages as plugins

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
# optional
BuildRequires:  kf5-kdoctools-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires: make

%description
KDE Frameworks 5 Tier 2 library to load and install non-binary packages as
if they were plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       extra-cmake-modules >= %{majmin}
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

%find_lang %{name} --all-name --with-man

# create/own dirs
mkdir -p %{buildroot}%{_kf5_qtplugindir}/kpackage/packagestructure/
mkdir -p %{buildroot}%{_kf5_datadir}/kpackage/

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Package.so.*
%{_kf5_qtplugindir}/kpackage/
%{_kf5_datadir}/kpackage/
%{_kf5_datadir}/kservicetypes5/kpackage-*.desktop
%{_kf5_bindir}/kpackagetool5
%{_mandir}/man1/kpackagetool5.1*

%files devel

%{_kf5_includedir}/KPackage/
%{_kf5_libdir}/libKF5Package.so
%{_kf5_libdir}/cmake/KF5Package/

%changelog
%autochangelog
