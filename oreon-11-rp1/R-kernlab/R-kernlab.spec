%global source0_hash 70c0787d6d3762c89bb68218fbee19e861fcb5d4c05b787a9692055d95dd3061

Name:           R-kernlab
Version:        %R_rpm_version 0.9-33
Release:        %autorelease
Summary:        GNU R package for kernel-based machine learning lab

License:	    GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

ExcludeArch:	%{ix86} s390x
BuildRequires:  R-devel

%description
Kernel-based machine learning methods for classification,
regression, clustering, novelty detection, quantile regression
and dimensionality reduction. Among other methods 'kernlab'
includes Support Vector Machines, Spectral Clustering, 
Kernel PCA, Gaussian Processes and a QP solver.

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
