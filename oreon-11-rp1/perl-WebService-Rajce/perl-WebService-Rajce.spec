%global source0_hash 6210219264fc30534191959dbe0a64bf55b5a60c4ffec0d996769faa8335c9b7
%global cpan_version 1.202830
Name:           perl-WebService-Rajce
Version:        %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:        16%{?dist}
Summary:        Perl interface for www.rajce.idnes.cz
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Rajce
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEK/WebService-Rajce-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(AutoLoader)
Requires:       perl(LWP::Protocol::https)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This is a Perl library implementing an API of a photo gallery service running
on www.rajce.idnes.cz server.

%package tools
Summary:        Utilities for accessing www.rajce.idnes.cz
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
%description tools
Command line tools for uploading and downloading images from a photo gallery
service running on www.rajce.idnes.cz server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WebService-Rajce-%{cpan_version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-WebService-Rajce-tools -f %{oreon_filedir}/perl-WebService-Rajce-tools.list

%changelog

%autochangelog
