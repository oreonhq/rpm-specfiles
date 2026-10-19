%global source0_hash d13d90951308b5b5f2d182d064360dc48bb73b7786163a5ac2e524822ae90a5b
Name:           retis
Version:        1.7.0
Release:        1%{?dist}
Summary:        Tracing packets in the Linux networking stack
License:        GPL-2.0-only
URL:            https://github.com/retis-org/retis
Source0:        https://github.com/retis-org/retis/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          retis-release-profile.diff
Patch:          retis-fix-deps.diff
Patch:          retis-downgrade-elf.diff
ExclusiveArch:  x86_64 aarch64
Requires:       python3
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
Tracing packets in the Linux networking stack, using eBPF and interfacing with
control and data paths such as OpenVSwitch.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

make release %{?_smp_mflags}
%install
env CARGO_INSTALL_OPTS="--no-track" make install
install -m 0755 -d %{buildroot}%{_datadir}/retis/profiles
install -m 0644 retis/profiles/* %{buildroot}%{_datadir}/retis/profiles
rm -rf %{buildroot}/include
rm -rf %{buildroot}/pkgconfig
rm -f %{buildroot}/libbpf.a
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
