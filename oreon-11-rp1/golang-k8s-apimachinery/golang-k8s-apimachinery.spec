%global source0_hash 33db9241f6e5259cc01af8a6497b5aff71ade2599e1a71437dc8cc6d39569995
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         k8s.io/apimachinery
%global forgeurl        https://github.com/kubernetes/apimachinery
Version:                1.22.0
%global tag             kubernetes-1.22.0
%global distprefix      %{nil}
%gometa
%global common_description %{expand:
Scheme, typing, encoding, decoding, and conversion packages for Kubernetes and
Kubernetes-like API objects.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md code-of-conduct.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Scheme, typing, encoding, decoding, and conversion packages for Kubernetes
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}/apimachinery-%{tag}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/elazarl/goproxy)
BuildRequires:  golang(github.com/evanphx/json-patch)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/googleapis/gnostic/openapiv2)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/moby/spdystream)
BuildRequires:  golang(github.com/modern-go/reflect2)
BuildRequires:  golang(github.com/mxk/go-flowrate/flowrate)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(gopkg.in/inf.v0)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util/proto)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/fieldpath)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/typed)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/value)
BuildRequires:  golang(sigs.k8s.io/yaml)
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

%gocheck -d pkg/util/validation
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
