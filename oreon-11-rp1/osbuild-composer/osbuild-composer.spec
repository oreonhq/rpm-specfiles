# Do not build with tests by default
# Pass --with tests to rpmbuild to override
%bcond_with tests

# When --with relax_requires is specified osbuild-composer-tests
# will require osbuild-composer only by name, excluding version/release
# This is used internally during nightly pipeline testing!
%bcond_with relax_requires

# The minimum required osbuild version
%global min_osbuild_version 171

%global goipath         github.com/osbuild/osbuild-composer

Version:        165

%gometa

%global common_description %{expand:
A service for building customized OS artifacts, such as VM images and OSTree
commits, that uses osbuild under the hood. Besides building images for local
usage, it can also upload images directly to cloud.

It is compatible with composer-cli and cockpit-composer clients.
}

Name:           osbuild-composer
Release:        1%{?dist}
Summary:        An image building service based on osbuild

# osbuild-composer doesn't have support for building i686 and armv7hl images
ExcludeArch:    i686 armv7hl

# Upstream license specification: Apache-2.0
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/osbuild/osbuild-composer/archive/v165/osbuild-composer-165.tar.gz
# oreon url source checksums begin
%global source0_sha256 cf09e18db18e93c60e5d5fa4827fb0de04d7515a8614929cb9f4232403f65b8a
%global source0_file osbuild-composer-165.tar.gz
# oreon url source checksums end


BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  systemd
BuildRequires:  krb5-devel
BuildRequires:  python3-docutils
BuildRequires:  make
# Build requirements of 'theproglottis/gpgme' package
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
# Build requirements of 'github.com/containers/storage' package
BuildRequires:  device-mapper-devel
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
# Build requirements of 'github.com/containers/storage' package
BuildRequires:  btrfs-progs-devel
# DO NOT REMOVE the BUNDLE_START and BUNDLE_END markers as they are used by 'tools/rpm_spec_add_provides_bundle.sh' to generate the Provides: bundled list
# BUNDLE_START
Provides: bundled(golang(cel.dev/expr)) = 0.24.0
Provides: bundled(golang(cloud.google.com/go)) = 0.123.0
Provides: bundled(golang(cloud.google.com/go/auth)) = 0.18.1
Provides: bundled(golang(cloud.google.com/go/auth/oauth2adapt)) = 0.2.8
Provides: bundled(golang(cloud.google.com/go/compute)) = 1.54.0
Provides: bundled(golang(cloud.google.com/go/compute/metadata)) = 0.9.0
Provides: bundled(golang(cloud.google.com/go/iam)) = 1.5.3
Provides: bundled(golang(cloud.google.com/go/monitoring)) = 1.24.3
Provides: bundled(golang(cloud.google.com/go/storage)) = 1.56.1
Provides: bundled(golang(dario.cat/mergo)) = 1.0.2
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/azcore)) = 1.19.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/azidentity)) = 1.11.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/internal)) = 1.11.2
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5)) = 5.7.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v7)) = 7.0.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources)) = 1.2.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/storage/armstorage)) = 1.8.1
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)) = 1.6.2
Provides: bundled(golang(github.com/AzureAD/microsoft-authentication-library-for-go)) = 1.4.2
Provides: bundled(golang(github.com/BurntSushi/toml)) = 1.6.0
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)) = 1.30.0
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric)) = 0.53.0
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)) = 0.53.0
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 0.6.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = 0.13.0
Provides: bundled(golang(github.com/VividCortex/ewma)) = 1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = 5a71ef0
Provides: bundled(golang(github.com/apapsch/go-jsonmerge/v2)) = 2.0.0
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2)) = 1.41.2
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream)) = 1.7.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/config)) = 1.32.10
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/credentials)) = 1.19.10
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)) = 1.18.18
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/feature/s3/manager)) = 1.19.4
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/configsources)) = 1.4.18
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)) = 2.7.18
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/ini)) = 1.8.4
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/v4a)) = 1.4.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/autoscaling)) = 1.64.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/ec2)) = 1.293.0
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)) = 1.13.5
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/checksum)) = 1.8.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)) = 1.13.18
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/s3shared)) = 1.19.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/s3)) = 1.87.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/signin)) = 1.0.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/sso)) = 1.30.11
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssooidc)) = 1.35.15
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/sts)) = 1.41.7
Provides: bundled(golang(github.com/aws/smithy-go)) = 1.24.2
Provides: bundled(golang(github.com/aymerick/douceur)) = 0.2.0
Provides: bundled(golang(github.com/beorn7/perks)) = 1.0.1
Provides: bundled(golang(github.com/cenkalti/backoff/v4)) = 4.3.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = 2.3.0
Provides: bundled(golang(github.com/cncf/xds/go)) = 0feb691
Provides: bundled(golang(github.com/containerd/cgroups/v3)) = 3.0.5
Provides: bundled(golang(github.com/containerd/errdefs)) = 1.0.0
Provides: bundled(golang(github.com/containerd/errdefs/pkg)) = 0.3.0
Provides: bundled(golang(github.com/containerd/stargz-snapshotter/estargz)) = 0.16.3
Provides: bundled(golang(github.com/containerd/typeurl/v2)) = 2.2.3
Provides: bundled(golang(github.com/containers/common)) = 0.64.1
Provides: bundled(golang(github.com/containers/image/v5)) = 5.36.1
Provides: bundled(golang(github.com/containers/libtrust)) = c1716e8
Provides: bundled(golang(github.com/containers/ocicrypt)) = 1.2.1
Provides: bundled(golang(github.com/containers/storage)) = 1.59.1
Provides: bundled(golang(github.com/coreos/go-semver)) = 0.3.1
Provides: bundled(golang(github.com/coreos/go-systemd/v22)) = 22.7.0
Provides: bundled(golang(github.com/cyberphone/json-canonicalization)) = 19d51d7
Provides: bundled(golang(github.com/cyphar/filepath-securejoin)) = 0.4.1
Provides: bundled(golang(github.com/davecgh/go-spew)) = d8f796a
Provides: bundled(golang(github.com/distribution/reference)) = 0.6.0
Provides: bundled(golang(github.com/docker/distribution)) = 2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = 28.3.2+incompatible
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = 0.9.3
Provides: bundled(golang(github.com/docker/go-connections)) = 0.5.0
Provides: bundled(golang(github.com/docker/go-units)) = 0.5.0
Provides: bundled(golang(github.com/dougm/pretty)) = add1dbc
Provides: bundled(golang(github.com/dprotaso/go-yit)) = 9ba8df1
Provides: bundled(golang(github.com/envoyproxy/go-control-plane/envoy)) = 1.35.0
Provides: bundled(golang(github.com/envoyproxy/protoc-gen-validate)) = 1.2.1
Provides: bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
Provides: bundled(golang(github.com/getkin/kin-openapi)) = 0.133.0
Provides: bundled(golang(github.com/getsentry/sentry-go)) = 0.43.0
Provides: bundled(golang(github.com/getsentry/sentry-go/echo)) = 0.43.0
Provides: bundled(golang(github.com/getsentry/sentry-go/logrus)) = 0.43.0
Provides: bundled(golang(github.com/go-jose/go-jose/v4)) = 4.1.3
Provides: bundled(golang(github.com/go-logr/logr)) = 1.4.3
Provides: bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides: bundled(golang(github.com/go-openapi/jsonpointer)) = 0.21.1
Provides: bundled(golang(github.com/go-openapi/swag)) = 0.23.1
Provides: bundled(golang(github.com/gobwas/glob)) = 0.2.3
Provides: bundled(golang(github.com/gogo/protobuf)) = 1.3.2
Provides: bundled(golang(github.com/golang-jwt/jwt/v4)) = 4.5.2
Provides: bundled(golang(github.com/golang-jwt/jwt/v5)) = 5.3.0
Provides: bundled(golang(github.com/golang/glog)) = 1.2.5
Provides: bundled(golang(github.com/golang/groupcache)) = 2c02b82
Provides: bundled(golang(github.com/golang/protobuf)) = 1.5.4
Provides: bundled(golang(github.com/google/go-cmp)) = 0.7.0
Provides: bundled(golang(github.com/google/go-containerregistry)) = 0.20.3
Provides: bundled(golang(github.com/google/go-intervals)) = 0.0.2
Provides: bundled(golang(github.com/google/s2a-go)) = 0.1.9
Provides: bundled(golang(github.com/google/uuid)) = 1.6.0
Provides: bundled(golang(github.com/googleapis/enterprise-certificate-proxy)) = 0.3.11
Provides: bundled(golang(github.com/googleapis/gax-go/v2)) = 2.17.0
Provides: bundled(golang(github.com/gorilla/css)) = 1.0.0
Provides: bundled(golang(github.com/gorilla/mux)) = 1.8.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = 1.1.0
Provides: bundled(golang(github.com/hashicorp/go-cleanhttp)) = 0.5.2
Provides: bundled(golang(github.com/hashicorp/go-multierror)) = 1.1.1
Provides: bundled(golang(github.com/hashicorp/go-retryablehttp)) = 0.7.8
Provides: bundled(golang(github.com/hashicorp/go-version)) = 1.7.0
Provides: bundled(golang(github.com/jackc/pgpassfile)) = 1.0.0
Provides: bundled(golang(github.com/jackc/pgservicefile)) = 5a60cdf
Provides: bundled(golang(github.com/jackc/pgtype)) = 1.14.4
Provides: bundled(golang(github.com/jackc/pgx/v5)) = 5.8.0
Provides: bundled(golang(github.com/jackc/puddle/v2)) = 2.2.2
Provides: bundled(golang(github.com/josharian/intern)) = 1.0.0
Provides: bundled(golang(github.com/json-iterator/go)) = 1.1.12
Provides: bundled(golang(github.com/julienschmidt/httprouter)) = 1.3.0
Provides: bundled(golang(github.com/klauspost/compress)) = 1.18.0
Provides: bundled(golang(github.com/klauspost/pgzip)) = 1.2.6
Provides: bundled(golang(github.com/kolo/xmlrpc)) = a4b6fa1
Provides: bundled(golang(github.com/kr/text)) = 0.2.0
Provides: bundled(golang(github.com/kylelemons/godebug)) = 1.1.0
Provides: bundled(golang(github.com/labstack/echo/v4)) = 4.15.1
Provides: bundled(golang(github.com/labstack/gommon)) = 0.4.2
Provides: bundled(golang(github.com/letsencrypt/boulder)) = de9c061
Provides: bundled(golang(github.com/mailru/easyjson)) = 0.9.0
Provides: bundled(golang(github.com/mattn/go-colorable)) = 0.1.14
Provides: bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides: bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides: bundled(golang(github.com/mattn/go-sqlite3)) = 1.14.28
Provides: bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.25
Provides: bundled(golang(github.com/miekg/pkcs11)) = 1.1.1
Provides: bundled(golang(github.com/mistifyio/go-zfs/v3)) = 3.0.1
Provides: bundled(golang(github.com/moby/docker-image-spec)) = 1.3.1
Provides: bundled(golang(github.com/moby/sys/capability)) = 0.4.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = 0.7.2
Provides: bundled(golang(github.com/moby/sys/user)) = 0.4.0
Provides: bundled(golang(github.com/modern-go/concurrent)) = bacd9c7
Provides: bundled(golang(github.com/modern-go/reflect2)) = 1.0.2
Provides: bundled(golang(github.com/mohae/deepcopy)) = c48cc78
Provides: bundled(golang(github.com/munnerz/goautoneg)) = a7dc8b6
Provides: bundled(golang(github.com/oapi-codegen/oapi-codegen/v2)) = 2.6.0
Provides: bundled(golang(github.com/oapi-codegen/runtime)) = 1.2.0
Provides: bundled(golang(github.com/oasdiff/yaml)) = f31be36
Provides: bundled(golang(github.com/oasdiff/yaml3)) = d218240
Provides: bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0
Provides: bundled(golang(github.com/opencontainers/image-spec)) = 1.1.1
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = 1.2.1
Provides: bundled(golang(github.com/opencontainers/selinux)) = 1.12.0
Provides: bundled(golang(github.com/openshift-online/ocm-sdk-go)) = 0.1.497
Provides: bundled(golang(github.com/oracle/oci-go-sdk/v54)) = 54.0.0
Provides: bundled(golang(github.com/osbuild/blueprint)) = 1.23.0
Provides: bundled(golang(github.com/osbuild/images)) = 0.245.0
Provides: bundled(golang(github.com/osbuild/osbuild-composer/pkg/splunk_logger)) = 0239db5
Provides: bundled(golang(github.com/perimeterx/marshmallow)) = 1.1.5
Provides: bundled(golang(github.com/pkg/browser)) = 5ac0b6a
Provides: bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides: bundled(golang(github.com/planetscale/vtprotobuf)) = 0393e58
Provides: bundled(golang(github.com/pmezard/go-difflib)) = 5d4384e
Provides: bundled(golang(github.com/proglottis/gpgme)) = 0.1.4
Provides: bundled(golang(github.com/prometheus/client_golang)) = 1.23.2
Provides: bundled(golang(github.com/prometheus/client_model)) = 0.6.2
Provides: bundled(golang(github.com/prometheus/common)) = 0.66.1
Provides: bundled(golang(github.com/prometheus/procfs)) = 0.16.1
Provides: bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides: bundled(golang(github.com/secure-systems-lab/go-securesystemslib)) = 0.9.0
Provides: bundled(golang(github.com/segmentio/ksuid)) = 1.0.4
Provides: bundled(golang(github.com/sigstore/fulcio)) = 1.6.6
Provides: bundled(golang(github.com/sigstore/protobuf-specs)) = 0.4.1
Provides: bundled(golang(github.com/sigstore/sigstore)) = 1.9.5
Provides: bundled(golang(github.com/sirupsen/logrus)) = 1.9.4
Provides: bundled(golang(github.com/skratchdot/open-golang)) = eef8423
Provides: bundled(golang(github.com/smallstep/pkcs7)) = 0.1.1
Provides: bundled(golang(github.com/sony/gobreaker)) = dd874f9
Provides: bundled(golang(github.com/speakeasy-api/jsonpath)) = 0.6.0
Provides: bundled(golang(github.com/speakeasy-api/openapi-overlay)) = 0.10.2
Provides: bundled(golang(github.com/spiffe/go-spiffe/v2)) = 2.6.0
Provides: bundled(golang(github.com/stefanberger/go-pkcs11uri)) = 7828495
Provides: bundled(golang(github.com/stretchr/testify)) = 1.11.1
Provides: bundled(golang(github.com/sylabs/sif/v2)) = 2.21.1
Provides: bundled(golang(github.com/tchap/go-patricia/v2)) = 2.3.3
Provides: bundled(golang(github.com/titanous/rocacheck)) = afe7314
Provides: bundled(golang(github.com/ubccr/kerby)) = 412be7b
Provides: bundled(golang(github.com/ulikunitz/xz)) = 0.5.12
Provides: bundled(golang(github.com/valyala/bytebufferpool)) = 1.0.0
Provides: bundled(golang(github.com/valyala/fasttemplate)) = 1.2.2
Provides: bundled(golang(github.com/vbatts/tar-split)) = 0.12.1
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = 8.10.2
Provides: bundled(golang(github.com/vmware-labs/yaml-jsonpath)) = 0.3.2
Provides: bundled(golang(github.com/vmware/govmomi)) = 0.52.0
Provides: bundled(golang(github.com/woodsbury/decimal128)) = 1.3.0
Provides: bundled(golang(go.opencensus.io)) = 0.24.0
Provides: bundled(golang(go.opentelemetry.io/auto/sdk)) = 1.2.1
Provides: bundled(golang(go.opentelemetry.io/contrib/detectors/gcp)) = 1.38.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)) = 0.61.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.61.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = 1.39.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = 1.39.0
Provides: bundled(golang(go.opentelemetry.io/otel/sdk)) = 1.39.0
Provides: bundled(golang(go.opentelemetry.io/otel/sdk/metric)) = 1.39.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = 1.39.0
Provides: bundled(golang(go.yaml.in/yaml/v2)) = 2.4.2
Provides: bundled(golang(go.yaml.in/yaml/v3)) = 3.0.3
Provides: bundled(golang(golang.org/x/crypto)) = 0.48.0
Provides: bundled(golang(golang.org/x/exp)) = 7d7fa50
Provides: bundled(golang(golang.org/x/mod)) = 0.32.0
Provides: bundled(golang(golang.org/x/net)) = 0.50.0
Provides: bundled(golang(golang.org/x/oauth2)) = 0.35.0
Provides: bundled(golang(golang.org/x/sync)) = 0.19.0
Provides: bundled(golang(golang.org/x/sys)) = 0.41.0
Provides: bundled(golang(golang.org/x/term)) = 0.40.0
Provides: bundled(golang(golang.org/x/text)) = 0.34.0
Provides: bundled(golang(golang.org/x/time)) = 0.14.0
Provides: bundled(golang(golang.org/x/tools)) = 0.41.0
Provides: bundled(golang(google.golang.org/api)) = 0.267.0
Provides: bundled(golang(google.golang.org/genproto)) = 8636f87
Provides: bundled(golang(google.golang.org/genproto/googleapis/api)) = 8636f87
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 546029d
Provides: bundled(golang(google.golang.org/grpc)) = 1.78.0
Provides: bundled(golang(google.golang.org/protobuf)) = 1.36.11
Provides: bundled(golang(gopkg.in/ini.v1)) = 1.67.0
Provides: bundled(golang(gopkg.in/yaml.v2)) = 2.4.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
# BUNDLE_END
%endif

Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-worker = %{version}-%{release}
Requires: systemd

Provides: weldr

%description
%{common_description}

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/osbuild-composer-165.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cf09e18db18e93c60e5d5fa4827fb0de04d7515a8614929cb9f4232403f65b8a" || { echo "oreon: Source0 SHA256 mismatch for osbuild-composer-165.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%if 0%{?rhel}
%forgeautosetup -p1
%else
%goprep -k
%endif

%build
export GOFLAGS="-buildmode=pie"
%if 0%{?rhel}
GO_BUILD_PATH=$PWD/_build
install -m 0755 -vd $(dirname $GO_BUILD_PATH/src/%{goipath})
ln -fs $PWD $GO_BUILD_PATH/src/%{goipath}
cd $GO_BUILD_PATH/src/%{goipath}
install -m 0755 -vd _bin
export PATH=$PWD/_bin${PATH:+:$PATH}
export GOPATH=$GO_BUILD_PATH:%{gopath}
export GOFLAGS+=" -mod=vendor"
%endif

# Fedora and RHEL versions disable Go modules by default, but we want to use them.
# Unconditionally undefine the macro which disables it to use the default behavior.
%undefine gomodulesmode

# btrfs-progs-devel is not available on RHEL
%if 0%{?rhel}
GOTAGS="exclude_graphdriver_btrfs"
%endif

# Set the commit hash so that composer can report what source version
# was used to build it. This has to be set explicitly when calling rpmbuild,
# this script will not attempt to automatically discover it.
%if %{?commit:1}0
export LDFLAGS="${LDFLAGS} -X 'github.com/osbuild/osbuild-composer/internal/common.GitRev=%{commit}'"
%endif
export LDFLAGS="${LDFLAGS} -X 'github.com/osbuild/osbuild-composer/internal/common.RpmVersion=%{name}-%{?epoch:%epoch:}%{version}-%{release}.%{_arch}'"

%gobuild ${GOTAGS:+-tags=$GOTAGS} -o _bin/osbuild-composer %{goipath}/cmd/osbuild-composer
%gobuild ${GOTAGS:+-tags=$GOTAGS} -o _bin/osbuild-worker %{goipath}/cmd/osbuild-worker
%gobuild ${GOTAGS:+-tags=$GOTAGS} -o _bin/osbuild-worker-executor %{goipath}/cmd/osbuild-worker-executor

make man

%if %{with tests} || 0%{?rhel}

# Build test binaries with `go test -c`, so that they can take advantage of
# golang's testing package. The golang rpm macros don't support building them
# directly. Thus, do it manually, taking care to also include a build id.

TEST_LDFLAGS="${LDFLAGS:-} -B 0x$(od -N 20 -An -tx1 -w100 /dev/urandom | tr -d ' ')"

%if 0%{?rhel}
GOTAGS="${GOTAGS:+$GOTAGS,}rhel%{rhel}"
%endif

go test -c -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-composer-cli-tests %{goipath}/cmd/osbuild-composer-cli-tests
go test -c -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-weldr-tests %{goipath}/internal/client/
go test -c -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-auth-tests %{goipath}/cmd/osbuild-auth-tests
go test -c -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-koji-tests %{goipath}/cmd/osbuild-koji-tests
go test -c -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-composer-dbjobqueue-tests %{goipath}/cmd/osbuild-composer-dbjobqueue-tests
go test -c -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-service-maintenance-tests %{goipath}/cmd/osbuild-service-maintenance
go build -tags="integration${GOTAGS:+,$GOTAGS}" -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-mock-openid-provider %{goipath}/cmd/osbuild-mock-openid-provider

%endif

%install
install -m 0755 -vd                                                %{buildroot}%{_libexecdir}/osbuild-composer
install -m 0755 -vp _bin/osbuild-composer                          %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp _bin/osbuild-worker                            %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp _bin/osbuild-worker-executor                   %{buildroot}%{_libexecdir}/osbuild-composer/

# Only include repositories for the distribution and release
install -m 0755 -vd                                                %{buildroot}%{_datadir}/osbuild-composer/repositories

# CentOS also defines rhel so we check for centos first
%if 0%{?centos}

# Latest CentOS supports building all CentOS versions
%if 0%{?centos} >= 10
install -m 0644 -vp vendor/github.com/osbuild/images/data/repositories/centos-*                          %{buildroot}%{_datadir}/osbuild-composer/repositories/

%else
# All other CentOS versions support building for the same version
install -m 0644 -vp vendor/github.com/osbuild/images/data/repositories/centos-%{centos}*                 %{buildroot}%{_datadir}/osbuild-composer/repositories/
# centos-stream-* are symlinks
cp -a repositories/centos-stream-%{centos}*          %{buildroot}%{_datadir}/osbuild-composer/repositories/
%endif

%else

%if 0%{?rhel}
# RHEL 10 supports building all RHEL versions
%if 0%{?rhel} >= 10
for REPO_FILE in $(ls vendor/github.com/osbuild/images/data/repositories/rhel-* ); do
    install -m 0644 -vp ${REPO_FILE}                               %{buildroot}%{_datadir}/osbuild-composer/repositories/$(basename ${REPO_FILE})

done

# temporary RHEL 9.7 and 9.8 overrides for new PQC key (for building RHEL 9 on 10)
for REPO_FILE in $(ls repositories/rhel-9*.json); do
    install -m 0644 -vp ${REPO_FILE}                               %{buildroot}%{_datadir}/osbuild-composer/repositories/$(basename ${REPO_FILE})
done

# RHEL-8 auxiliary key is signed using SHA-1, which is not enabled by default on RHEL-10 and later
for REPO_FILE in $(ls repositories/rhel-8*-no-aux-key.json); do
    install -m 0644 -vp ${REPO_FILE}                               %{buildroot}%{_datadir}/osbuild-composer/repositories/$(basename ${REPO_FILE} | sed 's/-no-aux-key//g')
done

%else
# All other RHEL versions support building for the same version
for REPO_FILE in $(ls vendor/github.com/osbuild/images/data/repositories/rhel-%{rhel}* ); do
    install -m 0644 -vp ${REPO_FILE}                               %{buildroot}%{_datadir}/osbuild-composer/repositories/$(basename ${REPO_FILE})
done

%if 0%{?rhel} == 9
# RHEL 9 supports building also for RHEL 8
for REPO_FILE in $(ls vendor/github.com/osbuild/images/data/repositories/rhel-8* ); do
    install -m 0644 -vp ${REPO_FILE}                               %{buildroot}%{_datadir}/osbuild-composer/repositories/$(basename ${REPO_FILE})
done

# temporary RHEL 9.7 and 9.8 overrides for new PQC key
for REPO_FILE in $(ls repositories/rhel-9*.json); do
    install -m 0644 -vp ${REPO_FILE}                               %{buildroot}%{_datadir}/osbuild-composer/repositories/$(basename ${REPO_FILE})
done

%endif

%endif
%endif
%endif

# Fedora can build for all included fedora releases
%if 0%{?fedora}
install -m 0644 -vp vendor/github.com/osbuild/images/data/repositories/fedora-*                          %{buildroot}%{_datadir}/osbuild-composer/repositories/
%endif

install -m 0755 -vd                                                %{buildroot}%{_unitdir}
install -m 0644 -vp distribution/*.{service,socket}                %{buildroot}%{_unitdir}/

install -m 0755 -vd                                                %{buildroot}%{_sysusersdir}
install -m 0644 -vp distribution/osbuild-composer.conf             %{buildroot}%{_sysusersdir}/

install -m 0755 -vd                                                %{buildroot}%{_localstatedir}/cache/osbuild-composer/dnf-cache

install -m 0755 -vd                                                %{buildroot}%{_mandir}/man7
install -m 0644 -vp docs/*.7                                       %{buildroot}%{_mandir}/man7/

%if %{with tests} || 0%{?rhel}

install -m 0755 -vd                                                %{buildroot}%{_libexecdir}/osbuild-composer-test
install -m 0755 -vp _bin/osbuild-composer-cli-tests                %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-weldr-tests                       %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-auth-tests                        %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-koji-tests                        %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-composer-dbjobqueue-tests         %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-service-maintenance-tests         %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp _bin/osbuild-mock-openid-provider              %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/define-compose-url.sh                    %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/provision.sh                             %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/gen-certs.sh                             %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/gen-ssh.sh                               %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/run-koji-container.sh                    %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/koji-compose.py                          %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/libvirt_test.sh                          %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/s3_test.sh                               %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/generic_s3_test.sh                       %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/generic_s3_https_test.sh                 %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/run-mock-auth-servers.sh                 %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vp tools/set-env-variables.sh                     %{buildroot}%{_libexecdir}/osbuild-composer-test/
install -m 0755 -vd                                                %{buildroot}%{_libexecdir}/tests/osbuild-composer
install -m 0755 -vp test/cases/*.sh                                %{buildroot}%{_libexecdir}/tests/osbuild-composer/

install -m 0755 -vd                                                %{buildroot}%{_libexecdir}/tests/osbuild-composer/api
install -m 0755 -vp test/cases/api/*.sh                            %{buildroot}%{_libexecdir}/tests/osbuild-composer/api/

install -m 0755 -vd                                                %{buildroot}%{_libexecdir}/tests/osbuild-composer/api/common
install -m 0755 -vp test/cases/api/common/*.sh                     %{buildroot}%{_libexecdir}/tests/osbuild-composer/api/common/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/ansible
install -m 0644 -vp test/data/ansible/*                            %{buildroot}%{_datadir}/tests/osbuild-composer/ansible/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/azure
install -m 0644 -vp test/data/azure/*                              %{buildroot}%{_datadir}/tests/osbuild-composer/azure/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/cloud-init
install -m 0644 -vp test/data/cloud-init/*                         %{buildroot}%{_datadir}/tests/osbuild-composer/cloud-init/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/composer
install -m 0644 -vp test/data/composer/*                           %{buildroot}%{_datadir}/tests/osbuild-composer/composer/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/worker
install -m 0644 -vp test/data/worker/*                             %{buildroot}%{_datadir}/tests/osbuild-composer/worker/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/repositories
install -m 0644 -vp test/data/repositories/*                       %{buildroot}%{_datadir}/tests/osbuild-composer/repositories/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/kerberos
install -m 0644 -vp test/data/kerberos/*                           %{buildroot}%{_datadir}/tests/osbuild-composer/kerberos/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/keyring
install -m 0644 -vp test/data/keyring/id_rsa.pub                   %{buildroot}%{_datadir}/tests/osbuild-composer/keyring/
install -m 0600 -vp test/data/keyring/id_rsa                       %{buildroot}%{_datadir}/tests/osbuild-composer/keyring/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/koji
install -m 0644 -vp test/data/koji/*                               %{buildroot}%{_datadir}/tests/osbuild-composer/koji/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/x509
install -m 0644 -vp test/data/x509/*                               %{buildroot}%{_datadir}/tests/osbuild-composer/x509/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/schemas
install -m 0644 -vp pkg/jobqueue/dbjobqueue/schemas/*              %{buildroot}%{_datadir}/tests/osbuild-composer/schemas/

install -m 0755 -vd                                                %{buildroot}%{_datadir}/tests/osbuild-composer/rhel-upgrade
install -m 0644 -vp test/data/rhel-upgrade/*                       %{buildroot}%{_datadir}/tests/osbuild-composer/rhel-upgrade/

%endif

%check
export GOFLAGS="-buildmode=pie"
%if 0%{?rhel}
export GOFLAGS+=" -tags=exclude_graphdriver_btrfs"
%endif

export GOPATH=$PWD/_build:%{gopath}
# cd inside GOPATH, otherwise go with GO111MODULE=off ignores vendor directory
cd $PWD/_build/src/%{goipath}

%post
%systemd_post osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-composer-prometheus.socket osbuild-remote-worker.socket

%preun
%systemd_preun osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-composer-prometheus.socket osbuild-remote-worker.socket

%postun
%systemd_postun_with_restart osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-composer-prometheus.socket osbuild-remote-worker.socket

%files
%license LICENSE
%doc README.md
%{_mandir}/man7/%{name}.7*
%{_unitdir}/osbuild-composer.service
%{_unitdir}/osbuild-composer.socket
%{_unitdir}/osbuild-composer-api.socket
%{_unitdir}/osbuild-composer-prometheus.socket
%{_unitdir}/osbuild-local-worker.socket
%{_unitdir}/osbuild-remote-worker.socket
%{_sysusersdir}/osbuild-composer.conf

%package core
Summary:    The core osbuild-composer binary
Requires:   osbuild-depsolve-dnf >= %{min_osbuild_version}
Provides:   %{name}-dnf-json = %{version}-%{release}
Obsoletes:  %{name}-dnf-json < %{version}-%{release}

%description core
The core osbuild-composer binary. This is suitable both for spawning in containers and by systemd.

%files core
%{_libexecdir}/osbuild-composer/osbuild-composer
%{_datadir}/osbuild-composer/

%package worker
Summary:    The worker for osbuild-composer
Requires:   systemd
Requires:   qemu-img
Requires:   osbuild >= %{min_osbuild_version}
Requires:   osbuild-ostree >= %{min_osbuild_version}
Requires:   osbuild-lvm2 >= %{min_osbuild_version}
Requires:   osbuild-luks2 >= %{min_osbuild_version}
Requires:   osbuild-depsolve-dnf >= %{min_osbuild_version}
Provides:   %{name}-dnf-json = %{version}-%{release}
Obsoletes:  %{name}-dnf-json < %{version}-%{release}

%description worker
The worker for osbuild-composer

%files worker
%{_libexecdir}/osbuild-composer/osbuild-worker
%{_libexecdir}/osbuild-composer/osbuild-worker-executor
%{_unitdir}/osbuild-worker@.service
%{_unitdir}/osbuild-remote-worker@.service

%post worker
%systemd_post osbuild-worker@.service osbuild-remote-worker@.service

%preun worker
# systemd_preun uses systemctl disable --now which doesn't work well with template services.
# See https://github.com/systemd/systemd/issues/15620
# The following lines mimicks its behaviour by running two commands.
# The scriptlet is supposed to run only when the package is being removed.
if [ $1 -eq 0 ] && [ -d /run/systemd/system ]; then
    # disable and stop all the worker services
    systemctl --no-reload disable osbuild-worker@.service osbuild-remote-worker@.service
    systemctl stop "osbuild-worker@*.service" "osbuild-remote-worker@*.service"
fi

%postun worker
# restart all the worker services
%systemd_postun_with_restart "osbuild-worker@*.service" "osbuild-remote-worker@*.service"

%if %{with tests} || 0%{?rhel}

%package tests
Summary:    Integration tests
%if %{with relax_requires}
Requires:   %{name}
%else
Requires:   %{name} = %{version}-%{release}
%endif
Requires:   composer-cli
Requires:   createrepo_c
Requires:   xorriso
Requires:   qemu-kvm-core
Requires:   systemd-container
Requires:   jq
Requires:   unzip
Requires:   container-selinux
Requires:   dnsmasq
Requires:   krb5-workstation
Requires:   podman
Requires:   python3
Requires:   sssd-krb5
Requires:   libvirt-client libvirt-daemon
Requires:   libvirt-daemon-config-network
Requires:   libvirt-daemon-config-nwfilter
Requires:   libvirt-daemon-driver-interface
Requires:   libvirt-daemon-driver-network
Requires:   libvirt-daemon-driver-nodedev
Requires:   libvirt-daemon-driver-nwfilter
Requires:   libvirt-daemon-driver-qemu
Requires:   libvirt-daemon-driver-secret
Requires:   libvirt-daemon-driver-storage
Requires:   libvirt-daemon-driver-storage-disk
Requires:   libvirt-daemon-kvm
Requires:   qemu-img
Requires:   qemu-kvm
Requires:   rpmdevtools
Requires:   virt-install
Requires:   expect
Requires:   python3-lxml
Requires:   httpd
Requires:   mod_ssl
Requires:   openssl
Requires:   firewalld
# podman-plugins has been deprecated since podman version 5.0.0,
# which is in Fedora 40+ and in c10s / el10
%if (0%{?rhel} && 0%{?rhel} < 10) || (0%{?fedora} && 0%{?fedora} < 40)
Requires:   podman-plugins
%endif
Requires:   dnf-plugins-core
Requires:   skopeo
Requires:   make
Requires:   python3-pip
%if 0%{?fedora}
# koji and ansible are not in RHEL repositories. Depending on them breaks RHEL
# gating (see OSCI-1541). The test script must enable EPEL and install those
# packages manually.
Requires:   koji
Requires:   ansible
%endif
%ifarch %{arm}
Requires:   edk2-aarch64
%endif

%description tests
Integration tests to be run on a pristine-dedicated system to test the osbuild-composer package.

%files tests
%{_libexecdir}/osbuild-composer-test/
%{_libexecdir}/tests/osbuild-composer/
%{_datadir}/tests/osbuild-composer/

%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 165-1
- Prepare for Oreon 11 (RP1)
