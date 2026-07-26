%global source0_hash b22a746be625eec49736d2a0a18d96c45c14d97e30e42bc81a0740f3194e07fa

Name:           R-waldo
Version:        %R_rpm_version 0.6.2
Release:        %autorelease
Summary:        Find Differences Between R Objects

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Compare complex R objects and reveal the key differences.  Designed
particularly for use in testing packages where being able to quickly
isolate key differences makes understanding test failures much easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f waldo/tests/testthat/test-compare.R # unconditional suggest, should be fixed
rm -f waldo/tests/testthat/test-proxy.R # unconditional suggest, should be fixed

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
