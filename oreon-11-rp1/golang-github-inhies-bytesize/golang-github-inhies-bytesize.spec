%global source0_hash 7ef9789428346a76a6a312966dbdaac73d7babb2bba6d9c8db9f999babbb4982
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/inhies/go-bytesize
%global commit          4913239db9cf578e44f49d7b813734678ef94f51
%gometa
%global common_description %{expand:
Package bytesize provides functionality for measuring and displaying byte
sizes.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Functionality for measuring and displaying byte sizes
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-bytesize-%{commit}.tar.gz
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
