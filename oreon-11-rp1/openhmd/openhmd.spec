%global source0_hash 4c961c6b0809272b5bb2a8395170cff98292dea34a5cda925fd24adfc37b4bed
%global srcname OpenHMD
%global forgeurl https://github.com/thaytan/OpenHMD
%global date 20250112
%global commit 4dbc6c9e5929029023a0a1c09cfde6bbbb15761e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           openhmd
Version:        0.3.0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Free and Open Source API and drivers for immersive technology
License:        BSL-1.0 AND MIT AND Unlicense
URL:            http://www.openhmd.net
Source0:        %{forgeurl}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Source1:        LICENSE.miniz
Source2:        LICENSE.nxjson
Patch:          openhmd-missing-headers.patch
Recommends:     xr-hardware
Provides:       bundled(miniz) = 1.15
Provides:       bundled(nxjson) = 20180520
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  hidapi-devel
BuildRequires:  libusb1-devel
BuildRequires:  meson
BuildRequires:  opencv-devel
# /oreon:deps
%description
OpenHMD aims to provide a Free and Open Source API and drivers for immersive
technology, such as head mounted displays with built in head tracking.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}
%description    devel
This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains developer documentation for %{name}.

%package        examples
Summary:        Examples for %{name}
%description    examples
This package contains examples making use of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit} -p1

# Copy license texts for bundled dependencies
cp -p %SOURCE1 %SOURCE2 .

%build

%meson -Dexamples=simple,opengl
%meson_build
doxygen
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n openhmd-devel -f %{oreon_filedir}/openhmd-devel.list
%files -n openhmd-doc -f %{oreon_filedir}/openhmd-doc.list
%files -n openhmd-examples -f %{oreon_filedir}/openhmd-examples.list

%changelog

%autochangelog
