%global source0_hash 6d2a1dd2a5f6a5d74d9ecd74c4812cadca7a74b8da22ac2da0d993697638e58e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xdg/stringprep
Version:                1.0.0
%gometa
%global common_description %{expand:
This library provides an implementation of the stringprep algorithm (RFC-3454)
in Go, including all data tables.
A pre-built SASLprep (RFC-4013) profile is provided as well.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of rfc-3454 stringprep and rfc-4013 saslprep
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/stringprep-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/text/unicode/norm)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
