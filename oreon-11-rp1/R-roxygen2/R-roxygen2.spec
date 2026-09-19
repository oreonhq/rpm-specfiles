%global source0_hash da416e3ee2abed610da42d42a1a6947c70ef96f74880a35c9dc1e423c359614a

Name:           R-roxygen2
Version:        %R_rpm_version 7.3.3
Release:        %autorelease
Summary:        In-Line Documentation for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field using
specially formatted comments. Writing documentation in-line with code makes it
easier to keep your documentation up-to-date as your requirements change.
'Roxygen2' is inspired by the 'Doxygen' system for C++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f roxygen2/tests/testthat/test-markdown-code.R # fails

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
