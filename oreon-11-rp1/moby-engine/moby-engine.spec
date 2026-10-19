%global source0_hash ac591291294da599e824f91d6a21a43bf93503b8ab608faa198899b3f973d7c5
%bcond check 0
%global goipath0        github.com/moby/moby
%global version0        29.3.0
%{lua:
    local version0 = rpm.expand("%{version0}"):gsub("~", "-")
    rpm.define("tag0 " .. "docker-v" .. version0)
    rpm.define("distprefix0 %{nil}")
    rpm.define("tag2 " .. "v" .. version0)
}
%global goipath2        github.com/docker/cli
%global version2        %{version0}
%gometa -L -a -f
%global engine_dir ../%{topdir0}
%global cli_dir ../%{topdir2}
%global common_description %{expand:
Docker is an open source project to build, ship and run any application as a
lightweight container.
Docker containers are both hardware-agnostic and platform-agnostic. This means
they can run anywhere, from your laptop to the largest EC2 compute instance and
everything in between — and they do not require you to use a particular
language, framework or packaging system. That makes them great building blocks
for deploying and scaling web apps, databases, and backend services without
depending on a particular stack or provider.
}
Name:           moby-engine
Version:        %{version0}
Release:        1%{?dist}
Summary:        The open-source application container engine
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND (Apache-2.0 OR GPL-2.0-or-later)
URL:            %{gourl}
Source0:        https://%{goipath0}/archive/docker-v%{version}/moby-docker-v%{version}.tar.gz
Source1:        %{archivename0}-vendor.tar.bz2
Source2:        %{gosource2}
Source3:        %{archivename2}-vendor.tar.bz2
Source100:      moby-engine-systemd-sysusers.conf
Source101:      macros.moby
Source102:      LICENSE.macros
Source200:      engine_go-vendor-tools.toml
Source201:      cli_go-vendor-tools.toml
Patch0:         0001-systemd-adjust-docker.service-for-downstream.patch
Requires:       containerd
Requires:       docker-cli = %{version}-%{release}
Requires:       moby-filesystem = %{version}-%{release}
Requires:       /usr/bin/tini-static
Requires:       container-selinux
Requires:       iptables
Requires:       libseccomp
Requires:       nftables
Requires:       pigz
Requires:       systemd
Requires:       tar
Requires:       xz
Provides:       docker = %{version}-%{release}
Conflicts:      docker-ce
Conflicts:      docker-ee
# oreon:deps
BuildRequires:  /usr/bin/go-md2man
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  make
BuildRequires:  nftables-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
# /oreon:deps
%description %{common_description}

%package nano
Summary:        GNU nano syntax highlighting files for Moby
BuildArch:      noarch
Requires:       nano
Supplements:    moby-engine
%description nano %{common_description}
This package installs %{summary}.

%package rootless-extras
Summary:        Rootless extras for Moby
BuildArch:      noarch
Requires:       moby-engine = %{version}-%{release}
Requires:       rootlesskit
Requires:       (slirp4netns or passt)
Suggests:       slirp4netns
Supplements:    moby-engine
%description rootless-extras %{common_description}

This package provides supplementary scripts that run dockerd as a non-root user.

# We name this package docker-cli, as that's the name of the upstream project.
# moby-engine is github.com/moby/moby.
%package -n docker-cli
Version:        %{forgeversion -z1}
Summary:        The Docker CLI
%global cli_license Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
License:        %{cli_license}
Requires:       moby-filesystem = %{version}-%{release}
Recommends:     moby-engine
Recommends:     docker-buildx
Conflicts:      moby-engine < %{version}-%{release}
Conflicts:      moby-engine > %{version}-%{release}
Conflicts:      docker-ce-cli
Conflicts:      docker-ee-cli
Conflicts:      podman-docker
Obsoletes:      moby-engine-fish-completion < 24.0.5-6
Obsoletes:      moby-engine-zsh-completion < 24.0.5-6
%description -n docker-cli %{common_description}

This package provides the Docker CLI.

%package -n moby-filesystem
Summary:        Filesystem package for the Moby/Docker stack
License:        LicenseRef-Not-Copyrightable
BuildArch:      noarch
%description -n moby-filesystem %{common_description}

This is the filesystem subpackage for the Moby/Docker stack.

%package -n moby-rpm-macros
Summary:        RPM Macros for the Moby/Docker stack
License:        MIT
BuildArch:      noarch
%description -n moby-rpm-macros %{common_description}

This package provides RPM macros for the Moby/Docker stack.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -a -A

# moby-engine
cd %{_builddir}/%{extractdir0}
# Unpack vendor archive
tar -xf %{S:1}
# Apply patches 0-1000
# Leave this here despite warnings so we can easily add and remove patches.
%autopatch -M999 -p1
cp -p %{S:100} %{S:101} %{S:102} .

# docker-cli
cd %{cli_dir}
# Unpack vendor archive
tar -xf %{S:3}
# Apply patches 1000+.
# Leave this here despite warnings so we can easily add and remove patches.
%autopatch -m1000 -p1
# See comment in go-vendor-tools.toml
rm -f man/go.mod

%build

export GO_LDFLAGS="" GO_BUILDTAGS="" CGO_ENABLED=1
%global gomodulesmode GO111MODULE=on
cd %{engine_dir}
BUILDFLAGS="%{gocompilerflags} -a -v" \
CGO_CFLAGS="%{build_cflags}" \
CGO_LDFLAGS="%{build_ldflags}" \
DOCKER_BUILDTAGS="rpm_crashback journald" \
DOCKER_GITCOMMIT=%{release} \
DOCKER_DEBUG=1 \
DOCKER_LDFLAGS=%{gobuild_ldflags_shescaped} \
LDFLAGS=%{gobuild_ldflags_shescaped} \
VERSION=%{version} \
GOPATH=%{gobuilddir} \
    bash -x ./hack/make.sh dynbinary
pushd man
GO_MD2MAN=go-md2man %make_build all
popd
cd %{cli_dir}
%make_build dynbinary \
    DISABLE_WARN_OUTSIDE_CONTAINER=1 \
    GITCOMMIT=%{release} \
    GO_BUILDTAGS="rpm_crashback" \
    GO_LDFLAGS=%{gobuild_ldflags_shescaped} \
    VERSION=%{version} \
dynbinary manpages
%install
mkdir -p %{buildroot}%{_libexecdir}/docker
mkdir %{buildroot}%{_libexecdir}/docker/cli-plugins
cd %{engine_dir}
%go_vendor_license_install -c %{S:200}
install -Dpm 0755 bundles/dynbinary*/* -t %{buildroot}%{_bindir}
ln -s %{_bindir}/tini-static %{buildroot}%{_libexecdir}/docker/docker-init
install -Dpm 0644 contrib/init/systemd/* -t %{buildroot}%{_unitdir}
install -Dpm 0644 moby-engine-systemd-sysusers.conf %{buildroot}%{_sysusersdir}/moby-engine.conf
install -Dpm 644 man/man8/*.8 -t %{buildroot}%{_mandir}/man8/
install -Dpm 0755 contrib/dockerd-rootless* -t %{buildroot}%{_bindir}
cd %{cli_dir}
%go_vendor_license_install -c %{S:201}
install -Dpm 0755 build/docker -t %{buildroot}%{_bindir}
install -Dpm 644 contrib/completion/bash/docker -t %{buildroot}%{bash_completions_dir}
install -Dpm 644 contrib/completion/zsh/_docker -t %{buildroot}%{zsh_completions_dir}
install -Dpm 644 contrib/completion/fish/docker.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 644 man/man1/*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 644 man/man5/*.5 -t %{buildroot}%{_mandir}/man5/
cd -
install -Dpm 0644 macros.moby -t %{buildroot}%{_rpmmacrodir}
%oreon_autofiles docker-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles moby-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles moby-rpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PATH="%{buildroot}%{_bindir}:${PATH}" TZ=utc
cd %{engine_dir}
%go_vendor_license_check -c %{S:200}
cd %{cli_dir}
%go_vendor_license_check -c %{S:201} %{cli_license}
%if %{with check}
cd %{engine_dir}
%global engine_ignores %{shrink:
   %dnl assertion failed
    -s "TestC8dSnapshotterWithUsernsRemap"
    -s "TestSCTP4Proxy"
    %dnl flaky test will fail on x86_64 - sometimes
    -s "TestSCTP6Proxy"
    %dnl Failed to enter netns: operation not permitted
    %dnl -s "TestSCTP4ProxyNoListener"
    %dnl -s "TestSCTP6ProxyNoListener"
    %dnl possibly flaky test failing on ppc64le
    %[ "%{_arch}" == "ppc64le" ? "-s TestSCTP6ProxyNoListener" : "" ]
    %dnl network_proxy_linux_test.go:73: protocol not supported; fails in COPR rawhide
    -s "TestIfaceAddrs"
    %dnl failed to mount resolved path: operation not permitted
    -s "TestJoinGoodSymlink"
    -s "TestJoinWithSymlinkReplace"
    -s "TestJoinCloseInvalidates"
    %dnl Test timeout
    -s "TestImageLoad"
    %dnl doesn't provide the requested platform
    -s "TestContentStoreForPull"
    -s "TestManifestStore"
    %dnl all with error is not nil: create tmp file
    %[ "%{_arch}" == "s390x" ? "-s TestCloseRunningCommand" : "" ]
    %dnl graphdriver tests require extra permissions
    -t daemon/graphdriver
    %dnl integration tests require a running docker daemon
    -t integration
    %dnl libnetwork tests cannot create netns in mock
    -t daemon/libnetwork
    %dnl integration-cli: we don't want to run integration tests or benchmarks
    -d integration-cli
}
%gocheck2 -F %{engine_ignores}
cd %{cli_dir}
%global cli_ignores %{shrink:
    -s "TestInitializeFromClientHangs"
    %dnl Needs network
    -s "TestRunBuildFromGitHubSpecialCase"
    %dnl Test is flaky
    -s "TestConnectAndWait"
    %dnl Test panics
    -s "TestRunAttachTermination"
    -s "TestRunPullTermination"
    -s "TestUpgradePromptTermination"
}
%gocheck2 -F -t e2e %{cli_ignores}
%endif
%post

%systemd_post docker.service docker.socket
%preun

%systemd_preun docker.service docker.socket
%postun

%systemd_postun_with_restart docker.service
%files -f %{oreon_filedir}/main.list
%files -n moby-engine-nano -f %{oreon_filedir}/moby-engine-nano.list
%files -n moby-engine-rootless-extras -f %{oreon_filedir}/moby-engine-rootless-extras.list
%files -n docker-cli -f %{oreon_filedir}/docker-cli.list
%files -n moby-filesystem -f %{oreon_filedir}/moby-filesystem.list
%files -n moby-rpm-macros -f %{oreon_filedir}/moby-rpm-macros.list

%changelog

%autochangelog
