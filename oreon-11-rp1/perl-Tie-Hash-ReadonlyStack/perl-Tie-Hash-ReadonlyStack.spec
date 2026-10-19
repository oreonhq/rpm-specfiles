%global source0_hash a28ab5151c234df2e0afeb84435b3fe15435410d56372d6839afcd0eb7fbc913
Name:           perl-Tie-Hash-ReadonlyStack
Version:        0.2
Release:        1%{?dist}
Summary:        Treat multiple hashes as a single hash with copy-on-write modifications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-Hash-ReadonlyStack
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/Tie-Hash-ReadonlyStack-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module allows you to have your main hash and then assign hashes to
look for the given key in either before or after the main hash. It also allows
you to use hashes that are read-only in said stack and then assign new values
there without modifying the hashes they came from.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Hash-ReadonlyStack-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
