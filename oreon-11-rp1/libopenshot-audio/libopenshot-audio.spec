%global source0_hash 80dc23fff901064194fcc7732d41cc953df6b7ed2742376fcf28df23b5a10a29
%global soversion 10
Name:           libopenshot-audio
Version:        1.0.0
Release:        1%{?dist}
Summary:        Audio library used by OpenShot
License:        GPL-3.0-or-later
URL:            http://openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    ppc64le
Provides:       bundled(JUCE) = 5.4.3
Provides:       bundled(flac) = 1.3.1
Provides:       bundled(libvorbis) = 1.3.2
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
# /oreon:deps
%description
OpenShot Audio Library (libopenshot-audio) is an open-source
project based on JUCE, and enables high-quality audio editing
and playback for libopenshot.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        demo
Summary:        Program for demonstrating %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    demo
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libopenshot-audio-devel -f %{oreon_filedir}/libopenshot-audio-devel.list
%files -n libopenshot-audio-demo -f %{oreon_filedir}/libopenshot-audio-demo.list

%changelog

%autochangelog
