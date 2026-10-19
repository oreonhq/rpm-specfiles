%global source0_hash 8621d7b62f1792539965ad4ad67ea4ac563db17a5d77641d2e05ba26e58c7d61
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/circonus-labs/go-apiclient
Version:                0.7.24
%gometa
%global common_description %{expand:
Package Apiclient provides methods for interacting with the Circonus API. See
the full Circonus API Documentation at https://login.circonus.com/resources/api
for more information. }
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md examples
Name:           %{goname}
Release:        1%{?dist}
Summary:        Circonus api client
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-apiclient-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)
BuildRequires:  golang(github.com/pkg/errors)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
