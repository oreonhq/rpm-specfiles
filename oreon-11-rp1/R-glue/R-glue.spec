%global source0_hash c86f364ba899b8662f5da3e1a75f43ae081ab04e0d51171d052356e7ee4b72a0

Name:           R-glue
Version:        %R_rpm_version 1.8.0
Release:        %autorelease
Summary:        Interpreted String Literals

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
An implementation of interpreted string literals, inspired by Python's
Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
Triple-Quoted String Literals
<https://docs.julialang.org/en/v1.3/manual/strings/#Triple-Quoted-String-Literals-1>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f glue/tests/testthat/test-vctrs.R # unconditional suggest, should be fixed

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
