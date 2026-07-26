%global source0_hash abd96a51eb5c74985a59bcdb3667fa555058cfe0d7d73ece29cc4298ac3de15e

Name:           pdbg
Version:        3.6
Release:        11%{?dist}
Summary:        PowerPC FSI Debugger

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/open-power/pdbg
Source0:        https://github.com/open-power/pdbg/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf automake libtool
BuildRequires:  dtc
BuildRequires:  make
BuildRequires:  ragel
BuildRequires:  libfdt-devel

# makes sense only on the host (Power-based) and the BMC (usually an embedded Arm system)
ExclusiveArch:  ppc64le

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Library files for %{name}

%description    libs
The %{name}-libs package contains libraries for %{name}.

%description
pdbg is a simple application to allow debugging of the host POWER processors
from the BMC and the host itself. It works in a similar way to JTAG programmers
for embedded system development in that it allows you to access GPRs, SPRs and
system memory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
sh ./bootstrap.sh
%configure --disable-static
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%files
%doc README.md
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
