%global source0_hash 09637828a22c3c63cdb7d55f0f53ce0c009c7602ce365cbb02ee0478497da073
Name:           perl-Data-Password-zxcvbn
Version:        1.1.3
Release:        1%{?dist}
Summary:        Dropbox's password estimation logic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-Password-zxcvbn
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAKKAR/Data-Password-zxcvbn-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Perl port of Dropbox's password strength estimation
library, zxcvbn.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Password-zxcvbn-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
