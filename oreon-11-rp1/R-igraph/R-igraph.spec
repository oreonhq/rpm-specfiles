%global source0_hash 14ab70a615b6cd9b75a67560ed3d36fc4d1ab635765530cd9cf80e39a0c14996
Name:           R-igraph
Version:        %R_rpm_version 2.2.1
Release:        1%{?dist}
Summary:        Network Analysis and Visualization
License:        GPL-2.0-or-later AND TCL
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=igraph&version=%{version}#/igraph_%{version}.tar.gz
Patch:          0002-Unbundle-uuid.patch
ExcludeArch:    %{ix86}
Provides:       bundled(igraph) = 0.10.17
Provides:       bundled(arpack)
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  arpack-devel
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
# /oreon:deps
%description
Routines for simple graphs and network analysis. It can handle large graphs
very well and provides functions for generating random and regular graphs,
graph visualization, centrality methods and much more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
