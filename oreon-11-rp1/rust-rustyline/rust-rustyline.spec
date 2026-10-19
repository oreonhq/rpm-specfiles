%global source0_hash 53f6a737db68eb1a8ccff86b584b2fc13eca6a7bb6f78ebc7c529547e3ab9684
%bcond check 1
%global debug_package %{nil}
%global crate rustyline
Name:           rust-rustyline
Version:        18.0.1
Release:        1%{?dist}
Summary:        Readline implementation based on Antirez's Linenoise
License:        MIT
URL:            https://crates.io/crates/rustyline
Source0:        https://static.crates.io/crates/rustyline/rustyline-%{version}.crate
Patch:          rustyline-fix-metadata-auto.diff
Patch:          rustyline-fix-metadata.diff
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
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+case_insensitive_history_search-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+case_insensitive_history_search-devel

This package contains library source intended for building other packages which
use the "case_insensitive_history_search" feature of the "%{crate}" crate.

%package     -n %{name}+custom-bindings-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+custom-bindings-devel

This package contains library source intended for building other packages which
use the "custom-bindings" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+fd-lock-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+fd-lock-devel

This package contains library source intended for building other packages which
use the "fd-lock" feature of the "%{crate}" crate.

%package     -n %{name}+home-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+home-devel

This package contains library source intended for building other packages which
use the "home" feature of the "%{crate}" crate.

%package     -n %{name}+radix_trie-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+radix_trie-devel

This package contains library source intended for building other packages which
use the "radix_trie" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+rusqlite-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+rusqlite-devel

This package contains library source intended for building other packages which
use the "rusqlite" feature of the "%{crate}" crate.

%package     -n %{name}+rustyline-derive-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+rustyline-derive-devel

This package contains library source intended for building other packages which
use the "rustyline-derive" feature of the "%{crate}" crate.

%package     -n %{name}+signal-hook-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+signal-hook-devel

This package contains library source intended for building other packages which
use the "signal-hook" feature of the "%{crate}" crate.

%package     -n %{name}+termios-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+termios-devel

This package contains library source intended for building other packages which
use the "termios" feature of the "%{crate}" crate.

%package     -n %{name}+with-dirs-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+with-dirs-devel

This package contains library source intended for building other packages which
use the "with-dirs" feature of the "%{crate}" crate.

%package     -n %{name}+with-file-history-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+with-file-history-devel

This package contains library source intended for building other packages which
use the "with-file-history" feature of the "%{crate}" crate.

%package     -n %{name}+with-sqlite-history-devel
Summary:        Readline implementation based on Antirez's Linenoise
BuildArch:      noarch
%description -n %{name}+with-sqlite-history-devel

This package contains library source intended for building other packages which
use the "with-sqlite-history" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip binding::test::size_of_event
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rustyline-devel -f %{oreon_filedir}/rust-rustyline-devel.list

%changelog

%autochangelog
