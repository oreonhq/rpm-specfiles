%global source7_hash 685adf14bd8e9c015b78097c1dc22f2f01343756f196acdc76a678e1ae352e11
%global source6_hash 1ab2de20460d4641553addfdfe6acd4109d871d5531f8f519a52ea4926303087
%global source5_hash 55c2da7574bc5f6f862da833698d828db34096133f4bb03f5ad86b0f6ea01a8d
%global source4_hash 7529a1c8ac501191ad470b166773364e66d9926aad632690c72c63a1dea7e9a6
%global source3_hash 234d99057242b914c3f787a7334b761ec549bd2c1a551c7dc9966283246e61ef
%global source0_hash 8f9f40d93838b912bd9ed35e598c0b7eabd08024cb18aa620c6aa9f9d49d0b57
%if 0%{?flatpak}
%bcond_with perltests
%else
%bcond_without perltests
%endif
Name:           prusa-slicer
Version:        2.9.6
Release:        1%{?dist}
Summary:        3D printing slicer optimized for Prusa printers
License:        AGPL-3.0-only
URL:            https://github.com/prusa3d/PrusaSlicer/
Source0:        https://github.com/prusa3d/PrusaSlicer/archive/version_%{version}.tar.gz
Source2:        %name.appdata.xml
%global libbgcode_commit 5041c093b33e2748e76d6b326f2251310823f3df
Source3:        https://github.com/prusa3d/libbgcode/archive/%{libbgcode_commit}.tar.gz#/libbgcode-%{libbgcode_commit}.tar.gz
Source4:        https://github.com/atomicobject/heatshrink/archive/refs/tags/v0.4.1.tar.gz#/heatshrink-0.4.1.tar.gz
Source5:        https://github.com/prusa3d/openvdb/archive/a68fd58d0e2b85f01adeb8b13d7555183ab10aa5.tar.gz#/openvdb-8.2.tar.gz
Source6:        https://github.com/catchorg/Catch2/archive/refs/tags/v3.8.0.tar.gz#/Catch2-3.8.0.tar.gz
Source7:        https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.tar.bz2
Patch5:         prusa-slicer-fix-uninitialized-imgui-segfault.patch
Patch6:         prusa-slicer-libseqarrange-notest.patch
Patch351:       https://github.com/archlinux/svntogit-community/blob/1dea61c0b5/trunk/prusa-slicer-openexr3.patch
Patch395:       prusa-slicer-opencascade.patch
Patch396:	prusa-slicer-pr-13761.patch
Patch421:       prusa-slicer-pr-13081.patch
Patch431:       prusa-slicer-pr-14388-cmake-4.patch
Patch441:	prusa-slicer-boost-1.88.patch
Patch442:	prusa-slicer-boost-1.84567.patch
Patch423:	prusa-slicer-boost-1.89.patch
%ifarch ppc64le
%global _smp_ncpus_max 8
%endif
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
%if %{with perltests}
%endif
Requires:       hicolor-icon-theme
Provides: bundled(admesh-libs) = 0.98.1
Provides: bundled(agg) = 2.4
Provides: bundled(avrdude) = 6.3
Provides: bundled(imgui) = 1.66
Provides: bundled(mesa-libGLU)
Provides: bundled(miniz) = 2.1.0prusa
Provides: bundled(libnest2d) = 0.3.2
Provides: bundled(nanosvg)
Provides: bundled(polyclipping) = 6.2.9
Provides: bundled(polypartition)
Provides: bundled(semver) = 1.0.0
Provides: bundled(shinyprofiler) = 2.6~rc1
Provides: bundled(libbgcode)
Provides: bundled(heatshrink) = 0.4.1
Provides: bundled(openvdb) = 8.2.0
Provides: bundled(eigen) = 3.3.7
Provides: PrusaSlicer = %version-%release
Obsoletes: slic3r-prusa3d < 1.41.3-2
Provides: slic3r-prusa3d = %version-%release
%undefine __cmake_in_source_build
%ifarch %ix86 %arm
%define _lto_cflags %{nil}
%endif
# oreon:deps
BuildRequires:  CGAL-devel
BuildRequires:  ImageMagick
BuildRequires:  NLopt-devel
BuildRequires:  boost-devel
BuildRequires:  cereal-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glew-devel
BuildRequires:  gtest-devel
BuildRequires:  ilmbase-devel
BuildRequires:  libgudev
BuildRequires:  nanosvg-devel
BuildRequires:  opencascade-devel
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(ExtUtils::Typemaps::Basic)
BuildRequires:  perl(ExtUtils::XSpp)
BuildRequires:  perl(ExtUtils::XSpp::Cmd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::WithXSpp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Wx)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(parent)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  qhull-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  tbb-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  wxGTK-devel
BuildRequires:  z3-devel
# /oreon:deps
%description
PrusaSlicer takes 3D models (STL, OBJ, AMF) and converts them into G-code
instructions for FFF printers or PNG layers for mSLA 3D printers. It's
compatible with any modern printer based on the RepRap toolchain, including all
those based on the Marlin, Prusa, Sprinter and Repetier firmware. It also works
with Mach3, LinuxCNC and Machinekit controllers.

PrusaSlicer is based on Slic3r by Alessandro Ranelucci and the RepRap
community.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n PrusaSlicer-version_%version -N
# Apply patches, but only apply 340+ on Fedora 34, 350+ on Fedora 35, etc...
%autopatch -M %[%{?fedora} * 10 + 9]

commit () { git commit -q -a -m "$1" --author "%{__scm_author}"; }

# Fix the "UNKNOWN" in the displayed version string
sed -i 's/UNKNOWN/Fedora/' version.inc
commit "Fix version string"

( cd bundled_deps && tar xvzf %SOURCE3 && mv libbgcode-* libbgcode )
sed -i 's#set(LibBGCode_SOURCE_DIR ""#set(LibBGCode_SOURCE_DIR "../../bundled_deps/libbgcode"#' deps/+LibBGCode/LibBGCode.cmake

( cd bundled_deps && tar xvzf %SOURCE4 && mv heatshrink-* heatshrink )
sed -i 's#URL https.*#SOURCE_DIR ../../bundled_deps/heatshrink#' deps/+heatshrink/heatshrink.cmake

( cd bundled_deps && tar xvzf %SOURCE5 && mv openvdb-* openvdb )
sed -i 's#URL https.*#SOURCE_DIR ../../bundled_deps/openvdb#; s/-DUSE_BLOSC=ON/-DUSE_BLOSC=OFF/' deps/+OpenVDB/OpenVDB.cmake

( cd bundled_deps && tar xvzf %SOURCE6 && mv Catch2-* Catch2 )
sed -i 's#URL "https.*#SOURCE_DIR ../../bundled_deps/Catch2#' deps/+Catch2/Catch2.cmake

( cd bundled_deps && tar xvjf %SOURCE7 && mv eigen-* Eigen )
sed -i 's#URL "https.*#SOURCE_DIR ../../bundled_deps/Eigen#' deps/+Eigen/Eigen.cmake

# We can't trivially patch Eigen to enable support for Cmake4, so here come the sed hacks
sed -i 's#cmake_minimum_required(VERSION 2.8.5#cmake_minimum_required(VERSION 2.8.5...4.0#' bundled_deps/Eigen/CMakeLists.txt

mkdir deps/ignored
mv deps/+* deps/ignored
mv deps/ignored/+LibBGCode deps/ignored/+heatshrink deps/ignored/+OpenVDB deps/ignored/+Catch2 deps/ignored/+Eigen deps

# Copy out specific license files so we can reference them later.
license () { basename=$( basename $1 ) ; mv bundled_deps/$1/$2 $2-$basename; git add $2-$basename; echo %%license $2-$basename >> license-files; }
license agg/agg copying
license avrdude/avrdude COPYING
license imgui LICENSE.txt
license libnest2d LICENSE.txt
license libbgcode LICENSE
license heatshrink LICENSE
license openvdb LICENSE
license Eigen COPYING.README
license Eigen COPYING.BSD
license Eigen COPYING.MINPACK
license Eigen COPYING.MPL2
git add license-files
commit "Move license files"

%build

%cmake -DSLIC3R_PCH=0 -DSLIC3R_FHS=1 -DSLIC3R_GTK=3 \
    -DSLIC3R_BUILD_TESTS=1 -DCMAKE_BUILD_TYPE=Release \
    -DPrusaSlicer_BUILD_DEPS:BOOL=ON \
    -DOPENVDB_USE_STATIC_LIBS=1 \
    -DCMAKE_EXE_LINKER_FLAGS=-lcrypto \
%if %{with perltests}
    -DSLIC3R_PERL_XS=1
%endif
%cmake_build
pushd resources/icons
find . -type f -name "*.png" -exec convert {} -strip {} \;
popd
%install
%cmake_install
mv %buildroot%_bindir/prusa-slicer %buildroot%_bindir/prusa-slicer.wrapped
cat >> %buildroot%_bindir/prusa-slicer <<'END'
export GDK_BACKEND=x11
exec %_bindir/prusa-slicer.wrapped "$@"
END
chmod 755 %buildroot%_bindir/prusa-slicer
mkdir -p %buildroot%_datadir/appdata
install -m 644 %SOURCE2 %buildroot%_datadir/appdata/%name.appdata.xml
%{?perl_vendorarch:rm -rf %buildroot/%perl_vendorarch}
%{?perl_vendorlib:rm -rf %buildroot/%perl_vendorlib}
ls -lR %buildroot%_datadir/PrusaSlicer/localization
rm %buildroot%_datadir/PrusaSlicer/localization/{PrusaSlicer.pot,list.txt}
find %buildroot%_datadir/PrusaSlicer/localization/ -name \*.po -delete
find %buildroot%_datadir/PrusaSlicer/localization -type f -o -type l | sed '
    s:'"%buildroot"'::
    s:\(.*/PrusaSlicer/localization/\)\([^/_]\+\)\(.*\.mo$\):%%lang(\2) \1\2\3:
    s:^\([^%].*\)::
    s:%lang(C) ::
    /^$/d
' > lang-files
find %buildroot%_datadir/PrusaSlicer/localization -type d | sed '
    s:'"%buildroot"'::
    s:\(.*\):%dir \1:
' >> lang-files
%if 0%{?flatpak}
rm -f %buildroot%_prefix/lib/udev/rules.d/90-3dconnexion.rules
%endif
rm -rf %buildroot%_datadir/PrusaSlicer/fonts
%oreon_autofiles main

%check

desktop-file-validate %buildroot%_datadir/applications/PrusaGcodeviewer.desktop
%ifarch x86_64 aarch64
%ctest
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
