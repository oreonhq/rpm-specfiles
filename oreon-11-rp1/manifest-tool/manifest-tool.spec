%global source0_hash c493f15cf3770aa2873fabe47baf2bbc33622f27b7b5c8dfcaa2cd91ee7369dd
%global with_debug 0
%global with_check 0
%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global provider        github
%global provider_tld    com
%global project         estesp
%global repo            manifest-tool
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit         a28af2b6bf3748859149bf161eb0630e677c3906
%global shortcommit    %(c=%{commit}; echo ${c:0:7})
Name:           manifest-tool
Version:        2.2.2
Release:        1%{?dist}
Summary:        A command line tool used for creating manifest list objects
License:        Apache-2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/%{name}-%{version}.tar.gz
Patch0:         go-mod.patch
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
Provides:       %{repo} = %{version}-%{release}
Provides:       bundled(golang(github.com/containerd))
Provides:       bundled(golang(github.com/docker/cli))
Provides:       bundled(golang(github.com/docker/distribution))
Provides:       bundled(golang(github.com/docker))
Provides:       bundled(golang(github.com/fatih/color))
Provides:       bundled(golang(github.com/opencontainers/go-digest))
Provides:       bundled(golang(github.com/opencontainers/image-spec))
Provides:       bundled(golang(github.com/pkg/errors))
Provides:       bundled(golang(github.com/sirupsen/logrus))
Provides:       bundled(golang(github.com/urfave/cli))
Provides:       bundled(golang(gopkg.in/yaml.v3))
Provides:       bundled(golang(oras.land/oras-go/v2))
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2/md2man))
Provides:       bundled(golang(github.com/docker/docker-credential-helpers))
Provides:       bundled(golang(github.com/golang/protobuf))
Provides:       bundled(golang(github.com/klauspost/compress))
Provides:       bundled(golang(github.com/kr/text))
Provides:       bundled(golang(github.com/mattn/go-colorable))
Provides:       bundled(golang(github.com/mattn/go-isatty))
Provides:       bundled(golang(github.com/moby/locker))
Provides:       bundled(golang(github.com/niemeyer/pretty))
Provides:       bundled(golang(github.com/russross/blackfriday/v2))
Provides:       bundled(golang(github.com/xrash/smetrics))
Provides:       bundled(golang(golang.org/x/net))
Provides:       bundled(golang(golang.org/x/sync))
Provides:       bundled(golang(golang.org/x/sys))
Provides:       bundled(golang(google.golang.org/genproto))
Provides:       bundled(golang(google.golang.org/grpc))
Provides:       bundled(golang(google.golang.org/protobuf))
Provides:       bundled(golang(gopkg.in/check.v1))
# oreon:deps
BuildRequires:  compiler(go-compiler)
BuildRequires:  git
BuildRequires:  make
# /oreon:deps
%description
This tool was mainly created for the purpose of viewing, creating, and
pushing the new manifests list object type in the Docker registry. Manifest
lists are defined in the v2.2 image specification and exist mainly for the
purpose of supporting multi-architecture and/or multi-platform images within
a Docker registry.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make binary
%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
