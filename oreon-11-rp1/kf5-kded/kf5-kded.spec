%global source0_hash 5cb67255f866ad765a88a091ad864e4fa83c7bd8b59fa96717817f448e6fa03d
%undefine __cmake_in_source_build
%global framework kded
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 addon with extensible daemon for system-level services
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
mkdir -p %{buildroot}%{_kf5_plugindir}/kded
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_user_post  plasma-kded.service
%preun

%systemd_user_preun plasma-kded.service
%files -f %{oreon_filedir}/main.list
%files -n kf5-kded-devel -f %{oreon_filedir}/kf5-kded-devel.list

%changelog

%autochangelog
