%global source0_hash 7fb70998f56e4ad9a1eeb749b04b7b5c2ede6f7aad561f18bbd3c71db537c11d

Version:       1.5.0
# Default no vendored crates (crate BRs, no Source1). Oreon sets %%{?rhel} but does not ship vendor.tar.xz.
# Offline RHEL-style: add vendor tarball to SOURCES and build with --with libblkio_vendor
%bcond_with libblkio_vendor

%global forgeurl https://gitlab.com/libblkio/libblkio
%global tag    v%{version}
%forgemeta

%if %{defined copr_username}
%define copr_build 1
%endif

Summary:       Block device I/O library
Name:          libblkio
Release:       8%{?dist}
URL:           %{forgeurl}
Source0:        https://gitlab.com/libblkio/libblkio/-/archive/v1.5.0/libblkio-v1.5.0.tar.bz2
%if %{with libblkio_vendor}
# To create the vendor tarball:
#   tar xf %%{name}-v%%{version}.tar.bz2 ; pushd %%{name}-v%%{version} ; \
#   cargo vendor && tar Jcvf ../%%{name}-v%%{version}-vendor.tar.xz vendor/ ; popd
Source1:       %{name}-v%{version}-vendor.tar.xz
%endif
License:       (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND BSD-3-Clause

# Basic build requirements.
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: meson
%if %{with libblkio_vendor}
BuildRequires: rust-toolset
%else
BuildRequires: rust-packaging >= 21
BuildRequires: rustfmt
BuildRequires: cargo
%endif
BuildRequires: python3-docutils
BuildRequires: pkgconf
%if %{defined copr_build}
BuildRequires: git
%endif

# XXX Eventually use %%generate_buildrequires but it does not support
# workspaces yet.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=2124697#c57
#
# For major version >= 1, we are requiring that the major version does
# not change.
#
# For major version >= 0, we are requiring that the minor version does
# not change.
%if %{without libblkio_vendor}
BuildRequires: (crate(autocfg/default) >= 1.0.0 with crate(autocfg/default) < 2.0.0~)
BuildRequires: (crate(bitflags/default) >= 2.5.0 with crate(bitflags/default) < 3.0.0~)
BuildRequires: (crate(bitflags/default) >= 1.2.0 with crate(bitflags/default) < 2.0.0~)
BuildRequires: (crate(cc/default) >= 1.0.0 with crate(cc/default) < 2.0.0~)
BuildRequires: (crate(io-uring/default) >= 0.6.0 with crate(io-uring/default) < 0.7.0~)
BuildRequires: (crate(lazy_static/default) >= 1.0.0 with crate(lazy_static/default) < 2.0.0~)
BuildRequires: (crate(libc/default) >= 0.2.153 with crate(libc/default) < 0.3.0~)
BuildRequires: (crate(memmap2/default) >= 0.5.7 with crate(memmap2/default) < 0.10.0~)
BuildRequires: (crate(num-traits/default) >= 0.2.15 with crate(num-traits/default) < 0.3.0~)
BuildRequires: (crate(paste/default) >= 1.0.0 with crate(paste/default) < 2.0.0~)
BuildRequires: (crate(pci-driver/default) >= 0.1.2 with crate(pci-driver/default) < 0.2.0~)
BuildRequires: (crate(rustix/default) >= 0.38.0 with crate(rustix/default) < 0.39.0~)
BuildRequires: (crate(virtio-bindings/default) >= 0.2.0 with crate(virtio-bindings/default) < 0.3.0~)
%endif


%description
libblkio is a library for high-performance block device I/O with
support for multi-queue devices. A C API is provided so that
applications can use the library from most programming languages.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}


%description devel
This package contains development tools for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if %{defined copr_build}
%autosetup -Sgit %{name}-%{version}
%else
%forgeautosetup -p1

%if %{with libblkio_vendor}
tar xf %{SOURCE1}
%cargo_prep -v vendor
%else
%cargo_prep
%endif
sed -e 's/--locked//' -i src/cargo-build.sh

%endif


%build
export RUSTFLAGS="%build_rustflags"
%{meson}
%{meson_build}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if %{with libblkio_vendor}
%cargo_vendor_manifest
%endif


%install
%{meson_install}


%files
%license LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%license LICENSE.dependencies
%if %{with libblkio_vendor}
%license cargo-vendor.txt
%endif
%doc README.rst
%{_libdir}/libblkio.so.1{,.*}


%files devel
%license LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%doc README.rst
%{_includedir}/blkio.h
%{_libdir}/libblkio.so
%{_libdir}/pkgconfig/blkio.pc
%{_mandir}/man3/blkio.3*


%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-8
- %%bcond_with libblkio_vendor default off so no Source1 vendor.xz use rpmbuild --with libblkio_vendor when needed

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-7
- Source1 vendor tarball only for rhel Fedora uses crates BR

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-6
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-5
- Prepare for Oreon 11 (RP1)
