%global source0_hash fdefc1465d8631807deaf504dacdeff628b978de515653b47976ca7c28ab2a7a
%bcond check 0
%global debug_package %{nil}
%global crate gix
Name:           rust-gix
Version:        0.87.1
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

%package     -n %{name}+gix-status-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+gix-status-devel

This package contains library source intended for building other packages which
use the "gix-status" feature of the "%{crate}" crate.

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

%package     -n %{name}+notes-devel
Summary:        Interact with git repositories just like git would
BuildArch:      noarch
%description -n %{name}+notes-devel

This package contains library source intended for building other packages which
use the "notes" feature of the "%{crate}" crate.

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

%prep
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
%files -n rust-gix-devel -f %{oreon_filedir}/rust-gix-devel.list

%changelog

%autochangelog
