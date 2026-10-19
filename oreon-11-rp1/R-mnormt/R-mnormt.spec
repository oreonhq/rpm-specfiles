%global source0_hash 95fca70378af0afd5a388982ba5528f5b27e02157eeb9940a0a9762d11511308
Name:           R-mnormt
Version:        %R_rpm_version 2.1.1
Release:        1%{?dist}
Summary:        The Multivariate Normal and t Distributions
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=mnormt&version=%{version}#/mnormt_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
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
%oreon_prep
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
