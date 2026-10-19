%global source0_hash 7857a4f0c066d2e43a1b7912458b028b6fa351eb1a1d41b022dd6ac347e96b4f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gofrs/uuid
Version:                4.0.0
%gometa
%global common_description %{expand:
Package uuid provides a pure Go implementation of Universally Unique Identifiers
(UUID) variant as defined in RFC-4122. This package supports both the creation
and parsing of UUIDs in different formats.
This package supports the following UUID versions:
 - Version 1, based on timestamp and MAC address (RFC-4122)
 - Version 2, based on timestamp, MAC address and POSIX UID/GID (DCE 1.1)
 - Version 3, based on MD5 hashing of a named value (RFC-4122)
 - Version 4, based on random numbers (RFC-4122)
 - Version 5, based on SHA-1 hashing of a named value (RFC-4122)
}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure Go implementation of Universally Unique Identifiers (UUID)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/uuid-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
