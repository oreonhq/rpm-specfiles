%global source0_hash b57be793a96bec568bed5b619e62ec1f4efaf879adc0e57e486b891768148b98

Name:           R-sp
Version:        %R_rpm_version 2.2-0
Release:        %autorelease
Summary:        Classes and Methods for Spatial Data

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 2.2.0

%description
Classes and methods for spatial data; the classes document where the spatial
location information resides, for 2D or 3D data. Utility functions are
provided, e.g. for plotting data as maps, spatial selection, as well as methods
for retrieving coordinates, for subsetting, print, summary, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f sp/tests/agg.R* sp/tests/over2.R* # whole file requires rgeos

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
