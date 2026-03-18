#
# Copyright (C) 2011-2017 Red Hat, Inc
#
%bcond_without check
#%%global debug_package %%{nil}

#%%global version_suffix -rc2
#%%global release_suffix .test3

Summary: Device-mapper Persistent Data Tools
Name: device-mapper-persistent-data
Version: 1.3.1
Release: 3%{?dist}%{?release_suffix}
License: GPL-3.0-only AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)

#ExcludeArch: %%{ix86}
URL: https://github.com/jthornber/thin-provisioning-tools
#Source0: https://github.com/jthornber/thin-provisioning-tools/archive/thin-provisioning-tools-%%{version}.tar.gz
Source0: https://github.com/jthornber/thin-provisioning-tools/archive/v%{version}%{?version_suffix}.tar.gz
Source1: dmpd131-vendor.tar.gz

%if %{defined rhel}
BuildRequires: rust-toolset
%else
BuildRequires: rust-packaging
BuildRequires: rust >= 1.35
BuildRequires: cargo
%endif
BuildRequires: make
BuildRequires: systemd-devel
BuildRequires: clang-libs
BuildRequires: glibc-static
BuildRequires: device-mapper-devel
BuildRequires: clang
#BuildRequires: gcc

%description
thin-provisioning-tools contains check,dump,restore,repair,rmap
and metadata_size tools to manage device-mapper thin provisioning
target metadata devices; cache check,dump,metadata_size,restore
and repair tools to manage device-mapper cache metadata devices
are included and era check, dump, restore and invalidate to manage
snapshot eras

%prep
%autosetup -p1 -n thin-provisioning-tools-%{version}%{?version_suffix} -a1
%cargo_prep -v vendor

# NOTE: Following could replace Cargo.toml patching, but some macros are not working well with it
# Notably at least one of cargo_license_summary, cargo_license_summary, or cargo_vendor_manifest
#cat >> .cargo/config.toml << EOF
#
#[source."git+https://github.com/jthornber/rio?branch=master"]
#git = "https://github.com/jthornber/rio"
#branch = "master"
#replace-with = "vendored-sources"
#
#EOF

echo %{version}-%{release} > VERSION

%generate_buildrequires

%build
#make %{?_smp_mflags} V=
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest

%install
# TODO: Check that MANDIR is unused and remove
%make_install STRIP=true MANDIR=%{_mandir} BINDIR=%{buildroot}%{_sbindir}

%if %{with check}
%check
%cargo_test
#cargo test --test thin_shrink -- --nocapture --test-threads=1
%endif

%files
%doc README.md
%license COPYING
%license LICENSE.dependencies
%license cargo-vendor.txt
%{_mandir}/man8/cache_check.8.gz
%{_mandir}/man8/cache_dump.8.gz
%{_mandir}/man8/cache_metadata_size.8.gz
%{_mandir}/man8/cache_repair.8.gz
%{_mandir}/man8/cache_restore.8.gz
%{_mandir}/man8/cache_writeback.8.gz
%{_mandir}/man8/era_check.8.gz
%{_mandir}/man8/era_dump.8.gz
%{_mandir}/man8/era_invalidate.8.gz
%{_mandir}/man8/era_restore.8.gz
%{_mandir}/man8/thin_check.8.gz
%{_mandir}/man8/thin_delta.8.gz
%{_mandir}/man8/thin_dump.8.gz
%{_mandir}/man8/thin_ls.8.gz
%{_mandir}/man8/thin_metadata_size.8.gz
%{_mandir}/man8/thin_migrate.8.gz
%{_mandir}/man8/thin_repair.8.gz
%{_mandir}/man8/thin_restore.8.gz
%{_mandir}/man8/thin_rmap.8.gz
%{_mandir}/man8/thin_trim.8.gz
%{_mandir}/man8/thin_metadata_pack.8.gz
%{_mandir}/man8/thin_metadata_unpack.8.gz
%{_sbindir}/pdata_tools
%{_sbindir}/cache_check
%{_sbindir}/cache_dump
%{_sbindir}/cache_metadata_size
%{_sbindir}/cache_repair
%{_sbindir}/cache_restore
%{_sbindir}/cache_writeback
%{_sbindir}/era_check
%{_sbindir}/era_dump
%{_sbindir}/era_invalidate
%{_sbindir}/era_restore
%{_sbindir}/thin_check
%{_sbindir}/thin_delta
%{_sbindir}/thin_dump
%{_sbindir}/thin_ls
%{_sbindir}/thin_metadata_size
%{_sbindir}/thin_migrate
%{_sbindir}/thin_repair
%{_sbindir}/thin_restore
%{_sbindir}/thin_rmap
%{_sbindir}/thin_trim
%{_sbindir}/thin_metadata_pack
%{_sbindir}/thin_metadata_unpack
#% {_sbindir}/thin_show_duplicates

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-3
- Prepare for Oreon 11 (RP1)
