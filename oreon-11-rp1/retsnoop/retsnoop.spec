%global source0_hash 3060814be3ed93f3674dd6a3de6d7b6652ba99d49f10fdfd686baaec6211cd28
%bcond check 1
%global toolchain clang
%global bpftool_url https://github.com/libbpf/bpftool
%global bpftool_commit 64402b8ea43b2ef62ee8ba71d9b50a5e32603fd2
%global bpftool_shortcommit %(c=%{bpftool_commit}; echo ${c:0:7})
%global bpftool_date 20240716
%global bpftool_version 7.7.0^%{bpftool_date}git%{bpftool_shortcommit}
%global libbpf_url https://github.com/libbpf/libbpf
%global libbpf_commit 3f077472ee7e703b733c2c9ae15ef3f4c13ee25b
%global libbpf_shortcommit %(c=%{libbpf_commit}; echo ${c:0:7})
%global libbpf_date 20250826
%global libbpf_version 1.7^%{libbpf_date}git%{libbpf_shortcommit}
Name:           retsnoop
Version:        0.11
Release:        1%{?dist}
Summary:        A tool for investigating kernel error call stacks
License:        BSD-2-Clause AND (LGPL-2.1-only OR BSD-2-Clause) AND (Apache-2.0 OR MIT) AND MIT AND (0BSD OR Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND (Apache-2.0 OR MIT OR Zlib)
URL:            https://github.com/anakryiko/retsnoop
Source0:        https://github.com/anakryiko/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{bpftool_url}/archive/%{bpftool_commit}/bpftool-%{bpftool_version}.tar.gz
Source2:        %{libbpf_url}/archive/%{libbpf_commit}/libbpf-%{libbpf_version}.tar.gz
Source3:        README.Fedora
Patch:          retsnoop-0.11-gimli-0.32-etc.patch
ExclusiveArch:  %{rust_arches}
ExcludeArch:    %{ix86}
ExcludeArch:    ppc64le
Provides:       bundled(bpftool) = %{bpftool_version}
Provides:       bundled(libbpf) = %{libbpf_version}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  elfutils-libelf-devel
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description
retsnoop is BPF-based tool that is meant to help debugging kernel issues. It
allows to capture call stacks of kernel functions that return errors (NULL or
-Exxx) and emits every such detected call stack, along with the captured
results.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
tar xf %{SOURCE1}
rmdir bpftool
mv bpftool-%{bpftool_commit} bpftool
tar xf %{SOURCE2}
rmdir libbpf
mv libbpf-%{libbpf_commit} libbpf
mv libbpf/LICENSE libbpf-LICENSE
mv libbpf/LICENSE.BSD-2-Clause  libbpf-LICENSE.BSD-2-Clause
mv libbpf/LICENSE.LGPL-2.1 libbpf-LICENSE.LGPL-2.1
cp -p %{SOURCE3} .
ln -s sidecar/Cargo.toml .
rm sidecar/Cargo.lock
%oreon_vendor_cargo
%build

cd sidecar
%cargo_build
%{cargo_license_summary}
%{cargo_license} > ../LICENSE.dependencies
cd -
%make_build -C src HOSTCC=clang
%install
%make_install -C src prefix=%{_prefix}
%oreon_autofiles main
%if %{with check}
%check

./src/simfail -a
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
