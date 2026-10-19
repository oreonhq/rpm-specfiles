%global source0_hash 85676225aadb76e8666a6abe2e0659d40eb4581ad6385b170eea4e1d6bf34bf7
Name:           perl-Class-C3-Adopt-NEXT
Version:        0.14
Release:        31%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Reduce one's dependency on NEXT
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-C3-Adopt-NEXT-%{version}.tar.gz
Url:            https://metacpan.org/release/Class-C3-Adopt-NEXT
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(NEXT)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
NEXT was a good solution a few years ago, but isn't any more. It's
slow, and the order in which it re-dispatches methods appears random
at times. It also encourages bad programming practices, as you end up
with code to redispatch methods when all you really wanted to do was
run some code before or after a method fired.  However, if you have a large
application, then weaning yourself off 'NEXT' isn't easy.This module is
intended as a drop-in replacement for NEXT, supporting the same interface,
but using Class::C3 to do the hard work. You can then write new code
without 'NEXT', and migrate individual source files to use 'Class::C3'
or method modifiers as appropriate, at whatever pace you're comfortable with.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-C3-Adopt-NEXT-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
