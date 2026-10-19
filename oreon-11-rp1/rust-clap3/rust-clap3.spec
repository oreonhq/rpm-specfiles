%global source0_hash 4ea181bf566f71cb9a5d17a59e1871af638180a18fb0035c92ae62b705207123
%bcond check 0
%global debug_package %{nil}
%global crate clap
Name:           rust-clap3
Version:        3.2.25
Release:        1%{?dist}
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap
Source0:        https://static.crates.io/crates/clap/clap-%{version}.crate
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
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+atty-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+atty-devel

This package contains library source intended for building other packages which
use the "atty" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+cargo-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+cargo-devel

This package contains library source intended for building other packages which
use the "cargo" feature of the "%{crate}" crate.

%package     -n %{name}+clap_derive-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+clap_derive-devel

This package contains library source intended for building other packages which
use the "clap_derive" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+deprecated-devel

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+env-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+env-devel

This package contains library source intended for building other packages which
use the "env" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+strsim-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+strsim-devel

This package contains library source intended for building other packages which
use the "strsim" feature of the "%{crate}" crate.

%package     -n %{name}+suggestions-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+suggestions-devel

This package contains library source intended for building other packages which
use the "suggestions" feature of the "%{crate}" crate.

%package     -n %{name}+termcolor-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+termcolor-devel

This package contains library source intended for building other packages which
use the "termcolor" feature of the "%{crate}" crate.

%package     -n %{name}+terminal_size-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+terminal_size-devel

This package contains library source intended for building other packages which
use the "terminal_size" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-doc-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unstable-doc-devel

This package contains library source intended for building other packages which
use the "unstable-doc" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-grouped-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unstable-grouped-devel

This package contains library source intended for building other packages which
use the "unstable-grouped" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-replace-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unstable-replace-devel

This package contains library source intended for building other packages which
use the "unstable-replace" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-v4-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+unstable-v4-devel

This package contains library source intended for building other packages which
use the "unstable-v4" feature of the "%{crate}" crate.

%package     -n %{name}+wrap_help-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+wrap_help-devel

This package contains library source intended for building other packages which
use the "wrap_help" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-rust-devel
Summary:        A simple to use, efficient, and full-featured Command Line Argument P...
BuildArch:      noarch
%description -n %{name}+yaml-rust-devel

This package contains library source intended for building other packages which
use the "yaml-rust" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
rm -f %{buildroot}%{_bindir}/stdio-fixture
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-clap3-devel -f %{oreon_filedir}/rust-clap3-devel.list

%changelog

%autochangelog
