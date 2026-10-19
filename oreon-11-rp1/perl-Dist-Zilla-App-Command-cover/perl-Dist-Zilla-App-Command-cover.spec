%global source0_hash 5dab6ab0d6e7b8c2f2fb865d056e7011402917a36c0566a9cbbd69de790a6e78
Name:           perl-Dist-Zilla-App-Command-cover
Version:        1.101001
Release:        30%{?dist}
Summary:        Code coverage metrics for your distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-App-Command-cover
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOHERTY/Dist-Zilla-App-Command-cover-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl-Devel-Cover
Requires:       perl(File::chdir)
Requires:       perl(File::Temp)
Requires:       perl(Path::Class)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Dist::Zilla::App)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
