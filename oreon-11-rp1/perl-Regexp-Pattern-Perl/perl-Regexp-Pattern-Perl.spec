%global source0_hash b59ee18f758b51b92a5c25532bbcd3a4d800f4b9b9d4318bdbf8af04a61c3165
Name:           perl-Regexp-Pattern-Perl
Version:        0.007
Release:        1%{?dist}
Summary:        Regexp patterns related to Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Regexp-Pattern-Perl/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Regexp-Pattern-Perl-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Regexp::Pattern::Perl)
Provides:       perl(Regexp::Pattern::Perl::Module)
Provides:       perl(Regexp::Pattern::Perl::Module)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Regexp::Pattern is a convention for organizing reusable regex patterns.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Regexp-Pattern-Perl-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
