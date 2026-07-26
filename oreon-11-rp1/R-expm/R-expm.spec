%global source0_hash 02c536f8f6af55b132210a50b1e9694a3549806bf97c49e0fe03595945aab254

Name:           R-expm
Version:        %R_rpm_version 1.0-0
Release:        %autorelease
Summary:        Computation of the matrix exponential and related quantities

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Efficient calculation of the exponential of a matrix. The package
contains an R interface and a C API that package authors can use.

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
