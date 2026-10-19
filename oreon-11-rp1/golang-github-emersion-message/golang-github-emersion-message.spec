%global source0_hash 2a7ec0dd4e8058ecd93c1a5a15c2160c88eed5a5bc656902b72fd09206f0623c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/emersion/go-message
Version:                0.15.0
%gometa
%global common_description %{expand:
A streaming Go library for the Internet Message Format and mail
messages.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Streaming Go library for the Internet Message Format and mail messages
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-message-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/emersion/go-textwrapper)
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(golang.org/x/text/encoding/htmlindex)
BuildRequires:  golang(golang.org/x/text/encoding/ianaindex)
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
