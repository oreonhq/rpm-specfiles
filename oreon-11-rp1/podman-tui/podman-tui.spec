%global source0_hash bf2bbd547ae7d64812ebd35552c234d3d34f2f06a06651e25b0467aa4ee81d9c

%bcond check 0
%bcond_without bundled
%if 0%{?rhel}
%bcond_without bundled
%endif

%if %{defined rhel} && 0%{?rhel} < 10
%define gobuild(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "-linkmode=external -compressdwarf=false ${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'" -a -v -x %{?**};
%endif

%if %{with bundled}
%global gomodulesmode   GO111MODULE=on
%endif

# https://github.com/containers/podman-tui
%global goipath github.com/containers/podman-tui

Version: 1.11.1
%gometa

%global goname podman-tui

%global common_description %{expand:
%{goname} is a terminal user interface for Podman.
%{goname} is using podman.socket service to communicate with podman environment
and SSH to connect to remote podman machines.
}

%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name: %{goname}
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
Summary: Podman Terminal User Interface

License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL: %{gourl}
Source0:         %{gosource}
Source1:         vendor-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: golang
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make

%if 0%{?fedora} >= 35
BuildRequires: shadow-utils-subid-devel
%endif

%description
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep %{?with_bundledc:-k}
%if %{with bundled}
%setup -q -T -D -a 1 -n %{name}-%{version}
%endif

%if %{without bundled}
%generate_buildrequires
%go_generate_buildrequires
%endif

%build
%if %{with bundled}
export GOFLAGS="-mod=vendor"
%endif

export BUILDTAGS="exclude_graphdriver_devicemapper exclude_graphdriver_btrfs btrfs_noversion containers_image_openpgp remote"
%if 0%{?rhel}
export BUILDTAGS="$BUILDTAGS libtrust_openssl"
%endif

export CGO_LDFLAGS="${CGO_LDFLAGS} -Wl,--allow-multiple-definition"
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%endif

%files
%license %{golicenses}
%doc
%{_bindir}/*

%changelog
%autochangelog
