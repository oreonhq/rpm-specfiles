%global source0_hash fb53732f08479a8057f60e7d7535e3717ecd013e362d65f474272b44374e0f97
%bcond_with check
%global goipath         github.com/coreos/butane
%global gomodulesmode   GO111MODULE=on
Version:                0.29.0
%gometa -f
%global common_description %{expand:
Butane translates human-readable Butane Configs into machine-readable Ignition
configs for provisioning operating systems that use Ignition.}
%global golicenses      LICENSE
%global godocs          docs README.md
Name:           butane
Release:        1%{?dist}
Summary:        Butane config transpiler
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/coreos/butane/archive/refs/tags/v%{version}.tar.gz#/butane-0.29.0.tar.gz
Provides:       fedora-coreos-config-transpiler = %{version}-%{release}
Obsoletes:      fedora-coreos-config-transpiler < 0.10.0-2
Provides:       fcct = %{version}-%{release}
Provides: bundled(golang(github.com/clarketm/json)) = 1.17.1
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 0.3.1
Provides: bundled(golang(github.com/coreos/go-systemd/v22/unit)) = 22.7.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/doc)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/merge)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/shared/errors)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/shared/parse)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/shared/validations)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/util)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_0/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_1/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_2/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_3/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_4/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_5/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_6/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/v3_7_experimental/types)) = 2.26.0
Provides: bundled(golang(github.com/coreos/ignition/v2/config/validate)) = 2.26.0
Provides: bundled(golang(github.com/coreos/vcontext/json)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/path)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/report)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/tree)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/validate)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/yaml)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.10
Provides: bundled(golang(github.com/stretchr/testify/assert)) = 1.11.1
Provides: bundled(golang(github.com/stretchr/testify/assert/yaml)) = 1.11.1
Provides: bundled(golang(github.com/vincent-petithory/dataurl)) = 1.0.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%package redistributable
Summary:       Statically built Butane for Linux, macOS and Windows
License:       Apache-2.0
BuildArch:     noarch
Obsoletes:     butane-nonlinux < 0.13.1-3
%description redistributable
%{common_description}

This package contains statically linked Linux, macOS and Windows Butane
binaries built through cross-compilation. Do not install it. It is only
used for building release binaries to be signed by Fedora release
engineering and uploaded to the Butane GitHub releases page.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%goprep -k
%autopatch -p1

%build

export LDFLAGS="-X github.com/coreos/butane/internal/version.Raw=%{version} "
export GOFLAGS="-mod=vendor"
echo "Building butane..."
%gobuild -o ./butane internal/main.go
%global gocrossbuild go build -ldflags "${LDFLAGS:-} -B 0x$(head -c8 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x 
echo "Building Linux Butane with static linking..."
CGO_ENABLED=0 GOARCH=arm64 GOOS=linux %gocrossbuild -o butane-aarch64-unknown-linux-gnu-static internal/main.go
CGO_ENABLED=0 GOARCH=ppc64le GOOS=linux %gocrossbuild -o butane-ppc64le-unknown-linux-gnu-static internal/main.go
CGO_ENABLED=0 GOARCH=s390x GOOS=linux %gocrossbuild -o butane-s390x-unknown-linux-gnu-static internal/main.go
CGO_ENABLED=0 GOARCH=amd64 GOOS=linux %gocrossbuild -o butane-x86_64-unknown-linux-gnu-static internal/main.go
echo "Building macOS Butane..."
GOARCH=amd64 GOOS=darwin %gocrossbuild -o butane-x86_64-apple-darwin internal/main.go
GOARCH=arm64 GOOS=darwin %gocrossbuild -o butane-aarch64-apple-darwin internal/main.go
echo "Building Windows Butane..."
GOARCH=amd64 GOOS=windows %gocrossbuild -o butane-x86_64-pc-windows-gnu.exe internal/main.go
%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./butane %{buildroot}%{_bindir}
ln -s butane %{buildroot}%{_bindir}/fcct
install -d -p %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-aarch64-apple-darwin %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-aarch64-unknown-linux-gnu-static %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-ppc64le-unknown-linux-gnu-static %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-s390x-unknown-linux-gnu-static %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-x86_64-apple-darwin %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-x86_64-pc-windows-gnu.exe %{buildroot}%{_datadir}/butane
install -p -m 0644 ./butane-x86_64-unknown-linux-gnu-static %{buildroot}%{_datadir}/butane
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n butane-redistributable -f %{oreon_filedir}/butane-redistributable.list

%changelog

%autochangelog
