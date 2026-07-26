%global source0_hash 27b81ade7dd3ec74ae7aca4b22e0c9f552eba663ff54f91f2dada57a371f37f4

Name:           obs-studio-plugin-pwvideo
Version:        0.2.3
Release:        %autorelease
Summary:        Generic PipeWire video source for OBS Studio

License:        GPL-2.0-or-later
URL:            https://github.com/hoshinolina/obs-pwvideo
Source0:        %{url}/archive/%{version}/obs-pwvideo-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.22
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gl)

Requires:       obs-studio%{?_isa}
Supplements:    obs-studio%{?_isa}

ExcludeArch:    %{ix86}

%description
Generic PipeWire video source for OBS.
Useful for routing arbitrary video streams into
your scenes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C

%conf
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -GNinja

%build
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/obs-pwvideo.so
%{_datadir}/obs/obs-plugins/obs-pwvideo/

%changelog
%autochangelog
