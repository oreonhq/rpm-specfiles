%global source0_hash 47fae24e5a51d75211c2b78795e3c745fa2e7059a7553ea1cb096ed8c08c9af6
%define stamp 20081006
Name:           uread
Version:        0
Release:        1%{?dist}
Summary:        Utilities for unformatted fortran files
License:        GPL-1.0-or-later
URL:            http://www.engineers.auckland.ac.nz/~snor007/software.html#uread
Source0:        %{name}-%{stamp}.tar.gz
Source1:        uread-licence.email
Patch1:         uread-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
These utilities enable you to have a look at a Fortran unformatted file to 
see the size of the data records, and to swap its endianess from big to 
little, or vis versa.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n uread

cp -p %{SOURCE1} .

%build

export CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m755 $RPM_BUILD_ROOT%{_bindir}/
install -p -m644 *.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m0755 uread ustrip uswap $RPM_BUILD_ROOT%{_bindir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
