%global source0_hash a8038531f506a34ab4612b93f97d5f40759768cd34a83fd2af041b84fcbde474
%bcond check 1
%global debug_package %{nil}
%global crate uucore
Name:           rust-uucore
Version:        0.7.0
Release:        1%{?dist}
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
License:        MIT
URL:            https://crates.io/crates/uucore
Source0:        https://static.crates.io/crates/uucore/uucore-%{version}.crate
Patch:          uucore-fix-metadata-auto.diff
Patch:          uucore-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backup-control-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+backup-control-devel

This package contains library source intended for building other packages which
use the "backup-control" feature of the "%{crate}" crate.

%package     -n %{name}+base64-simd-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+base64-simd-devel

This package contains library source intended for building other packages which
use the "base64-simd" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+blake2b_simd-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+blake2b_simd-devel

This package contains library source intended for building other packages which
use the "blake2b_simd" feature of the "%{crate}" crate.

%package     -n %{name}+blake3-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+blake3-devel

This package contains library source intended for building other packages which
use the "blake3" feature of the "%{crate}" crate.

%package     -n %{name}+bstr-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+bstr-devel

This package contains library source intended for building other packages which
use the "bstr" feature of the "%{crate}" crate.

%package     -n %{name}+buf-copy-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+buf-copy-devel

This package contains library source intended for building other packages which
use the "buf-copy" feature of the "%{crate}" crate.

%package     -n %{name}+checksum-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+checksum-devel

This package contains library source intended for building other packages which
use the "checksum" feature of the "%{crate}" crate.

%package     -n %{name}+colors-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+colors-devel

This package contains library source intended for building other packages which
use the "colors" feature of the "%{crate}" crate.

%package     -n %{name}+crc-fast-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+crc-fast-devel

This package contains library source intended for building other packages which
use the "crc-fast" feature of the "%{crate}" crate.

%package     -n %{name}+data-encoding-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+data-encoding-devel

This package contains library source intended for building other packages which
use the "data-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+data-encoding-macro-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+data-encoding-macro-devel

This package contains library source intended for building other packages which
use the "data-encoding-macro" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+dns-lookup-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+dns-lookup-devel

This package contains library source intended for building other packages which
use the "dns-lookup" feature of the "%{crate}" crate.

%package     -n %{name}+dunce-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+dunce-devel

This package contains library source intended for building other packages which
use the "dunce" feature of the "%{crate}" crate.

%package     -n %{name}+encoding-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+encoding-devel

This package contains library source intended for building other packages which
use the "encoding" feature of the "%{crate}" crate.

%package     -n %{name}+entries-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+entries-devel

This package contains library source intended for building other packages which
use the "entries" feature of the "%{crate}" crate.

%package     -n %{name}+extendedbigdecimal-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+extendedbigdecimal-devel

This package contains library source intended for building other packages which
use the "extendedbigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+fast-inc-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+fast-inc-devel

This package contains library source intended for building other packages which
use the "fast-inc" feature of the "%{crate}" crate.

%package     -n %{name}+feat_systemd_logind-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+feat_systemd_logind-devel

This package contains library source intended for building other packages which
use the "feat_systemd_logind" feature of the "%{crate}" crate.

%package     -n %{name}+format-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+format-devel

This package contains library source intended for building other packages which
use the "format" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+fsext-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+fsext-devel

This package contains library source intended for building other packages which
use the "fsext" feature of the "%{crate}" crate.

%package     -n %{name}+fsxattr-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+fsxattr-devel

This package contains library source intended for building other packages which
use the "fsxattr" feature of the "%{crate}" crate.

%package     -n %{name}+glob-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+glob-devel

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%package     -n %{name}+hardware-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+hardware-devel

This package contains library source intended for building other packages which
use the "hardware" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-all-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+i18n-all-devel

This package contains library source intended for building other packages which
use the "i18n-all" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-charmap-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+i18n-charmap-devel

This package contains library source intended for building other packages which
use the "i18n-charmap" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-collator-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+i18n-collator-devel

This package contains library source intended for building other packages which
use the "i18n-collator" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-common-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+i18n-common-devel

This package contains library source intended for building other packages which
use the "i18n-common" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-datetime-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+i18n-datetime-devel

This package contains library source intended for building other packages which
use the "i18n-datetime" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-decimal-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+i18n-decimal-devel

This package contains library source intended for building other packages which
use the "i18n-decimal" feature of the "%{crate}" crate.

%package     -n %{name}+icu_calendar-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+icu_calendar-devel

This package contains library source intended for building other packages which
use the "icu_calendar" feature of the "%{crate}" crate.

%package     -n %{name}+icu_collator-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+icu_collator-devel

This package contains library source intended for building other packages which
use the "icu_collator" feature of the "%{crate}" crate.

%package     -n %{name}+icu_datetime-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+icu_datetime-devel

This package contains library source intended for building other packages which
use the "icu_datetime" feature of the "%{crate}" crate.

%package     -n %{name}+icu_decimal-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+icu_decimal-devel

This package contains library source intended for building other packages which
use the "icu_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+icu_locale-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+icu_locale-devel

This package contains library source intended for building other packages which
use the "icu_locale" feature of the "%{crate}" crate.

%package     -n %{name}+icu_provider-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+icu_provider-devel

This package contains library source intended for building other packages which
use the "icu_provider" feature of the "%{crate}" crate.

%package     -n %{name}+itertools-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+itertools-devel

This package contains library source intended for building other packages which
use the "itertools" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+jiff-devel

This package contains library source intended for building other packages which
use the "jiff" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-icu-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+jiff-icu-devel

This package contains library source intended for building other packages which
use the "jiff-icu" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+lines-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+lines-devel

This package contains library source intended for building other packages which
use the "lines" feature of the "%{crate}" crate.

%package     -n %{name}+md-5-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+md-5-devel

This package contains library source intended for building other packages which
use the "md-5" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+mode-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+mode-devel

This package contains library source intended for building other packages which
use the "mode" feature of the "%{crate}" crate.

%package     -n %{name}+num-traits-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+num-traits-devel

This package contains library source intended for building other packages which
use the "num-traits" feature of the "%{crate}" crate.

%package     -n %{name}+parser-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+parser-devel

This package contains library source intended for building other packages which
use the "parser" feature of the "%{crate}" crate.

%package     -n %{name}+parser-glob-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+parser-glob-devel

This package contains library source intended for building other packages which
use the "parser-glob" feature of the "%{crate}" crate.

%package     -n %{name}+parser-num-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+parser-num-devel

This package contains library source intended for building other packages which
use the "parser-num" feature of the "%{crate}" crate.

%package     -n %{name}+parser-size-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+parser-size-devel

This package contains library source intended for building other packages which
use the "parser-size" feature of the "%{crate}" crate.

%package     -n %{name}+perms-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+perms-devel

This package contains library source intended for building other packages which
use the "perms" feature of the "%{crate}" crate.

%package     -n %{name}+pipes-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+pipes-devel

This package contains library source intended for building other packages which
use the "pipes" feature of the "%{crate}" crate.

%package     -n %{name}+proc-info-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+proc-info-devel

This package contains library source intended for building other packages which
use the "proc-info" feature of the "%{crate}" crate.

%package     -n %{name}+process-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+process-devel

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%package     -n %{name}+procfs-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+procfs-devel

This package contains library source intended for building other packages which
use the "procfs" feature of the "%{crate}" crate.

%package     -n %{name}+quoting-style-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+quoting-style-devel

This package contains library source intended for building other packages which
use the "quoting-style" feature of the "%{crate}" crate.

%package     -n %{name}+ranges-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+ranges-devel

This package contains library source intended for building other packages which
use the "ranges" feature of the "%{crate}" crate.

%package     -n %{name}+ringbuffer-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+ringbuffer-devel

This package contains library source intended for building other packages which
use the "ringbuffer" feature of the "%{crate}" crate.

%package     -n %{name}+safe-traversal-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+safe-traversal-devel

This package contains library source intended for building other packages which
use the "safe-traversal" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+sha3-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+sha3-devel

This package contains library source intended for building other packages which
use the "sha3" feature of the "%{crate}" crate.

%package     -n %{name}+signals-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+signals-devel

This package contains library source intended for building other packages which
use the "signals" feature of the "%{crate}" crate.

%package     -n %{name}+sm3-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+sm3-devel

This package contains library source intended for building other packages which
use the "sm3" feature of the "%{crate}" crate.

%package     -n %{name}+smack-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+smack-devel

This package contains library source intended for building other packages which
use the "smack" feature of the "%{crate}" crate.

%package     -n %{name}+sum-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+sum-devel

This package contains library source intended for building other packages which
use the "sum" feature of the "%{crate}" crate.

%package     -n %{name}+tempfile-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+tempfile-devel

This package contains library source intended for building other packages which
use the "tempfile" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tty-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+tty-devel

This package contains library source intended for building other packages which
use the "tty" feature of the "%{crate}" crate.

%package     -n %{name}+unit-prefix-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+unit-prefix-devel

This package contains library source intended for building other packages which
use the "unit-prefix" feature of the "%{crate}" crate.

%package     -n %{name}+update-control-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+update-control-devel

This package contains library source intended for building other packages which
use the "update-control" feature of the "%{crate}" crate.

%package     -n %{name}+uptime-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+uptime-devel

This package contains library source intended for building other packages which
use the "uptime" feature of the "%{crate}" crate.

%package     -n %{name}+utf8-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+utf8-devel

This package contains library source intended for building other packages which
use the "utf8" feature of the "%{crate}" crate.

%package     -n %{name}+utmpx-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+utmpx-devel

This package contains library source intended for building other packages which
use the "utmpx" feature of the "%{crate}" crate.

%package     -n %{name}+version-cmp-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+version-cmp-devel

This package contains library source intended for building other packages which
use the "version-cmp" feature of the "%{crate}" crate.

%package     -n %{name}+walkdir-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+walkdir-devel

This package contains library source intended for building other packages which
use the "walkdir" feature of the "%{crate}" crate.

%package     -n %{name}+wide-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+wide-devel

This package contains library source intended for building other packages which
use the "wide" feature of the "%{crate}" crate.

%package     -n %{name}+xattr-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+xattr-devel

This package contains library source intended for building other packages which
use the "xattr" feature of the "%{crate}" crate.

%package     -n %{name}+z85-devel
Summary:        Uutils ~ 'core' uutils code library (cross-platform)
BuildArch:      noarch
%description -n %{name}+z85-devel

This package contains library source intended for building other packages which
use the "z85" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip mods::clap_localization::tests::test_french_localization
    --skip mods::locale::tests::test_setup_localization_fallback_to_embedded
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-uucore-devel -f %{oreon_filedir}/rust-uucore-devel.list

%changelog

%autochangelog
