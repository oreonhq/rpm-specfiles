%global source0_hash 84f2a52aed4c228bce3a47737c12b6c3b575c8532e5806e02695d8f80bd65ae1
Name:           perl-MooX-Role-EventEmitter
Version:        0.04
Release:        8%{?dist}
Summary:        Event emitter role based on Mojo::EventEmitter
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooX-Role-EventEmitter
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/MooX-Role-EventEmitter-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(warnings)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Event emitter role for perl Moo.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Role-EventEmitter-%{version}
chmod -x Changes LICENSE

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
