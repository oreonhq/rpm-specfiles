%global source0_hash 4c961c6b0809272b5bb2a8395170cff98292dea34a5cda925fd24adfc37b4bed

%global srcname OpenHMD
%global forgeurl https://github.com/thaytan/OpenHMD
%global date 20250112
%global commit 4dbc6c9e5929029023a0a1c09cfde6bbbb15761e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           openhmd
Version:        0.3.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Free and Open Source API and drivers for immersive technology

# OpenHMD is BSL-1.0, the rest comes from bundled dependencies
License:        BSL-1.0 AND MIT AND Unlicense
URL:            http://www.openhmd.net
Source0:        %{forgeurl}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
# License text based on the comment on top of src/ext_deps/nxjson.c
Source1:        LICENSE.miniz
# License text extracted from the comment at the bottom of src/ext_deps/miniz.c
Source2:        LICENSE.nxjson
# Add missing headers to fix the build with GCC 15 (#2340971)
Patch:          openhmd-missing-headers.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  glew-devel
BuildRequires:  hidapi-devel
BuildRequires:  libusb1-devel
BuildRequires:  opencv-devel
BuildRequires:  SDL2-devel

Recommends:     xr-hardware

# Vendored under src/ext_deps/miniz.c and included via a header wrapper
# License: Unlicense
Provides:       bundled(miniz) = 1.15
# Vendored under src/ext_deps/nxjson.{c,h} and modified
# License: MIT
Provides:       bundled(nxjson) = 20180520

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

# Build documentation
doxygen

%install
%meson_install

%check
%meson_test

%files
%license LICENSE LICENSE.miniz LICENSE.nxjson
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license LICENSE
%doc html

%files examples
%{_bindir}/openhmd_simple_example
%{_bindir}/openhmd_opengl_example

%changelog
%autochangelog
