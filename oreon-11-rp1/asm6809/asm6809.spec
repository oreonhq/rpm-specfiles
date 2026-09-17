%global source0_hash 6051624597d94d69a68a08e194cfe18cbdb12f829c80d92b84f641794b8b09bb

Name:           asm6809
Version:        2.16
Release:        4%{?dist}
Summary:        Multiple pass 6809 & 6309 cross assembler

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.6809.org.uk/asm6809/
Source0:        http://www.6809.org.uk/asm6809/dl/asm6809-%{version}.tar.gz

# https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib)

BuildRequires:  gcc
BuildRequires: make

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

%files
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%license COPYING.GPL

%changelog
%autochangelog
