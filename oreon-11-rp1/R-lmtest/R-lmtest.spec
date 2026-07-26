%global source0_hash 64400d4d6cc635316531042971f1783539686e9015c76f5741c07304fa14d997

Name:           R-lmtest
Version:        %R_rpm_version 0.9-40
Release:        %autorelease
Summary:        Testing Linear Regression Models for R

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A collection of tests, data sets and examples for diagnostic checking in
linear regression models in R.

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
