# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f2672a0381cb59196e9c246bf8bcc43d5568bc457700a697f1a1df762b9af884
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:		numactl
Summary:	Library for tuning for Non Uniform Memory Access machines
Version:	2.0.19
Release:	4%{?dist}
# libnuma is LGPLv2 and GPLv2
# numactl binaries are GPLv2 only
License:	GPL-2.0-only
URL:		https://github.com/numactl/numactl
Source0:        https://github.com/numactl/numactl/releases/download/v2.0.19/numactl-2.0.19.tar.gz

BuildRequires: make
BuildRequires: libtool automake autoconf

ExcludeArch: s390 %{arm}

%description
Simple NUMA policy support. It consists of a numactl program to run
other programs with a specific NUMA policy.

%package libs
Summary: libnuma libraries
# There is a tiny bit of GPLv2 code in libnuma.c
License: LGPL-2.1-only and GPL-2.0-only

%description libs
numactl-libs provides libnuma, a library to do allocations with
NUMA policy in applications.

%package devel
Summary: Development package for building Applications that use numa
Requires: %{name}-libs = %{version}-%{release}
License: LGPL-2.1-only and GPL-2.0-only

%description devel
Provides development headers for numa library calls

%prep
%oreon_verify_sources
%autosetup

%build
%configure --prefix=/usr --libdir=%{_libdir}
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%ldconfig_scriptlets
%ldconfig_scriptlets libs

%files
%doc README.md
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/memhog
%{_bindir}/migspeed
%{_bindir}/migratepages
%{_mandir}/man8/*.8*
%exclude %{_mandir}/man2/*.2*

%files libs
%{_libdir}/libnuma.so.1.0.0
%{_libdir}/libnuma.so.1

%files devel
%{_libdir}/libnuma.so
%exclude %{_libdir}/libnuma.a
%{_libdir}/pkgconfig/numa.pc
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.19-4
- Prepare for Oreon 11 (RP1)
