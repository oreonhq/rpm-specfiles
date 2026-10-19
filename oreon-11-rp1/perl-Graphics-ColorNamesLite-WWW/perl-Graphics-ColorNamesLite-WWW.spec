%global source0_hash 0b85aa04277a986086970a9e5f7b968c784262bbcb4a2bd9ea0792f892276f33
Name:           perl-Graphics-ColorNamesLite-WWW
Version:        1.14.000
Release:        16%{?dist}
Summary:        WWW color names and equivalent RGB values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-ColorNamesLite-WWW/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Graphics-ColorNamesLite-WWW-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Graphics::ColorNamesLite::WWW)
# oreon:deps
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
WWW color names and equivalent RGB values (lite version).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Graphics-ColorNamesLite-WWW-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
