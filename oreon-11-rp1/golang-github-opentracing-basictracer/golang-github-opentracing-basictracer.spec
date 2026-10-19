%global source0_hash 6f5aec89b4a248f4e018c4d8f7d7093301613b9e94f55522ef843cf6d1ea9ca7
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/opentracing/basictracer-go
Version:                1.1.0
%gometa
%global common_description %{expand:
The Go incarnation of the cross-platform "BasicTracer" reference impl for
OpenTracing.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go incarnation of the cross-platform "BasicTracer" reference impl for OpenTracing
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/basictracer-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/harness)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/trace)
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
