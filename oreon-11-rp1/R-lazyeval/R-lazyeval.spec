%global source0_hash d6904112a21056222cfcd5eb8175a78aa063afe648a562d9c42c6b960a8820d4

Name:           R-lazyeval
Version:        %R_rpm_version 0.2.2
Release:        %autorelease
Summary:        Lazy (Non-Standard) Evaluation

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
An alternative approach to non-standard evaluation using formulas.
Provides a full implementation of LISP style 'quasiquotation', making it
easier to generate code with other code.

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
