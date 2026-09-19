%global source0_hash 3eaa3afc4e8d1109a88d7e138657c6144fb8901af1c3505663208f25538ba426

%global toolchain clang

# upstream build system requires the use of libbpf and bpftool sources
# the commits for libbpf and bpftool should match those in the meson.build
# for the scx version
%global bpftool_url https://github.com/libbpf/bpftool
%global bpftool_commit 20ce6933869b70bacfdd0dd1a8399199290bf8ff
%global bpftool_shortcommit %(c=%{bpftool_commit}; echo ${c:0:7})
%global bpftool_date 20230926
%global bpftool_version 7.2.0^%{bpftool_date}git%{bpftool_shortcommit}

%global libbpf_url https://github.com/libbpf/libbpf
%global libbpf_commit 6d3595d215b014d3eddb88038d686e1c20781534
%global libbpf_shortcommit %(c=%{libbpf_commit}; echo ${c:0:7})
%global libbpf_date 20240125
%global libbpf_version 1.4.0~^%{libbpf_date}git%{libbpf_shortcommit}
 
Name:           scx_c_schedulers
Version:        0.1.8
Release:        %autorelease
Summary:        sched_ext schedulers written in c

%global scx_dir scx-%{version}

# scx: GPL-2.0-only
# bundled libbpf: LGPL-2.1-only OR BSD-2-Clause
# bpftool: GPL-2.0-only OR BSD-2-Clause
License:        GPL-2.0-only AND (GPL-2.0-only OR BSD-2-Clause) AND (LGPL-2.1-only OR BSD-2-Clause)
URL:            https://github.com/sched-ext/scx
Source0:        %{url}/archive/v%{version}/%{scx_dir}.tar.gz
Source1:        %{bpftool_url}/archive/%{bpftool_commit}/bpftool-%{bpftool_version}.tar.gz
Source2:        %{libbpf_url}/archive/%{libbpf_commit}/libbpf-%{libbpf_version}.tar.gz
Source3:        %{name}.rpmlintrc

# Minimum version of clang is required to build the bpf schedulers
BuildRequires:  clang >= 17
BuildRequires:  meson >= 1.2.0
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  jq
# libbpf deps
BuildRequires:  elfutils-libelf-devel
ExcludeArch:    %{ix86}

# upstream does not support dynamic linking
Provides:       bundled(bpftool) = %{bpftool_version}
Provides:       bundled(libbpf) = %{libbpf_version}
 
%description
Example sched_ext schedulers written in C (as opposed to Rust) that include:
scx_central, scx_flatcg, scx_nest, scx_pair, scx_qmap, scx_simple, scx_userland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{name}-%{version} -c -q -a 0
# provide the bpftool version we specify
tar xf %{SOURCE1}
mv bpftool-%{bpftool_commit} bpftool
# same license files as libbpf, no-op
 
# provide the libbpf version we specify
tar xf %{SOURCE2}
rmdir bpftool/libbpf
mv libbpf-%{libbpf_commit}/LICENSE libbpf-LICENSE
mv libbpf-%{libbpf_commit}/LICENSE.BSD-2-Clause  libbpf-LICENSE.BSD-2-Clause
mv libbpf-%{libbpf_commit}/LICENSE.LGPL-2.1 libbpf-LICENSE.LGPL-2.1
mv bpftool/LICENSE.GPL-2.0 bpftool-LICENSE.GPL-2.0
mv libbpf-%{libbpf_commit} bpftool/libbpf
cd bpftool/src
%make_build
cd ../libbpf/src
mkdir root
BUILD_STATIC_ONLY=y DESTDIR=root make install
 
%build
cd %{scx_dir}
%meson -Dbpftool=%{_builddir}/%{name}-%{version}/bpftool/src/bpftool -Dlibbpf_a=%{_builddir}/%{name}-%{version}/bpftool/libbpf/src/libbpf.a -Dlibbpf_h=%{_builddir}/%{name}-%{version}/bpftool/libbpf/src/root/usr/include -Denable_rust=false -Dsystemd=disabled -Dopenrc=disabled
%meson_build
 
%install
cd %{scx_dir}
%meson_install
 
%files
%license %{scx_dir}/LICENSE libbpf-LICENSE* bpftool-LICENSE*
%doc %{scx_dir}/README.md %{scx_dir}/OVERVIEW.md %{scx_dir}/BREAKING_CHANGES.md %{scx_dir}/INSTALL.md
%{_bindir}/scx_*
 
%changelog
%autochangelog
