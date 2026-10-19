%global source0_hash 7fac1c4b61eb9411275de0e1e7d7a8c3f34166f64f16413f50741e8fce2b8dc0
Summary:        Access I/O ports
Name:        ioport
Version:     1.2
Release:        1%{?dist}
License:     GPL-2.0-or-later
URL:         http://et.redhat.com/~rjones/ioport/
Source0:        http://et.redhat.com/~rjones/ioport/files/%{name}-%{version}.tar.gz
ExclusiveArch: %{ix86} x86_64
# oreon:deps
BuildRequires:  /usr/bin/perldoc
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
These commands enable command line and script access directly to I/O
ports on PC hardware.

The inb, inw and inl commands perform an input (read) operation on the
given I/O port, and print the result.

The outb, outw and outl commands perform an output (write) operation
to the given I/O port, sending the given data.  Note that the order of
the parameters is ADDRESS DATA.

The size of the operation is selected according to the suffix, with
'b' meaning byte, 'w' meaning word (16 bits) and 'l' meaning long
(32 bits).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
