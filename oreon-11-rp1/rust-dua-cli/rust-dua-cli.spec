%global source0_hash f880a083145f39b809a389b12ae4650dfe17499be42d833e10e748f96a9ebe5d
%bcond check 0
%global crate dua-cli
Name:           rust-dua-cli
Version:        2.45.0
Release:        1%{?dist}
Summary:        Tool to conveniently learn about the disk usage of directories
License:        MIT
URL:            https://crates.io/crates/dua-cli
Source0:        https://static.crates.io/crates/dua-cli/dua-cli-%{version}.crate
Patch:          dua-cli-fix-metadata.diff
Patch11:        dua-cli-2.32.2-no-atty.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool to conveniently learn about the disk usage of directories
License:        %{shrink:
    MIT AND
    Unicode-3.0 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT) AND
    Zlib
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crosstermion-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+crosstermion-devel

This package contains library source intended for building other packages which
use the "crosstermion" feature of the "%{crate}" crate.

%package     -n %{name}+open-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+open-devel

This package contains library source intended for building other packages which
use the "open" feature of the "%{crate}" crate.

%package     -n %{name}+trash-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+trash-devel

This package contains library source intended for building other packages which
use the "trash" feature of the "%{crate}" crate.

%package     -n %{name}+trash-move-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+trash-move-devel

This package contains library source intended for building other packages which
use the "trash-move" feature of the "%{crate}" crate.

%package     -n %{name}+tui-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+tui-devel

This package contains library source intended for building other packages which
use the "tui" feature of the "%{crate}" crate.

%package     -n %{name}+tui-crossplatform-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+tui-crossplatform-devel

This package contains library source intended for building other packages which
use the "tui-crossplatform" feature of the "%{crate}" crate.

%package     -n %{name}+tui-react-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+tui-react-devel

This package contains library source intended for building other packages which
use the "tui-react" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segmentation-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+unicode-segmentation-devel

This package contains library source intended for building other packages which
use the "unicode-segmentation" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-width-devel
Summary:        Tool to conveniently learn about the disk usage of directories
BuildArch:      noarch
%description -n %{name}+unicode-width-devel

This package contains library source intended for building other packages which
use the "unicode-width" feature of the "%{crate}" crate.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n dua-cli -f %{oreon_filedir}/dua-cli.list
%files -n rust-dua-cli-devel -f %{oreon_filedir}/rust-dua-cli-devel.list

%changelog

%autochangelog
