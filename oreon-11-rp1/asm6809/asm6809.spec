%global source0_hash a6d36dd29cb3b26505c46595c1f0f1c4d7e66d3838f6347ce33ce27f4b35cffa
Name:           asm6809
Version:        2.17
Release:        1%{?dist}
Summary:        Multiple pass 6809 & 6309 cross assembler
License:        GPL-3.0-or-later
URL:            http://www.6809.org.uk/asm6809/
Source0:        http://www.6809.org.uk/asm6809/dl/asm6809-%{version}.tar.gz
Provides:       bundled(gnulib)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
asm6809 is a multiple pass 6809 & 6309 cross assembler. Text is read
in and parsed, then as many passes are made over the parsed source as
necessary (up to a limit), until symbols are resolved and addresses
are stable.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
