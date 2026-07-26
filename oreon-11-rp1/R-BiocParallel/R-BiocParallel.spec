%global source0_hash 3b2069e6b5aeb9c2e0586c110527dc2557240f4a447b67b8061931ee0b9a23c2

Name:           R-BiocParallel
Version:        %R_rpm_version 1.44.0
Release:        %autorelease
Summary:        Bioconductor facilities for parallel evaluation

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel

%description
This package provides modified versions and novel implementation of functions
for parallel evaluation, tailored to use with Bioconductor objects.

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
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
