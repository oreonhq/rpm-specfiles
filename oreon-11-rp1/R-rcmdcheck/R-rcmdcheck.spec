%global source0_hash bbd4ef7d514b8c2076196a7c4a6041d34623d55fbe73f2771758ce61fd32c9d0

Name:           R-rcmdcheck
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Run 'R CMD check' from 'R' and Capture Results

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Run 'R CMD check' from 'R' and capture the results of the individual checks.
Supports running checks in the background, timeouts, pretty printing and
comparing check results.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Fix test
sed -i 's/bad3, tempfile(), character()/bad3, tempfile(), "--no-build-vignettes"/' \
    rcmdcheck/tests/testthat/test-build.R

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
