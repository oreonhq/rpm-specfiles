%global source0_hash 9f8547cab6d8c765f99ef77972642ea600b986ae71b19c2f22b7152494594617

# Requires forked dependencies, particularly a forked bindgen
# Related: https://github.com/rust-lang/rust/issues/118018
%bcond rust_vendorized 1

# For non-Fedora builds
%bcond dkms 0

# For FUSE fallback
%bcond fuse 1

# While there are no observable issues with LTO, Kent thinks it's bad,
# so disable for now until more testing can be done.
%global _lto_cflags %{nil}

%global make_opts VERSION="%{version}" %{?with_fuse:BCACHEFS_FUSE=1} BUILD_VERBOSE=1 PREFIX=%{_prefix} ROOT_SBINDIR=%{_sbindir}

Name:           bcachefs-tools
Version:        1.37.3
Release:        1%{?dist}
Summary:        Userspace tools for bcachefs

# --- rust ---
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# --- misc ---
# GPL-2.0-only
# GPL-2.0-or-later
# LGPL-2.1-only
# BSD-3-Clause
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only AND BSD-3-Clause AND (Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 with LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND MPL-2.0 AND (Unlicense OR MIT))
URL:            https://bcachefs.org/
Source0:        https://evilpiepirate.org/%{name}/%{name}-vendored-%{version}.tar.zst
Source1:        https://evilpiepirate.org/%{name}/%{name}-vendored-%{version}.tar.sign
Source2:        https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/13AB336D8DCA6E76.asc

# Upstream patches

# Upstreamable patches

# Fedora-specific patches
## Ensure that the makefile doesn't run rust itself, so we can build with our flags properly
Patch1001:      bcachefs-tools-no-make-rust.patch

BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  cargo
BuildRequires:  rust
%if %{with rust_vendorized}
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
%endif

%if %{with dkms}
Requires:       (dkms-bcachefs = %{version}-%{release} if kernel-core%{?_isa})
%endif

# Rust parts FTBFS on 32-bit arches
ExcludeArch:    %{ix86} %{arm32}

%description
The bcachefs-tools package provides all the userspace programs needed to create,
check, modify and correct any inconsistencies in the bcachefs filesystem.

%files
%license COPYING
%license LICENSE.rust-deps
%if %{with rust_vendorized}
%license cargo-vendor.txt
%license COPYING.rust-dependencies
%endif
%doc doc/bcachefs-principles-of-operation.tex
%doc doc/bcachefs.5.rst.tmpl
%{_sbindir}/bcachefs
%{_sbindir}/mount.bcachefs
%{_sbindir}/fsck.bcachefs
%{_sbindir}/mkfs.bcachefs
%{_mandir}/man8/bcachefs.8*
%{_udevrulesdir}/64-bcachefs.rules
%{bash_completions_dir}/bcachefs

%if %{with fuse}
%dnl ----------------------------------------------------------------------------

%package -n fuse-bcachefs
Summary:        FUSE implementation of bcachefs
BuildRequires:  pkgconfig(fuse3) >= 3.7
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-fuse < %{version}-%{release}
Provides:       %{name}-fuse = %{version}-%{release}
Provides:       %{name}-fuse%{?_isa} = %{version}-%{release}

%description -n fuse-bcachefs
This package is an experimental implementation of bcachefs leveraging FUSE to
mount, create, check, modify and correct any inconsistencies in the bcachefs filesystem.

%files -n fuse-bcachefs
%license COPYING
%{_sbindir}/mount.fuse.bcachefs
%{_sbindir}/fsck.fuse.bcachefs
%{_sbindir}/mkfs.fuse.bcachefs

%dnl ----------------------------------------------------------------------------
%endif

%if %{with dkms}
%dnl ----------------------------------------------------------------------------

%package -n dkms-bcachefs
Summary:        Bcachefs kernel module managed by DKMS
Requires:       diffutils
Requires:       dkms >= 3.2.1
Requires:       gcc
Requires:       make
Requires:       perl
Requires:       python3

Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description -n dkms-bcachefs
This package is an implementation of bcachefs built using DKMS to offer the kernel
module to mount, create, check, modify and correct any inconsistencies in the bcachefs
filesystem.

%preun -n dkms-bcachefs
if [  "$(dkms status -m bcachefs -v %{version})" ]; then
   dkms remove -m bcachefs -v %{version} --all --rpm_safe_upgrade
fi

%post -n dkms-bcachefs
if [ "$1" -ge "1" ]; then
   if [ -f /usr/lib/dkms/common.postinst ]; then
      /usr/lib/dkms/common.postinst bcachefs %{version}
      exit $?
   fi
fi

%files -n dkms-bcachefs
%license COPYING
%{_usrsrc}/bcachefs-%{version}/

%dnl ----------------------------------------------------------------------------
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the integrity of the sources
zstdcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
# Prep sources
%autosetup -S git_am
%if ! %{with rust_vendorized}
# Purge the vendor tree
rm -rf vendor
%endif

%if ! %{with rust_vendorized}
%generate_buildrequires
%cargo_generate_buildrequires
cd bch_bindgen
%cargo_generate_buildrequires
cd ../
%endif

%build
%make_build %{make_opts}
%cargo_prep %{?with_rust_vendorized:-v vendor}
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.rust-deps
%{?with_rust_vendorized:%cargo_vendor_manifest}

%install
%make_install %{make_opts}

# Purge debian stuff
rm -rfv %{buildroot}/%{_datadir}/initramfs-tools

%if ! %{with fuse}
# Purge useless symlink stubs
rm -rf %{buildroot}%{_sbindir}/*.fuse.bcachefs
%endif

%if ! %{with dkms}
# Purge dkms files
rm -rf %{buildroot}%{_usrsrc}
%endif

%changelog
%autochangelog
