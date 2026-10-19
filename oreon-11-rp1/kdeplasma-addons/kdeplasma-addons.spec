%global source1_hash fc05baef0fdf2973be5948adb49783e34fc78ee6258269bc4b800bf3f9bc003b
%global source0_hash 1bc1c861487733f4944695d509c81f19b90a4d80c5825cc6df633b0313e3e8cc
%global stable_kf6 stable
Name:    kdeplasma-addons
Summary:        Additional Plasmoids for Plasma 6
Version:        6.7.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}-%{version}-vendor.tar.xz
%global source2_hash d951bcfb35454427640feb8b91c4862901898137106ff77ad51e16b277eeb46d
ExcludeArch: %{ix86}
%ifarch %{qt6_qtwebengine_arches}
%endif
Obsoletes: kdeplasma-addons-libs < 5.0.0
Requires:       kf6-plasma
Recommends:     kf6-purpose%{?_isa}
Requires:       qt6-qtquick3d%{?_isa}
Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
# oreon:deps
BuildRequires:  cmake(Corrosion)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libicu-devel
BuildRequires:  libksysguard-devel
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  plasma-workspace-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
# /oreon:deps
%description
%{summary}.

%package -n kate-krunner-plugin
Summary: KRunner plugin for searching Kate sessions
Requires: kate
Supplements: kate
Conflicts: kdeplasma-addons < 5.92.0-3
%description -n kate-krunner-plugin
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: cmake(Qt6Gui)
Requires: cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

# vendor the kameleon-qmk-helper subcrate so corrosion can build offline
tar xf %{SOURCE2}
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[net]
offline = true
EOF

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kdeplasmaaddons5_qt --with-qt --all-name
%oreon_autofiles kate-krunner-plugin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kate-krunner-plugin -f %{oreon_filedir}/kate-krunner-plugin.list
%files -n kdeplasma-addons-devel -f %{oreon_filedir}/kdeplasma-addons-devel.list

%changelog

%autochangelog
