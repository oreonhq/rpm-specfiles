%global source0_hash 7d46a381f607432bdb5201a08b889924b6a4883bf09e8efca82a86a7d122cc97
Name:           bpftool
Version:        7.7.0
Release:        1%{?dist}
Summary:        Inspection and simple manipulation of eBPF programs and maps
%global libname libbpf
%global sources %{name}-%{libname}-v%{version}-sources
License:        GPL-2.0-only OR BSD-2-Clause
URL:            https://github.com/libbpf/bpftool
Source0:        https://github.com/%{libname}/%{name}/releases/download/v%{version}/%{sources}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  binutils-devel
BuildRequires:  clang
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  kernel-devel
BuildRequires:  libcap-devel
BuildRequires:  libzstd-devel
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  python3-docutils
# /oreon:deps
%description
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{sources}

%build

%make_build -C src/ bootstrap EXTRA_CFLAGS="%{build_cflags}" EXTRA_LDFLAGS="%{build_ldflags} -lzstd"
%install
install -D src/bootstrap/bpftool %{buildroot}%{_bindir}/bpftool
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
