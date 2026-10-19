%global source0_hash 200776fac271093e7c2f21edd6d62657ecd2be578d9328633f2a86bfa6ef4f1d
%global forgeurl https://github.com/jemalloc/jemalloc
Name:           jemalloc
Version:        5.4.0
Release:        1%{?dist}
Summary:        General-purpose scalable concurrent malloc implementation
License:        LicenseRef-Callaway-BSD
URL:            https://jemalloc.net/
VCS:            git:%{forgeurl}
Source0:        %{forgeurl}/releases/download/%{version}/%{name}-%{version}.tar.bz2
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
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
rm %{buildroot}%{_datadir}/doc/%{name}/jemalloc.html
find %{buildroot}%{_libdir}/ -name '*.a' -exec rm -vf {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n jemalloc-devel -f %{oreon_filedir}/jemalloc-devel.list

%changelog

%autochangelog

