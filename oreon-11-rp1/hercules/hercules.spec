%global source0_hash 890c57c558d58708e55828ae299245bd2763318acf53e456a48aac883ecfe67d
Summary:        Hercules S/370, ESA/390, and z/Architecture emulator
Name: hercules
Version: 3.13
Release:        1%{?dist}
License: QPL-1.0
URL: http://www.hercules-390.eu/
Source0:        http://downloads.hercules-390.eu/%{name}-%{version}.tar.gz
Source1: hercules.cnf
Source2: hercules-run
Source3: README-rpm
Source4: generic.prm
Patch0: %{name}-3.10-fedora.patch
Patch1: hercules-configure-c99.patch
Conflicts: sdl-hercules
Conflicts: sdl-hercules-data
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Hercules is an emulator for the IBM System/370, ESA/390, and z/Architecture
series of mainframe computers. It is capable of running any IBM operating
system and applications that a real system will run, as long as the hardware
needed is emulated. Hercules can emulate FBA and CKD DASD, tape, printer,
card reader, card punch, channel-to-channel adapter, LCS Ethernet, and
printer-keyboard, 3270 terminal, and 3287 printer devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .fedora
%patch -P1 -p1

rm autoconf/libtool.m4
autoreconf -f -i

# remove unbundled stuff
rm ltdl.[ch]

# Scripts to be looked at, not executed from the docs
chmod -x util/*
# remove Makefile
rm util/Makefile*

%build

%configure \
    --enable-external-gui \
    --enable-optimization="%{optflags} -std=gnu17"
make %{?_smp_mflags} V=1
%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/hercules
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/hercules/
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/hercules/
install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/hercules-run
install -p -m 0644 %{SOURCE3} README-rpm
mkdir -p %{buildroot}%{_sharedstatedir}/hercules
rm html/Makefile*
rm %{buildroot}%{_libdir}/hercules/*.la
rm %{buildroot}%{_libdir}/*.la
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
