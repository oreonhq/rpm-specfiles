%global source0_hash e20e7f534bc89b9258ad63d508aabed60f3bd504a7532a33e6ea230ca8fa4171

Name:           R-mvtnorm
Version:        %R_rpm_version 1.3-3
Release:        %autorelease
Summary:        Multivariate normal and T distribution R Package

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.3.3

%description
This R package computes multivariate normal and t probabilities, quantiles
and densities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f mvtnorm/tests/regtest-aperm.R # unconditional suggest, should be fixed

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
