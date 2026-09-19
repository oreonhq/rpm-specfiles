%global source0_hash 99600737b9627251fc9caaac2413a0773c7172a7421fcba29926f821cfebe787

Summary:       Counting pipe
Name:          cpipe
Version:       3.0.1
Release:       37%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://developer.berlios.de/projects/cpipe
Source0:       http://download.berlios.de/cpipe/cpipe-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make
%description
Cpipe copies its standard input to its standard output while measuring
the time it takes to read an input buffer and write an output
buffer. Statistics of average throughput and the total amount of bytes
copied are printed to the standard error output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# Use included filess
touch cmdline.c cmdline.h cpipe.1
make %{?_smp_mflags} CFLAGS='%{optflags}'

%install
make install \
    BINDIR=%{buildroot}%{_bindir} \
    MANDIR=%{buildroot}%{_mandir}/man1
chmod 0644 %{buildroot}%{_mandir}/man1/cpipe*

%files
%license COPYING-2.0
%doc CHANGES README
%{_bindir}/cpipe
%{_mandir}/man1/cpipe*

%changelog
%autochangelog
