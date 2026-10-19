%global source14_hash 9c4974e07c61547dae14af4ed1f358b7d04618ae194e54d6be72ee126f0d2f53
%global source13_hash e4fbbdacbeffb560715e6c74c128aee07a7053a1fec78dc904bcc0a88e2efd67
%global source11_hash fee364242fb4eea72e082ec674b6e6661856408a06719e1e88ce8673a22dc78a
%global source10_hash b37fc5aefd552c8d78acb896d115bfee1ed8aa4c9880b307b150f505f0a4d52e
%global source0_hash 5a3bf360a5240086324aa7f7005ab7eeee91095e2091078b3f9783eaf6e7288a
%undefine _debugsource_packages
%global package_version 1.5.3
%global gocryptfs_version 2.5.1
%global squashfuse_version 0.6.0
%global e2fsprogs_version 1.47.3
%global fuse_overlayfs_version 1.15
%global squashfs_tools_version 4.6.1
%global last_singularity_version 3.8.7-3
Summary:        Application and environment virtualization formerly known as Singularity
Name: apptainer
Version: 1.5.3
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD AND BSD-3-Clause-LBNL AND Apache-2.0
URL: https://apptainer.org
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if "%{?gocryptfs_version}" != ""
Source10: https://github.com/rfjakob/gocryptfs/archive/v%{gocryptfs_version}/gocryptfs-%{gocryptfs_version}.tar.gz
%endif
%if "%{?squashfuse_version}" != ""
Source11: https://github.com/vasi/squashfuse/archive/%{squashfuse_version}/squashfuse-%{squashfuse_version}.tar.gz
%endif
%if "%{?e2fsprogs_version}" != ""
Source12: e2fsprogs-%{e2fsprogs_version}.tar.gz
Patch121: e2fsprogs-246.patch
Patch122: e2fsprogs-250.patch
Patch123: e2fsprogs-251.patch
%endif
Source13: https://github.com/containers/fuse-overlayfs/archive/v%{fuse_overlayfs_version}/fuse-overlayfs-%{fuse_overlayfs_version}.tar.gz
%if "%{?squashfs_tools_version}" != ""
Source14: https://github.com/plougher/squashfs-tools/archive/%{squashfs_tools_version}/squashfs-tools-%{squashfs_tools_version}.tar.gz
%endif
Conflicts: singularity <= %{last_singularity_version}
Obsoletes: singularity-runtime < 3.0
Provides: sif-runtime
Conflicts: sif-runtime
Provides: bundled(gocryptfs) = %{gocryptfs_version}
Provides: bundled(squashfuse) = %{squashfuse_version}
Provides: bundled(e2fsprogs) = %{e2fsprogs_version}
Provides: bundled(fuse2fs) = %{e2fsprogs_version}
Provides: bundled(fuse-overlayfs) = %{fuse_overlayfs_version}
Provides: bundled(squashfs-tools) = %{squashfs_tools_version}
Provides: bundled(golang(github.com/AdaLogics/go_fuzz_headers)) = v0.0.0_20230811130428_ced1acdcaa24
Provides: bundled(golang(github.com/AdamKorcz/go_fuzz_headers)) = v0.0.0_20210319161527_f761c2329661
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20230124172434_306776ec8161
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.4.0
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.2
Provides: bundled(golang(github.com/Netflix/go_expect)) = v0.0.0_20220104043353_73e0943537d2
Provides: bundled(golang(github.com/ProtonMail/go_crypto)) = v1.1.6
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/adigunhammedolalekan/registry_auth)) = v0.0.0_20200730122110_8cde180a3a60
Provides: bundled(golang(github.com/alexflint/go_filemutex)) = v1.3.0
Provides: bundled(golang(github.com/apex/log)) = v1.9.0
Provides: bundled(golang(github.com/apptainer/container_key_client)) = v0.8.0
Provides: bundled(golang(github.com/apptainer/container_library_client)) = v1.4.10
Provides: bundled(golang(github.com/apptainer/sif/v2)) = v2.20.2
Provides: bundled(golang(github.com/asaskevich/govalidator)) = v0.0.0_20230301143203_a9d515a09cc2
Provides: bundled(golang(github.com/astromechza/etcpwdparse)) = v0.0.0_20170319193008_f0e5f0779716
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/buger/goterm)) = v1.0.4
Provides: bundled(golang(github.com/buger/jsonparser)) = v1.1.1
Provides: bundled(golang(github.com/cenkalti/backoff/v4)) = v4.3.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.3.0
Provides: bundled(golang(github.com/cilium/ebpf)) = v0.16.0
Provides: bundled(golang(github.com/cloudflare/circl)) = v1.3.7
Provides: bundled(golang(github.com/containerd/log)) = v0.1.0
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.15.1
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.2.3
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.5.1
Provides: bundled(golang(github.com/containers/image/v5)) = v5.33.1
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20230121012942_c1716e8a8d01
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.2.0
Provides: bundled(golang(github.com/containers/storage)) = v1.56.1
Provides: bundled(golang(github.com/coreos/go_iptables)) = v0.7.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.5.0
Provides: bundled(golang(github.com/cpuguy83/go_md2man/v2)) = v2.0.6
Provides: bundled(golang(github.com/creack/pty)) = v1.1.24
Provides: bundled(golang(github.com/cyberphone/json_canonicalization)) = v0.0.0_20231217050601_ba74d44ecf5f
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.5.1
Provides: bundled(golang(github.com/d2g/dhcp4)) = v0.0.0_20170904100407_a1d1b6c41b1c
Provides: bundled(golang(github.com/d2g/dhcp4client)) = v1.0.0
Provides: bundled(golang(github.com/distribution/reference)) = v0.6.0
Provides: bundled(golang(github.com/docker/cli)) = v27.5.1+incompatible
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v27.5.1+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.8.2
Provides: bundled(golang(github.com/docker/go_connections)) = v0.5.0
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/docker/libtrust)) = v0.0.0_20160708172513_aabc10ec26b7
Provides: bundled(golang(github.com/fatih/color)) = v1.18.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = v1.0.4
Provides: bundled(golang(github.com/garyburd/redigo)) = v0.0.0_20150301180006_535138d7bcd7
Provides: bundled(golang(github.com/go_jose/go_jose/v4)) = v4.0.4
Provides: bundled(golang(github.com/go_log/log)) = v0.2.0
Provides: bundled(golang(github.com/go_logr/logr)) = v1.4.2
Provides: bundled(golang(github.com/go_logr/stdr)) = v1.2.2
Provides: bundled(golang(github.com/go_openapi/analysis)) = v0.23.0
Provides: bundled(golang(github.com/go_openapi/errors)) = v0.22.0
Provides: bundled(golang(github.com/go_openapi/jsonpointer)) = v0.21.0
Provides: bundled(golang(github.com/go_openapi/jsonreference)) = v0.21.0
Provides: bundled(golang(github.com/go_openapi/loads)) = v0.22.0
Provides: bundled(golang(github.com/go_openapi/runtime)) = v0.28.0
Provides: bundled(golang(github.com/go_openapi/spec)) = v0.21.0
Provides: bundled(golang(github.com/go_openapi/strfmt)) = v0.23.0
Provides: bundled(golang(github.com/go_openapi/swag)) = v0.23.0
Provides: bundled(golang(github.com/go_openapi/validate)) = v0.24.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.4
Provides: bundled(golang(github.com/google/go_cmp)) = v0.6.0
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.20.2
Provides: bundled(golang(github.com/google/uuid)) = v1.6.0
Provides: bundled(golang(github.com/gorilla/handlers)) = v1.5.1
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.1
Provides: bundled(golang(github.com/gosimple/slug)) = v1.15.0
Provides: bundled(golang(github.com/gosimple/unidecode)) = v1.0.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.1.0
Provides: bundled(golang(github.com/josharian/intern)) = v1.0.0
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.17.11
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.6
Provides: bundled(golang(github.com/letsencrypt/boulder)) = v0.0.0_20240620165639_de9c06129bec
Provides: bundled(golang(github.com/mailru/easyjson)) = v0.7.7
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.13
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.20
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.16
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/mattn/go_sqlite3)) = v1.14.24
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.1
Provides: bundled(golang(github.com/mitchellh/go_homedir)) = v1.1.0
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = v1.5.0
Provides: bundled(golang(github.com/moby/docker_image_spec)) = v1.3.1
Provides: bundled(golang(github.com/moby/patternmatcher)) = v0.5.0
Provides: bundled(golang(github.com/moby/sys/capability)) = v0.3.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.7.2
Provides: bundled(golang(github.com/moby/sys/sequential)) = v0.6.0
Provides: bundled(golang(github.com/moby/sys/user)) = v0.3.0
Provides: bundled(golang(github.com/moby/sys/userns)) = v0.1.0
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/muesli/cancelreader)) = v0.2.2
Provides: bundled(golang(github.com/munnerz/goautoneg)) = v0.0.0_20191010083416_a7dc8b61c822
Provides: bundled(golang(github.com/networkplumbing/go_nft)) = v0.4.0
Provides: bundled(golang(github.com/oklog/ulid)) = v1.3.1
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.1
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.2.8
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.2.1
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20221107090550_2e043c6bd626
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.13.1
Provides: bundled(golang(github.com/opencontainers/umoci)) = v0.4.7
Provides: bundled(golang(github.com/pelletier/go_toml/v2)) = v2.2.3
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.3
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.20.2
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.6.1
Provides: bundled(golang(github.com/prometheus/common)) = v0.57.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.15.1
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.4.7
Provides: bundled(golang(github.com/rootless_containers/proto)) = v0.1.0
Provides: bundled(golang(github.com/russross/blackfriday/v2)) = v2.1.0
Provides: bundled(golang(github.com/safchain/ethtool)) = v0.4.0
Provides: bundled(golang(github.com/samber/lo)) = v1.49.1
Provides: bundled(golang(github.com/seccomp/containers_golang)) = v0.6.0
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.10.0
Provides: bundled(golang(github.com/secure_systems_lab/go_securesystemslib)) = v0.9.0
Provides: bundled(golang(github.com/shopspring/decimal)) = v1.4.0
Provides: bundled(golang(github.com/sigstore/fulcio)) = v1.6.4
Provides: bundled(golang(github.com/sigstore/protobuf_specs)) = v0.4.0
Provides: bundled(golang(github.com/sigstore/rekor)) = v1.3.6
Provides: bundled(golang(github.com/sigstore/sigstore)) = v1.8.14
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.3
Provides: bundled(golang(github.com/spf13/cobra)) = v1.9.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.6
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20230803200340_78284954bff6
Provides: bundled(golang(github.com/sylabs/json_resp)) = v0.9.4
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/titanous/rocacheck)) = v0.0.0_20171023193734_afe73141d399
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.15
Provides: bundled(golang(github.com/vbatts/go_mtree)) = v0.5.0
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.6
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = v8.9.1
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.2.1_beta.2
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.4
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(go.mongodb.org/mongo_driver)) = v1.14.0
Provides: bundled(golang(go.mozilla.org/pkcs7)) = v0.0.0_20210826202110_33d05740a352
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = v0.53.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = v1.28.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = v1.28.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = v1.28.0
Provides: bundled(golang(golang.org/x/crypto)) = v0.33.0
Provides: bundled(golang(golang.org/x/exp)) = v0.0.0_20241009180824_f66d83c29e7c
Provides: bundled(golang(golang.org/x/net)) = v0.33.0
Provides: bundled(golang(golang.org/x/sync)) = v0.11.0
Provides: bundled(golang(golang.org/x/sys)) = v0.30.0
Provides: bundled(golang(golang.org/x/term)) = v0.29.0
Provides: bundled(golang(golang.org/x/text)) = v0.22.0
Provides: bundled(golang(google.golang.org/genproto/googleapis/api)) = v0.0.0_20240814211410_ddb44dafa142
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = v0.0.0_20240903143218_8af14fe29dc1
Provides: bundled(golang(google.golang.org/grpc)) = v1.67.0
Provides: bundled(golang(google.golang.org/protobuf)) = v1.36.4
Provides: bundled(golang(gopkg.in/yaml.v2)) = v2.4.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = v3.0.1
Provides: bundled(golang(gotest.tools/v3)) = v3.5.2
Provides: bundled(golang(mvdan.cc/sh/v3)) = v3.10.0
%if "%{_target_vendor}" == "suse"
%if 0%{?suse_version} > 1600
%endif
%else
%endif
%if ("%{?squashfuse_version}" != "") || ("%{e2fsprogs_version}" != "") || ("%{fuse_overlayfs_version}" != "") || ("%{?squashfs_tools_version}" != "")
%endif
%if "%{_target_vendor}" == "suse"
Recommends: fakeroot
%else
Requires: fakeroot
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cryptsetup
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  golang
BuildRequires:  libseccomp-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  shadow-utils-subid-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Apptainer provides functionality to make portable
containers that can be used across host environments.

%package suid
Summary: Setuid component of Apptainer
Requires: %{name} = %{version}-%{release}
Obsoletes: singularity <= %{last_singularity_version}
Provides: alternative-for(singularity)
%description suid
Provides the optional setuid-root portion of Apptainer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{name}-%{package_version}
# don't need to setup dependent source packages and patches because
# that is done by the compile-dependencies script

%build

%if "%{?SOURCE1}" != ""
GOVERSION="$(echo %SOURCE1|sed 's,.*/,,;s/go//;s/\.src.*//')"
if ! ./mlocal/scripts/check-min-go-version go $GOVERSION; then
	pushd ..
	tar -xf %SOURCE1
	cd go/src
	./make.bash
	cd ../..
	export PATH=$PWD/go/bin:$PATH
	popd
fi
%endif
export GODEBUG=fips140=on
./scripts/compile-dependencies $(dirname %{SOURCE10})
./mconfig %{?mconfig_opts} -V %{version}-%{release} --with-suid \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_sharedstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir}
%make_build -C builddir V= old_config=
%install
%if "%{?SOURCE1}" != ""
export PATH=$PWD/go/bin:$PATH
%endif
%make_install -C builddir V=
%if "%{?gocryptfs_version}" != ""
install -m 755 gocryptfs-%{gocryptfs_version}/gocryptfs %{buildroot}%{_libexecdir}/%{name}/bin/gocryptfs
%endif
%if "%{?squashfuse_version}" != ""
install -m 755 squashfuse-%{squashfuse_version}/squashfuse_ll %{buildroot}%{_libexecdir}/%{name}/bin/squashfuse_ll
%endif
%if "%{?e2fsprogs_version}" != ""
install -m 755 e2fsprogs-%{e2fsprogs_version}/fuse2fs %{buildroot}%{_libexecdir}/%{name}/bin/fuse2fs
%endif
%if "%{?fuse_overlayfs_version}" != ""
install -m 755 fuse-overlayfs-%{fuse_overlayfs_version}/fuse-overlayfs %{buildroot}%{_libexecdir}/%{name}/bin/fuse-overlayfs
%endif
%if "%{?squashfs_tools_version}" != ""
install -m 755 squashfs-tools-%{squashfs_tools_version}/squashfs-tools/mksquashfs %{buildroot}%{_libexecdir}/%{name}/bin/mksquashfs
install -m 755 squashfs-tools-%{squashfs_tools_version}/squashfs-tools/unsquashfs %{buildroot}%{_libexecdir}/%{name}/bin/unsquashfs
%oreon_autofiles apptainer-suid usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

if [ "$1" -eq 1 ] && [ -d %{_sysconfdir}/singularity ]; then
	touch %{_sysconfdir}/%{name}/.singularityupgrade
fi
%posttrans

rmdir %{_sysconfdir}/singularity/* %{_sysconfdir}/singularity 2>/dev/null || true
if [ -f %{_sysconfdir}/%{name}/.singularityupgrade ]; then
	pushd %{_sysconfdir}/%{name} >/dev/null
	rm .singularityupgrade
	find %{_sysconfdir}/singularity ! -type d 2>/dev/null|while read F; do
		B="$(echo $F|sed 's,%{_sysconfdir}/singularity/,,;s/\.rpmsave//')"
		if [ "$B" == singularity.conf ]; then
			echo "info: renaming $PWD/%{name}.conf to $PWD/%{name}.conf.rpmorig" >&2
			mv %{name}.conf %{name}.conf.rpmorig
			echo "info: converting configuration from $F into $PWD/%{name}.conf" >&2
			%{_bindir}/%{name} confgen $F %{name}.conf
		elif [ "$B" == remote.yaml ]; then
			echo "info: renaming $PWD/$B to $PWD/$B.rpmorig" >&2
			mv $B $B.rpmorig
			echo "info: merging $F into $PWD/$B" >&2
			(
			sed -n '1p' $F
			sed -n '2,$p' $B.rpmorig
			sed -n '3,$p' $F
			) >$B
		else
			if [ -f "$B" ]; then
				echo "info: renaming $PWD/$B to $PWD/$B.rpmorig" >&2
				mv $B $B.rpmorig
			fi
			echo "info: copying $F into $PWD/$B" >&2
			cp $F $B
		fi
	done
	popd >/dev/null
fi
%{!?_licensedir:%global license %doc}
%files -f %{oreon_filedir}/main.list
%files -n apptainer-suid -f %{oreon_filedir}/apptainer-suid.list

%changelog

%autochangelog
