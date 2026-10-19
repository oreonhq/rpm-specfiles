Name:    kf5
Version: 5.116.0
Release:        1%{?dist}
Summary:        Filesystem and RPM macros for KDE Frameworks 5
License: BSD-3-Clause
URL:     http://www.kde.org
Source0:        macros.kf5
Source1: BSD-3-Clause.txt
# oreon:deps

# /oreon:deps
%description
Filesystem and RPM macros for KDE Frameworks 5

%package filesystem
Summary: Filesystem for KDE Frameworks 5
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
Requires: kde-filesystem >= 5
%endif
Obsoletes: kf5-filesystem < 5.10.0-2
Obsoletes: kf5-libkgeomap < 20.09~
Obsoletes: kf5-libkgeomap-devel < 20.09~
%{?_qt5_version:Requires: qt5-qtbase%{?_isa} >= %{_qt5_version}}
%description filesystem
Filesystem for KDE Frameworks 5.

%package rpm-macros
Summary: RPM macros for KDE Frameworks 5
Requires: cmake >= 3
Requires: qt5-rpm-macros >= 5.11
Requires: gcc-c++
BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 5 packages.

%prep

cp %{S:1} LICENSE

%install
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/plugins/kf5/
mkdir -p %{buildroot}%{_includedir}/KF5
mkdir -p %{buildroot}%{_datadir}/{kf5,kservicetypes5}
mkdir -p %{buildroot}%{_datadir}/kservices5/ServiceMenus
mkdir -p %{buildroot}%{_datadir}/qlogging-categories5/
mkdir -p %{buildroot}%{_docdir}/qt5
mkdir -p %{buildroot}%{_libexecdir}/kf5
mkdir -p %{buildroot}%{_datadir}/locale/tok
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p %{buildroot}%{_datadir}/{config.kcfg,kconf_update}
mkdir -p %{buildroot}%{_datadir}/kpackage/{genericqml,kcms}
mkdir -p %{buildroot}%{_datadir}/knsrcfiles/
mkdir -p %{buildroot}%{_datadir}/solid/{actions,devices}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}
install -Dpm644 %{_sourcedir}/macros.kf5 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
sed -i \
  -e "s|@@KF5_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-filesystem -f %{oreon_filedir}/kf5-filesystem.list
%files -n kf5-rpm-macros -f %{oreon_filedir}/kf5-rpm-macros.list

%changelog

%autochangelog
