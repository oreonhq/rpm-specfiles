%global source0_hash b1167be254ed1cae2f1152d72e642259823a4e558124ce89d3ff46ab8cdfba92

%global octpkg metch

Name:           octave-%{octpkg}
Version:        0.6
Release:        20%{?dist}
Summary:        Mesh/volume registration toolbox
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://iso2mesh.sourceforge.net/cgi-bin/index.cgi?metch
Source0:        https://github.com/fangq/%{octpkg}/archive/%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave
Requires(post): octave
Requires(postun): octave

%description
Matlab/Octave-based mesh/volume registration toolbox. It provides
straightforward functions to register point clouds (or surfaces) to a
triangular/cubic surface mesh by calculating an optimal affine transformation
(in terms of matrix A for scaling and rotation, and b for translation). It
also allows one to project a point cloud onto the surface using surface norms
and guarantee the conformity of the points to the surface. At this point, metch
can only perform rigid-body registration in terms of a linear transformation. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{octpkg}-%{version}

# Matlab only
rm -vf metchgui*.m

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Matlab/Octave-based mesh/volume registration toolbox. It provides
 straightforward functions to register point clouds (or surfaces) to a
 triangular/cubic surface mesh by calculating an optimal affine transformation
 (in terms of matrix A for scaling and rotation, and b for translation). It
 also allows one to project a point cloud onto the surface using surface norms
 and guarantee the conformity of the points to the surface. At this point, metch
 can only perform rigid-body registration in terms of a linear transformation. 
Categories: Mesh
EOF

cat > INDEX << EOF
metch >> metch
metch
 regpt2surf
 proj2mesh
 affinemap
 dist2surf
 getplanefrom3pt
 linextriangle
 nodesurfnorm
 trisurfnorm
EOF

mkdir -p inst/
mv *.m inst/
chmod -x inst/*

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
%license COPYING
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
%autochangelog
