%global source0_hash none

%global forgeurl https://github.com/jemalloc/jemalloc

Name:           jemalloc
Version:        5.3.1

Release:        1%{?dist}
Summary:        General-purpose scalable concurrent malloc implementation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://jemalloc.net/
VCS:            git:%{forgeurl}
Source0:        %{forgeurl}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  perl-generators
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
BuildRequires: make

%description
General-purpose scalable concurrent malloc(3) implementation.
This distribution is the stand-alone "portable" implementation of %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Override PAGESIZE, bz #1545539
%ifarch %ix86 %arm x86_64 s390x riscv64
%define lg_page --with-lg-page=12
%endif

%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Disable thp on systems not supporting this for now
%ifarch %ix86 %arm aarch64 s390x
%define disable_thp --disable-thp
%endif


%build
%if 0%{?rhel} && 0%{?rhel} < 7
export LDFLAGS="%{?__global_ldflags} -lrt"
%endif

%if 0%{?fedora} > 41
export CFLAGS="$CFLAGS -std=gnu17"
%endif

echo "For debugging package builders"
echo "What is the pagesize?"
getconf PAGESIZE

echo "What mm features are available?"
ls /sys/kernel/mm
ls /sys/kernel/mm/transparent_hugepage || true
cat /sys/kernel/mm/transparent_hugepage/enabled || true

echo "What kernel version and config is this?"
uname -a

%configure %{?disable_thp} %{?lg_page} --enable-prof
make %{?_smp_mflags}


%check
make %{?_smp_mflags} check


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# Install this with doc macro instead
rm %{buildroot}%{_datadir}/doc/%{name}/jemalloc.html

# None of these in fedora
find %{buildroot}%{_libdir}/ -name '*.a' -exec rm -vf {} ';'



%files
%{_libdir}/libjemalloc.so.*
%{_bindir}/jemalloc.sh
%doc COPYING README VERSION
%doc doc/jemalloc.html

%files devel
%{_includedir}/jemalloc
%{_bindir}/jemalloc-config
%{_libdir}/pkgconfig/jemalloc.pc
%{_bindir}/jeprof
%{_libdir}/libjemalloc.so
%{_mandir}/man3/jemalloc.3*

%ldconfig_scriptlets

%changelog
%autochangelog

