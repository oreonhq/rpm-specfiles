%undefine __cmake_in_source_build
%global framework akonadi-search

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The Akonadi Search library and indexing agent

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# libical (and thus kcalendarcore) not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-ki18n-devel >= 5.15
BuildRequires:  kf5-kconfig-devel >= 5.15
BuildRequires:  kf5-kcrash-devel >= 5.15
BuildRequires:  kf5-krunner-devel >= 5.15
BuildRequires:  kf5-kcmutils-devel >= 5.15
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver} 
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  xapian-core-devel
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

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


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_bindir}/akonadi_html_to_text
%{_kf5_bindir}/akonadi_indexing_agent
%{_kf5_datadir}/akonadi/agents/akonadiindexingagent.desktop
%{_kf5_plugindir}/krunner/kcms/kcm_krunner_pimcontacts.so
%{_kf5_plugindir}/krunner/krunner_pimcontacts.so
%{_kf5_qtplugindir}/pim5/akonadi/

%files libs -f %{name}.lang
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5AkonadiSearchCore.so.*
%{_kf5_libdir}/libKPim5AkonadiSearchDebug.so.*
%{_kf5_libdir}/libKPim5AkonadiSearchPIM.so.*
%{_kf5_libdir}/libKPim5AkonadiSearchXapian.so.*

%files devel
%{_includedir}/KPim5/AkonadiSearch/
%{_kf5_libdir}/cmake/KPim5AkonadiSearch/
%{_kf5_libdir}/libKPim5AkonadiSearchCore.so
%{_kf5_libdir}/libKPim5AkonadiSearchDebug.so
%{_kf5_libdir}/libKPim5AkonadiSearchPIM.so
%{_kf5_libdir}/libKPim5AkonadiSearchXapian.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
