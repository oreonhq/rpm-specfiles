%global source0_hash a179dc3f3af0389cbd0a8d238ea047abbd72b47225bb49cbadb9a3824a44938e
%bcond check 1
%ifarch s390x
%global rustflags_debuginfo 1
%endif
%global crate coreutils
Name:           rust-coreutils
Version:        0.12.0
Release:        1%{?dist}
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
License:        MIT
URL:            https://crates.io/crates/coreutils
Source0:        https://static.crates.io/crates/coreutils/coreutils-%{version}.crate
Patch:          coreutils-fix-metadata.diff
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-devel
# /oreon:deps
%description

%package     -n uutils-coreutils
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
License:        %{shrink:
  (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND
  Zlib AND
  (0BSD OR MIT OR Apache-2.0) AND
  Apache-2.0 AND
  (Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND
  (Apache-2.0 OR GPL-2.0-only) AND
  (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
  BSD-2-Clause AND
  (BSD-2-Clause OR Apache-2.0 OR MIT) AND
  BSD-3-Clause AND
  CC0-1.0 AND
  ISC AND
  MIT AND
  (MIT OR Zlib OR Apache-2.0) AND
  (MIT-0 OR Apache-2.0) AND
  Unicode-3.0 AND
  (Unlicense OR MIT)
}
%description -n uutils-coreutils

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arch-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+arch-devel

This package contains library source intended for building other packages which
use the "arch" feature of the "%{crate}" crate.

%package     -n %{name}+b2sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+b2sum-devel

This package contains library source intended for building other packages which
use the "b2sum" feature of the "%{crate}" crate.

%package     -n %{name}+base32-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+base32-devel

This package contains library source intended for building other packages which
use the "base32" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+basename-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+basename-devel

This package contains library source intended for building other packages which
use the "basename" feature of the "%{crate}" crate.

%package     -n %{name}+basenc-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+basenc-devel

This package contains library source intended for building other packages which
use the "basenc" feature of the "%{crate}" crate.

%package     -n %{name}+cat-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+cat-devel

This package contains library source intended for building other packages which
use the "cat" feature of the "%{crate}" crate.

%package     -n %{name}+chcon-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+chcon-devel

This package contains library source intended for building other packages which
use the "chcon" feature of the "%{crate}" crate.

%package     -n %{name}+chgrp-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+chgrp-devel

This package contains library source intended for building other packages which
use the "chgrp" feature of the "%{crate}" crate.

%package     -n %{name}+chmod-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+chmod-devel

This package contains library source intended for building other packages which
use the "chmod" feature of the "%{crate}" crate.

%package     -n %{name}+chown-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+chown-devel

This package contains library source intended for building other packages which
use the "chown" feature of the "%{crate}" crate.

%package     -n %{name}+chroot-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+chroot-devel

This package contains library source intended for building other packages which
use the "chroot" feature of the "%{crate}" crate.

%package     -n %{name}+cksum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+cksum-devel

This package contains library source intended for building other packages which
use the "cksum" feature of the "%{crate}" crate.

%package     -n %{name}+comm-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+comm-devel

This package contains library source intended for building other packages which
use the "comm" feature of the "%{crate}" crate.

%package     -n %{name}+cp-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+cp-devel

This package contains library source intended for building other packages which
use the "cp" feature of the "%{crate}" crate.

%package     -n %{name}+csplit-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+csplit-devel

This package contains library source intended for building other packages which
use the "csplit" feature of the "%{crate}" crate.

%package     -n %{name}+cut-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+cut-devel

This package contains library source intended for building other packages which
use the "cut" feature of the "%{crate}" crate.

%package     -n %{name}+date-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+date-devel

This package contains library source intended for building other packages which
use the "date" feature of the "%{crate}" crate.

%package     -n %{name}+dd-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+dd-devel

This package contains library source intended for building other packages which
use the "dd" feature of the "%{crate}" crate.

%package     -n %{name}+df-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+df-devel

This package contains library source intended for building other packages which
use the "df" feature of the "%{crate}" crate.

%package     -n %{name}+dir-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+dir-devel

This package contains library source intended for building other packages which
use the "dir" feature of the "%{crate}" crate.

%package     -n %{name}+dircolors-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+dircolors-devel

This package contains library source intended for building other packages which
use the "dircolors" feature of the "%{crate}" crate.

%package     -n %{name}+dirname-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+dirname-devel

This package contains library source intended for building other packages which
use the "dirname" feature of the "%{crate}" crate.

%package     -n %{name}+du-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+du-devel

This package contains library source intended for building other packages which
use the "du" feature of the "%{crate}" crate.

%package     -n %{name}+echo-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+echo-devel

This package contains library source intended for building other packages which
use the "echo" feature of the "%{crate}" crate.

%package     -n %{name}+env-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+env-devel

This package contains library source intended for building other packages which
use the "env" feature of the "%{crate}" crate.

%package     -n %{name}+expand-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+expand-devel

This package contains library source intended for building other packages which
use the "expand" feature of the "%{crate}" crate.

%package     -n %{name}+expensive_tests-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+expensive_tests-devel

This package contains library source intended for building other packages which
use the "expensive_tests" feature of the "%{crate}" crate.

%package     -n %{name}+expr-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+expr-devel

This package contains library source intended for building other packages which
use the "expr" feature of the "%{crate}" crate.

%package     -n %{name}+factor-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+factor-devel

This package contains library source intended for building other packages which
use the "factor" feature of the "%{crate}" crate.

%package     -n %{name}+false-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+false-devel

This package contains library source intended for building other packages which
use the "false" feature of the "%{crate}" crate.

%package     -n %{name}+feat_Tier1-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_Tier1-devel

This package contains library source intended for building other packages which
use the "feat_Tier1" feature of the "%{crate}" crate.

%package     -n %{name}+feat_acl-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_acl-devel

This package contains library source intended for building other packages which
use the "feat_acl" feature of the "%{crate}" crate.

%package     -n %{name}+feat_common_core-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_common_core-devel

This package contains library source intended for building other packages which
use the "feat_common_core" feature of the "%{crate}" crate.

%package     -n %{name}+feat_external_libstdbuf-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_external_libstdbuf-devel

This package contains library source intended for building other packages which
use the "feat_external_libstdbuf" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_macos-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_macos-devel

This package contains library source intended for building other packages which
use the "feat_os_macos" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_unix-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_unix-devel

This package contains library source intended for building other packages which
use the "feat_os_unix" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_unix_android-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_unix_android-devel

This package contains library source intended for building other packages which
use the "feat_os_unix_android" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_unix_fuchsia-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_unix_fuchsia-devel

This package contains library source intended for building other packages which
use the "feat_os_unix_fuchsia" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_unix_gnueabihf-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_unix_gnueabihf-devel

This package contains library source intended for building other packages which
use the "feat_os_unix_gnueabihf" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_unix_musl-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_unix_musl-devel

This package contains library source intended for building other packages which
use the "feat_os_unix_musl" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_unix_redox-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_unix_redox-devel

This package contains library source intended for building other packages which
use the "feat_os_unix_redox" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_windows-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_windows-devel

This package contains library source intended for building other packages which
use the "feat_os_windows" feature of the "%{crate}" crate.

%package     -n %{name}+feat_os_windows_legacy-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_os_windows_legacy-devel

This package contains library source intended for building other packages which
use the "feat_os_windows_legacy" feature of the "%{crate}" crate.

%package     -n %{name}+feat_require_selinux-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_require_selinux-devel

This package contains library source intended for building other packages which
use the "feat_require_selinux" feature of the "%{crate}" crate.

%package     -n %{name}+feat_require_unix-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_require_unix-devel

This package contains library source intended for building other packages which
use the "feat_require_unix" feature of the "%{crate}" crate.

%package     -n %{name}+feat_require_unix_core-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_require_unix_core-devel

This package contains library source intended for building other packages which
use the "feat_require_unix_core" feature of the "%{crate}" crate.

%package     -n %{name}+feat_require_unix_hostid-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_require_unix_hostid-devel

This package contains library source intended for building other packages which
use the "feat_require_unix_hostid" feature of the "%{crate}" crate.

%package     -n %{name}+feat_require_unix_musl-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_require_unix_musl-devel

This package contains library source intended for building other packages which
use the "feat_require_unix_musl" feature of the "%{crate}" crate.

%package     -n %{name}+feat_require_unix_utmpx-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_require_unix_utmpx-devel

This package contains library source intended for building other packages which
use the "feat_require_unix_utmpx" feature of the "%{crate}" crate.

%package     -n %{name}+feat_selinux-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_selinux-devel

This package contains library source intended for building other packages which
use the "feat_selinux" feature of the "%{crate}" crate.

%package     -n %{name}+feat_smack-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_smack-devel

This package contains library source intended for building other packages which
use the "feat_smack" feature of the "%{crate}" crate.

%package     -n %{name}+feat_systemd_logind-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_systemd_logind-devel

This package contains library source intended for building other packages which
use the "feat_systemd_logind" feature of the "%{crate}" crate.

%package     -n %{name}+feat_wasm-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+feat_wasm-devel

This package contains library source intended for building other packages which
use the "feat_wasm" feature of the "%{crate}" crate.

%package     -n %{name}+fmt-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+fmt-devel

This package contains library source intended for building other packages which
use the "fmt" feature of the "%{crate}" crate.

%package     -n %{name}+fold-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+fold-devel

This package contains library source intended for building other packages which
use the "fold" feature of the "%{crate}" crate.

%package     -n %{name}+groups-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+groups-devel

This package contains library source intended for building other packages which
use the "groups" feature of the "%{crate}" crate.

%package     -n %{name}+head-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+head-devel

This package contains library source intended for building other packages which
use the "head" feature of the "%{crate}" crate.

%package     -n %{name}+hostid-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+hostid-devel

This package contains library source intended for building other packages which
use the "hostid" feature of the "%{crate}" crate.

%package     -n %{name}+hostname-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+hostname-devel

This package contains library source intended for building other packages which
use the "hostname" feature of the "%{crate}" crate.

%package     -n %{name}+id-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+id-devel

This package contains library source intended for building other packages which
use the "id" feature of the "%{crate}" crate.

%package     -n %{name}+install-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+install-devel

This package contains library source intended for building other packages which
use the "install" feature of the "%{crate}" crate.

%package     -n %{name}+join-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+join-devel

This package contains library source intended for building other packages which
use the "join" feature of the "%{crate}" crate.

%package     -n %{name}+kill-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+kill-devel

This package contains library source intended for building other packages which
use the "kill" feature of the "%{crate}" crate.

%package     -n %{name}+link-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+link-devel

This package contains library source intended for building other packages which
use the "link" feature of the "%{crate}" crate.

%package     -n %{name}+ln-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+ln-devel

This package contains library source intended for building other packages which
use the "ln" feature of the "%{crate}" crate.

%package     -n %{name}+logname-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+logname-devel

This package contains library source intended for building other packages which
use the "logname" feature of the "%{crate}" crate.

%package     -n %{name}+ls-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+ls-devel

This package contains library source intended for building other packages which
use the "ls" feature of the "%{crate}" crate.

%package     -n %{name}+macos-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+macos-devel

This package contains library source intended for building other packages which
use the "macos" feature of the "%{crate}" crate.

%package     -n %{name}+md5sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+md5sum-devel

This package contains library source intended for building other packages which
use the "md5sum" feature of the "%{crate}" crate.

%package     -n %{name}+mkdir-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+mkdir-devel

This package contains library source intended for building other packages which
use the "mkdir" feature of the "%{crate}" crate.

%package     -n %{name}+mkfifo-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+mkfifo-devel

This package contains library source intended for building other packages which
use the "mkfifo" feature of the "%{crate}" crate.

%package     -n %{name}+mknod-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+mknod-devel

This package contains library source intended for building other packages which
use the "mknod" feature of the "%{crate}" crate.

%package     -n %{name}+mktemp-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+mktemp-devel

This package contains library source intended for building other packages which
use the "mktemp" feature of the "%{crate}" crate.

%package     -n %{name}+more-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+more-devel

This package contains library source intended for building other packages which
use the "more" feature of the "%{crate}" crate.

%package     -n %{name}+mv-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+mv-devel

This package contains library source intended for building other packages which
use the "mv" feature of the "%{crate}" crate.

%package     -n %{name}+nice-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+nice-devel

This package contains library source intended for building other packages which
use the "nice" feature of the "%{crate}" crate.

%package     -n %{name}+nl-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+nl-devel

This package contains library source intended for building other packages which
use the "nl" feature of the "%{crate}" crate.

%package     -n %{name}+nohup-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+nohup-devel

This package contains library source intended for building other packages which
use the "nohup" feature of the "%{crate}" crate.

%package     -n %{name}+nproc-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+nproc-devel

This package contains library source intended for building other packages which
use the "nproc" feature of the "%{crate}" crate.

%package     -n %{name}+numfmt-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+numfmt-devel

This package contains library source intended for building other packages which
use the "numfmt" feature of the "%{crate}" crate.

%package     -n %{name}+od-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+od-devel

This package contains library source intended for building other packages which
use the "od" feature of the "%{crate}" crate.

%package     -n %{name}+paste-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+paste-devel

This package contains library source intended for building other packages which
use the "paste" feature of the "%{crate}" crate.

%package     -n %{name}+pathchk-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+pathchk-devel

This package contains library source intended for building other packages which
use the "pathchk" feature of the "%{crate}" crate.

%package     -n %{name}+pinky-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+pinky-devel

This package contains library source intended for building other packages which
use the "pinky" feature of the "%{crate}" crate.

%package     -n %{name}+pr-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+pr-devel

This package contains library source intended for building other packages which
use the "pr" feature of the "%{crate}" crate.

%package     -n %{name}+printenv-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+printenv-devel

This package contains library source intended for building other packages which
use the "printenv" feature of the "%{crate}" crate.

%package     -n %{name}+printf-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+printf-devel

This package contains library source intended for building other packages which
use the "printf" feature of the "%{crate}" crate.

%package     -n %{name}+ptx-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+ptx-devel

This package contains library source intended for building other packages which
use the "ptx" feature of the "%{crate}" crate.

%package     -n %{name}+pwd-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+pwd-devel

This package contains library source intended for building other packages which
use the "pwd" feature of the "%{crate}" crate.

%package     -n %{name}+readlink-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+readlink-devel

This package contains library source intended for building other packages which
use the "readlink" feature of the "%{crate}" crate.

%package     -n %{name}+realpath-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+realpath-devel

This package contains library source intended for building other packages which
use the "realpath" feature of the "%{crate}" crate.

%package     -n %{name}+rm-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+rm-devel

This package contains library source intended for building other packages which
use the "rm" feature of the "%{crate}" crate.

%package     -n %{name}+rmdir-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+rmdir-devel

This package contains library source intended for building other packages which
use the "rmdir" feature of the "%{crate}" crate.

%package     -n %{name}+runcon-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+runcon-devel

This package contains library source intended for building other packages which
use the "runcon" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%package     -n %{name}+seq-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+seq-devel

This package contains library source intended for building other packages which
use the "seq" feature of the "%{crate}" crate.

%package     -n %{name}+sha1sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sha1sum-devel

This package contains library source intended for building other packages which
use the "sha1sum" feature of the "%{crate}" crate.

%package     -n %{name}+sha224sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sha224sum-devel

This package contains library source intended for building other packages which
use the "sha224sum" feature of the "%{crate}" crate.

%package     -n %{name}+sha256sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sha256sum-devel

This package contains library source intended for building other packages which
use the "sha256sum" feature of the "%{crate}" crate.

%package     -n %{name}+sha384sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sha384sum-devel

This package contains library source intended for building other packages which
use the "sha384sum" feature of the "%{crate}" crate.

%package     -n %{name}+sha512sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sha512sum-devel

This package contains library source intended for building other packages which
use the "sha512sum" feature of the "%{crate}" crate.

%package     -n %{name}+shred-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+shred-devel

This package contains library source intended for building other packages which
use the "shred" feature of the "%{crate}" crate.

%package     -n %{name}+shuf-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+shuf-devel

This package contains library source intended for building other packages which
use the "shuf" feature of the "%{crate}" crate.

%package     -n %{name}+sleep-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sleep-devel

This package contains library source intended for building other packages which
use the "sleep" feature of the "%{crate}" crate.

%package     -n %{name}+sort-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sort-devel

This package contains library source intended for building other packages which
use the "sort" feature of the "%{crate}" crate.

%package     -n %{name}+split-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+split-devel

This package contains library source intended for building other packages which
use the "split" feature of the "%{crate}" crate.

%package     -n %{name}+stat-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+stat-devel

This package contains library source intended for building other packages which
use the "stat" feature of the "%{crate}" crate.

%package     -n %{name}+stdbuf-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+stdbuf-devel

This package contains library source intended for building other packages which
use the "stdbuf" feature of the "%{crate}" crate.

%package     -n %{name}+stty-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+stty-devel

This package contains library source intended for building other packages which
use the "stty" feature of the "%{crate}" crate.

%package     -n %{name}+sum-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sum-devel

This package contains library source intended for building other packages which
use the "sum" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+tac-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+tac-devel

This package contains library source intended for building other packages which
use the "tac" feature of the "%{crate}" crate.

%package     -n %{name}+tail-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+tail-devel

This package contains library source intended for building other packages which
use the "tail" feature of the "%{crate}" crate.

%package     -n %{name}+tee-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+tee-devel

This package contains library source intended for building other packages which
use the "tee" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%package     -n %{name}+test_risky_names-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+test_risky_names-devel

This package contains library source intended for building other packages which
use the "test_risky_names" feature of the "%{crate}" crate.

%package     -n %{name}+timeout-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+timeout-devel

This package contains library source intended for building other packages which
use the "timeout" feature of the "%{crate}" crate.

%package     -n %{name}+touch-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+touch-devel

This package contains library source intended for building other packages which
use the "touch" feature of the "%{crate}" crate.

%package     -n %{name}+tr-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+tr-devel

This package contains library source intended for building other packages which
use the "tr" feature of the "%{crate}" crate.

%package     -n %{name}+true-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+true-devel

This package contains library source intended for building other packages which
use the "true" feature of the "%{crate}" crate.

%package     -n %{name}+truncate-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+truncate-devel

This package contains library source intended for building other packages which
use the "truncate" feature of the "%{crate}" crate.

%package     -n %{name}+tsort-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+tsort-devel

This package contains library source intended for building other packages which
use the "tsort" feature of the "%{crate}" crate.

%package     -n %{name}+tty-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+tty-devel

This package contains library source intended for building other packages which
use the "tty" feature of the "%{crate}" crate.

%package     -n %{name}+uname-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+uname-devel

This package contains library source intended for building other packages which
use the "uname" feature of the "%{crate}" crate.

%package     -n %{name}+unexpand-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+unexpand-devel

This package contains library source intended for building other packages which
use the "unexpand" feature of the "%{crate}" crate.

%package     -n %{name}+uniq-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+uniq-devel

This package contains library source intended for building other packages which
use the "uniq" feature of the "%{crate}" crate.

%package     -n %{name}+unix-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+unix-devel

This package contains library source intended for building other packages which
use the "unix" feature of the "%{crate}" crate.

%package     -n %{name}+unlink-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+unlink-devel

This package contains library source intended for building other packages which
use the "unlink" feature of the "%{crate}" crate.

%package     -n %{name}+uptime-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+uptime-devel

This package contains library source intended for building other packages which
use the "uptime" feature of the "%{crate}" crate.

%package     -n %{name}+users-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+users-devel

This package contains library source intended for building other packages which
use the "users" feature of the "%{crate}" crate.

%package     -n %{name}+uu_test-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+uu_test-devel

This package contains library source intended for building other packages which
use the "uu_test" feature of the "%{crate}" crate.

%package     -n %{name}+uudoc-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+uudoc-devel

This package contains library source intended for building other packages which
use the "uudoc" feature of the "%{crate}" crate.

%package     -n %{name}+vdir-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+vdir-devel

This package contains library source intended for building other packages which
use the "vdir" feature of the "%{crate}" crate.

%package     -n %{name}+wc-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+wc-devel

This package contains library source intended for building other packages which
use the "wc" feature of the "%{crate}" crate.

%package     -n %{name}+who-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+who-devel

This package contains library source intended for building other packages which
use the "who" feature of the "%{crate}" crate.

%package     -n %{name}+whoami-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+whoami-devel

This package contains library source intended for building other packages which
use the "whoami" feature of the "%{crate}" crate.

%package     -n %{name}+windows-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+windows-devel

This package contains library source intended for building other packages which
use the "windows" feature of the "%{crate}" crate.

%package     -n %{name}+yes-devel
Summary:        coreutils ~ GNU coreutils reimplementation in Rust
BuildArch:      noarch
%description -n %{name}+yes-devel

This package contains library source intended for building other packages which
use the "yes" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f feat_acl,feat_os_unix,feat_selinux,feat_systemd_logind,uudoc
%{cargo_license_summary -f feat_acl,feat_os_unix,feat_selinux,feat_systemd_logind,uudoc}
%{cargo_license -f feat_acl,feat_os_unix,feat_selinux,feat_systemd_logind,uudoc} > LICENSE.dependencies
mkdir -p data/man/man1
mkdir -p data/completions/{bash,fish,zsh}
for utility in $(target/rpm/coreutils --list); do
  target/release/uudoc manpage $utility > data/man/man1/uu_${utility}.1
  for s in bash zsh; do
    target/release/uudoc completion $utility $s > data/completions/$s/uu_${utility}
  done
  target/release/uudoc completion $utility fish > data/completions/fish/uu_${utility}.fish
done
target/release/uudoc manpage coreutils > data/man/man1/uutils-coreutils.1
for s in bash zsh; do
  target/release/uudoc completion coreutils $s > data/completions/$s/uutils-coreutils
done
target/release/uudoc completion coreutils fish > data/completions/fish/uutils-coreutils.fish
%install
%cargo_install -f feat_acl,feat_os_unix,feat_selinux,feat_systemd_logind,uudoc
mv %{buildroot}/%{_bindir}/coreutils %{buildroot}/%{_bindir}/uutils-coreutils
for utility in $(target/rpm/coreutils --list); do
  ln -sr %{buildroot}%{_bindir}/uutils-coreutils  %{buildroot}%{_bindir}/uu_$utility
done
mkdir -p %{buildroot}%{_mandir}/man1
cp -p data/man/man1/* %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
cp -p data/completions/bash/* %{buildroot}%{bash_completions_dir}/
cp -p data/completions/fish/* %{buildroot}%{fish_completions_dir}/
cp -p data/completions/zsh/* %{buildroot}%{zsh_completions_dir}/
rm -rf %{buildroot}%{crate_instdir}/tests
rm %{buildroot}%{_bindir}/uudoc
%oreon_autofiles uutils-coreutils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -f feat_acl,feat_os_unix,feat_selinux,feat_systemd_logind,uudoc -- -- %{shrink:
    --skip common::util::tests::test_compare_xattrs
    --skip test_chcon::
    --skip test_runcon::
    --skip test_cp::test_copy_dir_preserve_permissions
    --skip test_cp::test_copy_dir_preserve_permissions_inaccessible_file
    --skip test_cp::test_copy_dir_preserve_subdir_permissions
    --skip test_cp::test_copy_through_dangling_symlink_no_dereference_permissions
    --skip test_cp::test_cp_current_directory_preserve_attributes
    --skip test_cp::test_cp_debug_reflink_auto_sparse_always_non_sparse_file_with_long_zero_sequence
    --skip test_cp::test_cp_parents_2_dirs
    --skip test_cp::test_cp_parents_with_permissions_copy_dir
    --skip test_cp::test_cp_parents_with_permissions_copy_file
    --skip test_cp::test_cp_preserve_xattr
    --skip test_cp::test_cp_sparse_always_empty
    --skip test_cp::test_cp_sparse_always_non_empty
    --skip test_cp::test_preserve_hardlink_attributes_in_directory
    --skip test_cp::test_preserve_mode
    --skip test_df::test_exclude_all_types
    --skip test_df::test_file_column_width_if_filename_contains_unicode_chars
    --skip test_df::test_nonexistent_file
    --skip test_df::test_output_file_specific_files
    --skip test_df::test_output_mp_repeat
    --skip test_df::test_output_option_without_equals_sign
    --skip test_df::test_total_label_in_correct_column
    --skip test_df::test_type_option_with_file
    --skip test_du::test_du_dereference_args
    --skip test_du::test_du_no_dereference
    --skip test_env::test_env_french
    --skip test_ls::test_device_number
    --skip test_ls::test_localized_possible_values
    --skip test_ls::test_ls_allocation_size
    --skip test_ls::test_ls_inode
    --skip test_ls::test_ls_long_format
    --skip test_ls::test_ls_long_formats
%ifarch s390x
    --skip test_od::test_od_options_after_filename
    --skip test_od::test_suppress_duplicates
%endif
    --skip test_seq::test_count_down_floats
    --skip test_seq::test_float_precision_increment
    --skip test_seq::test_inf_width
    --skip test_seq::test_neg_inf_width
    --skip test_seq::test_separator_and_terminator_floats
    --skip test_seq::test_width_decimal_scientific_notation_increment
    --skip test_seq::test_width_decimal_scientific_notation_trailing_zeros_end
    --skip test_seq::test_width_decimal_scientific_notation_trailing_zeros_increment
    --skip test_seq::test_width_floats
    --skip test_seq::test_width_negative_zero_decimal_notation
    --skip test_seq::test_width_negative_zero_scientific_notation
    --skip test_sort::test_argument_suggestion
    --skip test_sort::test_clap_localization_help_message
    --skip test_sort::test_clap_localization_invalid_value
    --skip test_sort::test_clap_localization_unknown_argument
    --skip test_sort::test_error_colors_disabled
    --skip test_sort::test_error_colors_enabled
    --skip test_sort::test_french_translations
    --skip test_sort::test_help_colors_disabled
    --skip test_sort::test_help_colors_enabled
    --skip test_sort::test_keys_closed_range
    --skip test_sort::test_keys_multiple_ranges
    --skip test_sort::test_keys_no_field_match
    --skip test_sort::test_keys_open_ended
    --skip test_tail::test_follow_name_truncate4
    --skip test_tail::test_retry7
    --skip test_tail::test_retry9
    --skip test_error_messages_french_translation
    --skip test_french_colored_error_messages
    --skip test_help_messages_french_translation
    --skip uudoc_check_sums
    --skip uudoc_check_test
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n uutils-coreutils -f %{oreon_filedir}/uutils-coreutils.list
%files -n rust-coreutils-devel -f %{oreon_filedir}/rust-coreutils-devel.list

%changelog

%autochangelog
