%global source0_hash b20f68039c0b21bd4a342456f45a4981417fd0d6d18135cfbb1234b6ee3408a3
Name:           simh
Version:        3.12.5
Release:        1%{?dist}
Summary:        Highly portable, multi-system emulator
License:        MIT AND GPL-1.0-or-later
URL:            http://simh.trailing-edge.com/
Source0:        simh-%{version}-noroms.tar.gz
Source1:        simh-generate-tarball.sh
Patch:          https://gitlab.archlinux.org/archlinux/packaging/packages/simh/-/raw/3.12.5-1/build-fix.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
SIMH is a historical computer simulation system. It consists of simulators
for many different computers, all written around a common user
interface package and set of supporting libraries.
SIMH can be used to simulate any computer system for which sufficient detail
is available, but the focus to date has been on simulating computer systems
of historic interest.

SIMH implements simulators for:

* Data General Nova, Eclipse
* Digital Equipment Corporation PDP-1, PDP-4, PDP-7, PDP-8, PDP-9, PDP-10,
  PDP-11, PDP-15, VAX
* GRI Corporation GRI-909, GRI-99
* IBM 1401, 1620, 7090/7094, System 3
* Interdata (Perkin-Elmer) 16b and 32b systems
* Hewlett-Packard 2114, 2115, 2116, 2100, 21MX, 1000
* Honeywell H316/H516
* MITS Altair 8800, with both 8080 and Z80
* Royal-Mcbee LGP-30, LGP-21
* Scientific Data Systems SDS 940

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}/sim -p1

# Convert docs to UNIX line endings
sed -i 's/\r$//' */*.txt

%build

CC="$CC -I . -fPIE -g -D_LARGEFILE64_SOURCE"
LDFLAGS="$LDFLAGS -lm -lpcap"
%make_build -e ROMS_OPT="%{optflags}" USE_NETWORK=1 LIBPATH="${_libdir}"
%install
for i in BIN/*; do
  [ -f "$i" ] && install -Dpm0755 "$i" "%{buildroot}%{_bindir}/simh-$(basename "$i")"
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
