%global source0_hash 7281b2e9246408f19b5aad27eaf95387f149f34cd3418f381d6c63166f04cdee
Name:           hyperhdr
Version:        20.0.0.0
Release:        1%{?dist}
Summary:        Ambient lighting
License:        MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/awawa-dev/HyperHDR
Source0:        https://github.com/awawa-dev/HyperHDR/archive/refs/tags/v%{version}beta1/%{name}-%{version}beta1.tar.gz
Patch0:         fix.patch
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
Requires:       %{name}-common
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(flatbuffers)
BuildRequires:  cmake(mdns)
BuildRequires:  desktop-file-utils
BuildRequires:  flatbuffers-compiler
BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Open source ambient lighting implementation for television sets based on the
video and audio streams analysis, using performance improvements especially
for USB grabbers.

%package        common
Summary:        LUT files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    common
The %{name}-common package contains LUT files for
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir HyperHDR-%{version}beta1
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_CXX_STANDARD=17 \
    -DUSE_SYSTEM_FLATBUFFERS_LIBS:BOOL=ON \
    -DUSE_SYSTEM_MBEDTLS_LIBS:BOOL=ON \
    -DENABLE_MQTT:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DPLATFORM=linux
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/lut/
tar -xf resources/lut/lut_lin_tables.tar.xz -C %{buildroot}%{_datadir}/%{name}/lut/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n hyperhdr-common -f %{oreon_filedir}/hyperhdr-common.list

%changelog

%autochangelog
