%global source0_hash fc14f9f1d10d60a5888536df5a08e9e0fd7dad3412b9051a370edfe4cccf538d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gdamore/encoding
Version:                1.0.1
%gometa
%global common_description %{expand:
Package encoding provides a number of encodings that are missing from the
standard Go encoding package.
We hope that we can contribute these to the standard Go library someday. It
turns out that some of these are useful for dealing with I/O streams coming
from non-UTF friendly sources.
The UTF8 Encoder is also useful for situations where valid UTF-8 might be
carried in streams that contain non-valid UTF; in particular I use it for
helping me cope with terminals that embed escape sequences in otherwise valid
UTF-8.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Various character map encodings missing from golang.org/x/net/encoding
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/encoding-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/transform)
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
