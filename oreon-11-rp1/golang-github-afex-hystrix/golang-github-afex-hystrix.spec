%global source0_hash 45d6aa4f0571c1720748998a1cdeca357b7de895c4f39b10de4db8645aa19b76
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/afex/hystrix-go
%global commit          fa1af6a1f4f56e0e50d427fe901cd604d8c6fb8a
%gometa
%global common_description %{expand:
Hystrix is a latency and fault tolerance library designed to isolate points of
access to remote systems, services and 3rd party libraries, stop cascading
failure and enable resilience in complex distributed systems where failure is
inevitable.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Netflix's hystrix latency and fault tolerance library, for go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/hystrix-go-%{commit}.tar.gz
Patch0:         0001-Make-compatible-with-statsd-5.0.0.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/DataDog/datadog-go/statsd)
BuildRequires:  golang(github.com/cactus/go-statsd-client/statsd)
BuildRequires:  golang(github.com/rcrowley/go-metrics)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
