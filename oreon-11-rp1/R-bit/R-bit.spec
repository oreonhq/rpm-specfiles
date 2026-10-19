%global source0_hash 48fe21c5d04c7b724d695eeb60074395c0c631a7fb234e2075de92471445de08
Name:           R-bit
Version:        %R_rpm_version 4.6.0
Release:        1%{?dist}
Summary:        Classes and Methods for Fast Memory-Efficient Boolean Selections
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=bit&version=%{version}#/bit_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provided are classes for boolean and skewed boolean vectors, fast boolean
methods, fast unique and non-unique integer sorting, fast set operations on
sorted and unsorted sets of integers, and foundations for ff (range index,
compression, chunked processing).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f bit/tests/ff_tests.R # unconditional suggest, should be fixed

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
