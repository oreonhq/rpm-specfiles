%global source0_hash 141edd95489d59e9af2597406d3200509a43bb6b012717a24c7afb163baa7f7f
%ifarch i686
%global libs_only 1
%else
%global libs_only 0
%endif
%global srcname obs-vkcapture
Name:           obs-studio-plugin-vkcapture
Version:        1.5.1
Release:        1%{?dist}
Summary:        OBS plugin for Vulkan/OpenGL game capture
License:        GPL-2.0-or-later and Zlib
URL:            https://github.com/nowrep/obs-vkcapture
Source0:        https://github.com/nowrep/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
ExcludeArch:    s390x
%if ! %{libs_only}
%endif
Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}
Obsoletes:      obs-studio-vkcapture < %{version}-%{release}
Provides:       obs-studio-vkcapture = %{version}-%{release}
Provides:       obs-studio-vkcapture%{?_isa} = %{version}-%{release}
Obsoletes:      obs-studio-gamecapture < %{version}-%{release}
Provides:       obs-studio-gamecapture = %{version}-%{release}
Provides:       obs-studio-gamecapture%{?_isa} = %{version}-%{release}
Provides:       obs-studio-plugin-gamecapture = %{version}-%{release}
Provides:       obs-studio-plugin-gamecapture%{?_isa} = %{version}-%{release}
Recommends:     %{name}-hook-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(libobs)
BuildRequires:  gcc
BuildRequires:  libglvnd-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  vulkan-loader-devel
# /oreon:deps
%description
%{name}.

%package hook-libs
Summary:        Hook libraries for OBS Vulkan/OpenGL game capture
Requires:       vulkan-loader%{?_isa}
Obsoletes:      obs-studio-plugin-vkcapture < %{version}-%{release}
Obsoletes:      obs-studio-vkcapture < %{version}-%{release}
Obsoletes:      obs-studio-gamecapture < %{version}-%{release}
%if ! %{libs_only}
Recommends:     %{name}%{?_isa} = %{version}-%{release}
%endif
%description hook-libs
Hook libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%cmake \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if ! %{libs_only}
%files -f %{oreon_filedir}/main.list
%files -n obs-studio-plugin-vkcapture-hook-libs -f %{oreon_filedir}/obs-studio-plugin-vkcapture-hook-libs.list

%changelog

%autochangelog
%endif
