%global source0_hash 59a83c3ad5f803092ed5d72ea02cd11e4582c04ccac3b17495d8f96ebb32210b
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/twinj/uuid
Version:                1.0.0
%gometa
%global common_description %{expand:
This package provides RFC 4122 and DCE 1.1 compliant UUIDs. It will generate the
following:
 - Version 1: based on a Timestamp and MAC address as Node id
 - Version 2: based on DCE Security - Experimental
 - Version 3: based on MD5 hash
 - Version 4: based on cryptographically secure random numbers
 - Version 5: based on SHA-1 hash
Functions NewV1, NewV2, NewV3, NewV4, NewV5, New, NewHex and Parse() for
generating version 1, 2, 3, 4 and 5 Uuid's.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go RFC4122 UUID implementation
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/uuid-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/stretchr/testify.v1/assert)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
find . -name "*.go" -exec sed -i "s|github.com/myesui/uuid|github.com/twinj/uuid|" "{}" +;

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
