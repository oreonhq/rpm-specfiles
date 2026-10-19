%global source0_hash 2b0d17a6e016f47b86f9c00e2cb82600041b1ea1f7d2a00c2d46ae542cbfed3c
Name:           plutovg
Version:        1.3.3
Release:        1%{?dist}
Summary:        Tiny 2D vector graphics library in C
License:        MIT AND FTL
URL:            https://github.com/sammycage/plutovg
Source0:        https://github.com/sammycage/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-system-stb.patch
Patch1:         %{name}-soversion-cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_truetype-devel
# /oreon:deps
%description
PlutoVG is a standalone 2D vector graphics library in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        samples
Summary:        Sample programs for %{name}
%description    samples
Sample programs that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove bundled stb:
rm -fv source/%{name}-stb-*.h

%build

%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DPLUTOVG_BUILD_EXAMPLES=ON
%cmake_build
%install
%cmake_install
install -p -m 0755 -D %{_vpath_builddir}/examples/smiley %{buildroot}%{_bindir}/smiley
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
export LD_LIBRARY_PATH=%{_vpath_builddir}
%{_vpath_builddir}/examples/smiley
%files -f %{oreon_filedir}/main.list
%files -n plutovg-devel -f %{oreon_filedir}/plutovg-devel.list
%files -n plutovg-samples -f %{oreon_filedir}/plutovg-samples.list

%changelog

%autochangelog
