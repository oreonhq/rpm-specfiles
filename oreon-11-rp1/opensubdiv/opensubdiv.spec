%global source0_hash f843eb49daf20264007d807cbc64516a1fed9cdb1149aaf84ff47691d97491f9
%undefine       __cmake_in_source_build
%global         upstream_version 3_7_0
Name:           opensubdiv
Version:        3_7_0
Release:        1%{?dist}
Summary:        High performance subdivision surface libraries
License:        Pixar AND MIT
Url:	            https://github.com/PixarAnimationStudios/OpenSubdiv
Source0:        https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:         	%{name}-rpath.patch
Patch:          opensubdiv-3.5.0-reproducible-docs.patch
Patch:          0001-Downstream-only-do-not-compile-static-libraries.patch
Obsoletes:      %{name}-libs < %{version}-%{release}
Obsoletes:      %{name}-doc < 3.5.0-10
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(ptex)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pygments)
# /oreon:deps
%description
OpenSubdiv is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and
GPU architectures. 
This codepath is optimized for drawing deforming subdivs with static topology
at interactive framerates.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%autosetup -p1 -n OpenSubdiv-%{upstream_version}%{?prerelease:_%{prerelease}}

# work around linking glitch
# https://github.com/PixarAnimationStudios/OpenSubdiv/issues/1196
sed -i 's|${PLATFORM_GPU_LIBRARIES}|${PLATFORM_GPU_LIBRARIES} ${CMAKE_DL_LIBS}|' opensubdiv/CMakeLists.txt

# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/#_compilationminification
find . -type f -name '*.min.js' -print -delete

%build

%cmake \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_LIBDIR_BASE=%{_libdir} \
       -DGLEW_LOCATION=%{_libdir} \
       -DGLFW_LOCATION=%{_libdir} \
       -DNO_CLEW=1 \
       -DNO_CUDA=1 \
       -DNO_DOC=1\
       -DNO_EXAMPLES=1 \
       -DNO_GLFW_X11=1 \
       -DNO_METAL=1 \
       -DNO_REGRESSION=1 \
       -DNO_TUTORIALS=1 \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DTBB_LOCATION=%{_libdir}
%cmake_build
%{?_with_tests:
%check

make test V=1
}
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n opensubdiv-devel -f %{oreon_filedir}/opensubdiv-devel.list

%changelog

%autochangelog
