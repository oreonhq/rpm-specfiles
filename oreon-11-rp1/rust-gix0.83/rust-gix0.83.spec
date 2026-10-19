%global source0_hash 6ce52001b946a6249d5d0d3011df0a042ac3f8a4d013460db6476577b0b9c567
%bcond check 0
%global debug_package %{nil}
%global crate gix
Name:           rust-gix0.83
Version:        0.83.0
Release:        1%{?dist}
Summary:        Interact with git repositories just like git would
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix
Source0:        https://static.crates.io/crates/gix/gix-%{version}.crate
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
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-network-client-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+async-network-client-devel

This package contains library source intended for building other packages which
use the "async-network-client" feature of the "%{crate}" crate.

%package     -n %{name}+async-network-client-async-std-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+async-network-client-async-std-devel

This package contains library source intended for building other packages which
use the "async-network-client-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+attributes-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+attributes-devel

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%package     -n %{name}+auto-chain-error-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+auto-chain-error-devel

This package contains library source intended for building other packages which
use the "auto-chain-error" feature of the "%{crate}" crate.

%package     -n %{name}+basic-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+basic-devel

This package contains library source intended for building other packages which
use the "basic" feature of the "%{crate}" crate.

%package     -n %{name}+blame-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blame-devel

This package contains library source intended for building other packages which
use the "blame" feature of the "%{crate}" crate.

%package     -n %{name}+blob-diff-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blob-diff-devel

This package contains library source intended for building other packages which
use the "blob-diff" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-curl-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-curl-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-curl" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-curl-openssl-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-curl-openssl-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-curl-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-curl-rustls-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-curl-rustls-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-curl-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-reqwest-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-reqwest-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-reqwest-native-tls-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-reqwest-native-tls-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-reqwest-rust-tls-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest-rust-tls" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns-devel

This package contains library source intended for building other packages which
use the "blocking-http-transport-reqwest-rust-tls-trust-dns" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-network-client-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+blocking-network-client-devel

This package contains library source intended for building other packages which
use the "blocking-network-client" feature of the "%{crate}" crate.

%package     -n %{name}+cache-efficiency-debug-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+cache-efficiency-debug-devel

This package contains library source intended for building other packages which
use the "cache-efficiency-debug" feature of the "%{crate}" crate.

%package     -n %{name}+comfort-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+comfort-devel

This package contains library source intended for building other packages which
use the "comfort" feature of the "%{crate}" crate.

%package     -n %{name}+command-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+command-devel

This package contains library source intended for building other packages which
use the "command" feature of the "%{crate}" crate.

%package     -n %{name}+credentials-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+credentials-devel

This package contains library source intended for building other packages which
use the "credentials" feature of the "%{crate}" crate.

%package     -n %{name}+dirwalk-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+dirwalk-devel

This package contains library source intended for building other packages which
use the "dirwalk" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+excludes-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+excludes-devel

This package contains library source intended for building other packages which
use the "excludes" feature of the "%{crate}" crate.

%package     -n %{name}+extras-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+extras-devel

This package contains library source intended for building other packages which
use the "extras" feature of the "%{crate}" crate.

%package     -n %{name}+gix-archive-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-archive-devel

This package contains library source intended for building other packages which
use the "gix-archive" feature of the "%{crate}" crate.

%package     -n %{name}+gix-attributes-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-attributes-devel

This package contains library source intended for building other packages which
use the "gix-attributes" feature of the "%{crate}" crate.

%package     -n %{name}+gix-blame-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-blame-devel

This package contains library source intended for building other packages which
use the "gix-blame" feature of the "%{crate}" crate.

%package     -n %{name}+gix-command-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-command-devel

This package contains library source intended for building other packages which
use the "gix-command" feature of the "%{crate}" crate.

%package     -n %{name}+gix-credentials-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-credentials-devel

This package contains library source intended for building other packages which
use the "gix-credentials" feature of the "%{crate}" crate.

%package     -n %{name}+gix-dir-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-dir-devel

This package contains library source intended for building other packages which
use the "gix-dir" feature of the "%{crate}" crate.

%package     -n %{name}+gix-filter-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-filter-devel

This package contains library source intended for building other packages which
use the "gix-filter" feature of the "%{crate}" crate.

%package     -n %{name}+gix-ignore-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-ignore-devel

This package contains library source intended for building other packages which
use the "gix-ignore" feature of the "%{crate}" crate.

%package     -n %{name}+gix-index-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-index-devel

This package contains library source intended for building other packages which
use the "gix-index" feature of the "%{crate}" crate.

%package     -n %{name}+gix-mailmap-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-mailmap-devel

This package contains library source intended for building other packages which
use the "gix-mailmap" feature of the "%{crate}" crate.

%package     -n %{name}+gix-merge-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-merge-devel

This package contains library source intended for building other packages which
use the "gix-merge" feature of the "%{crate}" crate.

%package     -n %{name}+gix-negotiate-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-negotiate-devel

This package contains library source intended for building other packages which
use the "gix-negotiate" feature of the "%{crate}" crate.

%package     -n %{name}+gix-pathspec-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-pathspec-devel

This package contains library source intended for building other packages which
use the "gix-pathspec" feature of the "%{crate}" crate.

%package     -n %{name}+gix-prompt-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-prompt-devel

This package contains library source intended for building other packages which
use the "gix-prompt" feature of the "%{crate}" crate.

%package     -n %{name}+gix-status-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-status-devel

This package contains library source intended for building other packages which
use the "gix-status" feature of the "%{crate}" crate.

%package     -n %{name}+gix-submodule-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-submodule-devel

This package contains library source intended for building other packages which
use the "gix-submodule" feature of the "%{crate}" crate.

%package     -n %{name}+gix-transport-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-transport-devel

This package contains library source intended for building other packages which
use the "gix-transport" feature of the "%{crate}" crate.

%package     -n %{name}+gix-worktree-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-worktree-devel

This package contains library source intended for building other packages which
use the "gix-worktree" feature of the "%{crate}" crate.

%package     -n %{name}+gix-worktree-state-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-worktree-state-devel

This package contains library source intended for building other packages which
use the "gix-worktree-state" feature of the "%{crate}" crate.

%package     -n %{name}+gix-worktree-stream-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-worktree-stream-devel

This package contains library source intended for building other packages which
use the "gix-worktree-stream" feature of the "%{crate}" crate.

%package     -n %{name}+hp-tempfile-registry-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+hp-tempfile-registry-devel

This package contains library source intended for building other packages which
use the "hp-tempfile-registry" feature of the "%{crate}" crate.

%package     -n %{name}+index-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+index-devel

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%package     -n %{name}+interrupt-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+interrupt-devel

This package contains library source intended for building other packages which
use the "interrupt" feature of the "%{crate}" crate.

%package     -n %{name}+mailmap-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+mailmap-devel

This package contains library source intended for building other packages which
use the "mailmap" feature of the "%{crate}" crate.

%package     -n %{name}+max-control-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+max-control-devel

This package contains library source intended for building other packages which
use the "max-control" feature of the "%{crate}" crate.

%package     -n %{name}+max-performance-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+max-performance-devel

This package contains library source intended for building other packages which
use the "max-performance" feature of the "%{crate}" crate.

%package     -n %{name}+max-performance-safe-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+max-performance-safe-devel

This package contains library source intended for building other packages which
use the "max-performance-safe" feature of the "%{crate}" crate.

%package     -n %{name}+merge-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+merge-devel

This package contains library source intended for building other packages which
use the "merge" feature of the "%{crate}" crate.

%package     -n %{name}+need-more-recent-msrv-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+need-more-recent-msrv-devel

This package contains library source intended for building other packages which
use the "need-more-recent-msrv" feature of the "%{crate}" crate.

%package     -n %{name}+pack-cache-lru-dynamic-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+pack-cache-lru-dynamic-devel

This package contains library source intended for building other packages which
use the "pack-cache-lru-dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+pack-cache-lru-static-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+pack-cache-lru-static-devel

This package contains library source intended for building other packages which
use the "pack-cache-lru-static" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+prodash-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+prodash-devel

This package contains library source intended for building other packages which
use the "prodash" feature of the "%{crate}" crate.

%package     -n %{name}+progress-tree-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+progress-tree-devel

This package contains library source intended for building other packages which
use the "progress-tree" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+revision-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+revision-devel

This package contains library source intended for building other packages which
use the "revision" feature of the "%{crate}" crate.

%package     -n %{name}+revparse-regex-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+revparse-regex-devel

This package contains library source intended for building other packages which
use the "revparse-regex" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

%package     -n %{name}+signal-hook-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+signal-hook-devel

This package contains library source intended for building other packages which
use the "signal-hook" feature of the "%{crate}" crate.

%package     -n %{name}+status-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+status-devel

This package contains library source intended for building other packages which
use the "status" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-detail-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+tracing-detail-devel

This package contains library source intended for building other packages which
use the "tracing-detail" feature of the "%{crate}" crate.

%package     -n %{name}+tree-editor-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+tree-editor-devel

This package contains library source intended for building other packages which
use the "tree-editor" feature of the "%{crate}" crate.

%package     -n %{name}+tree-error-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+tree-error-devel

This package contains library source intended for building other packages which
use the "tree-error" feature of the "%{crate}" crate.

%package     -n %{name}+worktree-archive-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+worktree-archive-devel

This package contains library source intended for building other packages which
use the "worktree-archive" feature of the "%{crate}" crate.

%package     -n %{name}+worktree-mutation-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+worktree-mutation-devel

This package contains library source intended for building other packages which
use the "worktree-mutation" feature of the "%{crate}" crate.

%package     -n %{name}+worktree-stream-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+worktree-stream-devel

This package contains library source intended for building other packages which
use the "worktree-stream" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+zlib-ng-devel

This package contains library source intended for building other packages which
use the "zlib-ng" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-compat-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+zlib-ng-compat-devel

This package contains library source intended for building other packages which
use the "zlib-ng-compat" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-rs-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+zlib-rs-devel

This package contains library source intended for building other packages which
use the "zlib-rs" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-stock-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+zlib-stock-devel

This package contains library source intended for building other packages which
use the "zlib-stock" feature of the "%{crate}" crate.

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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-gix0.83-devel -f %{oreon_filedir}/rust-gix0.83-devel.list

%changelog

%autochangelog
