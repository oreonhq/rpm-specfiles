%global source0_hash 812a2a91b65cfca91cf9187eb8c829c376df2a0b1e8b6aae395c2575a670a160
%bcond check 1
%global cargo_install_lib 0
%global crate threecpio
Name:           rust-threecpio
Version:        0.14.0
Release:        1%{?dist}
Summary:        Manage initrd cpio archives
License:        ISC
URL:            https://crates.io/crates/threecpio
Source0:        https://static.crates.io/crates/threecpio/threecpio-%{version}.crate
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/asciidoctor
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  lz4
BuildRequires:  lzma
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n 3cpio
Summary:        Manage initrd cpio archives
License:        ISC AND MIT AND (MIT OR Apache-2.0)
%description -n 3cpio

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%if 0%{?__isa_bits} == 32
export RUST_LIBC_UNSTABLE_GNU_TIME_BITS=64
%endif
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
asciidoctor -b manpage man/3cpio.1.adoc
%install
%if 0%{?__isa_bits} == 32
export RUST_LIBC_UNSTABLE_GNU_TIME_BITS=64
%endif
%cargo_install
install -p -m 0644 -D -t '%{buildroot}%{_mandir}/man1' man/3cpio.1
%oreon_autofiles 3cpio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%if 0%{?__isa_bits} == 32
export RUST_LIBC_UNSTABLE_GNU_TIME_BITS=64
%endif
%cargo_test -- -- --skip test_file_from_line_location_character_device
%endif
%files -f %{oreon_filedir}/main.list
%files -n 3cpio -f %{oreon_filedir}/3cpio.list

%changelog

%autochangelog
