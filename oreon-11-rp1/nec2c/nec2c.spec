%global source0_hash e044708cc425f094dbdc1845e6ead33d4a40c838382031335af79ac9f1721168

Name:           nec2c
Version:        1.3.2
Release:        5%{?dist}
Summary:        Translation of NEC2 antenna modeling tool from FORTRAN to C

License:        GPL-3.0-only
URL:            https://github.com/KJ7LNW/nec2c
Source0:        https://github.com/KJ7LNW/nec2c/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        nec2c.1

BuildRequires:  autoconf automake make
BuildRequires:  gcc
# Should not be required but configure checks for it.
BuildRequires:  gcc-c++
%if ! 0%{?rhel}
BuildRequires:  help2man
%endif

%description
nec2c is a translation of the Numerical Electromagnetics Code (NEC2)
from FORTRAN to C. 

Operationally nec2c differs from NEC2 by being a command line
non-interactive program, taking as arguments the input file name
and optionally the output file name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -fi
%configure
%make_install CFLAGS="%{optflags}"

%install
#skip make install and do manual install, it's just one file
install -D -m 0755 nec2c %{buildroot}%{_bindir}/nec2c

mkdir -p %{buildroot}%{_mandir}/man1
%if 0%{?rhel}
    install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1
%else
    help2man -o %{buildroot}%{_mandir}/man1/%{name}.1 -h -h -v -v --no-discard-stderr -N %{buildroot}%{_bindir}/%{name}
%endif

%files
%doc AUTHORS README NEC2-bug.txt
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
