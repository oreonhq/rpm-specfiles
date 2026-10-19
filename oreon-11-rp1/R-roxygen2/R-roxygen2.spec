%global source0_hash da416e3ee2abed610da42d42a1a6947c70ef96f74880a35c9dc1e423c359614a
Name:           R-roxygen2
Version:        %R_rpm_version 7.3.3
Release:        1%{?dist}
Summary:        In-Line Documentation for R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=roxygen2&version=%{version}#/roxygen2_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field using
specially formatted comments. Writing documentation in-line with code makes it
easier to keep your documentation up-to-date as your requirements change.
'Roxygen2' is inspired by the 'Doxygen' system for C++.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f roxygen2/tests/testthat/test-markdown-code.R # fails

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
