%global source0_hash 123c91e7eaacd3514a368a31c30617d36a874def37f6cafdacc0c7d1409be373

Name:           R-rlang
Version:        %R_rpm_version 1.1.7
Release:        %autorelease
Summary:        Functions for Base Types and Core R and 'Tidyverse' Features

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          0001-Unbundle-libxxhash.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libxxhash)

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
rm -f rlang/tests/testthat/test-deparse.R # pillar stuff

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
