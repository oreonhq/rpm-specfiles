%global source0_hash e7a1ac9ef4a1235b3fdbd5888f86c347182306467bd79abc9b0756a64b441cbc
Name:           perl-Net-DBus
Version:        1.2.0
Release:        1%{?dist}
Summary:        Use and provide DBus services
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-DBus
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Net-DBus-%{version}.tar.gz
Requires:       perl(XSLoader)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  dbus-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
# /oreon:deps
%description
Net::DBus provides a Perl API for the DBus message system. The DBus Perl
interface is currently operating against the 0.33 development version of
DBus, but should work with later versions too, providing the API changes
have not been too drastic.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-DBus-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
