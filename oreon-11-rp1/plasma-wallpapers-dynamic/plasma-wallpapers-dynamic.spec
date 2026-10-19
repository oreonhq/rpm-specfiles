%global source0_hash 0364434ec647353cf84daa14684342171a070814f1d8093f498c58d6c624956d
%global component wallpapers-dynamic
%global somajor 5
Name:           plasma-%{component}
Version: 5.0.1
Release:        1%{?dist}
Summary:        Dynamic wallpaper plugin for KDE Plasma
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://github.com/zzag/plasma5-%{component}
Source0:        https://github.com/zzag/plasma5-wallpapers-dynamic/archive/refs/tags/5.0.1.tar.gz#/plasma5-wallpapers-dynamic-5.0.1.tar.gz
Recommends:     %{name}-builder
# oreon:deps
BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(libavif)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libexif)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
A simple dynamic wallpaper plugin for KDE Plasma.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains the development headers and libraries.

%package        builder
Summary:        Wallpaper builder for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    builder
Command-line utility to build dynamic wallpapers.

%package        builder-bash-completion
Summary:        Bash completion support for %{name}-builder
BuildArch:      noarch
Requires:       %{name}-builder = %{version}-%{release}
Supplements:    (%{name}-builder and bash-completion)
Requires:       bash
Requires:       bash-completion
%description    builder-bash-completion
Files needed to support bash completion.

%package        builder-fish-completion
Summary:        Fish completion support for %{name}-builder
BuildArch:      noarch
Requires:       %{name}-builder = %{version}-%{release}
Supplements:    (%{name}-builder and fish)
Requires:       fish
%description    builder-fish-completion
Files needed to support fish completion.

%package        builder-zsh-completion
Summary:        Zsh completion support for %{name}-builder
BuildArch:      noarch
Requires:       %{name}-builder = %{version}-%{release}
Supplements:    (%{name}-builder and zsh)
Requires:       zsh
%description    builder-zsh-completion
Files needed to support zsh completion.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n plasma5-%{component}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang plasma_wallpaper_com.github.zzag.dynamic
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n plasma-wallpapers-dynamic-devel -f %{oreon_filedir}/plasma-wallpapers-dynamic-devel.list
%files -n plasma-wallpapers-dynamic-builder -f %{oreon_filedir}/plasma-wallpapers-dynamic-builder.list
%files -n plasma-wallpapers-dynamic-builder-bash-completion -f %{oreon_filedir}/plasma-wallpapers-dynamic-builder-bash-completion.list
%files -n plasma-wallpapers-dynamic-builder-fish-completion -f %{oreon_filedir}/plasma-wallpapers-dynamic-builder-fish-completion.list
%files -n plasma-wallpapers-dynamic-builder-zsh-completion -f %{oreon_filedir}/plasma-wallpapers-dynamic-builder-zsh-completion.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.1-1
- Prepare for Oreon 11 (RP1)
