%global source0_hash f85034ee98c8ca07fb3cd826142c1cd1e1e5747075a94c75a45783bbc4fe2deb

Name:           R-memoise
Version:        %R_rpm_version 2.0.1
Release:        %autorelease
Summary:        Memoisation of functions

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Cache the results of a function so that when you call it again with the same
arguments it returns the pre-computed value.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f memoise/tests/testthat/test-filesystem.R # unconditional suggest

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
