%global source0_hash abd96a51eb5c74985a59bcdb3667fa555058cfe0d7d73ece29cc4298ac3de15e
Name:           pdbg
Version:        3.6
Release:        1%{?dist}
Summary:        PowerPC FSI Debugger
License:        Apache-2.0
URL:            https://github.com/open-power/pdbg
Source0:        https://github.com/open-power/pdbg/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  ppc64le
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dtc
BuildRequires:  gcc
BuildRequires:  libfdt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ragel
# /oreon:deps
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
%oreon_prep
%build

sh ./bootstrap.sh
%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pdbg-devel -f %{oreon_filedir}/pdbg-devel.list
%files -n pdbg-libs -f %{oreon_filedir}/pdbg-libs.list

%changelog

%autochangelog
