%global source0_hash e68fa7d5aaf4658e48fe1778f9d044baa68721db94870d13da618d38c95f9ba8
%bcond check 0
Name:           bpfman
Version:        0.5.4
Release:        1%{?dist}
Summary:        EBPF Program Manager
License:        %{shrink:
    Apache-2.0
    AND BSD-3-Clause
    AND ISC
    AND MIT
    AND MPL-2.0
    AND OpenSSL
    AND Unicode-DFS-2016
    AND Zlib
    AND (0BSD OR MIT OR Apache-2.0)
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR ISC OR MIT)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (MIT AND BSD-3-Clause)
    AND (MIT OR Apache-2.0 OR BSD-1-Clause)
    AND (MIT OR Apache-2.0 OR Zlib)
    AND (Unlicense OR MIT)
    AND GPL-2.0-only
    AND GPL-2.0-only OR BSD-2-Clause
    }
URL:            https://bpfman.io
Source0:        https://github.com/bpfman/bpfman/archive/refs/tags/v%{version}.tar.gz
Source1:        bpfman-%{version}-vendor.tar.xz
Patch0:         0001-bump-cargo-lock-for-idna-1-0-3.diff
Patch1:         0002-bump-openssl-to-0.10.70-CVE-2025-0977.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n bpfman-%{version} -p1 -a1
find vendor -name .cargo-checksum.json \
-exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'
find -name '*.rs' -type f -perm /111 -exec chmod -v -x '{}' '+'
sed -i 's/license-file = "LICENSE"/license = "ISC AND MIT AND OpenSSL"/' vendor/ring-0.17.8/Cargo.toml
sed -i 's|/usr/sbin/bpfman-rpc|/usr/bin/bpfman-rpc|' ./scripts/bpfman.service
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
%install
install -Dpm 0755 \
    -t %{buildroot}%{_bindir} \
    ./target/release/bpfman
install -Dpm 0755 \
    -t %{buildroot}%{_bindir} \
    ./target/release/bpfman-ns
install -Dpm 0755 \
    -t %{buildroot}%{_bindir} \
    ./target/release/bpfman-rpc
install -Dpm 644 \
    -t %{buildroot}%{_unitdir} \
    ./scripts/bpfman.socket
install -Dpm 644 \
    -t %{buildroot}%{_unitdir} \
    ./scripts/bpfman.service
%oreon_autofiles main

%post

%systemd_post bpfman.service
%preun

%systemd_preun bpfman.service
%postun

%systemd_postun_with_restart bpfman.service
%check

%cargo_test -- -- --skip image_pull_
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
