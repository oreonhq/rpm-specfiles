%global source0_hash 6a3f342a327ec7684198eb0e15114940b6101506db48d9a96590f5942cb3b335
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif
%global gomodulesmode GO111MODULE=on
%define conditional_epoch 2
%define fips 1
%if %{defined copr_username} && "%{copr_username}" == "rhcontainerbot" && "%{copr_projectname}" == "podman-next"
%define next_build 1
%endif
Name: skopeo
%if %{defined next_build}
Epoch: 102
%else
Epoch: %{conditional_epoch}
%endif
Version: 1.24.1
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
Release:        1%{?dist}
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary:        Inspect container images and repositories on registries
URL: https://github.com/containers/%{name}
Source0:        https://github.com/containers/skopeo/archive/refs/tags/v1.24.1.tar.gz#/skopeo-1.24.1.tar.gz
%if %{defined build_with_btrfs}
%endif
%if !%{defined gobuild}
%endif
Requires: containers-common >= 4:1-21
%if %{defined sequoia}
Requires: podman-sequoia
%endif
# oreon:deps
BuildRequires:  /usr/bin/go-md2man
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  golang
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
BuildRequires:  make
BuildRequires:  shadow-utils-subid-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Command line utility to inspect images and repositories directly on Docker
registries without the need to pull them.

# NOTE: The tests subpackage is only intended for testing and will not be supported
# for end-users and/or customers.
%package tests
Summary: Test dependencies for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: gnupg
Requires: jq
Requires: golang
Requires: podman
Requires: crun
Requires: httpd-tools
Requires: openssl
Requires: squashfs-tools
Recommends: bats
Recommends: fakeroot
%description tests
This package installs system test dependencies for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git %{name}-%{version}
# The %%install stage should not rebuild anything but only install what's
# built in the %%build stage. So, remove any dependency on build targets.
sed -i 's/^install-binary: bin\/%{name}.*/install-binary:/' Makefile
sed -i 's/^completions: bin\/%{name}.*/completions:/' Makefile
sed -i 's/^install-docs: docs.*/install-docs:/' Makefile

%build

%set_build_flags
export CGO_CFLAGS=$CFLAGS
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
%ifarch x86_64
export CGO_CFLAGS="$CGO_CFLAGS -m64 -mtune=generic -fcf-protection=full"
%endif
BASEBUILDTAGS="$(hack/libsubid_tag.sh) libsqlite3"
%if %{defined build_with_btrfs}
export BUILDTAGS="$BASEBUILDTAGS $(hack/btrfs_installed_tag.sh)"
%else
export BUILDTAGS="$BASEBUILDTAGS exclude_graphdriver_btrfs"
%endif
%if %{defined fips}
export BUILDTAGS="$BUILDTAGS libtrust_openssl"
%endif
%if %{defined sequoia}
export BUILDTAGS="$BUILDTAGS containers_image_sequoia"
%endif
LDFLAGS=''
%gobuild -o bin/%{name} ./cmd/%{name}
%{__make} docs
%install
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    install-binary install-docs install-completions
%{!?_licensedir:%global license %doc}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n skopeo-tests -f %{oreon_filedir}/skopeo-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.22.0-1
- Prepare for Oreon 11 (RP1)
