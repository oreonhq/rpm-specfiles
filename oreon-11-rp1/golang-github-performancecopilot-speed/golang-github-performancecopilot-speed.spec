%global source0_hash 85efceddf3203d910403c91a807d3609accc98f952d5a87843709c6b63ae2c8f
%ifnarch %{ix86} %{arm} s390x
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/performancecopilot/speed
Version:                4.0.0
%gometa
%global common_description %{expand:
Package Speed implements a Golang client for the Performance Co-Pilot
instrumentation API.}
%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of the PCP instrumentation API
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/speed-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/codahale/hdrhistogram)
BuildRequires:  golang(github.com/edsrzf/mmap-go)
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
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
