%global source0_hash 54435dfda4fbb689329420b1355166105ee178040d863aa3e059eca085cae045

Name:           perl-GnuPG-Interface
Version:        1.05
Release:        2%{?dist}
Summary:        Perl interface to GnuPG
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GnuPG-Interface
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/GnuPG-Interface-%{version}.tar.gz
# https://github.com/bestpractical/gnupg-interface/issues/8
Patch0:         version-stdin.patch
BuildArch:      noarch
BuildRequires:  gpg

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(MooX::late)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

Requires:       gpg

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%license GPL Artistic
%doc Changes README
%{perl_vendorlib}/GnuPG
%{_mandir}/man3/*.3*

%changelog
%autochangelog
