%global source2_hash d4b2543626bee31d9438d4a31731aae712c072893c7aed8854f16c42fafc742b
%global source1_hash c19bf37a7366d64b9605dfee0b5dd0fce5c1ec1edbb34b53d4c87a9e536525a8
%global source0_hash 503756a080d66141fc3103952b6a5c0253c45da8475673c8d4ee5c948f4dade4
%global project containers
%global repo container-libs
%if %{defined copr_username}
%define copr_build 1
%endif
%if %{defined copr_build}
%define netavark_epoch 102
%else
%define netavark_epoch 2
%endif
Name: containers-common
%if %{defined copr_build}
Epoch: 102
%else
Epoch: 5
%endif
Version: 0.67.0
Release:        1%{?dist}
License: Apache-2.0
BuildArch: noarch
ExclusiveArch: %{golang_arches} noarch
Summary:        Common configuration and documentation for containers
Provides: skopeo-containers = %{epoch}:%{version}-%{release}
Requires: (container-selinux >= 2:2.162.1 if selinux-policy)
Suggests: fuse-overlayfs
URL: https://github.com/%{project}/%{repo}
Source0:        https://github.com/containers/container-libs/archive/refs/tags/common/v%{version}.tar.gz#/v%{version}.tar.gz
Source1: https://raw.githubusercontent.com/containers/shortnames/refs/heads/main/shortnames.conf
Source2: https://access.redhat.com/security/data/fd431d51.txt
# oreon:deps
BuildRequires:  git-core
BuildRequires:  go-md2man
# /oreon:deps
%description
This package contains common configuration files and documentation for container
tools ecosystem, such as Podman, Buildah and Skopeo.

It is required because the most of configuration files and docs come from projects
which are vendored into Podman, Buildah, Skopeo, etc. but they are not packaged
separately.

%package extra
Summary: Extra dependencies for Podman and Buildah
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: container-network-stack
Requires: oci-runtime
Requires: passt
%description extra
This subpackage will handle dependencies common to Podman and Buildah which are
not required by Skopeo.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{repo}-common-v%{version}

# Fine-grain distro- and release-specific tuning of config files,
# e.g., seccomp, composefs, registries on different RHEL/Fedora versions
bash common/rpm/update-config-files.sh

%build

mkdir -p man5
for i in common/docs/*.5.md image/docs/*.5.md storage/docs/*.5.md; do
   go-md2man -in $i -out man5/$(basename $i .md)
done
%install
install -dp %{buildroot}%{_sysconfdir}/containers/{certs.d,oci/hooks.d,networks,systemd}
install -dp %{buildroot}%{_sharedstatedir}/containers/sigstore
install -dp %{buildroot}%{_datadir}/containers/systemd
install -dp %{buildroot}%{_prefix}/lib/containers/storage
install -dp -m 700 %{buildroot}%{_prefix}/lib/containers/storage/overlay-images
touch %{buildroot}%{_prefix}/lib/containers/storage/overlay-images/images.lock
install -dp -m 700 %{buildroot}%{_prefix}/lib/containers/storage/overlay-layers
touch %{buildroot}%{_prefix}/lib/containers/storage/overlay-layers/layers.lock
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
install -Dp -m0644 image/default.yaml %{buildroot}%{_sysconfdir}/containers/registries.d/default.yaml
install -Dp -m0644 image/default-policy.json %{buildroot}%{_sysconfdir}/containers/policy.json
install -Dp -m0644 image/registries.conf %{buildroot}%{_sysconfdir}/containers/registries.conf
install -Dp -m0644 storage/storage.conf %{buildroot}%{_datadir}/containers/storage.conf
install -Dp -m0644 common/contrib/redhat/registry.access.redhat.com.yaml -t %{buildroot}%{_sysconfdir}/containers/registries.d
install -Dp -m0644 common/contrib/redhat/registry.redhat.io.yaml -t %{buildroot}%{_sysconfdir}/containers/registries.d
for i in man5/*.5; do
    install -Dp -m0644 $i -t %{buildroot}%{_mandir}/man5
done
ln -s containerignore.5 %{buildroot}%{_mandir}/man5/.containerignore.5
install -m0644 common/pkg/subscriptions/mounts.conf %{buildroot}%{_datadir}/containers/mounts.conf
install -m0644 common/pkg/seccomp/seccomp.json %{buildroot}%{_datadir}/containers/seccomp.json
install -m0644 common/pkg/config/containers.conf %{buildroot}%{_datadir}/containers/containers.conf
install -d -p -m 755 %{buildroot}/%{_datadir}/rhel/secrets
ln -s ../../../..%{_sysconfdir}/pki/entitlement %{buildroot}%{_datadir}/rhel/secrets/etc-pki-entitlement
ln -s ../../../..%{_sysconfdir}/rhsm %{buildroot}%{_datadir}/rhel/secrets/rhsm
ln -s ../../../..%{_sysconfdir}/yum.repos.d/redhat.repo %{buildroot}%{_datadir}/rhel/secrets/redhat.repo
%oreon_autofiles containers-common-extra usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n containers-common-extra -f %{oreon_filedir}/containers-common-extra.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.67.0-1
- Prepare for Oreon 11 (RP1)
