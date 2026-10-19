%global source0_hash 1566bc3b99113734c46b8cb189c6a759117c890684378e67edbfa67c29a41bb8
%global octpkg mcxlab
%global project mcxcl
%global forgeurl  https://github.com/fangq/%{project}
Name:           octave-%{octpkg}
Version:        2024.2
Release:        1%{?dist}
Summary:        MCXLAB - A GPU Monte Carlo 3-D photon transport simulator for MATLAB/Octave
License:        GPL-3.0-or-later
URL:            http://mcx.space
%forgemeta
Source0:        %{forgeurl}/archive/v%{version}/%{project}-%{version}.tar.gz
Patch:          %{forgeurl}/pull/51.patch
Requires:       octave opencl-filesystem
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  ocl-icd-devel
BuildRequires:  octave-devel
BuildRequires:  opencl-headers
BuildRequires:  vim-common
# /oreon:deps
%description
Monte Carlo eXtreme OpenCL (MCX-CL) is a fast photon transport simulation
software for 3D heterogeneous turbid media, accelerated by GPUs.
MCXLAB-CL is the native MEX version of MCX-CL for Matlab and GNU Octave.
It contains the entire MCX-CL code into a MEX function which can be called
directly inside Matlab or Octave. The input and output files in MCX are
replaced by convenient in-memory struct variables in MCXLAB-CL, thus,
making it much easier to use and interact. Matlab/Octave also provides
convenient plotting and data analysis functions. With MCXLAB-CL, your
analysis can be streamlined and speed-up without involving disk files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S git

rm -rf .git_filters deploy setup example
cp utils/*.m mcxlabcl

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Monte Carlo eXtreme OpenCL (MCX-CL) is a fast photon transport simulation 
 software for 3D heterogeneous turbid media, accelerated by GPUs.
 MCXLAB-CL is the native MEX version of MCX-CL for Matlab and GNU Octave. 
 It contains the entire MCX-CL code into a MEX function which can be called 
 directly inside Matlab or Octave. The input and output files in MCX are 
 replaced by convenient in-memory struct variables in MCXLAB-CL, thus, 
 making it much easier to use and interact. Matlab/Octave also provides 
 convenient plotting and data analysis functions. With MCXLAB-CL, your 
 analysis can be streamlined and speed-up without involving disk files.
EOF

cp LICENSE.txt COPYING

cat > INDEX << EOF
mcxlabcl >> MCXLABCL
MCXLABCL
 cwdiffusion
 getdistance
 hobbysplines
 image3i
 islicer
 loadmc2
 loadmch
 json2mcx
 mcx2json
 mcxdcsg1
 mcxdetphoton
 mcxdettime
 mcxdettpsf
 mcxdetweight
 mcxfluence2energy
 mcxlabcl
 mcxloadfile
 mcxloadnii
 mcxmeanpath
 mcxmeanscat
 mcxplotphotons
 mcxplotvol
 normalizemcx
 serialcorr
 slice3i
 stacked_bar3
 tddiffusion
EOF

%build

cd src
make oct LIBOPENCLDIR=`octave-config -p OCTLIBDIR`
cd ../
rm README.txt
mv mcxlabcl/README.txt .
rm mcxlabcl/*.txt
mv mcxlabcl/examples .
mv mcxlabcl inst
rm -rf src
rm -rf doc
%octave_pkg_build
%install
%octave_pkg_install
%oreon_autofiles main

%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
