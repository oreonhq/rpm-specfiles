%global source0_hash abf7e240eae2f45017f7cc6008e151a039440ca47431d5d7837ec3e36e5d7bca

%bcond check 0

Name:           bcvk
# Replaced by cargo xtask spec
Version: 0.10.0
Release:        1%{?dist}
Summary:        Bootable container VM toolkit

# Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://github.com/bootc-dev/bcvk
Source0: bcvk-0.10.0.tar.zstd
Source1: bcvk-0.10.0-vendor.tar.zstd

# Only build for architectures with full support and testing
ExclusiveArch:  x86_64 aarch64

BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: go-md2man
BuildRequires: openssh-clients
%if 0%{?rhel}
BuildRequires: rust-toolset
%else
BuildRequires: cargo-rpm-macros >= 25
%endif

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a1
# Default -v vendor config doesn't support non-crates.io deps (i.e. git)
cp .cargo/vendor-config.toml .
%cargo_prep -N
cat vendor-config.toml >> .cargo/config.toml
rm vendor-config.toml

%build
%cargo_build

make manpages

%cargo_vendor_manifest
# https://pagure.io/fedora-rust/rust-packaging/issue/33
sed -i -e '/https:\/\//d' cargo-vendor.txt
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%make_install INSTALL="install -p -c"

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE-MIT
%license LICENSE-APACHE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/bcvk
%{_mandir}/man*/*bcvk*

%changelog
%autochangelog
