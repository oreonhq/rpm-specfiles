%global source0_hash f026ec13aa4d0613720c483e2b6ec28251f4d4b7cc6624cab689ecfcac189a5b

Name:           R-S7
Version:        %R_rpm_version 0.2.1
Release:        %autorelease
Summary:        An Object Oriented System Meant to Become a Successor to S3 and S4

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
A new object oriented programming system designed to be a successor to S3
and S4. It includes formal class, generic, and method specification, and
a limited form of multiple dispatch. It has been designed and implemented
collaboratively by the R Consortium Object-Oriented Programming Working
Group, which includes representatives from R-Core, 'Bioconductor',
'Posit'/'tidyverse', and the wider R community.

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
