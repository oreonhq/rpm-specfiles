%global source0_hash c7cb9d023f6e5cd01d76568c3590303ea3ecb4ebe9535b31862957846f5e898a

## include -nepomuk subpkg support
%if 0%{?fedora} < 24 || 0%{?oreon}
%define nepomuk 1
%endif

## favor kf5-kactivities
%if 0%{?fedora} > 21 || 0%{?oreon}
%define plasma5 1
%endif

Name:    kactivities
Summary: API for using and interacting with Activities 
Version: 4.13.3
Release: 45%{?dist}

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdelibs/kactivities
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/4.13.3/src/kactivities-4.13.3.tar.xz

BuildRequires: kdelibs4-devel >= %{version}
%if ! 0%{?nepomuk}
Obsoletes: kactivities-nepomuk < 4.13.3-20
%endif

%if 0%{?rhel} == 6 || 0%{?oreon}
# see http://people.centos.org/tru/devtools-1.1/
BuildRequires: devtoolset-1.1-gcc-c++
%global devtoolset 1
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake

# libkactivities moved from kdelibs, but turns out there's no actual conflicts
# kactivitymanagerd moved here from kde-runtime 
Conflicts: kdebase-runtime < 4.7.3-10

Obsoletes: libkactivities < 6.1-100
Provides:  libkactivities = 6.2-1

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
API for using and interacting with Activities as a consumer, 
application adding information to them or as an activity manager.

%package libs
Summary: Runtime libraries for %{name}
Requires: kdelibs4%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
# upgrade path, -libs was originally split out in 4.13.1-3, but bumping
# due to one irc user who somehow still had 4.13.3-1.i686 (on x86_64)
# bumped again to -7 for bug#1172523
Obsoletes: kactivities < 4.13.3-7
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Obsoletes: libkactivities-devel < 6.1-100
Provides:  libkactivities-devel = 6.2-1
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if ! 0%{?nepomuk}
Obsoletes: kactivities-nepomuk-devel < 4.13.3-20
%endif
Requires: kdelibs4-devel
%description devel
%{summary}.

%if 0%{?nepomuk}
%package nepomuk
Summary: KActivities nepomuk support
BuildRequires: nepomuk-core-devel >= %{version}
BuildRequires: pkgconfig(soprano)
BuildRequires: make
# upgrade path
Obsoletes: kactivities < 4.13.0-2
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# not sure if an explicit dep is needed or worth it -- rex
#Requires: nepomuk-core%{?_isa} >= %{version}
%description nepomuk
%{summary}.

%package nepomuk-devel
Summary: KActivities nepomuk development files
Obsoletes: kactivities-devel < 4.13.3-2
Requires: %{name}-nepomuk%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description nepomuk-devel
%{summary}.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q 


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}

%if 0%{?devtoolset:1}
# build missing pieces with separate compiler
PATH=`scl enable devtoolset-1.1 'echo "$PATH"'`; export PATH

CXXFLAGS=`echo $RPM_OPT_FLAGS | sed 's|-g |-gdwarf-3 -gstrict-dwarf |g'`

mkdir %{_target_platform}-devtoolset
pushd %{_target_platform}-devtoolset
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}-devtoolset/src/service
%make_build -C %{_target_platform}-devtoolset/src/workspace
%endif


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%if 0%{?devtoolset:1}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-devtoolset/src/service
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-devtoolset/src/workspace
%endif

## unpackaged files
%if ! 0%{?nepomuk}
rm -rfv %{buildroot}%{_kde4_datadir}/ontology/kde/
%endif
%if 0%{?plasma5}
rm -fv %{buildroot}%{_kde4_bindir}/kactivitymanagerd
rm -fv %{buildroot}%{_kde4_libdir}/kde4/activitymanager_plugin_{activityranking,globalshortcuts,slc,sqlite,virtualdesktopswitch}.so
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/activitymanager-plugin-{activityranking,globalshortcuts,slc,sqlite,virtualdesktopswitch}.desktop
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/kactivitymanagerd.desktop
rm -fv %{buildroot}%{_kde4_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%endif


%if ! 0%{?plasma5}
%files
%{_kde4_bindir}/kactivitymanagerd
%{_kde4_libdir}/kde4/activitymanager_plugin_activityranking.so
%{_kde4_libdir}/kde4/activitymanager_plugin_globalshortcuts.so
%{_kde4_libdir}/kde4/activitymanager_plugin_slc.so
%{_kde4_libdir}/kde4/activitymanager_plugin_sqlite.so
%{_kde4_libdir}/kde4/activitymanager_plugin_virtualdesktopswitch.so
%{_kde4_datadir}/kde4/services/activitymanager-plugin-activityranking.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-globalshortcuts.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-sqlite.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-virtualdesktopswitch.desktop
%{_kde4_datadir}/kde4/services/kactivitymanagerd.desktop
%{_kde4_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%endif

%ldconfig_scriptlets libs

%files libs
%{_kde4_libdir}/libkactivities.so.6*
%{_kde4_libdir}/kde4/kcm_activities.so
%{_kde4_datadir}/kde4/services/kcm_activities.desktop
%{_kde4_appsdir}/activitymanager/

%files devel
%{_kde4_libdir}/libkactivities.so
%{_kde4_libdir}/cmake/KActivities/
%{_kde4_libdir}/pkgconfig/libkactivities.pc
%{_kde4_includedir}/KDE/KActivities/
%{_kde4_includedir}/kactivities/

%if 0%{?nepomuk}
%ldconfig_scriptlets nepomuk

%files nepomuk
%{_kde4_libdir}/kde4/kio_activities.so
%{_kde4_libdir}/libkactivities-models.so.1*
%{_kde4_libdir}/kde4/activitymanager_plugin_nepomuk.so
%{_kde4_libdir}/kde4/kactivitymanagerd_fileitem_linking_plugin.so
%{_kde4_datadir}/kde4/services/activities.protocol
%{_kde4_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_kde4_datadir}/kde4/services/kactivitymanagerd_fileitem_linking_plugin.desktop
%{_kde4_datadir}/ontology/kde/
%dir %{_kde4_libdir}/kde4/imports/org/kde
%{_kde4_libdir}/kde4/imports/org/kde/activities

%files nepomuk-devel
%{_kde4_libdir}/libkactivities-models.so
%{_kde4_libdir}/cmake/KActivities-Models/
%{_kde4_libdir}/pkgconfig/libkactivities-models.pc
%{_kde4_includedir}/kactivities-models/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.3-45
- Import
