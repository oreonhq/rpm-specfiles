%undefine __cmake_in_source_build
%global framework kded

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon with extensible daemon for system-level services

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-kconfig-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcrash-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kdoctools-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kservice-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  qt5-qtbase-devel

BuildRequires:  systemd-rpm-macros


%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs
in the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

Custom KDED modules can be provided by 3rd party frameworks and
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang kded5 --with-man --without-mo

# create/own this
mkdir -p %{buildroot}%{_kf5_plugindir}/kded


%post
%systemd_user_post  plasma-kded.service

%preun
%systemd_user_preun plasma-kded.service

%files -f kded5.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/kded5
# fake, nodisplay, placeholder mostly
%{_kf5_datadir}/applications/org.kde.kded5.desktop
%{_kf5_datadir}/dbus-1/services/*.service
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man8/kded5.8*
%dir %{_kf5_plugindir}/kded/
%{_userunitdir}/plasma-kded.service

%files devel
%{_kf5_libdir}/cmake/KDED/
%{_kf5_datadir}/dbus-1/interfaces/*.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
