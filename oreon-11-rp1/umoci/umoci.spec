%global source0_hash 400a26c5f7ac06e40af907255e0e23407237d950e78e8d7c9043a1ad46da9ae5
%global goipath         github.com/opencontainers/umoci
Name:           umoci
Version:        0.6.0
Release:        1%{?dist}
Summary:        Open Container Image manipulation tool
License:        Apache-2.0 AND MIT AND BSD-2-Clause AND BSD-3-Clause AND ISC
URL:            https://umo.ci
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        umoci-%{version}-vendor.tar.gz
Source2:        create-vendor-tarball.sh
ExclusiveArch:  %{golang_arches_future}
Provides:       bundled(golang(github.com/AdaLogics/go-fuzz-headers)) = 43070de
Provides:       bundled(golang(github.com/docker/go-units)) = 0.5.0
Provides:       bundled(golang(github.com/moby/sys/user)) = 0.4.0
Provides:       bundled(golang(github.com/moby/sys/userns)) = 0.1.0
Provides:       bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0
Provides:       bundled(golang(github.com/opencontainers/image-spec)) = 1.0.2
Provides:       bundled(golang(github.com/opencontainers/runtime-spec)) = 1c3f411
Provides:       bundled(golang(github.com/rootless-containers/proto/go-proto)) = 4cd87eb
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
Provides:       bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.1.0
Provides:       bundled(golang(gopkg.in/check.v1)) = 8fa4692
Provides:       bundled(golang(github.com/cyphar/filepath-securejoin)) = 0.4.1
Provides:       bundled(golang(github.com/klauspost/compress)) = 1.11.3
Provides:       bundled(golang(github.com/klauspost/pgzip)) = 1.2.6
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
Provides:       bundled(golang(github.com/vbatts/go-mtree)) = 0.5.4
Provides:       bundled(golang(golang.org/x/crypto)) = 0.37.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.33.0
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.36.6
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
Provides:       bundled(golang(github.com/apex/log)) = 1.9.0
Provides:       bundled(golang(github.com/blang/semver/v4)) = 4.0.0
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = 2.0.4
Provides:       bundled(golang(github.com/fatih/color)) = 1.17.0
Provides:       bundled(golang(github.com/kr/text)) = 0.2.0
Provides:       bundled(golang(github.com/mattn/go-colorable)) = 0.1.13
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mohae/deepcopy)) = c48cc78
Provides:       bundled(golang(github.com/niemeyer/pretty)) = a10e7ca
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.10.0
Provides:       bundled(golang(github.com/urfave/cli)) = 1.22.12
# oreon:deps
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{expand:
umoci (pronounced /uːmoˈʨi/ or approximately "oo-mo-tchee") is a reference
implementation of the OCI image specification and provides users with the
ability to create, manipulate, and otherwise interact with container images. It
is designed to be as small and unopinonated as possible, so as to act as a
foundation for larger systems to be built on top of.}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

%build

export GOPATH=$PWD
export GO_LDFLAGS="-X %{goipath}.version=%{version}-%{release}"
%gobuild -o bin/umoci %{goipath}/cmd/umoci
for manpage in doc/man/*.md; do
    go-md2man -in ${manpage} > ${manpage/.md/}
done
%install
install -Dpm 0755 -t %{buildroot}%{_bindir} bin/umoci
install -d %{buildroot}%{_mandir}/man1
cp -p doc/man/*.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

export GOPATH=$PWD
cd src/%{goipath}
%gotest ./...
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
