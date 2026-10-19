%global source0_hash abf7e240eae2f45017f7cc6008e151a039440ca47431d5d7837ec3e36e5d7bca
%bcond check 0
Name:           bcvk
Version: 0.20.0
Release:        1%{?dist}
Summary:        Bootable container VM toolkit
License:        Apache-2.0 OR MIT
URL:            https://github.com/bootc-dev/bcvk
Source0:        bcvk-0.10.0.tar.zstd
Source1: bcvk-0.10.0-vendor.tar.zstd
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  go-md2man
BuildRequires:  make
BuildRequires:  openssh-clients
BuildRequires:  openssl-devel
BuildRequires:  rustc
# /oreon:deps
%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -a1
cp .cargo/vendor-config.toml .
cat vendor-config.toml >> .cargo/config.toml
rm vendor-config.toml
%oreon_vendor_cargo
%build

%cargo_build
make manpages
%cargo_vendor_manifest
sed -i -e '/https:\/\//d' cargo-vendor.txt
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
%make_install INSTALL="install -p -c"
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
