%global source0_hash 989ed3c1a3db8ff0f7c08dd43953c6b9d0c3ac252653a48d566aaedf98bc80ca
%global source1_hash 69467234c3c009952fea99dd057e5200160603c7e3e04ecb74458e29746e5b95

%global githubname   libbpf
%global githubver    1.6.3
%global githubfull   %{githubname}-%{githubver}
%global libver       1.6.3

%global usdtname     usdt
%global usdtver      0.1.0
%global usdtref      f4ea2f524efa80d062f4d586d78daafb83dc7d24

Name:           %{githubname}
Version:        %{githubver}
Release:        2%{?dist}
Summary:        Libbpf library

License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://github.com/%{githubname}/%{githubname}
Source0:        https://github.com/%{githubname}/%{githubname}/archive/v%{githubver}.tar.gz
Source1:        https://github.com/%{githubname}/usdt/archive/%{usdtref}/%{usdtname}-%{usdtver}.tar.gz

BuildRequires:  gcc elfutils-libelf-devel elfutils-devel
BuildRequires: make

Patch1:         libbpf-Add-the-ability-to-suppress-perf-event-enable.patch
Patch2:         libbpf-sync-bpf_stream_vprintk-declaration-with-kern.patch

# This package supersedes libbpf from kernel-tools,
# which has default Epoch: 0. By having Epoch: > 0
# this libbpf will take over smoothly
Epoch:          2

%description
A mirror of bpf-next linux tree bpf-next/tools/lib/bpf directory plus its
supporting header files. The version of the package reflects the version of
ABI.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = 2:%{version}-%{release}
Requires:       kernel-headers >= 5.16.0
Requires:       zlib

%description devel
The %{name}-devel package contains libraries header files for
developing applications that use %{name}

%package static
Summary: Static library for libbpf development
Requires: %{name}-devel = 2:%{version}-%{release}

%description static
The %{name}-static package contains static library for
developing applications that use %{name}

%package usdt-devel
Summary:        The header for defining USDTs
Version:        %{usdtver}
Release:        4%{?dist}
BuildArch:      noarch

%description usdt-devel
A single-header library which defines a collection of macros for defining and
triggering USDTs (User Statically-Defined Tracepoints).

%define _lto_cflags %{nil}

%global make_flags PREFIX=%{_prefix} INCLUDEDIR=%{_includedir} DESTDIR=%{buildroot} \
	OBJDIR=%{_builddir} CFLAGS="%{build_cflags} -fPIC" LDFLAGS="%{build_ldflags} \
	-Wl,--no-as-needed" LIBDIR=/%{_libdir} NO_PKG_CONFIG=1

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{githubfull} -p1 -a1

%build
%make_build -C ./src %{make_flags}

%install
%make_install -C ./src %{make_flags}
install -D -m644 usdt-%{usdtref}/usdt.h %{buildroot}%{_includedir}/%{usdtname}/usdt.h

%files
%{_libdir}/libbpf.so.%{libver}
%{_libdir}/libbpf.so.1

%files devel
%{_libdir}/libbpf.so
%{_includedir}/bpf/
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%files usdt-devel
%{_includedir}/%{usdtname}/usdt.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{githubver}-2
- Prepare for Oreon 11 (RP1)
