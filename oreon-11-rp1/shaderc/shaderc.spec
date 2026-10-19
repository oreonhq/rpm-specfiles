%global source0_hash b938f85dec78ca7eb8139dcd1f613930eb7a84a8ce5ea944b6f861c291d916bc
%global glslang_version 301b4ede53d59b68bf55f95bb26412d9233c8187
Name:           shaderc
Version:        2026.4
Release:        1%{?dist}
Summary:        Collection of tools, libraries, and tests for Vulkan shader compilation
License:        Apache-2.0
URL:            https://github.com/google/shaderc
Source0:        https://github.com/google/%{name}/archive/%{glslang_version}.tar.gz
Patch:          0001-Drop-third-party-code-in-CMakeLists.txt.patch
Patch:          glslang_linker_flags.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
# /oreon:deps
%description
A collection of tools, libraries and tests for shader compilation.

Shaderc aims to to provide:
 - a command line compiler with GCC- and Clang-like usage, for better
   integration with build systems
 - an API where functionality can be added without breaking existing clients
 - an API supporting standard concurrency patterns across multiple
   operating systems
 - increased functionality such as file #include support

%package    -n  glslc
Summary:        A command line compiler for GLSL/HLSL to SPIR-V
%description -n glslc
A command line compiler for GLSL/HLSL to SPIR-V.

%package    -n  libshaderc
Summary:        A library for compiling shader strings into SPIR-V
%description -n libshaderc
A library for compiling shader strings into SPIR-V.

%package -n     libshaderc-devel
Summary:        Development files for libshaderc
Requires:       libshaderc%{?_isa} = %{version}-%{release}
%description -n libshaderc-devel
A library for compiling shader strings into SPIR-V.

Development files for libshaderc.

%package -n     libshaderc-static
Summary:        A library for compiling shader strings into SPIR-V (static libraries)
%description -n libshaderc-static
A library for compiling shader strings into SPIR-V.

Static libraries for libshaderc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{glslang_version}

rm -r third_party

# Stolen from Gentoo
# Create build-version.inc since we want to use our packaged
# SPIRV-Tools and glslang
sed -i -e '/build-version/d' glslc/CMakeLists.txt
echo \"shaderc $(grep -m1 -o '^v[[:digit:]]\{4\}\.[[:digit:]]\(-dev\)\? [[:digit:]]\{4\}-[[:digit:]]\{2\}-[[:digit:]]\{2\}$' CHANGES)\" \
        > glslc/src/build-version.inc
echo \"spirv-tools $(grep -m1 -o '^v[[:digit:]]\{4\}\.[[:digit:]]\(-dev\)\? [[:digit:]]\{4\}-[[:digit:]]\{2\}-[[:digit:]]\{2\}$' /usr/share/doc/spirv-tools/CHANGES)\" \
        >> glslc/src/build-version.inc
echo \"glslang %{glslang_version}\" >> glslc/src/build-version.inc

# Point to correct include
sed -i 's|SPIRV/GlslangToSpv.h|glslang/SPIRV/GlslangToSpv.h|' libshaderc_util/src/compiler.cc

%build

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_SKIP_RPATH=True \
       -DSHADERC_SKIP_TESTS=True \
       -DPYTHON_EXECUTABLE=%{python3} \
       -GNinja
%cmake_build
%install
%cmake_install
%oreon_autofiles glslc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libshaderc usr/*/lib*.so.*
%oreon_autofiles libshaderc-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libshaderc-static usr/*/lib*.so.*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n glslc -f %{oreon_filedir}/glslc.list
%files -n libshaderc -f %{oreon_filedir}/libshaderc.list
%files -n libshaderc-devel -f %{oreon_filedir}/libshaderc-devel.list
%files -n libshaderc-static -f %{oreon_filedir}/libshaderc-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2026.1-1
- Prepare for Oreon 11 (RP1)
