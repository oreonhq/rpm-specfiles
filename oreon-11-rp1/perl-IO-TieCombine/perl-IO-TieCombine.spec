%global source0_hash 402d4db8300b3d271632f4995e0ade329d89280a7e47f2badf8b38af6e5569af
Name:       perl-IO-TieCombine 
Version:    1.005
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Produce tied (and other) separate but combined variables
Url:        https://metacpan.org/release/IO-TieCombine
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IO-TieCombine-%{version}.tar.gz
BuildArch:  noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package allows you to tie separate variables into a combined whole, using
ties and other magic.  This can be very useful when, say, you want a unified
output from various different things that return data in different ways
(STDIN/ERR, scalars, handles, etc).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-TieCombine-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
