%global source0_hash 5dab6ab0d6e7b8c2f2fb865d056e7011402917a36c0566a9cbbd69de790a6e78

Name:           perl-Dist-Zilla-App-Command-cover
Version:        1.101001
Release:        30%{?dist}
Summary:        Code coverage metrics for your distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-App-Command-cover
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOHERTY/Dist-Zilla-App-Command-cover-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl-Devel-Cover
BuildRequires:  perl(Dist::Zilla::App)
# XXX: BuildRequires:  perl(File::chdir)
# XXX: BuildRequires:  perl(File::Temp)
# XXX: BuildRequires:  perl(Path::Class)
# Tests only
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
Requires:       perl-Devel-Cover
Requires:       perl(File::chdir)
Requires:       perl(File::Temp)
Requires:       perl(Path::Class)

%description
This is a command plugin for Dist::Zilla. It provides the cover command,
which generates code coverage metrics for your distribution using
Devel::Cover.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-App-Command-cover-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
