%global source1_hash 892bdcf7499f977757061dedf9e676bbeae4997013cb16a291592d3d36a94614
%global source0_hash 44fa63e4d2efdc890ad59a3883077ad1f064e5d2fa72dd0d10ab0df2298d6d7c
%bcond_without check
%bcond_with tests
%if 0%{?rhel} >= 9 || 0%{?fedora} > 41 || (0%{?oreon} >= 11)
    %bcond_without ostree_ext
%else
    %bcond_with ostree_ext
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
    %bcond_without rhsm
%else
    %bcond_with rhsm
%endif
%if 0%{?fedora} || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%global rust_minor 89
%else
%global rust_minor 0
%endif
%if 0%{?fedora} || 0%{?rhel} >= 10 || 0%{?rust_minor} >= 89 || (0%{?oreon} >= 11)
    %global new_cargo_macros 1
%else
    %global new_cargo_macros 0
%endif
Name:           bootc
Version:        1.16.13
Release:        1%{?dist}
Summary:        Bootable container system
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://github.com/bootc-dev/bootc
Source0:        https://github.com/bootc-dev/bootc/releases/download/v%{version}/bootc-%{version}.tar.zstd
Source1:        https://github.com/bootc-dev/bootc/releases/download/v%{version}/bootc-%{version}-vendor.tar.zstd
ExcludeArch:    %{ix86}
%if 0%{?oreon} >= 11
%elif 0%{?rhel}
%else
%endif
Requires: composefs
Requires: ostree
Requires: skopeo
Requires: podman
Requires: util-linux-core
Requires: /usr/bin/chcon
Recommends: bootupd
%if %{with ostree_ext}
Provides: ostree-cli(ostree-container)
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  clang-libs
BuildRequires:  go-md2man
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  ostree
BuildRequires:  ostree-devel
BuildRequires:  rustc
BuildRequires:  skopeo
BuildRequires:  systemd
# /oreon:deps
%description
%{summary}

# (-n because we don't want the subpackage name to start with bootc-)
%package -n system-reinstall-bootc
Summary: Utility to reinstall the current system using bootc
Recommends: podman
%description -n system-reinstall-bootc
This package provides a utility to simplify reinstalling the current system to a given bootc image.

%if %{with tests}
%package tests
Summary: Integration tests for bootc
Requires: %{name} = %{version}-%{release}
%description tests
This package contains the integration test suite for bootc.
%endif

%global system_reinstall_bootc_install_podman_path %{_prefix}/lib/system-reinstall-bootc/install-podman

%if 0%{?container_build}
# Source is already at /src, no subdirectory
%global _buildsubdir .
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if ! 0%{?container_build}
%autosetup -p1 -a1
cp .cargo/vendor-config.toml .
cat vendor-config.toml >> .cargo/config.toml
rm vendor-config.toml
%else
cd ..
rm -rf %{name}-%{version}-build
ln -s . %{name}-%{version}-build
cd %{name}-%{version}-build
%endif
%oreon_vendor_cargo
%build

export SYSTEM_REINSTALL_BOOTC_INSTALL_PODMAN_PATH=%{system_reinstall_bootc_install_podman_path}
make manpages
%if 0%{?container_build}
cargo build -j%{_smp_build_ncpus} --release %{?with_rhsm:--features rhsm} --bins
%else
%if %new_cargo_macros
    %cargo_build %{?with_rhsm:-f rhsm} -- --bins
%else
    %cargo_build %{?with_rhsm:--features rhsm} -- --bins
%endif
%endif
%if ! 0%{?container_build}
%cargo_vendor_manifest
sed -i -e '/https:\/\//d' cargo-vendor.txt
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%endif
%install
%make_install INSTALL="install -p -c" CARGO_FEATURES="%{?with_rhsm:rhsm}"
%if %{with ostree_ext}
make install-ostree-hooks DESTDIR=%{?buildroot}
%endif
%if %{with tests}
install -D -m 0755 target/release/tests-integration %{buildroot}%{_bindir}/bootc-integration-tests
%endif
mkdir -p %{buildroot}/%{dirname:%{system_reinstall_bootc_install_podman_path}}
cat >%{?buildroot}/%{system_reinstall_bootc_install_podman_path} <<EOF
exec dnf -y install podman
EOF
chmod +x %{?buildroot}/%{system_reinstall_bootc_install_podman_path}
touch %{?buildroot}/%{_docdir}/bootc/baseimage/base/sysroot/.keepdir
find %{?buildroot}/%{_docdir} ! -type d -printf '%{_docdir}/%%P\n' | sort > bootcdoclist.txt
rm -f %{buildroot}/%{_datadir}/elvish/lib/bootc.elv
rm -f %{buildroot}/%{_datadir}/powershell/Modules/Bootc/Bootc.psm1
%oreon_autofiles system-reinstall-bootc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

if grep -qEe 'Seccomp:.*0$' /proc/self/status; then
    %cargo_test
else
    echo "skipping unit tests due to https://github.com/rpm-software-management/mock/pull/1613#issuecomment-3421908652"
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n system-reinstall-bootc -f %{oreon_filedir}/system-reinstall-bootc.list
%files -n bootc-tests -f %{oreon_filedir}/bootc-tests.list

%changelog

%autochangelog
