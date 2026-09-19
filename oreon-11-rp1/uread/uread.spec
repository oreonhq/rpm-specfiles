%global source0_hash 47fae24e5a51d75211c2b78795e3c745fa2e7059a7553ea1cb096ed8c08c9af6

%define stamp 20081006

Name:           uread
Version:        0
Release:        0.36.%{stamp}%{?dist}
Summary:        Utilities for unformatted fortran files

License:        GPL-1.0-or-later
URL:            http://www.engineers.auckland.ac.nz/~snor007/software.html#uread
Source0:        uread-%{stamp}.tar.gz
# unversioned upstream source, downloaded with wget -N
# renamed to uread-YYYYMMDD.tar.gz
#Source0:        http://www.engineers.auckland.ac.nz/~snor007/src/uread.tar.gz

# this is a mail exchange where the author gives the right to redistribute 
# his work under the GPL
Source1:        uread-licence.email
#Patch0:         uread-include_stdlib.diff
Patch1:         uread-c99.patch

#BuildRequires:  
#Requires:       

BuildRequires: make
BuildRequires:  gcc
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

%files
%doc uread-licence.email
%{_bindir}/uread
%{_bindir}/ustrip
%{_bindir}/uswap
%{_mandir}/man1/u*.1*

%changelog
%autochangelog
