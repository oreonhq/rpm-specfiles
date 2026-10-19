%global source0_hash 6afc2b2035df98e4b5b6922c34f5b6d0b01be34ba4085870a76cb64e1aa0575c
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global provider github
%global provider_tld com
%global project containerd
%global repo stargz-snapshotter
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}
%global built_tag v0.14.3
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})
Name: %{repo}
Version: %{gen_version}
Release:        1%{?dist}
Summary:        Fast container image distribution plugin with lazy pulling
License: Apache-2.0 AND LicenseRef-Callaway-BSD AND ISC AND LicenseRef-Callaway-MIT AND MPL-2.0
URL: %{git0}
Source0:        %{built_tag}-vendor.tar.gz
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.1
Provides: bundled(golang(github.com/containerd/go_cni)) = v1.1.3
Provides: bundled(golang(github.com/containerd/stargz_snapshotter)) = v0.11.3
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.11.3
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/ipfs)) = v0.11.3
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/goccy/go_json)) = v0.9.5
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/ipfs/go_ipfs_http_client)) = v0.2.0
Provides: bundled(golang(github.com/ipfs/interface_go_ipfs_core)) = v0.5.2
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.2_0.20211117181255_693428a734f5
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20210326190908_1c3f411f0417
Provides: bundled(golang(github.com/pelletier/go_toml)) = v1.9.4
Provides: bundled(golang(github.com/rs/xid)) = v1.3.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/urfave/cli)) = v1.22.5
Provides: bundled(golang(k8s.io/cri_api)) = v0.24.0_alpha.3
# oreon:deps
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -Sgit -n %{name}-%{built_tag_strip}

%build

%set_build_flags
export CGO_CFLAGS=$CFLAGS
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
export LDFLAGS=''
%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd
mv cmd/vendor src
export GOPATH=$(pwd)/_build:$(pwd)
%gobuild -o out/%{project}-stargz-grpc %{import_path}/cmd/%{project}-stargz-grpc
%gobuild -o out/ctr-remote %{import_path}/cmd/ctr-remote
%gobuild -o out/stargz-store %{import_path}/cmd/stargz-store
%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make CMD_DESTDIR=%{buildroot}%{_prefix} install
sed -i 's/\/local//' script/config-cri-o/etc/systemd/system/stargz-store.service
install -D -m 644 script/config-cri-o/etc/systemd/system/stargz-store.service %{buildroot}%{_unitdir}/stargz-store.service
%{!?_licensedir:%global license %doc}
%oreon_autofiles main

%post

%systemd_post stargz-store.service
%preun

%systemd_preun stargz-store.service
%postun

%systemd_postun stargz-store.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
