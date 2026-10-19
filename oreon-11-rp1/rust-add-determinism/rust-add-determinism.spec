%global source0_hash c4e7290ec7ac71e8292fc71657e173ad4f50745b196391c648be2d994e3501b5
%bcond_without check
%global cargo_install_lib 0
%global crate add-determinism
Name:           rust-add-determinism
Version:        0.7.3
Release:        1%{?dist}
Summary:        RPM buildroot helper to make builds reproducible and hardlink identical files
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/add-determinism
Source0:        https://crates.io/api/v1/crates/add-determinism/0.7.3/download#/add-determinism-0.7.3.crate
Patch0:         add-determinism-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  selinux-policy-targeted
# /oreon:deps
%description

%package     -n %{crate}
Summary:        RPM buildroot helper to strip nondeterministic bits in files
License:        GPL-3.0-or-later AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

%package     -n linkdupes
Summary:      RPM buildroot helper to hardlink identical files
License:      GPL-3.0-or-later AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
%description -n linkdupes

%package     -n build-reproducibility-srpm-macros
Summary:     Configuration to integrate add-determinism in package builds
BuildArch:   noarch
Requires:    add-determinism = %{version}-%{release}
Requires:    linkdupes = %{version}-%{release}
Requires:    selinux-policy-any
Suggests:    selinux-policy-targeted
%description -n build-reproducibility-srpm-macros
%{summary}.

This package is intended to be pulled in by redhat-rpm-config.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} >LICENSE.dependencies
%install
%cargo_install -a
ln -s add-det %{buildroot}%{_bindir}/add-determinism
install -m0644 -Dt %{buildroot}%{rpmmacrodir} rpm/macros.build-reproducibility
%oreon_autofiles linkdupes usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles build-reproducibility-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -a
test "$(target/release/linkdupes --print-selinux-contexts /)" = "/ → system_u:object_r:root_t:s0"
%endif
%files -f %{oreon_filedir}/main.list
%files -n add-determinism -f %{oreon_filedir}/add-determinism.list
%files -n linkdupes -f %{oreon_filedir}/linkdupes.list
%files -n build-reproducibility-srpm-macros -f %{oreon_filedir}/build-reproducibility-srpm-macros.list

%changelog

* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.3-1
- Import from Fedora f44 dist-git for Oreon 11 provides build-reproducibility-srpm-macros
