%global source0_hash 442c246b89ff3afd202980bb3c91c0e4ec1ee7aca38d8edfbc3cf9f079896284
Name:           R-webfakes
Version:        %R_rpm_version 1.4.0
Release:        1%{?dist}
Summary:        Fake Web Apps for HTTP Testing
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=webfakes&version=%{version}#/webfakes_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
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

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
