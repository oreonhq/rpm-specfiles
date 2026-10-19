%global source0_hash 6188d0f0c180db7a30467b5b6065a3cb5d2665b937d2e8c40366efb52bf689fe
Summary:        Beep the PC speaker any number of ways
Name:           beep
Version:        1.4.12
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/spkr-beep/beep/
Source0:        https://github.com/spkr-beep/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        README.fedora
Source2:        70-pcspkr-beep.rules
Source3:        90-pcspkr-beep.rules
Source4:        pcspkr-beep.conf
%{!?el7:BuildRequires:  libubsan}
Requires:       kmod
%{?el7:Requires:  systemd}
%{!?el7:Requires: systemd-udev}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-kernheaders
BuildRequires:  libubsan
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Beep allows the user to control the PC speaker with precision,
allowing different sounds to indicate different events. While it
can be run quite happily from the command line, its intended place
of use is within scripts, notifying the user when something
interesting occurs. Of course, it has no notion of what is
interesting, but it is really good at the notifying part.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's|^\.\\" \(\.BR .*\)README.Distro\(.*\)|\1README.fedora\2|' beep.1.in && : #"

# Create a sysusers.d config file
cat >beep.sysusers.conf <<EOF
g beep -
EOF

%build

if test "x%{build_cppflags}" = "x%%{build_cppflags}"; then
   BUILD_CPPFLAGS=""
else
   BUILD_CPPFLAGS="%{build_cppflags}"
fi
cat>local.mk<<EOF
CC = %{__cc}
CFLAGS = %{build_cflags}
CFLAGS += ${CFLAGS}
CPPFLAGS = ${BUILD_CPPFLAGS}
CPPFLAGS += ${CPPFLAGS}
LDFLAGS = %{build_ldflags}
LDFLAGS += ${LDFLAGS}
prefix = %{_prefix}
exec_prefix = %{_exec_prefix}
bindir = %{_bindir}
docdir = %{_pkgdocdir}
mandir = %{_mandir}
EOF
make %{?_smp_mflags}
%{?el7:sed -i '1s|.*|#!/bin/sed -f|' contrib/morse/morse2beep.sed}
%install
rm -rf "%{buildroot}"
make %{?_smp_mflags} install DESTDIR="%{buildroot}" CC=false
install -p -m 0644 "%{SOURCE1}" "%{buildroot}%{_pkgdocdir}/README.fedora"
install -d -m 0755              "%{buildroot}%{_sysconfdir}/modprobe.d/"
install -p -m 0644 "%{SOURCE4}" "%{buildroot}%{_sysconfdir}/modprobe.d/beep.conf"
install -d -m 0755              "%{buildroot}%{_udevrulesdir}/"
install -p -m 0644 "%{SOURCE2}" "%{buildroot}%{_udevrulesdir}/"
install -p -m 0644 "%{SOURCE3}" "%{buildroot}%{_udevrulesdir}/"
install -m0644 -D beep.sysusers.conf %{buildroot}%{_sysusersdir}/beep.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
