%global source0_hash 54435dfda4fbb689329420b1355166105ee178040d863aa3e059eca085cae045
Name:           perl-GnuPG-Interface
Version:        1.05
Release:        1%{?dist}
Summary:        Perl interface to GnuPG
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GnuPG-Interface
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/GnuPG-Interface-%{version}.tar.gz
Patch0:         version-stdin.patch
BuildArch:      noarch
Requires:       gpg
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gpg
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(MooX::late)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n GnuPG-Interface-%{version}
perldoc -t perlgpl > GPL
perldoc -t perlartistic > Artistic
# gpg as being used by the testsuite requires test to be 0700
chmod 0700 test

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
