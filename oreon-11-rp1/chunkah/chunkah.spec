%global source0_hash 6a3e959359f5c51a5abf497902d9a6edaf43583e2b1253570ca990d8f47224f6
%global crate chunkah
Name:           chunkah
Version:        0.3.2
Release:        1%{?dist}
Summary:        OCI building tool for content-based container image layers
License:        Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND LGPL-2.1-or-later AND MIT AND Zlib AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/coreos/chunkah
Source0:        https://github.com/coreos/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  rustc
BuildRequires:  zlib-devel
# /oreon:deps
%description
chunkah is an OCI building tool that takes a flat rootfs and outputs a
layered OCI image with content-based layers. It optimizes container image
layer reuse by grouping files based on their content (e.g., by RPM package)
rather than by Dockerfile instruction order.

It is a generalized successor to rpm-ostree's build-chunked-oci command.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tar xf %{SOURCE1}
%oreon_vendor_cargo
%build

%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main

%check

%cargo_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
