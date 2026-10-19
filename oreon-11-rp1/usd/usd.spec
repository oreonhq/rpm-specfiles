%global source0_hash none
%global downstream_so_version 0.26.3
%bcond alembic       1
%bcond draco         1
%bcond embree        1
%bcond jemalloc      0
%bcond materialx     1
%bcond ninja         1
%bcond openshading   1
%bcond openvdb       1
%bcond ocio          1
%bcond oiio          1
%bcond ptex          1
%bcond usdview       1
%bcond test          0
Name:           usd
Version:        26.08
Release:        1%{?dist}
Summary:        3D VFX pipeline interchange file format
License:        %{shrink:
                Pixar AND
                Apache-2.0 AND
                BSD-3-Clause AND
                BSD-2-Clause AND
                BSL-1.0 AND
                MIT AND
                (MIT OR Unlicense) AND
                (Pixar AND GPL-3.0-or-later WITH Bison-exception-2.2)
                }
URL:            http://www.openusd.org/
%global forgeurl https://github.com/PixarAnimationStudios/OpenUSD
Source0:        %{forgeurl}/archive/v%{version}/OpenUSD-%{version}.tar.gz
Source1:        org.openusd.usdview.desktop
Patch:          0001-Downstream-only-add-an-SONAME-version.patch
Patch:          0001-Downstream-only-use-Valgrind-macro-instead-of-inline.patch
Patch:          0001-Downstream-only-use-the-system-double-conversion-lib.patch
Patch:          0002-Downstream-only-use-the-system-lz4-library.patch
Patch:          0003-Downstream-only-use-the-system-pugixml-library.patch
Patch:          0004-Downstream-only-use-the-system-rapidjson-library.patch
Patch:          0005-Downstream-only-use-the-system-libdeflate.patch
Patch:          0006-Downstream-only-use-the-system-libavif.patch
Patch:          %{forgeurl}/pull/3903.patch
%if %{with ninja}
%endif
%if %{with alembic}
%endif
%if %{with draco}
%endif
%if %{with embree}
%endif
%if %{with jemalloc}
%endif
%if %{with materialx}
%endif
%if %{with ocio}
%endif
%if %{with oiio}
%endif
%if %{with openshading}
%endif
%if %{with openvdb}
%endif
%if %{with ptex}
%endif
Requires:       usd-libs%{?_isa} = %{version}-%{release}
Requires:       python3-usd%{?_isa} = %{version}-%{release}
ExclusiveArch:  %{arm64} %{x86_64}
# oreon:deps
BuildRequires:  cli11-devel
BuildRequires:  cli11-static
BuildRequires:  cmake
BuildRequires:  cmake(Alembic)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenImageIO)
BuildRequires:  cmake(OpenSubdiv)
BuildRequires:  cmake(double-conversion)
BuildRequires:  cmake(materialx)
BuildRequires:  cmake(pugixml)
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  draco-devel
BuildRequires:  embree-devel
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  help2man
BuildRequires:  materialx-data
BuildRequires:  ninja-build
BuildRequires:  openshadinglanguage
BuildRequires:  openvdb-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(oslexec)
BuildRequires:  pkgconfig(ptex)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pyside6-tools
BuildRequires:  python3-materialx
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pyopengl)
BuildRequires:  python3dist(pyside6)
BuildRequires:  rapidjson-devel
BuildRequires:  rapidjson-static
BuildRequires:  robin-map-devel
BuildRequires:  robin-map-static
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_image_write-static
BuildRequires:  valgrind-devel
# /oreon:deps
%description
Universal Scene Description (USD) is a time-sampled scene
description for interchange between graphics applications.

%package        libs
Summary:        Universal Scene Description library
Provides:       bundled(ilmbase) = 2.5.3
Provides:       bundled(PEGTL) = 3.2.7
Provides:       bundled(openexr) = 3.2.0
Provides:       bundled(boost) = 1.85.0
Provides:       bundled(pbrt-v4) = 4~20251208.8c19f30
Provides:       bundled(cycles) = 4.5.0^20251210.0be21d4
%description libs
Universal Scene Description (USD) is an efficient, scalable system for
authoring, reading, and streaming time-sampled scene description for
interchange between graphics applications.

%package        devel
Summary:        Development files for USD
Requires:       usd-libs%{?_isa} = %{version}-%{release}
Requires:       cli11-devel cli11-static
Requires:       robin-map-devel robin-map-static
Requires:       cmake(OpenSubdiv)
%if %{with materialx}
Requires:       cmake(materialx)
%endif
%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for usd. If you would like to develop programs using usd,
you will need to install usd-devel.

# For usdview, usdcompress
%package -n python3-usd
Summary:        Development files for USD
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2)
%if %{with usdview}
BuildRequires:  desktop-file-utils
BuildRequires:  python3dist(pyside6)
BuildRequires:  pyside6-tools
BuildRequires:  python3dist(pyopengl)
%endif
Requires:       font(roboto)
Requires:       font(robotoblack)
Requires:       font(robotolight)
Requires:       font(robotomono)
Requires:       python3dist(jinja2)
%if %{with usdview}
Requires:       python3dist(pyside6)
Requires:       python3dist(pyopengl)
%endif
Requires:       usd-libs%{?_isa} = %{version}-%{release}
%py_provides    python3-pxr
%description -n python3-usd
Python language bindings for the Universal Scene Description (USD) C++ API

%prep

%autosetup -p1 -n OpenUSD-%{version}

# Convert NOTICE.txt from CRNL line encoding
dos2unix NOTICE.txt

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

# Further drop shebangs line for some py files
sed -r -i '1{/^#!/d}' \
        pxr/usd/sdr/shaderParserTestUtils.py \
        pxr/usd/usdUtils/updateSchemaWithSdrNode.py \
        pxr/usdImaging/usdviewq/usdviewApi.py

# Unbundle Google Roboto fonts
rm -rvf pxr/usdImaging/usdviewq/fonts/*
ln -s %{_datadir}/fonts/google-roboto pxr/usdImaging/usdviewq/fonts/Roboto
ln -s %{_datadir}/fonts/google-roboto-mono \
    pxr/usdImaging/usdviewq/fonts/Roboto_Mono

# Unbundle stb_image, stb_image_write, stb_image_resize:
pushd pxr/imaging/hio/stb
cp -p %{_usr}/include/stb_image.h .
patch -p1 < stb_image.patch
ln -svf %{_usr}/include/stb_image_resize.h \
    %{_usr}/include/stb_image_write.h ./
popd

# Remove bundled doxygen-awesome-css (CSS and JS files) since we are not
# building Doxygen-generated HTML documentation.
rm -rf docs/doxygen/doxygen-awesome-css/

# Remove the bundled copy of double-conversion.
#
# From pxr/base/tf/pxrDoubleConversion/README, the upstream double-conversion
# is patched with pxr/base/tf/pxrDoubleConversion/pxr-double-conversion.patch;
# examination of that patch shows that it merely adds namespaces and renames
# symbols, rather than making functional changes, so using the system library
# should be safe.
find pxr/base/tf/pxrDoubleConversion -type f ! -name '*.h' -print -delete
for hdr in pxr/base/tf/pxrDoubleConversion/*.h
do
  cat > "${hdr}" <<EOF
#include <double-conversion/$(basename "${hdr}")>
namespace pxr_double_conversion = double_conversion;
EOF
done
# Similarly, remove the bundled copy of lz4. Change in the bundled copy can be
# identified by source-code comments, and appear to be limited to adding
# namespaces and removing C linkage.
rm -v pxr/base/tf/pxrLZ4/*
cat > pxr/base/tf/pxrLZ4/lz4.h <<'EOF'
#include <lz4.h>
// System LZ4 has C linkage; this just allows "using namespace"
namespace pxr_lz4 {}
EOF
# Remove the bundled copy of cli11.
rm -v pxr/base/tf/pxrCLI11/*
cat > pxr/base/tf/pxrCLI11/CLI11.h <<'EOF'
#include <CLI/CLI.hpp>
namespace pxr_CLI = CLI;
EOF
# Remove the bundled copy of pugixml.
find third_party/renderman/plugin/rmanArgsParser/pugixml/ \
    -type f ! -name '*.hpp' -print -delete
for hdr in third_party/renderman/plugin/rmanArgsParser/pugixml/*.hpp
do
  cat > "${hdr}" <<EOF
#include <$(basename "${hdr}")>
EOF
done
# Remove the bundled copy of rapidjson. It does not seem to have been modified
# or forked at all.
rm -rv pxr/base/js/rapidjson/
# Remove the bundled copy of robin-map. There are several macros that are
# renamed from TSL_*/tsl_* to PXR_TSL_*/pxr_tsl_* in the bundled copy, and we
# could “alias” these if necessary to avoid patching call sites, but for now
# are not used outside the library headers and we can get by with merely
# aliasing the namespace.
find pxr/base/tf/pxrTslRobinMap -type f ! -name '*.h' -print -delete
for hdr in pxr/base/tf/pxrTslRobinMap/*.h
do
  cat > "${hdr}" <<EOF
#include <tsl/$(basename "${hdr}")>
namespace pxr_tsl = tsl;
EOF
done
# Remove the bundled copy of libdeflate.
rm -rv pxr/imaging/plugin/hioOpenEXR/OpenEXR/deflate/
# Remove the bundled copies of libavif, along with the associated libaom and
# the libyuv that is in the libavif sources.
rm -rv pxr/imaging/plugin/hioAvif/aom/ \
    pxr/imaging/plugin/hioAvif/AVIF/

# Use c++17 standard otherwise build fails
sed -i 's|set(CMAKE_CXX_STANDARD 14)|set(CMAKE_CXX_STANDARD 17)|g' \
        cmake/defaults/CXXDefaults.cmake

# Fix libdir installation
sed -i 's|lib/usd|%{_libdir}/usd|g' \
        cmake/macros/{Private,Public}.cmake
sed -i 's|plugin/usd|%{_libdir}/usd/plugin|g' \
        cmake/macros/{Private,Public}.cmake
sed -i 's|"lib"|%{_libdir}|g' \
        cmake/macros/{Private,Public}.cmake
sed -i 's|/python|/python%{python3_version}/site-packages|g' \
        cmake/macros/{Private,Public}.cmake pxr/usdImaging/usdviewq/CMakeLists.txt
sed -i 's|/pxrConfig.cmake|%{_libdir}/cmake/pxr/pxrConfig.cmake|g' \
        pxr/CMakeLists.txt
sed -i 's|"cmake"|"%{_libdir}/cmake/pxr"|g' \
        pxr/CMakeLists.txt
sed -i 's|${PXR_CMAKE_DIR}/cmake|${PXR_CMAKE_DIR}|g' \
        pxr/pxrConfig.cmake.in
sed -i 's|${PXR_CMAKE_DIR}/include|/usr/include|g' \
        pxr/pxrConfig.cmake.in
sed -i 's|EXACT COMPONENTS|COMPONENTS|g' \
        pxr/pxrConfig.cmake.in

# Fix cmake directory destination
sed -i 's|"${CMAKE_INSTALL_PREFIX}"|%{_libdir}/cmake/pxr|g' pxr/CMakeLists.txt

# Use Embree4 instead of Embree3. The find-then-modify pattern preserves mtimes
# on sources that did not need to be modified.
find . -type f -exec gawk '/embree3/ { print FILENAME }' '{}' '+' |
  xargs -r sed -r -i 's/(embree)3/\14/'

%build

extra_flags="${extra_flags-} $(pkgconf --cflags Imath)"
extra_flags="${extra_flags-} -DTBB_SUPPRESS_DEPRECATED_MESSAGES=1"
%cmake \
%if %{with ninja}
     -GNinja \
%endif
%if %{with jemalloc}
     -DPXR_MALLOC_LIBRARY="%{_libdir}/libjemalloc.so" \
%endif
     \
     -DCMAKE_CXX_FLAGS_RELEASE="${CXXFLAGS-} ${extra_flags}" \
     -DCMAKE_CXX_STANDARD=17 \
     -DCMAKE_C_FLAGS_RELEASE="${CFLAGS-} ${extra_flags}" \
     -DCMAKE_EXE_LINKER_FLAGS="${LDFLAGS}" \
     -DCMAKE_SHARED_LINKER_FLAGS="${LDFLAGS}" \
     -DCMAKE_SKIP_INSTALL_RPATH=ON \
     -DCMAKE_SKIP_RPATH=ON \
     -DCMAKE_VERBOSE_MAKEFILE=ON \
     \
     -DPXR_BUILD_HTML_DOCUMENTATION=FALSE \
     -DPXR_BUILD_PYTHON_DOCUMENTATION=FALSE \
     -DPXR_BUILD_EXAMPLES=OFF \
     -DPXR_BUILD_IMAGING=ON \
     -DPXR_BUILD_MONOLITHIC=ON \
     -DPXR_BUILD_TESTS=%{expr:%{with test}?"ON":"OFF"} \
     -DPXR_BUILD_TUTORIALS=OFF \
     -DPXR_BUILD_USD_IMAGING=ON \
     -DPXR_BUILD_EXEC=ON \
     -DPXR_BUILD_USD_TOOLS=ON \
     -DPXR_BUILD_USDVIEW=%{expr:%{with usdview}?"ON":"OFF"} \
     \
     -DPXR_BUILD_ALEMBIC_PLUGIN=%{expr:%{with alembic}?"ON":"OFF"} \
     -DPXR_BUILD_DRACO_PLUGIN=%{expr:%{with draco}?"ON":"OFF"} \
     -DPXR_BUILD_EMBREE_PLUGIN=%{expr:%{with embree}?"ON":"OFF"} \
     -DPXR_BUILD_OPENCOLORIO_PLUGIN=%{expr:%{with ocio}?"ON":"OFF"} \
     -DPXR_BUILD_OPENIMAGEIO_PLUGIN=%{expr:%{with oiio}?"ON":"OFF"} \
     -DPXR_BUILD_PRMAN_PLUGIN=OFF \
     \
     -DPXR_ENABLE_OPENVDB_SUPPORT=%{expr:%{with openvdb}?"ON":"OFF"} \
     -DPXR_ENABLE_HDF5_SUPPORT=ON \
     -DPXR_ENABLE_PTEX_SUPPORT=%{expr:%{with ptex}?"ON":"OFF"} \
     -DPXR_ENABLE_OSL_SUPPORT=%{expr:%{with openshading}?"ON":"OFF"} \
     -DPXR_ENABLE_MALLOCHOOK_SUPPORT=OFF \
     -DPXR_ENABLE_MATERIALX_SUPPORT=%{expr:%{with materialx}?"ON":"OFF"} \
     -DPXR_ENABLE_PYTHON_SUPPORT=ON \
     \
     -DPXR_INSTALL_LOCATION="%{_libdir}/usd/plugin" \
     \
     -DPXR_VALIDATE_GENERATED_CODE=OFF \
     \
     -DPYSIDEUICBINARY:PATH=pyside6-uic \
     -DPYSIDE_AVAILABLE=ON \
     -DPYTHON_EXECUTABLE=%{python3}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitearch}/pxr/Usd/usdGenSchema.py'
%if %{with usdview}
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{SOURCE1}
%endif
sed -i 's|OpenGL::GL|${OPENGL_gl_LIBRARY}|g' \
        %{buildroot}%{_libdir}/cmake/pxr/pxrTargets.cmake
rm -vrf '%{buildroot}%{_datadir}/usd/examples'
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  PYTHONPATH='%{buildroot}%{python3_sitearch}' \
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
%oreon_autofiles python3-usd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with usdview}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.openusd.usdview.desktop
%endif
%{?with_test:%ctest}
%files -f %{oreon_filedir}/main.list
%files -n usd-libs -f %{oreon_filedir}/usd-libs.list
%files -n usd-devel -f %{oreon_filedir}/usd-devel.list
%files -n python3-usd -f %{oreon_filedir}/python3-usd.list

%changelog

%autochangelog
