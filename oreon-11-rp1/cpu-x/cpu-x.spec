%global source0_hash 40c34c0ac14eead0f9626518e0783fd9f365af84aa05761e39795c07086f3fef
%global forgeurl https://github.com/TheTumultuousUnicornOfDarkness/CPU-X
%global tag v%{version}
%global appid io.github.thetumultuousunicornofdarkness.%{name}
Name:           cpu-x
Version:        5.4.1
%forgemeta
Release:        1%{?dist}
Summary:        Free software that gathers information on CPU, motherboard and more
ExclusiveArch:  x86_64 aarch64
License:        GPL-3.0-or-later
URL:            https://thetumultuousunicornofdarkness.github.io/CPU-X/
Source0:        %{forgeurl}/archive/%{tag}/CPU-X-%{version}.tar.gz
Patch0:         %{name}_policy.patch
%if 0%{?flatpak}
%else
%endif
Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme
Recommends:     polkit
Provides:       bundled(bandwidth) = 1.5.1
Provides:       bundled(dmidecode) = 3.6
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  nasm
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcpuid)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(vulkan)
# /oreon:deps
%description

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    data

Data files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
%if 0%{?flatpak}
sed -i -e 's#lib/\(aarch64\|x86_64\)-linux-gnu#lib64#' src/daemon/client.cpp
%endif

%build

%cmake %{?flatpak:-DFLATPAK=ON}
%cmake_build
%install
%cmake_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/384x384
rm -r %{buildroot}%{_datadir}/locale/zh_Hant/
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n cpu-x-data -f %{oreon_filedir}/cpu-x-data.list

%changelog

%autochangelog
