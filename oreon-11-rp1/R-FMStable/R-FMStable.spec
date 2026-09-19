%global source0_hash 2a391061dc2d2e89f6639aada07e839fdf950c0b20e27566219bb89befb4e93a

Name:           R-FMStable
Version:        %R_rpm_version 0.1-4
Release:        %autorelease
Summary:        Finite Moment Stable Distributions

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
This package implements some basic procedures for dealing with log
maximally skew stable distributions, which are also called finite moment
log stable distributions.

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
