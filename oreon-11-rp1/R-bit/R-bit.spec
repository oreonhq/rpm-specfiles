%global source0_hash 48fe21c5d04c7b724d695eeb60074395c0c631a7fb234e2075de92471445de08

Name:           R-bit
Version:        %R_rpm_version 4.6.0
Release:        %autorelease
Summary:        Classes and Methods for Fast Memory-Efficient Boolean Selections

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Provided are classes for boolean and skewed boolean vectors, fast boolean
methods, fast unique and non-unique integer sorting, fast set operations on
sorted and unsorted sets of integers, and foundations for ff (range index,
compression, chunked processing).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f bit/tests/ff_tests.R # unconditional suggest, should be fixed

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
