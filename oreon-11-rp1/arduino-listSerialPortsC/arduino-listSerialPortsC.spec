%global source0_hash 8769ddf5395c47744cde01cdf1d943a260b1dc4d03658255c1cf719a2592d5eb

%global shortname listSerialPortsC

Name:		arduino-%{shortname}
Version:	1.4.0
Release:	24%{?dist}
Summary:	Simple multiplatform program to list serial ports with vid/pid/iserial fields
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:	LGPL-3.0-or-later
URL:		http://www.arduino.cc
Source0:	https://github.com/arduino/listSerialPortsC/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz
BuildRequires:	libserialport-devel
%ifarch %{java_arches}
BuildRequires:	java-devel
%endif
BuildRequires:	gcc

%description
Simple environment to test libserialport in a single build machine fashion.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{shortname}-%{version}

%build
gcc `pkg-config --cflags libserialport` %{optflags} main.c `pkg-config --libs libserialport` -o listSerialC
%ifarch %{java_arches}
gcc `pkg-config --cflags libserialport` %{optflags} jnilib.c -I/usr/lib/jvm/java/include/ -I/usr/lib/jvm/java/include/linux -shared -fPIC `pkg-config --libs libserialport` -o liblistSerialsj.so
%endif

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 listSerialC %{buildroot}%{_bindir}
# Yes, this is not normal, but this isn't really a useful lib, it's only for arduino.
%ifarch %{java_arches}
mkdir -p %{buildroot}%{_datadir}/arduino/lib/
install -m755 liblistSerialsj.so %{buildroot}%{_datadir}/arduino/lib/
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/listSerialC
%ifarch %{java_arches}
%{_datadir}/arduino/lib/liblistSerialsj.so
%endif

%changelog
%autochangelog
