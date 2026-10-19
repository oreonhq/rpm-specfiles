%global source0_hash dc70adcf38b85fba3233ce1ffa025274c57c23f8f470693fbf7fe2ed164781f4
%global goipath         github.com/andybalholm/cascadia
Version:                1.3.5
%global debug_package %{nil}
%gometa
%global common_description %{expand:
The Cascadia package implements CSS selectors for use with the parse trees
produced by the html package.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        CSS selector library in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cascadia-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/net/html)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main

%check

%gocheck
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
