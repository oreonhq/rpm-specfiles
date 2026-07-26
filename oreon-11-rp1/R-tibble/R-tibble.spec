%global source0_hash fb309f8a1939021b237c7e85ff7ad6e8ff5acd57a6230d220a452094b492b28f

Name:           R-tibble
Version:        %R_rpm_version 3.3.1
Release:        %autorelease
Summary:        Simple Data Frames

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Provides a 'tbl_df' class (the 'tibble') with stricter checking and better
formatting than the traditional data frame.

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
