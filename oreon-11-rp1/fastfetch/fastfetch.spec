%global source0_hash d0e42faf307e39e7b531d632745a56e4eb558a6545f557280099c622562355ee
Name:           fastfetch
Version:        2.69.0
Release:        1%{?dist}
Summary:        Fast neofetch-like system information tool
License:        MIT
URL:            https://github.com/fastfetch-cli/fastfetch
Source0:        https://github.com/%{name}-cli/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if "%{_arch}" != "s390x"
%endif
Recommends:     hwdata
Suggests:       libXrandr
Suggests:       dconf
Suggests:       sqlite-libs
Suggests:       zlib
Suggests:       libglvnd-glx
Suggests:       ImageMagick-libs
Suggests:       glib2
Suggests:       ocl-icd
Suggests:       chafa-libs
Suggests:       libddcutil
Suggests:       libdrm
Suggests:       pulseaudio-libs
Suggests:       elfutils-libelf
Provides:       fastfetch-bash-completion = %{version}%{release}
Provides:       fastfetch-zsh-completion = %{version}%{release}
Provides:       fastfetch-fish-completion = %{version}%{release}
Obsoletes:      fastfetch-bash-completion < 2.31.0-2
Obsoletes:      fastfetch-zsh-completion < 2.31.0-2
Obsoletes:      fastfetch-fish-completion < 2.31.0-2
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  chafa-devel
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  dconf-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  hwdata-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libddcutil-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3
BuildRequires:  rpm-devel
BuildRequires:  sqlite-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  wayland-devel
BuildRequires:  yyjson-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way. It is written in c to achieve much better
performance, in return only Linux and Android are supported. It also uses
mechanisms like multithreading and caching to finish as fast as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_TESTS=ON -DENABLE_SYSTEM_YYJSON=ON -DBUILD_FLASHFETCH=OFF
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
