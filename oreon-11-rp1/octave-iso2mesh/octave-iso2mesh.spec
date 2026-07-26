%global source0_hash e46a4434a3e7c00044c8f4f167e18b6f4a85be7d22838c8f948ce8cc8c01b850

%global octpkg iso2mesh

Name:           octave-%{octpkg}
Version:        1.9.8
Release:        6%{?dist}
Summary:        A 3D surface and volumetric mesh generator for MATLAB/Octave
# Main package: GPLv3+
# Meshfix: GPLv2+
# JMeshLib: GPLv2+
# Tetgen: AGPLv3+
# Automatically converted from old format: GPLv3+ and GPLv2+ and AGPLv3+ - review is highly recommended.
License: GPL-3.0-or-later AND GPL-2.0-or-later AND AGPL-3.0-or-later

URL:            http://iso2mesh.sf.net
# the following utilities are called internally by iso2mesh (stored under a private folder),
# this is needed for making outputs reproducible
Source0:        https://github.com/fangq/iso2mesh/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Source1:        https://github.com/fangq/cork/archive/v0.9.1/cork-0.9.1.tar.gz
Source2:        https://github.com/fangq/meshfix/archive/v1.2.2/meshfix-1.2.2.tar.gz
Source3:        http://ftp.mcs.anl.gov/pub/petsc/externalpackages/tetgen1.5.1.tar.gz

#  Policy CMP0064 is not set: Support new TEST if() operator.
# See also https://github.com/CGAL/cgal/issues/5857
Patch0:         iso2mesh-1.9.6-CMakeCMP0064.patch
# Fix build with suplerlu 7
# https://github.com/fangq/iso2mesh/issues/86
Patch1:         octave-iso2mesh-superlu7.patch
Patch2:         octave-iso2mesh-c99.patch

ExcludeArch:    armv7hl
BuildRequires:  cmake
BuildRequires:  cmake(cgal)
BuildRequires:  cmake(superlu)
BuildRequires:  cmake(tbb)
BuildRequires:  cmake(zlib)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(octave)

%if 0%{?fedora} >=32
Requires:       octave mpfr-devel boost-devel SuperLU octave-jsonlab octave-jnifti octave-zmat
%else
Requires:       octave CGAL SuperLU octave-jsonlab octave-jnifti octave-zmat
%endif

Requires(post): octave
Requires(postun): octave

%description
Iso2Mesh is a MATLAB/Octave-based mesh generation toolbox,
designed for easy creation of high quality surface and
tetrahedral meshes from 3D volumetric images. It contains
a rich set of mesh processing scripts/programs, working
either independently or interacting with external free
meshing utilities. Iso2Mesh toolbox can directly convert
a 3D image stack, including binary, segmented or gray-scale
images such as MRI or CT scans, into quality volumetric
meshes. This makes it particularly suitable for multi-modality
medical imaging data analysis and multi-physics modeling.
Iso2Mesh is cross-platform and is compatible with both MATLAB
and GNU Octave.

%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for the Iso2Mesh toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg}
Recommends:     %{octpkg}-demos

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -b 1 -n %{octpkg}-%{version}
%setup -q -T -D -b 2 -n meshfix-1.2.2
%setup -q -T -D -b 3 -n %{octpkg}-%{version}
%patch -P 0 -z .bak -p1
rm -rf tools/cork
rm -rf tools/meshfix
rm -rf tools/tetgen
mv ../cork-0.9.1 tools/cork
mv ../meshfix-1.2.2 tools/meshfix
mv ../tetgen1.5.1 tools/tetgen
%patch -P 1 -p1
%patch -P 2 -p1
rm -rf bin/*.mex* bin/*.exe bin/*.dll

cp COPYING.txt COPYING

mkdir -p inst/

rm -rf base64decode base64encode fast_match_bracket gzipdecode gzipencode \
jdatadecode jdataencode jnifticreate loadjnifti loadjson loadmsgpack \
loadnifti loadubjson lz4decode lz4encode lz4hcdecode lz4hcencode lzipdecode \
lzipencode lzmadecode lzmaencode match_bracket nestbracket2dim nifticreate \
nii2jnii niicodemap niiformat readnifti savebnii savejnifti savejnii \
savemsgpack savenifti saveubjson zlibdecode zlibencode

mv *.m inst/
mv img2mesh.fig inst/

# Fix jmeshlib build flags
sed -e "s|-Wall|%{optflags}|;s|^LIBS = |&$RPM_LD_FLAGS |" \
    -i tools/meshfix/contrib/JMeshLib/test/Makefile

# Link FlexiBLAS instead of BLAS
sed -e "s| blas| flexiblas|" -i tools/meshfix/CMakeLists.txt

# Fix tetgen build flags
sed -e "s|^\(CXXFLAGS = \).*|\1%{optflags} $RPM_LD_FLAGS|" \
    -e "s|-O0|%{optflags} $RPM_LD_FLAGS|" \
    -i tools/tetgen/makefile

%build
%set_build_flags
%if 0%{?__isa_bits} == 32
# Reduce the debuginfo level to avoid virtual memory exhaustion
CXXFLAGS="${CXXFLAGS-} -g1"
%endif
pushd tools
# can't use make_build macro below because parallel make with CGAL exhausts
# vm's memory and crash the building process, use sequential make instead
make USERCCFLAGS="%{optflags}"
popd
pushd bin
ln -s tetgen1.5 tetgen
popd

mkdir inst/bin
pushd bin
for exec in *; do
   ln -s %{_libexecdir}/%{octpkg}/$exec ../inst/bin/$exec
done
popd
%octave_pkg_build

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install
install -m 0755 -vd  %{buildroot}%{_libexecdir}/%{octpkg}
install -m 0755 -vp  bin/* %{buildroot}%{_libexecdir}/%{octpkg}/

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license COPYING.txt
%doc README.txt
%doc Content.txt
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%dir %{octpkgdir}/doc
%dir %{octpkgdir}/bin
%{_libexecdir}/%{octpkg}
%{octpkgdir}/doc/*
%{octpkgdir}/bin/*
%{octpkgdir}/*.m
%{octpkgdir}/*.fig
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license COPYING.txt
%doc sample

%changelog
%autochangelog
