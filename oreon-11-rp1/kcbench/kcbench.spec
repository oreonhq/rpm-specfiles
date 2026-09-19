%global source0_hash cf17c207dacd61f2b891a463eb29bbda43c249d3cb6574fdc08644e59041948d

Name:           kcbench
Version:        0.9.15
Release:        1%{?dist}
Summary:        Benchmark that compiles a Linux kernel

License:        MIT
URL:            https://gitlab.com/knurd42/kcbench
Source0:        https://gitlab.com/knurd42/kcbench/-/archive/v%{version}/kcbench-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  make

# needed for compiling a modern Linux kernels:
Requires:       make
Requires:       gcc
Requires:       binutils
Requires:       bison
Requires:       flex
Requires:       %{_bindir}/awk
Requires:       %{_bindir}/time
Requires:       %{_bindir}/bc
Requires:       %{_bindir}/lscpu
Requires:       %{_bindir}/pkill
Requires:       /usr/bin/pkg-config
Requires:       elfutils-libelf-devel
Requires:       openssl-devel
Requires:       curl
Requires:       perl-interpreter

%description
Compiles a Linux kernel to benchmark a system or test its stability.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
%{make_install} PREFIX=/usr/

%files
%{_bindir}/kcbench
%{_bindir}/kcbenchrate
%{_mandir}/man1/*
%{_docdir}/kcbench/

%changelog
%autochangelog
