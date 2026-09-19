%global source0_hash f4386fac8410023292246203ef643ad92395ac188459fa4eccf94c4427b1b4dc

%global octpkg brain2mesh

Name:           octave-%{octpkg}
Version:        0.5
Release:        19%{?dist}
Summary:        A fully automated high-quality brain tetrahedral mesh generation toolbox
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://mcx.space/brain2mesh
Source0:        https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave octave-image octave-iso2mesh octave-jsonlab octave-zmat octave-jnifti
Requires(post): octave
Requires(postun): octave

%description
The Brain2Mesh toolbox provides a streamlined matlab function to convert
a segmented brain volumes and surfaces into a high-quality multi-layered
tetrahedral brain/full head mesh. Typical inputs include segmentation
outputs from SPM, FreeSurfer, FSL etc. This tool does not handle the
segmentation of MRI scans, but examples of how commonly encountered
segmented datasets can be used to create meshes can be found in the 
package named %{octpkg}-demos.

%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for the brain2mesh toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg}

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{octpkg}-%{version}

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com> and Anh Phong Tran <tran.anh@husky.neu.edu>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description:  The Brain2Mesh toolbox provides a streamlined matlab function to convert
 a segmented brain volumes and surfaces into a high-quality multi-layered
 tetrahedral brain/full head mesh. Typical inputs include segmentation
 outputs from SPM, FreeSurfer, FSL etc. This tool does not handle the
 segmentation of MRI scans, but examples of how commonly encountered
 segmented datasets can be used to create meshes can be found in the 
 package named %{octpkg}-demos.
URL: %{url}
Depends: image, iso2mesh, jsonlab, jnifti, zmat
EOF

cat > INDEX << EOF
brain2mesh >> Brain2Mesh
 brain2mesh
 intriangulation
EOF

mkdir -p inst/
mv *.m inst/

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc README.md
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license LICENSE.txt
%doc examples

%changelog
%autochangelog
