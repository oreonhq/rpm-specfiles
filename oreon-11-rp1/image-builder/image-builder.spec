# The minimum required osbuild version, note that this used to be 129
# but got bumped to 138 for librepo support which is not strictly
# required. So if this needs backport to places where there is no
# recent osbuild available we could simply make --use-librepo false
# and go back to 129.
%global min_osbuild_version 175

%global goipath         github.com/osbuild/image-builder-cli

Version:        53

%gometa

%global common_description %{expand:
A local binary for building customized OS artifacts such as VM images and
OSTree commits. Uses osbuild under the hood.
}

Name:           image-builder
Release:        1%{?dist}
Summary:        An image building executable using osbuild
ExcludeArch:    i686

# Upstream license specification: Apache-2.0
# Others generated with:
#   $ go_vendor_license -C <UNPACKED ARCHIVE> report expression
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-4.0 AND ISC AND MIT AND MPL-2.0 AND Unlicense

URL:            %{gourl}
Source0:        https://github.com/osbuild/image-builder-cli/releases/download/v%{version}/image-builder-cli-%{version}.tar.gz


BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
# Build requirements of 'theproglottis/gpgme' package
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
# Build requirements of 'github.com/containers/storage' package
BuildRequires:  device-mapper-devel
BuildRequires:  libxcrypt-devel
# Build requiremets of 'github.com/osbuild/images' package
BuildRequires:  libvirt-devel
%if 0%{?fedora}
# Build requirements of 'github.com/containers/storage' package
BuildRequires:  btrfs-progs-devel
# for _tmpfilesdir macro
BuildRequires:  systemd-rpm-macros
# DO NOT REMOVE the BUNDLE_START and BUNDLE_END markers as they are used by 'tools/rpm_spec_add_provides_bundle.sh' to generate the Provides: bundled list
# BUNDLE_START
Provides: bundled(golang(dario.cat/mergo)) = 1.0.2
Provides: bundled(golang(github.com/BurntSushi/toml)) = 1.6.0
Provides: bundled(golang(github.com/IBM/go-sdk-core/v5)) = 5.21.0
Provides: bundled(golang(github.com/IBM/ibm-cos-sdk-go)) = 1.12.3
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 0.6.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = 0.13.0
Provides: bundled(golang(github.com/VividCortex/ewma)) = 1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = 5a71ef0
Provides: bundled(golang(github.com/asaskevich/govalidator)) = a9d515a
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2)) = 1.38.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream)) = 1.7.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/config)) = 1.31.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/credentials)) = 1.18.10
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)) = 1.18.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/feature/s3/manager)) = 1.19.4
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/configsources)) = 1.4.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)) = 2.7.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/ini)) = 1.8.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/v4a)) = 1.4.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/ec2)) = 1.249.0
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)) = 1.13.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/checksum)) = 1.8.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)) = 1.13.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/s3shared)) = 1.19.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/s3)) = 1.87.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/sso)) = 1.29.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssooidc)) = 1.34.2
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/sts)) = 1.38.2
Provides: bundled(golang(github.com/aws/smithy-go)) = 1.23.0
Provides: bundled(golang(github.com/cheggaaa/pb/v3)) = 3.1.7
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
Provides: bundled(golang(github.com/cyberphone/json-canonicalization)) = 19d51d7
Provides: bundled(golang(github.com/cyphar/filepath-securejoin)) = 0.4.1
Provides: bundled(golang(github.com/davecgh/go-spew)) = d8f796a
Provides: bundled(golang(github.com/distribution/reference)) = 0.6.0
Provides: bundled(golang(github.com/docker/distribution)) = 2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = 28.3.3+incompatible
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = 0.9.3
Provides: bundled(golang(github.com/docker/go-connections)) = 0.5.0
Provides: bundled(golang(github.com/docker/go-units)) = 0.5.0
Provides: bundled(golang(github.com/fatih/color)) = 1.18.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
Provides: bundled(golang(github.com/gabriel-vasile/mimetype)) = 1.4.8
Provides: bundled(golang(github.com/go-jose/go-jose/v4)) = 4.0.5
Provides: bundled(golang(github.com/go-logr/logr)) = 1.4.3
Provides: bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides: bundled(golang(github.com/go-openapi/errors)) = 0.22.0
Provides: bundled(golang(github.com/go-openapi/strfmt)) = 0.23.0
Provides: bundled(golang(github.com/go-playground/locales)) = 0.14.1
Provides: bundled(golang(github.com/go-playground/universal-translator)) = 0.18.1
Provides: bundled(golang(github.com/go-playground/validator/v10)) = 10.26.0
Provides: bundled(golang(github.com/gobwas/glob)) = 0.2.3
Provides: bundled(golang(github.com/gogo/protobuf)) = 1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = 2c02b82
Provides: bundled(golang(github.com/golang/protobuf)) = 1.5.4
Provides: bundled(golang(github.com/google/go-containerregistry)) = 0.20.3
Provides: bundled(golang(github.com/google/go-intervals)) = 0.0.2
Provides: bundled(golang(github.com/google/uuid)) = 1.6.0
Provides: bundled(golang(github.com/gophercloud/gophercloud/v2)) = 2.8.0
Provides: bundled(golang(github.com/gorilla/mux)) = 1.8.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = 1.1.0
Provides: bundled(golang(github.com/hashicorp/go-cleanhttp)) = 0.5.2
Provides: bundled(golang(github.com/hashicorp/go-multierror)) = 1.1.1
Provides: bundled(golang(github.com/hashicorp/go-retryablehttp)) = 0.7.8
Provides: bundled(golang(github.com/hashicorp/go-version)) = 1.7.0
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides: bundled(golang(github.com/jmespath/go-jmespath)) = b0104c8
Provides: bundled(golang(github.com/json-iterator/go)) = 1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = 1.18.0
Provides: bundled(golang(github.com/klauspost/pgzip)) = 1.2.6
Provides: bundled(golang(github.com/leodido/go-urn)) = 1.4.0
Provides: bundled(golang(github.com/letsencrypt/boulder)) = de9c061
Provides: bundled(golang(github.com/mattn/go-colorable)) = 0.1.14
Provides: bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides: bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides: bundled(golang(github.com/mattn/go-sqlite3)) = 1.14.28
Provides: bundled(golang(github.com/miekg/pkcs11)) = 1.1.1
Provides: bundled(golang(github.com/mistifyio/go-zfs/v3)) = 3.0.1
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = 1.5.0
Provides: bundled(golang(github.com/moby/docker-image-spec)) = 1.3.1
Provides: bundled(golang(github.com/moby/sys/capability)) = 0.4.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = 0.7.2
Provides: bundled(golang(github.com/moby/sys/user)) = 0.4.0
Provides: bundled(golang(github.com/modern-go/concurrent)) = bacd9c7
Provides: bundled(golang(github.com/modern-go/reflect2)) = 1.0.2
Provides: bundled(golang(github.com/oklog/ulid)) = 1.3.1
Provides: bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0
Provides: bundled(golang(github.com/opencontainers/image-spec)) = 1.1.1
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = 1.2.1
Provides: bundled(golang(github.com/opencontainers/selinux)) = 1.12.0
Provides: bundled(golang(github.com/osbuild/blueprint)) = 1.25.0
Provides: bundled(golang(github.com/osbuild/images)) = 0.248.0
Provides: bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides: bundled(golang(github.com/pmezard/go-difflib)) = 5d4384e
Provides: bundled(golang(github.com/proglottis/gpgme)) = 0.1.4
Provides: bundled(golang(github.com/prometheus/client_golang)) = 1.23.0
Provides: bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides: bundled(golang(github.com/secure-systems-lab/go-securesystemslib)) = 0.9.0
Provides: bundled(golang(github.com/sigstore/fulcio)) = 1.6.6
Provides: bundled(golang(github.com/sigstore/protobuf-specs)) = 0.4.1
Provides: bundled(golang(github.com/sigstore/sigstore)) = 1.9.5
Provides: bundled(golang(github.com/sirupsen/logrus)) = 1.9.4
Provides: bundled(golang(github.com/smallstep/pkcs7)) = 0.1.1
Provides: bundled(golang(github.com/spf13/cobra)) = 1.10.2
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.10
Provides: bundled(golang(github.com/stefanberger/go-pkcs11uri)) = 7828495
Provides: bundled(golang(github.com/stretchr/testify)) = 1.11.1
Provides: bundled(golang(github.com/sylabs/sif/v2)) = 2.21.1
Provides: bundled(golang(github.com/tchap/go-patricia/v2)) = 2.3.3
Provides: bundled(golang(github.com/titanous/rocacheck)) = afe7314
Provides: bundled(golang(github.com/ulikunitz/xz)) = 0.5.12
Provides: bundled(golang(github.com/vbatts/tar-split)) = 0.12.1
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = 8.10.2
Provides: bundled(golang(go.mongodb.org/mongo-driver)) = 1.17.2
Provides: bundled(golang(go.opencensus.io)) = 0.24.0
Provides: bundled(golang(go.opentelemetry.io/auto/sdk)) = 1.1.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.61.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = 1.36.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = 1.36.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = 1.36.0
Provides: bundled(golang(go.yaml.in/yaml/v2)) = 2.4.2
Provides: bundled(golang(go.yaml.in/yaml/v3)) = 3.0.4
Provides: bundled(golang(golang.org/x/crypto)) = 0.41.0
Provides: bundled(golang(golang.org/x/exp)) = 7d7fa50
Provides: bundled(golang(golang.org/x/net)) = 0.43.0
Provides: bundled(golang(golang.org/x/sync)) = 0.16.0
Provides: bundled(golang(golang.org/x/sys)) = 0.41.0
Provides: bundled(golang(golang.org/x/term)) = 0.40.0
Provides: bundled(golang(golang.org/x/text)) = 0.28.0
Provides: bundled(golang(google.golang.org/genproto/googleapis/api)) = 3122310
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 3122310
Provides: bundled(golang(google.golang.org/grpc)) = 1.74.2
Provides: bundled(golang(google.golang.org/protobuf)) = 1.36.7
Provides: bundled(golang(gopkg.in/ini.v1)) = 1.67.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
Provides: bundled(golang(libvirt.org/go/libvirt)) = 1.11006.0
Provides: bundled(golang(sigs.k8s.io/yaml)) = 1.6.0
# BUNDLE_END
%endif

Requires:   osbuild >= %{min_osbuild_version}
Requires:   osbuild-ostree >= %{min_osbuild_version}
Requires:   osbuild-lvm2 >= %{min_osbuild_version}
Requires:   osbuild-luks2 >= %{min_osbuild_version}
Requires:   osbuild-depsolve-dnf >= %{min_osbuild_version}

%description
%{common_description}

%prep
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

%if 0%{?fedora}
# Fedora disables Go modules by default, but we want to use them.
# Undefine the macro which disables it to use the default behavior.
%undefine gomodulesmode
%endif

# btrfs-progs-devel is not available on RHEL
%if 0%{?rhel}
GOTAGS="exclude_graphdriver_btrfs"
%endif

export LDFLAGS="${LDFLAGS} -X 'main.version=%{version}'"
%gobuild ${GOTAGS:+-tags=$GOTAGS} -o %{gobuilddir}/bin/image-builder %{goipath}/cmd/image-builder

%install
install -m 0755 -vd                                 %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/image-builder %{buildroot}%{_bindir}/
# tmpfiles.d snippet
install -m 0755 -vd                                 %{buildroot}%{_tmpfilesdir}
install -m 0644 -vp data/tmpfiles.d/image-builder.conf %{buildroot}%{_tmpfilesdir}/image-builder.conf
%check
export GOFLAGS="-buildmode=pie"
%if 0%{?rhel}
export GOFLAGS+=" -mod=vendor -tags=exclude_graphdriver_btrfs"
export GOPATH=$PWD/_build:%{gopath}
# cd inside GOPATH, otherwise go with GO111MODULE=off ignores vendor directory
cd $PWD/_build/src/%{goipath}
%gotest ./...
%else
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/image-builder
%{_tmpfilesdir}/image-builder.conf
%ghost %attr(0755, root, root) %dir /var/cache/image-builder

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 53-1
- Prepare for Oreon 11 (RP1)
