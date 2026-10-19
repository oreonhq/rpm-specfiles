%global source0_hash b65366c6b421d08af4349f2808f02d0ede027023937187d5a8d462e5485580f9
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%ifarch x86_64
%bcond check 0
%endif
%global goipath         k8s.io/kube-openapi
%global forgeurl        https://github.com/kubernetes/kube-openapi
%global commit          3c818078ee3de6569a8f02b6345ea3c4cc8b0998
%gometa
%global common_description %{expand:
Kubernetes OpenAPI spec generation & serving.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md code-of-conduct.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Kubernetes OpenAPI spec generation & serving
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/kube-openapi-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(bitbucket.org/ww/goautoneg)
BuildRequires:  golang(github.com/NYTimes/gziphandler)
BuildRequires:  golang(github.com/asaskevich/govalidator)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/emicklei/go-restful)
BuildRequires:  golang(github.com/go-openapi/jsonreference)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/googleapis/gnostic/openapiv2)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/ginkgo/config)
BuildRequires:  golang(github.com/onsi/ginkgo/types)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(k8s.io/gengo/args)
BuildRequires:  golang(k8s.io/gengo/generator)
BuildRequires:  golang(k8s.io/gengo/namer)
BuildRequires:  golang(k8s.io/gengo/parser)
BuildRequires:  golang(k8s.io/gengo/types)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/schema)
BuildRequires:  golang(sigs.k8s.io/yaml)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
sed -i "s|github.com/munnerz/goautoneg|bitbucket.org/ww/goautoneg|" $(find . -name "*.go")
# sed -i 's|github.com/googleapis/gnostic|github.com/googleapis/gnostic-0.4|' $(find . -iname "*.go" -type f)

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d pkg/aggregator -d pkg/handler
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
