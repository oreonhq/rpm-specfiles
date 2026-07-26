%global source0_hash 5cb67255f866ad765a88a091ad864e4fa83c7bd8b59fa96717817f448e6fa03d

%undefine __cmake_in_source_build
%global framework kded

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon with extensible daemon for system-level services

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
