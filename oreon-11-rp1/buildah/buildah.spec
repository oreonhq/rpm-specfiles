%global source0_hash b48e701c75a2bd30dfe63fda5f886c8a7e0c3dd17b6aa0feb74cc93099254ca4
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global gomodulesmode GO111MODULE=on
%global git0 https://github.com/containers/%{name}
Name: buildah
%if %{defined copr_username}
Epoch: 102
%else
Epoch: 2
%endif
Version: 1.45.1
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
Release:        1%{?dist}
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary:        A command line tool used for creating OCI Images
URL: https://%{name}.io
Source0:        https://github.com/containers/buildah/archive/refs/tags/v1.45.1.tar.gz#/buildah-1.45.1.tar.gz
%if !%{defined gobuild}
%endif
%if %{defined build_with_btrfs}
%endif
Requires: containers-common-extra
Requires: libseccomp >= 2.4.1-0
Suggests: cpp
%if %{defined sequoia}
Requires: podman-sequoia
%endif
# oreon:deps
BuildRequires:  btrfs-progs-devel
BuildRequires:  device-mapper-devel
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  golang
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
BuildRequires:  libseccomp-static
BuildRequires:  make
BuildRequires:  shadow-utils-subid-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
The %{name} package provides a command line tool which can be used to
* create a working container from scratch
or
* create a working container from an image as a starting point
* mount/umount a working container's root file system for manipulation
* save container's root file system layer to create a new image
* delete a working container or an image

# This subpackage is only intended for CI testing.
# Not meant for end user/customer usage.
%package tests
Summary: Tests for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
%if %{defined bats_epel}
Requires: bats
%else
Recommends: bats
%endif
Requires: bzip2
Requires: podman
Requires: golang
Requires: jq
Requires: httpd-tools
Requires: openssl
Requires: nmap-ncat
Requires: git-daemon
%description tests
%{summary}

This package contains system tests for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%set_build_flags
export CGO_CFLAGS=$CFLAGS
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
export CNI_VERSION=`grep '^# github.com/containernetworking/cni ' src/modules.txt | sed 's,.* ,,'`
export LDFLAGS="-X main.buildInfo=`date +%s` -X main.cniVersion=${CNI_VERSION}"
export BUILDTAGS="seccomp $(hack/systemd_tag.sh) $(hack/libsubid_tag.sh) libsqlite3"
%if !%{defined build_with_btrfs}
export BUILDTAGS+=" exclude_graphdriver_btrfs"
%endif
%if %{defined fips}
export BUILDTAGS+=" libtrust_openssl"
%endif
%if %{defined sequoia}
export BUILDTAGS+=" containers_image_sequoia"
%endif
%gobuild -o bin/%{name} ./cmd/%{name}
%gobuild -o bin/imgtype ./tests/imgtype
%gobuild -o bin/copy ./tests/copy
%gobuild -o bin/tutorial ./tests/tutorial
%gobuild -o bin/inet ./tests/inet
%gobuild -o bin/dumpspec ./tests/dumpspec
%gobuild -o bin/passwd ./tests/passwd
%gobuild -o bin/crash ./tests/crash
%gobuild -o bin/wait ./tests/wait
%{__make} docs
%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install install.completions
install -d -p %{buildroot}/%{_datadir}/%{name}/test/system
cp -pav tests/. %{buildroot}/%{_datadir}/%{name}/test/system
cp bin/imgtype %{buildroot}/%{_bindir}/%{name}-imgtype
cp bin/copy    %{buildroot}/%{_bindir}/%{name}-copy
cp bin/tutorial %{buildroot}/%{_bindir}/%{name}-tutorial
cp bin/inet     %{buildroot}/%{_bindir}/%{name}-inet
cp bin/dumpspec %{buildroot}/%{_bindir}/%{name}-dumpspec
cp bin/passwd %{buildroot}/%{_bindir}/%{name}-passwd
cp bin/crash %{buildroot}/%{_bindir}/%{name}-crash
cp bin/wait %{buildroot}/%{_bindir}/%{name}-wait
rm %{buildroot}%{_datadir}/%{name}/test/system/tools/build/*
%{!?_licensedir:%global license %doc}
%oreon_autofiles buildah-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n buildah-tests -f %{oreon_filedir}/buildah-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.43.0-1
- Prepare for Oreon 11 (RP1)
