%global source0_hash 442c246b89ff3afd202980bb3c91c0e4ec1ee7aca38d8edfbc3cf9f079896284

Name:           R-webfakes
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Fake Web Apps for HTTP Testing

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Create a web app that makes it easier to test web clients without using the
internet. It includes a web app framework with path matching, parameters
and templates. Can parse various 'HTTP' request bodies. Can send 'JSON'
data or files from the disk. Includes a web app that implements the
<https://httpbin.org> web service.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f webfakes/tests/testthat/test-httpbin.R # network tests

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
