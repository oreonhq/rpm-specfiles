%global source0_hash 00f2611719f0a1c9585965c6c3c1fe599119aa8e932a569041b1876ffc944fb3
Name:		qat-zstd-plugin
Version:	1.0.0
Release:        1%{?dist}
Summary:        Intel QuickAssist Technology ZSTD Plugin
License:	BSD-3-Clause
URL:		https://github.com/intel/QAT-ZSTD-Plugin
Source0:        https://github.com/intel/QAT-ZSTD-Plugin/archive/refs/tags/v1.0.0.tar.gz#/qat-zstd-plugin-1.0.0.tar.gz
Patch0:        test.patch
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  numactl-devel
BuildRequires:  qatlib-devel
# /oreon:deps
%description
Intel QuickAssist Technology ZSTD is a plugin to Zstandard for accelerating
compression by QAT. ZSTD* is a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level and better compression ratios.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description static
The %{name}-static package contains the static %{name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n QAT-ZSTD-Plugin-%{version}

# fedora/rhel path fixes
sed -i -e 's|/usr/local|%{_prefix}|g' src/Makefile
sed -i -e 's|$(PREFIX)/lib|%{_libdir}|g' src/Makefile
sed -i -e 's|$(PREFIX)/include|%{_includedir}|g' src/Makefile

%build

%make_build LDFLAGS="$LDFLAGS -lzstd"
make test
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test/test README.md
%files -f %{oreon_filedir}/main.list
%files -n qat-zstd-plugin-devel -f %{oreon_filedir}/qat-zstd-plugin-devel.list
%files -n qat-zstd-plugin-static -f %{oreon_filedir}/qat-zstd-plugin-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-1
- Import
