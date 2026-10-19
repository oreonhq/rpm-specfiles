%global source10_hash 460ccfcdcc9c3877b9f7fae1dfd4f2a3f93d3b2a2af3e3b62ca32b163f923cca
%global source0_hash 52a88e3e5c2ad82e691b219e2b45a90eb5a51d26a434c7e191563e957a48e07a
%bcond check 1
%global crate oxipng
Name:           rust-oxipng
Version:        10.2.1
Release:        1%{?dist}
Summary:        Lossless PNG compression optimizer
License:        MIT
URL:            https://crates.io/crates/oxipng
Source0:        https://static.crates.io/crates/oxipng/oxipng-%{version}.crate
Source10:       https://github.com/shssoichiro/oxipng/archive/v%{version}/oxipng-%{version}.tar.gz
Patch:          oxipng-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Lossless PNG compression optimizer
License:        %{shrink:
                Apache-2.0 AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                MIT AND
                (Zlib OR Apache-2.0 OR MIT)
                }
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+binary-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+binary-devel

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%package     -n %{name}+freestanding-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+freestanding-devel

This package contains library source intended for building other packages which
use the "freestanding" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+sanity-checks-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+sanity-checks-devel

This package contains library source intended for building other packages which
use the "sanity-checks" feature of the "%{crate}" crate.

%package     -n %{name}+system-libdeflate-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+system-libdeflate-devel

This package contains library source intended for building other packages which
use the "system-libdeflate" feature of the "%{crate}" crate.

%package     -n %{name}+zopfli-devel
Summary:        Lossless PNG compression optimizer
BuildArch:      noarch
%description -n %{name}+zopfli-devel

This package contains library source intended for building other packages which
use the "zopfli" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tar -xzvf '%{SOURCE10}' --strip-components=1 oxipng-%{version}/xtask
rm xtask/Cargo.lock
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{__cargo} run --manifest-path xtask/Cargo.toml -- mangen
%install
%cargo_install
mansrc='target/xtask/mangen/manpages/oxipng.1'
mandest='%{buildroot}%{_mandir}/man1'
install -t "${mandest}" -D -p -m 0644 "${mansrc}"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

tar -xzvf '%{SOURCE10}' --strip-components=1 oxipng-%{version}/tests
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n oxipng -f %{oreon_filedir}/oxipng.list
%files -n rust-oxipng-devel -f %{oreon_filedir}/rust-oxipng-devel.list

%changelog

%autochangelog
