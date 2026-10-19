%global source0_hash 76d5a6cff8061d03b52bb219c26fa755d1a6ba529d8bb0b5fa4899dcedecbb3d
Name:           R-qtl
Version:        %R_rpm_version 1.74
Release:        1%{?dist}
Summary:        Tools for analyzing QTL experiments
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=qtl&version=%{version}#/qtl_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
R-qtl is an extensible, interactive environment for mapping
quantitative trait loci (QTLs) in experimental crosses. Our goal is to
make complex QTL mapping methods widely accessible and allow users to
focus on modeling rather than computing.

A key component of computational methods for QTL mapping is the hidden
Markov model (HMM) technology for dealing with missing genotype
data. We have implemented the main HMM algorithms, with allowance for
the presence of genotyping errors, for backcrosses, intercrosses, and
phase-known four-way crosses.

The current version of R-qtl includes facilities for estimating
genetic maps, identifying genotyping errors, and performing single-QTL
genome scans and two-QTL, two-dimensional genome scans, by interval
mapping (with the EM algorithm), Haley-Knott regression, and multiple
imputation. All of this may be done in the presence of covariates
(such as sex, age or treatment). One may also fit higher-order QTL
models by multiple imputation and Haley-Knott regression.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
