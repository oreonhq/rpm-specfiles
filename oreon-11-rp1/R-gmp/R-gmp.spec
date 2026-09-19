%global source0_hash f5cdaf9afb4cd921924f16682a6d6097ff372c95b697f363704c367f9b13ce78

Name:           R-gmp
Version:        %R_rpm_version 0.7-5
Release:        %autorelease
Summary:        Multiple Precision Arithmetic

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  gmp-devel >= 4.2.3

%description
Multiple Precision Arithmetic (big integers and rationals, prime number
tests, matrix computation), "arithmetic without limitations" using the C
library GMP (GNU Multiple Precision Arithmetic).

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
