Name:    kf5
Version: 5.116.0
Release: 6%{?dist}
Summary: Filesystem and RPM macros for KDE Frameworks 5
License: BSD-3-Clause
URL:     http://www.kde.org

Source0: macros.kf5
Source1: BSD-3-Clause.txt

%description
Filesystem and RPM macros for KDE Frameworks 5

%package filesystem
Summary: Filesystem for KDE Frameworks 5
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires: kde-filesystem >= 5
%endif
# noarch -> arch transition
Obsoletes: kf5-filesystem < 5.10.0-2
# Retired KDE5 packages without other transitions
Obsoletes: kf5-libkgeomap < 20.09~
Obsoletes: kf5-libkgeomap-devel < 20.09~

%{?_qt5_version:Requires: qt5-qtbase%{?_isa} >= %{_qt5_version}}
%description filesystem
Filesystem for KDE Frameworks 5.

%package rpm-macros
Summary: RPM macros for KDE Frameworks 5
%if 0%{?fedora} || 0%{?rhel} > 7
Requires: cmake >= 3
Requires: qt5-rpm-macros >= 5.11
%else
Requires: cmake3
Requires: qt5-qtbase-devel >= 5.11
%endif
%if 0%{?rhel} == 8
# This is where cmake-related macros live, e.g. %%cmake_build, %%cmake_install
# at least until fixed upstream, https://bugzilla.redhat.com/show_bug.cgi?id=1858941
Requires: epel-rpm-macros
%endif
# misc build environment dependencies
Requires: gcc-c++
BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 5 packages.

%prep
cp %{S:1} LICENSE

%install
# See macros.kf5 where the directories are specified
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/plugins/kf5/
mkdir -p %{buildroot}%{_includedir}/KF5
mkdir -p %{buildroot}%{_datadir}/{kf5,kservicetypes5}
mkdir -p %{buildroot}%{_datadir}/kservices5/ServiceMenus
mkdir -p %{buildroot}%{_datadir}/qlogging-categories5/
mkdir -p %{buildroot}%{_docdir}/qt5
mkdir -p %{buildroot}%{_libexecdir}/kf5
mkdir -p %{buildroot}%{_datadir}/locale/tok
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p %{buildroot}%{_datadir}/{config.kcfg,kconf_update}
mkdir -p %{buildroot}%{_datadir}/kpackage/{genericqml,kcms}
mkdir -p %{buildroot}%{_datadir}/knsrcfiles/
mkdir -p %{buildroot}%{_datadir}/solid/{actions,devices}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}
%endif
install -Dpm644 %{_sourcedir}/macros.kf5 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
sed -i \
  -e "s|@@KF5_VERSION@@|%{version}|g" \
%if 0%{?rhel} && 0%{?rhel} < 8
  -e 's|%{__cmake}|%{__cmake3}|' \
%endif
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5


%files filesystem
%license LICENSE
%{_prefix}/lib/qt5/plugins/kf5/
%{_prefix}/%{_lib}/qt5/plugins/kf5/
%{_includedir}/KF5/
%{_libexecdir}/kf5/
%{_datadir}/kf5/
%{_datadir}/kservices5/
%{_datadir}/kservicetypes5/
%{_datadir}/qlogging-categories5/
%{_docdir}/qt5/
%{_datadir}/locale/tok
%if ! (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
%{_sysconfdir}/xdg/plasma-workspace/
%{_prefix}/lib/kconf_update_bin/
%{_prefix}/%{_lib}/kconf_update_bin/
%{_datadir}/config.kcfg/
%{_datadir}/kconf_update/
%{_datadir}/kpackage/
%{_datadir}/knsrcfiles/
%{_datadir}/solid/
%endif

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf5


%changelog
%autochangelog
