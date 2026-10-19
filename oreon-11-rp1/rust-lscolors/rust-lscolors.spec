%global source0_hash d60e266dfb1426eb2d24792602e041131fdc0236bb7007abc0e589acafd60929
%bcond check 1
%global crate lscolors
Name:           rust-lscolors
Version:        0.21.0
Release:        1%{?dist}
Summary:        Colorize paths using the LS_COLORS environment variable
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lscolors
Source0:        https://static.crates.io/crates/lscolors/lscolors-%{version}.crate
Source10:       lscolors.1
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Colorize paths using the LS_COLORS environment variable
License:        MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Colorize paths using the LS_COLORS environment variable
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi_term-devel
Summary:        Colorize paths using the LS_COLORS environment variable
BuildArch:      noarch
%description -n %{name}+ansi_term-devel

This package contains library source intended for building other packages which
use the "ansi_term" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        Colorize paths using the LS_COLORS environment variable
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+gnu_legacy-devel
Summary:        Colorize paths using the LS_COLORS environment variable
BuildArch:      noarch
%description -n %{name}+gnu_legacy-devel

This package contains library source intended for building other packages which
use the "gnu_legacy" feature of the "%{crate}" crate.

%package     -n %{name}+nu-ansi-term-devel
Summary:        Colorize paths using the LS_COLORS environment variable
BuildArch:      noarch
%description -n %{name}+nu-ansi-term-devel

This package contains library source intended for building other packages which
use the "nu-ansi-term" feature of the "%{crate}" crate.

%package     -n %{name}+owo-colors-devel
Summary:        Colorize paths using the LS_COLORS environment variable
BuildArch:      noarch
%description -n %{name}+owo-colors-devel

This package contains library source intended for building other packages which
use the "owo-colors" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE10}'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n lscolors -f %{oreon_filedir}/lscolors.list
%files -n rust-lscolors-devel -f %{oreon_filedir}/rust-lscolors-devel.list

%changelog

%autochangelog
