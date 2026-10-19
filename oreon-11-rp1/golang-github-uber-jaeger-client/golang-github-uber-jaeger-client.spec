%global source0_hash 011db6e73f8dc8f0092c15b3eaca02589ac6b6318223409e877746e55d3b5dd0
%ifnarch %{ix86} %{arm} s390x
%bcond check 0
%endif
%global goipath         github.com/uber/jaeger-client-go
Version:                2.30.0
%gometa
%global goaltipaths     github.com/jaegertracing/jaeger-client-go
%global common_description %{expand:
Instrumentation library that implements an OpenTracing Tracer for Jaeger
(https://jaegertracing.io).}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md RELEASE.md CHANGELOG.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Jaeger Bindings for Go OpenTracing API
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jaeger-client-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/crossdock/crossdock-go)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/harness)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(github.com/uber/jaeger-lib/metrics)
BuildRequires:  golang(github.com/uber/jaeger-lib/metrics/metricstest)
BuildRequires:  golang(go.uber.org/atomic)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(go.uber.org/zap/zaptest/observer)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in crossdock; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
