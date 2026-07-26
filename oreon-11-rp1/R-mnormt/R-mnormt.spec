%global source0_hash 95fca70378af0afd5a388982ba5528f5b27e02157eeb9940a0a9762d11511308

Name:           R-mnormt
Version:        %R_rpm_version 2.1.1
Release:        %autorelease
Summary:        The Multivariate Normal and t Distributions

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Functions are provided for computing the density and the distribution function
of d-dimensional normal and "t" random variables, possibly truncated (on one
side or two sides), and for generating random vectors sampled from these
distributions, except sampling from the truncated "t". Moments of arbitrary
order of a multivariate truncated normal are computed, and converted to
cumulants up to order 4. Probabilities are computed via non-Monte Carlo
methods; different routines are used in the case d=1, d=2, d=3, d>3, if d
denotes the dimensionality.

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
