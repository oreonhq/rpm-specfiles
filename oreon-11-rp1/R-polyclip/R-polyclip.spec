%global source0_hash f58eaac3a5b2f6711c0c5f12fff91cf80a245ae45878f7217880ab062b5550d3
Name:           R-polyclip
Version:        %R_rpm_version 1.10-7
Release:        1%{?dist}
Summary:        Polygon Clipping
License:        BSL-1.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=polyclip&version=1.10-7#/polyclip_1.10-7.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  polyclipping-devel
# /oreon:deps
%description
R port of Angus Johnson's open source library Clipper. Performs polygon
clipping operations (intersection, union, set minus, set difference) for
polygonal regions of arbitrary complexity, including holes. Computes
offset polygons (spatial buffer zones, morphological dilations, Minkowski
dilations) for polygonal regions and polygonal lines. Computes Minkowski
Sum of general polygons. There is a function for removing
self-intersections from polygon data.

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
