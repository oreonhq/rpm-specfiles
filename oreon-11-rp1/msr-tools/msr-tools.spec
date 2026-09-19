%global source0_hash 9b87245ee091a798184e447066e9e0d7709b7c81f5e6ad55f2b958c1aa50c4a3

Summary:        Collection of tools for reading/writing CPU model specific registers
Name:           msr-tools
Version:        1.3
Release:        31%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://github.com/intel/msr-tools/archive/msr-tools-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
ExclusiveArch:  %{ix86} x86_64
Url:            https://github.com/intel/msr-tools

# Support for increased number of processors
# Patch submitted upstream:
# https://github.com/01org/msr-tools/pull/3

Patch:          bz1268604-increase-max-procs.patch

%description
This is a small collection of tools to allow reading and writing
of CPU model specific registers

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n msr-tools-msr-tools-%{version}

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
install -D rdmsr %{buildroot}%{_sbindir}/rdmsr
install -D wrmsr %{buildroot}%{_sbindir}/wrmsr
install -D cpuid %{buildroot}%{_sbindir}/msr-cpuid

%files
%{_sbindir}/rdmsr
%{_sbindir}/wrmsr
%{_sbindir}/msr-cpuid

%changelog
%autochangelog
