%global source0_hash 49d5cfe772d3aa10cd4879f2f6e189f5083c08e4c8ea01bf3d5b87c97dfca7d2
Name:           plutosvg
Version:        0.0.8
Release:        1%{?dist}
Summary:        Tiny SVG rendering library in C
License:        MIT
URL:            https://github.com/sammycage/plutosvg
Source0:        https://github.com/sammycage/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-plutovg-header.patch
Patch1:         %{name}-soversion-cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(plutovg)
# /oreon:deps
%description
PlutoSVG is a compact and efficient SVG rendering library written in C. It is
specifically designed for parsing and rendering SVG documents embedded in
OpenType fonts, providing an optimal balance between speed and minimal memory
usage. It is also suitable for rendering scalable icons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       plutovg-devel%{?_isa}       
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        samples
Summary:        Sample programs for %{name}
%description    samples
Sample programs that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DPLUTOSVG_BUILD_EXAMPLES=ON \
    -DPLUTOSVG_ENABLE_FREETYPE=ON
%cmake_build
%install
%cmake_install
install -p -m 0755 -D %{_vpath_builddir}/examples/camera2png %{buildroot}%{_bindir}/%{name}_camera2png
install -p -m 0755 -D %{_vpath_builddir}/examples/emoji2png %{buildroot}%{_bindir}/%{name}_emoji2png
install -p -m 0755 -D %{_vpath_builddir}/examples/svg2png %{buildroot}%{_bindir}/%{name}_svg2png
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
export LD_LIBRARY_PATH=%{_vpath_builddir}
%{_vpath_builddir}/examples/camera2png
%{_vpath_builddir}/examples/svg2png camera.svg camera.png
%files -f %{oreon_filedir}/main.list
%files -n plutosvg-devel -f %{oreon_filedir}/plutosvg-devel.list
%files -n plutosvg-samples -f %{oreon_filedir}/plutosvg-samples.list

%changelog

%autochangelog
