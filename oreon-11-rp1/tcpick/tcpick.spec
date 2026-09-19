%global source0_hash cf3c3814518f5565df3884d07e1e3015d88ac1dbfe3885635dd6e67d6ce46dd2

Summary:        TCP stream sniffer, tracker and capturer
Name:           tcpick
Version:        0.2.1
Release:        51%{?dist}
# tcpick itself is GPL-2.0-or-later but uses other source codes, breakdown:
# BSD-3-Clause: src/{tcp,udp}.h
# LGPL-2.1-or-later: src/{ip,udp}.h
License:        GPL-2.0-or-later AND BSD-3-Clause AND LGPL-2.1-or-later
URL:            http://tcpick.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         tcpick-0.2.1-CVE-2006-0048.patch
Patch1:         tcpick-0.2.1-ppc.patch
Patch2:         tcpick-0.2.1-pointers.patch
Patch3:         tcpick-0.2.1-cpu-loop.patch
Patch4:         tcpick-0.2.1-timezone.patch
Patch5:         tcpick-0.2.1-gcc5.patch
Patch6:         tcpick-0.2.1-gcc10.patch
BuildRequires:  gcc, make, libpcap-devel

%description
tcpick is a textmode sniffer that can track tcp streams and saves 
the data captured in files or displays them in the terminal. Useful 
for picking files in a passive way.

It can store all connections in different files, or it can display
all the stream on the terminal. It is useful to keep track of what
users of a network are doing, and is usable with textmode tools
like grep, sed and awk. It can handle eth and ppp interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .CVE-2006-0048
%patch -P1 -p1 -b .ppc
%patch -P2 -p1 -b .pointers
%patch -P3 -p1 -b .cpu-loop
%patch -P4 -p1 -b .timezone
%patch -P5 -p1 -b .gcc5
%patch -P6 -p1

%build
# Build with C89 compatibility because the package relies on many
# implicit function declarations.
%global build_type_safety_c 0
%configure --bindir=%{_sbindir}
%make_build

%install
%make_install

# Move the Italian man page to its correct place
mkdir -p $RPM_BUILD_ROOT%{_mandir}/it/man8
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/tcpick_italian.8 $RPM_BUILD_ROOT%{_mandir}/it/man8/tcpick.8

# Convert non-utf8 authors file into utf8
iconv -f iso-8859-1 -t utf-8 -o AUTHORS.utf8 AUTHORS
touch -c -r AUTHORS AUTHORS.utf8; mv -f AUTHORS.utf8 AUTHORS

%files 
%license COPYING
%doc AUTHORS ChangeLog EXAMPLES KNOWN-BUGS README THANKS
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_mandir}/it/man8/%{name}.8*

%changelog
%autochangelog
