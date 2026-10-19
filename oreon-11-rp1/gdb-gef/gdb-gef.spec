%global source0_hash 113a07c43c55d26005d78e0e1f988c16405aa27c388fe82a2ad727b7699d7e87
%bcond_without  check
%global forgeurl https://github.com/hugsy/gef
Name:           gdb-gef
Version:        2025.01
%global tag %{version}
%forgemeta
Release:        1%{?dist}
Summary:        GEF (GDB Enhanced Features)
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/gef-%{version}.tar.gz
Source1:        gdb-gef
Patch0:         gef-got-audit.patch
Patch1:         gef-gcc15.patch
Patch2:         gef-tcache-mark.patch
BuildArch:      noarch
ExclusiveArch:  x86_64
Requires:       gdb
Requires:       file
Requires:       binutils
Requires:       procps-ng
%if %{with check}
%endif
# oreon:deps
BuildRequires:  binutils
BuildRequires:  file
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gdb-gdbserver
BuildRequires:  git
BuildRequires:  make
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  python3-coverage
BuildRequires:  python3-pylint
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-requests
BuildRequires:  python3-rpyc
BuildRequires:  qemu-user
BuildRequires:  sed
# /oreon:deps
%description
GEF (pronounced ʤɛf - "Jeff") is a set of commands for x86/64, ARM,
MIPS, PowerPC and SPARC to assist exploit developers and
reverse-engineers when using old school GDB. It provides additional
features to GDB using the Python API to assist during the process of
dynamic analysis and exploit development. Application developers will
also benefit from it, as GEF lifts a great part of regular GDB
obscurity, avoiding repeating traditional commands, or bringing out
the relevant information from the debugging runtime.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build

%install
mkdir -p %{buildroot}/%{_datadir}/gdb
cp gef.py %{buildroot}/%{_datadir}/gdb/gef.py
sed -e "s:@datadir@:%{_datadir}:g" < %{SOURCE1} > %{SOURCE1}.sh
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE1}.sh %{buildroot}/%{_bindir}/gdb-gef
%oreon_autofiles main
%if %{with check}
%check

make -C tests/binaries
python3 -m pytest -v -m "not benchmark and not online and not tcache" tests/
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
