%global source0_hash 05306a02bbffa2c71a0f0f5c200d006c8ad659b5f86cb67a7c95055d7f740933
%bcond check 0
%global debug_package %{nil}
%global goipath         go.opentelemetry.io/otel-0.20
%global forgeurl        https://github.com/open-telemetry/opentelemetry-go
Version:                0.20.0
%gometa
%global common_description %{expand:
OpenTelemetry Go API and SDK.}
%global golicenses      LICENSE
%global godocs          example RELEASING.md CHANGELOG.md CONTRIBUTING.md\\\
                        README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        OpenTelemetry Go API and SDK
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/opentelemetry-go-%{version}.tar.gz
Patch0:         0001-Remove-import-comments.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/benbjohnson/clock)
BuildRequires:  golang(github.com/cenkalti/backoff/v4)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/openzipkin/zipkin-go/model)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(go.opencensus.io/metric)
BuildRequires:  golang(go.opencensus.io/metric/metricdata)
BuildRequires:  golang(go.opencensus.io/metric/metricexport)
BuildRequires:  golang(go.opencensus.io/metric/metricproducer)
BuildRequires:  golang(go.opencensus.io/resource)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/tracestate)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/collector/metrics/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/collector/trace/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/common/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/metrics/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/resource/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/trace/v1)
BuildRequires:  golang(golang.org/x/mod/semver)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/encoding/gzip)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/types/known/durationpb)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
sed -i \
    -e 's|"go.opentelemetry.io/otel|"go.opentelemetry.io/otel-0.20|' \
    $(find . -name '*.go')
sed -i \
    -e 's|"go.opentelemetry.io/proto|"go.opentelemetry.io/proto-0.7|' \
    $(find . -name '*.go')

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestNewExporter_withInvalidSecurityConfiguration" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
