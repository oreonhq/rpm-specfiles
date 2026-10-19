%global source0_hash f6dfaa2482c8a4dfc12ed40094fd120bd41c5053899d3f85c2ff6b8215659866
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%global framework kglobalaccel
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 integration module for global shortcuts
License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if %{without kf6_compat}
Conflicts:      kglobalacceld
%endif
# oreon:deps
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  systemd
BuildRequires:  xcb-util-keysyms-devel
# /oreon:deps
%description
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{framework}-%{version}

%build

%cmake_kf5 %{?with_kf6_compat:-DBUILD_RUNTIME=OFF}
%cmake_build
%install
%cmake_install
%if 0%{?flatpak:1}
rm -fv %{buildroot}%{_prefix}/lib/systemd/user/plasma-kglobalaccel.service
%endif
%find_lang_kf5 kglobalaccel5_qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kglobalaccel-libs -f %{oreon_filedir}/kf5-kglobalaccel-libs.list
%files -n kf5-kglobalaccel-devel -f %{oreon_filedir}/kf5-kglobalaccel-devel.list

%changelog

%autochangelog
