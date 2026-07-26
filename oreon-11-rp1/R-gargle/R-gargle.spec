%global source0_hash e4a33f23c2ad917782fff1902e23f2a4c6c333c6389f6bfe8350577ddb6af6e6

Name:           R-gargle
Version:        %R_rpm_version 1.6.0
Release:        %autorelease
Summary:        Utilities for Working with Google APIs

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions and
classes for handling common credential types and for preparing, executing, and
processing HTTP requests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f gargle/tests/testthat/test-secret.R # unconditional suggest

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
