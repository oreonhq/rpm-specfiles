%global source0_hash 550839fc2ae5d865db475ba2c1714144f07fa0c052c72135b0e4a70287492e21

Name:           R-cachem
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Cache R Objects with Automatic Pruning

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Key-value stores with automatic pruning. Caches can limit either their total
size or the age of the oldest object (or both), automatically pruning objects
to maintain the constraints.

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
