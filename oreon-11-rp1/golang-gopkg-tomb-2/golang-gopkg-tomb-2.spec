%global source0_hash 2379edcc225238167aa0d45cb28d3561c5193979b136a6cf3443a1fe3b85c78a
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/tomb.v2
%global forgeurl        https://github.com/go-tomb/tomb
%global commit          d5d1b5820637886def9eef33e03a27a9f166942c
%gometa
%global goaltipaths     gopkg.in/v2/tomb github.com/go-tomb/tomb
%global common_description %{expand:
The tomb package helps with clean goroutine termination in the Go language.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        2
Release:        1%{?dist}
Summary:        Clean goroutine termination in the Go language
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/tomb-%{commit}.tar.gz
Patch:          0001-Fix-incorrect-usage-of-t.Fatalf-in-test.-Closes-rhbz.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
