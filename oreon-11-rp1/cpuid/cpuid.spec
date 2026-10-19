%global source0_hash 8ee10fb48d4aa20c484a75d6852883710286ed2975c314bda6d0b0383908cbfe
Name:           cpuid
Version:        20260503
Release:        1%{?dist}
Summary:        Dumps information about the CPU(s)
License:        GPL-2.0-or-later
URL:            http://www.etallen.com/cpuid.html
Source0:        http://www.etallen.com/%{name}/%{name}-%{version}.src.tar.gz
Requires:       perl-autodie
ExclusiveArch:  %{ix86} x86_64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators
# /oreon:deps
%description
cpuid dumps detailed information about x86 CPU(s) gathered from the CPUID
instruction, and also determines the exact model of CPU(s). It supports Intel,
AMD, and VIA CPUs, as well as older Transmeta, Cyrix, UMC, NexGen, and Rise
CPUs. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make %{?_smp_mflags} CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -DVERSION=%{version}" LDFLAGS="$RPM_LD_FLAGS"
%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0755 cpuinfo2cpuid %{buildroot}%{_bindir}/cpuinfo2cpuid
install -Dp -m 0644 %{name}.man.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
