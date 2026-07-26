%global source0_hash e8ee79b1f399b2d167e6a90de52ccc90e52408f7ade1b9b7135727efe181347f

Summary:       System performance benchmark
Name:          sysbench
Version:       1.0.20
Release:       20%{?dist}
License:       GPL-2.0-or-later
URL:           https://github.com/akopytov/sysbench/
Source0:       https://github.com/akopytov/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/akopytov/sysbench/pull/379
Patch0:        sysbench-1.0.20-python3.patch
# egrep is deprecated, use grep -E instead in order to fix build on F38+
Patch1:        sysbench-1.0.20-fix_deprecated_egrep_call.patch

BuildRequires: make
BuildRequires: automake
BuildRequires: ck-devel
BuildRequires: docbook-style-xsl
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: luajit-devel
BuildRequires: mariadb-connector-c-devel
BuildRequires: libpq-devel
# Tests
BuildRequires: /usr/bin/cram
BuildRequires: python3

# luajit is needed but is not available for all arches.
# Use the same arches as luajit.
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
ExcludeArch:    riscv64 ppc64 ppc64le
%else
ExcludeArch:    riscv64 ppc64 ppc64le s390x
%endif

%description
SysBench is a modular, cross-platform and multi-threaded benchmark
tool for evaluating OS parameters that are important for a system
running a database under intensive load.

The idea of this benchmark suite is to quickly get an impression about
system performance without setting up complex database benchmarks or
even without installing a database at all. Current features allow to
test the following system parameters:
- file I/O performance
- scheduler performance
- memory allocation and transfer speed
- POSIX threads implementation performance
- database server performance (OLTP benchmark)

Primarily written for MySQL server benchmarking, SysBench will be
further extended to support multiple database backends, distributed
benchmarks and third-party plug-in modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
rm -r third_party/luajit/luajit/
rm -r third_party/concurrency_kit/ck/
rm -r third_party/cram/

%build
export CFLAGS="%{optflags}"
autoreconf -vif
%configure --with-mysql \
           --with-pgsql \
           --with-system-ck \
           --with-system-luajit \
           --without-gcc-arch

%make_build

%install
%make_install
mv %{buildroot}%{_docdir}/sysbench/manual.html .

%check
cd tests
./test_run.sh

%files
%license COPYING
%doc ChangeLog README.md manual.html
%{_bindir}/*
%{_datadir}/%{name}

%changelog
%autochangelog
