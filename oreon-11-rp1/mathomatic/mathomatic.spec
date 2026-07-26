%global source0_hash 976e6fed1014586bcd584e417c074fa86e4ca6a0fcc2950254da2efde99084ca

Summary:       Small, portable symbolic math program
Name:          mathomatic
Version:       16.0.5
Release:       36%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2
URL:           http://www.mathomatic.org/math/
#Source0:      http://mathomatic.org/mathomatic-${version}.tar.bz2
Source0:       http://mathomatic.orgserve.de/mathomatic-%{version}.tar.bz2
Source1:       http://mathomatic.orgserve.de/math/png/mathomatic192x195.png
Patch0:        mathomatic-16.0.5-libedit.patch
Patch1:        mathomatic-16.0.5-py3.patch
Patch2:        mathomatic-16.0.5-shebang.patch
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libedit-devel
BuildRequires: make
# for make test
BuildRequires: time
Requires:      m4
Requires:      rlwrap
%description
Mathomatic is a small, portable symbolic math program that can
automatically solve, simplify, differentiate, combine, and compare
algebraic equations, perform polynomial and complex arithmetic,
etc. It was written by George Gesslein II and has been under
development since 1986.

%package       tools
Summary:       Various small math tools from mathomatic
Requires:      %{name} = %{version}-%{release}
%description tools
This package contains small math tools from mathomatic to
 - calculate Pascal's triangle
 - compute any number of consecutive prime numbers
 - find the minimum number of positive integers that when squared 
   and added together, equal the given number

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CFLAGS="%{optflags} -std=gnu17"
make %{?_smp_mflags} EDITLINE=1 prefix=%{_prefix}
#make pdf
pushd primes
make %{?_smp_mflags} prefix=%{_prefix}

%install
make m4install-degrees DESTDIR=%{buildroot} prefix=%{_prefix}
ln -s %{name}.1.gz %{buildroot}/%{_mandir}/man1/rmath.1.gz
ln -s  %{name}.1.gz %{buildroot}/%{_mandir}/man1/matho.1.gz
rm -rf %{buildroot}%{_datadir}/doc/%{name}
desktop-file-install --delete-original \
    --dir %{buildroot}%{_datadir}/applications  \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
pushd primes
make install prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir}
convert %{SOURCE1} -resize 256x256 %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%check
make test
pushd primes
make test

%files
%license COPYING
%doc AUTHORS README.txt changes.txt doc
%{_bindir}/%{name}
%{_bindir}/rmath
%{_bindir}/matho
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/rmath.1*
%{_mandir}/man1/matho.1*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%files tools
%license COPYING
%doc AUTHORS README.txt changes.txt doc
%{_bindir}/matho-sum
%{_bindir}/matho-mult
%{_bindir}/matho-pascal
%{_bindir}/matho-primes
%{_bindir}/matho-sumsq
%{_bindir}/primorial
%{_mandir}/man1/matho-sum.1*
%{_mandir}/man1/matho-mult.1*
%{_mandir}/man1/matho-pascal.1*
%{_mandir}/man1/matho-primes.1*
%{_mandir}/man1/matho-sumsq.1*
%{_mandir}/man1/primorial.1*

%changelog
%autochangelog
