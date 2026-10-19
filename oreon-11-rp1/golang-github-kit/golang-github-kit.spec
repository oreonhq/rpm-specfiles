%global source0_hash 3d6850dd688d524a839300f374e7770c9f83459c90ee6073d194e1463c61ebde
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%bcond_without bootstrap
%global debug_package %{nil}
%global goipath         github.com/go-kit/kit
Version:                0.13.0
%gometa
%global goipaths0       github.com/go-kit/kit
%global goipathsex0     github.com/go-kit/kit/sd/etcd github.com/go-kit/kit/sd/etcdv3
%if %{without bootstrap}
%global goipaths1       github.com/go-kit/kit/sd/etcd github.com/go-kit/kit/sd/etcdv3
%endif
%global common_description %{expand:
Go kit is a programming toolkit for building microservices (or elegant
monoliths) in Go. We solve common problems in distributed systems and
application architecture so you can focus on delivering business value.}
%global golicenses      LICENSE log/term/LICENSE
%global godocs          examples CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Standard library for microservices
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/kit-%{version}.tar.gz
%if %{without bootstrap}
%endif
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/VividCortex/gohistogram)
BuildRequires:  golang(github.com/afex/hystrix-go/hystrix)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/cloudwatch)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/cloudwatch/types)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/cloudwatch)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/cloudwatch/cloudwatchiface)
BuildRequires:  golang(github.com/casbin/casbin/v2)
BuildRequires:  golang(github.com/casbin/casbin/v2/model)
BuildRequires:  golang(github.com/casbin/casbin/v2/persist/file-adapter)
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/go-logfmt/logfmt)
BuildRequires:  golang(github.com/go-zookeeper/zk)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hudl/fargo)
BuildRequires:  golang(github.com/influxdata/influxdb1-client/v2)
BuildRequires:  golang(github.com/nats-io/nats.go)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/openzipkin/zipkin-go)
BuildRequires:  golang(github.com/openzipkin/zipkin-go/model)
BuildRequires:  golang(github.com/openzipkin/zipkin-go/propagation/b3)
BuildRequires:  golang(github.com/performancecopilot/speed)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/sony/gobreaker)
BuildRequires:  golang(github.com/streadway/amqp)
BuildRequires:  golang(github.com/streadway/handy/breaker)
BuildRequires:  golang(go.opencensus.io/plugin/ochttp)
BuildRequires:  golang(go.opencensus.io/plugin/ochttp/propagation/b3)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/propagation)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%if %{without bootstrap}
%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

%gocheck -t metrics
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
