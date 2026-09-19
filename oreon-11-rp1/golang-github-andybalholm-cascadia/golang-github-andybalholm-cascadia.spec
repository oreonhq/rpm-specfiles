%global source0_hash 5f2cee3689470b1adc7af495402ccf7e047c7216d865b4b2bf55e910638e31e2

# https://github.com/andybalholm/cascadia
%global goipath         github.com/andybalholm/cascadia
Version:                1.2.0
%global debug_package %{nil}

%gometa

%global common_description %{expand:
The Cascadia package implements CSS selectors for use with the parse trees
produced by the html package.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        CSS selector library in Go

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
%autochangelog
