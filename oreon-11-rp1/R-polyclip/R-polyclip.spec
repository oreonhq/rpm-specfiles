%global source0_hash f58eaac3a5b2f6711c0c5f12fff91cf80a245ae45878f7217880ab062b5550d3

Name:           R-polyclip
Version:        %R_rpm_version 1.10-7
Release:        %autorelease
Summary:        Polygon Clipping

License:        BSL-1.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  polyclipping-devel

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

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
