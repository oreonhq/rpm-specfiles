%global source0_hash 6e40d98d32abbe0915a7a8996edcdbae61a54bb1f34f2f8a5c9c8d3d2962ec23
%define _lto_cflags %{nil}
Name:           ethq
Version:        0_7_0
Release:        1%{?dist}
Summary:        Ethernet NIC Queue stats viewer
%global gitver %{lua:gv,n=string.gsub(macros.version, '[.]', '_');print(gv)}
License:        MPL-2.0
URL:            https://github.com/isc-projects/ethq
Source0:        https://github.com/isc-projects/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Displays an auto-updating per-second count of the number of packets and
bytes being handled by each specified NIC, and on multi-queue NICs shows
the per-queue statistics too.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitver}

%build

%make_build CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"
%install
%dnl %make_install CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}"
mkdir -p %{buildroot}%{_sbindir}
install ethq %{buildroot}%{_sbindir}
%oreon_autofiles main

%check

./%{name} -h
./%{name}_test generic < /dev/null
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
