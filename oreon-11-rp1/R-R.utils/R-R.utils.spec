%global source0_hash ab2043c34e129928ff85a037ce7a3f7791f245f49a55ee9a95bd7df0813bcf25

Name:           R-R.utils
Version:        %R_rpm_version 2.13.0
Release:        %autorelease
Summary:        Various Programming Utilities

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Utility functions useful when programming and developing R packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f R.utils/tests/touchFile.R # unconditional suggest, should be fixed

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
