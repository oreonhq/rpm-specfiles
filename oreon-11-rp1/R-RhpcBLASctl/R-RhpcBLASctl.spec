%global source0_hash 5c889d5b69e264060b9f1f0383c447f594855b8afc15b7d76d39e4d62b946615

Name:           R-RhpcBLASctl
Version:        %R_rpm_version 0.23-42
Release:        %autorelease
Summary:        Control the Number of Threads on BLAS

License:        AGPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Control the number of threads on BLAS (aka GotoBLAS, OpenBLAS, ACML, BLIS and
MKL). And possible to control the number of threads in OpenMP. Get a number of
logical cores and physical cores if feasible.

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
