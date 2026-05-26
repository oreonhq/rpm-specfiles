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
# oreon url source checksums begin
%global source0_sha256 989ed3c1a3db8ff0f7c08dd43953c6b9d0c3ac252653a48d566aaedf98bc80ca
%global source0_file v1.6.3.tar.gz
%global source1_sha256 69467234c3c009952fea99dd057e5200160603c7e3e04ecb74458e29746e5b95
%global source1_file usdt-0.1.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v1.6.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "989ed3c1a3db8ff0f7c08dd43953c6b9d0c3ac252653a48d566aaedf98bc80ca" || { echo "oreon: Source0 SHA256 mismatch for v1.6.3.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/usdt-0.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "69467234c3c009952fea99dd057e5200160603c7e3e04ecb74458e29746e5b95" || { echo "oreon: Source1 SHA256 mismatch for usdt-0.1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
