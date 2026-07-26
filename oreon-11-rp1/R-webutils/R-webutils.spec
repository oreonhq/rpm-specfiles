%global source0_hash a534a225bfd08dc6ad61480f177eda97fadc3fc8fd66f23ad6cb327dcf68661e

Name:           R-webutils
Version:        %R_rpm_version 1.2.2
Release:        %autorelease
Summary:        Utility Functions for Developing Web Applications

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Parses http request data in application/json, multipart/form-data, or
application/x-www-form-urlencoded format. Includes example of hosting and
parsing html form data in R using either 'httpuv' or 'Rhttpd'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f webutils/tests/testthat/test-echo.R # unconditional suggest, should be fixed

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
