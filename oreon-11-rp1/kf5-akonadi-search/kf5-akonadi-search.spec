%global source0_hash ef21350b7468eea740b949f9f450f07a48b8585e6a83a5000ff4a8606581adb4
%undefine __cmake_in_source_build
%global framework akonadi-search
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The Akonadi Search library and indexing agent
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%if 0%{?tests}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  xapian-core-devel
# /oreon:deps
%description
%{summary}.

%package   libs
Summary:   Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-akonadi-server-devel
Requires:       kf5-akonadi-mime-devel
Requires:       kf5-kcontacts-devel
Requires:       kf5-kmime-devel
Requires:       kf5-kcalendarcore-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

find ./po -type f -execdir mv {} akonadi_search5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/akonadi_search/akonadi_search5/" CMakeLists.txt
sed -i "s/akonadi_search/akonadi_search5/" Messages.sh

%build

%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-akonadi-search-libs -f %{oreon_filedir}/kf5-akonadi-search-libs.list
%files -n kf5-akonadi-search-devel -f %{oreon_filedir}/kf5-akonadi-search-devel.list

%changelog

%autochangelog
