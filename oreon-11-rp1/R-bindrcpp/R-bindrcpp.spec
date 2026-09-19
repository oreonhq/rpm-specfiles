%global source0_hash 662dae785aee715855415f4e743281ccbf0832e426084dc2f0ca9c9c908ec9fa

Name:           R-bindrcpp
Version:        %R_rpm_version 0.2.3
Release:        %autorelease
Summary:        An 'Rcpp' Interface to Active Bindings

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.2.3

%description
Provides an easy way to fill an environment with active bindings that call
a C++ function.

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
