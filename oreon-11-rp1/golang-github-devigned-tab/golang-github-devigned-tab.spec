%global source0_hash 1bfa28afdd9623a5b6eff8861801b03de4ee396fdea1744272b861fd046dfd4f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/devigned/tab
Version:                0.1.3
%global tag             opencensus/v0.1.3
%global distprefix      %{nil}
%gometa
%global common_description %{expand:
OpenTracing and OpenCensus abstraction for tracing and logging.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        OpenTracing and OpenCensus abstraction for tracing and logging
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/tab-opencensus-v%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/propagation)
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
