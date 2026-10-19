%global source0_hash 832e76e93f1ea7a41e5c763a9710acf42d3d54f628015c1255f115a4b7ef2a06
%bcond_with check
%global bundled_rust_deps 0
%bcond_without gpu
%bcond_without snd
Name:           libkrun
Version:        1.19.0
Release:        1%{?dist}
Summary:        Dynamic library providing Virtualization-based process isolation capabilities
License:        Apache-2.0
URL:            https://github.com/libkrun/libkrun
Source0:        https://github.com/libkrun/libkrun/archive/refs/tags/v%{version}.tar.gz
%if 0%{?bundled_rust_deps}
Source1:        %{name}-%{version}-vendor.tar.xz
%else
Patch0:         libkrun-remove-unused-deps.diff
Patch1:         libkrun-remove-nitro-deps.diff
Patch2:         libkrun-remove-tdx-deps.diff
Patch3:         libkrun-bump-bzip-dep.diff
Patch4:         libkrun-bump-kvm-bindings-dep.diff
Patch5:         libkrun-bump-kvm-ioctls-dep.diff
Patch6:         libkrun-remove-sev-deps.diff
%endif
ExclusiveArch:  x86_64 aarch64
%if %{with gpu}
%endif
%if %{with snd}
%endif
%ifarch aarch64
%endif
%if ! 0%{?bundled_rust_deps}
%if 0%{?build_sev}
%endif
%endif
# oreon:deps
BuildRequires:  (crate(bitflags/default) >= 1.2.0 with crate(bitflags/default) < 2.0.0~)
BuildRequires:  (crate(bzip2/default) >= 0.6.0 with crate(bzip2/default) < 0.7.0~)
BuildRequires:  (crate(capng/default) >= 0.2.3 with crate(capng/default) < 0.3.0~)
BuildRequires:  (crate(caps/default) >= 0.5.0 with crate(caps/default) < 0.6.0~)
BuildRequires:  (crate(crossbeam-channel/default) >= 0.5.0 with crate(crossbeam-channel/default) < 0.6.0~)
BuildRequires:  (crate(env_logger/default) >= 0.11.0 with crate(env_logger/default) < 0.12.0~)
BuildRequires:  (crate(flate2/default) >= 1.0.0 with crate(flate2/default) < 2.0.0~)
BuildRequires:  (crate(imago/default) >= 0.2.1 with crate(imago/default) < 0.3.0~)
BuildRequires:  (crate(linux-loader/default) >= 0.13.0 with crate(linux-loader/default) < 0.14.0~)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0~)
BuildRequires:  (crate(memoffset/default) >= 0.9.1 with crate(memoffset/default) < 0.10.0~)
BuildRequires:  (crate(nix/default) >= 0.30.1 with crate(nix/default) < 0.31.0~)
BuildRequires:  (crate(once_cell/default) >= 1.4.1 with crate(once_cell/default) < 2.0.0~)
BuildRequires:  (crate(pipewire/default) >= 0.9.0 with crate(pipewire/default) < 0.10.0~)
BuildRequires:  (crate(rand/default) >= 0.8.5 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(rand/default) >= 0.9.2 with crate(rand/default) < 0.10.0~)
BuildRequires:  (crate(remain/default) >= 0.2.0 with crate(remain/default) < 0.3.0~)
BuildRequires:  (crate(static_assertions/default) >= 1.1.0 with crate(static_assertions/default) < 2.0.0~)
BuildRequires:  (crate(thiserror/default) >= 1.0.0 with crate(thiserror/default) < 2.0.0~)
BuildRequires:  (crate(thiserror/default) >= 2.0.0 with crate(thiserror/default) < 3.0.0~)
BuildRequires:  (crate(virtio-bindings/default) >= 0.2.0 with crate(virtio-bindings/default) < 0.3.0~)
BuildRequires:  (crate(zerocopy/default) >= 0.8.0 with crate(zerocopy/default) < 0.9.0~)
BuildRequires:  (crate(zstd/default) >= 0.13.0 with crate(zstd/default) < 0.14.0~)
BuildRequires:  binutils
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  glibc-static
BuildRequires:  libcap-ng-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  openssl-devel
BuildRequires:  pipewire-devel
BuildRequires:  rustc
BuildRequires:  virglrenderer-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Header files and libraries for libkrun development
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The libkrun-devel package containes the libraries and headers needed to
develop programs that use libkrun Virtualization-based process isolation
capabilities.

# SEV is a feature provided by AMD EPYC processors, so only it's only
# available on x86_64.
%if 0%{?build_sev}
%package sev
Summary: Dynamic library providing Virtualization-based process isolation capabilities (SEV variant)
Requires:  libkrunfw-sev >= 4.0.0
%description sev
Dynamic library providing Virtualization-based process isolation
capabilities, with the ability to use AMD SEV to create a microVM-based
Trusted Execution Environment (TEE).

%package sev-devel
Summary: Header files and libraries for libkrun development
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-sev%{?_isa} = %{version}-%{release}
%description sev-devel
The libkrun-sev-devel package containes the libraries and headers needed to
develop programs that use libkrun-sev Virtualization-based process isolation
capabilities.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?bundled_rust_deps}
%autosetup -n %{name}-%{version_no_tilde} -a1
%else
%setup -q -n %{name}-%{version_no_tilde}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%if ! 0%{?build_sev}
%patch -P 6 -p1
%endif
%endif
%oreon_vendor_cargo
%build

%make_build BLK=1 NET=1 %{?with_gpu:GPU=1} %{?with_snd:SND=1}
%if 0%{?build_sev}
    rm init/init
    %make_build SEV=1 init/init
    %cargo_build -f amd-sev
    mv target/release/libkrun.so target/release/libkrun-sev.so.%{version}
%endif
%if 0%{?bundled_rust_deps}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
%endif
%install
%make_install PREFIX=%{_prefix}
%if 0%{?build_sev}
    %make_install SEV=1 PREFIX=%{_prefix}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n libkrun-devel -f %{oreon_filedir}/libkrun-devel.list

%changelog

%autochangelog

