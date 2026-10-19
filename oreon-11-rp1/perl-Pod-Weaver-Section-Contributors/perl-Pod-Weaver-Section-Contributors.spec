%global source0_hash d4cc9a06c170b898d12e4262581b16ae8adca32955956dbe1bb8c7d17662f0a2
Name:           perl-Pod-Weaver-Section-Contributors
Version:        0.009
Release:        26%{?dist}
Summary:        Section listing contributors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Weaver-Section-Contributors
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KEEDI/Pod-Weaver-Section-Contributors-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Pod::Weaver::Role::Section)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Pod::Weaver section adds a listing of the documents contributors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Weaver-Section-Contributors-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
