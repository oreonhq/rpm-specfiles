%global source0_hash bac318405221f2f88d374683549338515b070ca7491497eda2ac9c17bcbb0458
Name:       bcal
Version:    2.6
Release:        1%{?dist}
Summary:        Storage conversion and expression calculator
License:    GPL-3.0-or-later
URL:        https://github.com/jarun/bcal
Source0:        https://github.com/jarun/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64 ppc64le s390x riscv64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
bcal (Byte CALculator) is a command-line utility for storage conversions
and calculations. Storage, hardware and firmware developers work
with numerical calculations regularly e.g., storage unit conversions,
address calculations etc. If you are one and can't calculate the hex address
offset for (512 - 16) MiB immediately, or the value when the 43rd bit of
a 64-bit address is set, bcal is for you

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i '/STRIP ?= strip/d;s/install: bcal/install: /;s/$(CFLAGS)/$(CFLAGS) $(LDFLAGS)/' Makefile

%build

%{set_build_flags}
export CFLAGS="-fPIC %{optflags}"
%make_build bcal
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
