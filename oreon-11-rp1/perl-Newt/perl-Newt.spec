%global source0_hash 35e78461b24ea7544d030fe71c82b6f633ea56f9bf0fa924ea61e1497863821f

Summary: Perl bindings for the Newt library
Name: perl-Newt
Version: 1.08
Release: 76%{?dist}
URL: https://metacpan.org/release/Newt-1.08
Source: https://cpan.metacpan.org/authors/id/A/AM/AMEDINA/Newt-1.08.tar.gz
Patch0: newt-perl-1.08-debian.patch
Patch1: newt-perl-1.08-typemap.patch
Patch2: newt-perl-1.08-fix.patch
Patch3: newt-perl-1.08-xs.patch
Patch4: newt-perl-1.08-lang.patch
Patch5: perl-Newt-bz385751.patch
Patch6: perl-Newt-1.08-export.patch
Patch7: perl-Newt-1.08-pod.patch
Patch8: perl-Newt-1.08-formdestroy.patch
Patch9: perl-Newt-1.08-fix_pointer_type.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: newt-devel, perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
Obsoletes: newt-perl < 1.08-15
Provides: newt-perl = %{version}-%{release}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl

%description
This package provides Perl bindings for the Newt widget
library, which provides a color text mode user interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Newt-%{version}
%patch -P0 -p1 -b .debian
%patch -P1 -p1 -b .valist
%patch -P2 -p1 -b .fix
%patch -P3 -p1 -b .exes
%patch -P4 -p1 -b .lang
%patch -P5 -p1 -b .bz385751
%patch -P6 -p1 -b .export
%patch -P7 -p1 -b .doc
%patch -P8 -p1 -b .formdestroy
%patch -P9 -p1 -b .pointertype
rm -rf newtlib

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%files
%doc ChangeLog README
%{perl_vendorarch}/Newt.pm
%{perl_vendorarch}/auto/Newt
%{_mandir}/man3/Newt*

%changelog
%autochangelog
