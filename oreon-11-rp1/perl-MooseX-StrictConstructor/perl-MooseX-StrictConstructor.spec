%global source0_hash c72a5ae9583706ccdec71d401dcb3054013a7536b750df1436613d858ea2920d

Name:           perl-MooseX-StrictConstructor 
Version:        0.21
Release:        27%{?dist}
# see lib/MooseX/StrictConstructor.pm
License:        Artistic-2.0
Summary:        Make your object constructors blow up on unknown attributes 
Source:         https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-StrictConstructor-%{version}.tar.gz 
Url:            https://metacpan.org/release/MooseX-StrictConstructor
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

Provides:       perl(MooseX::StrictConstructor)
%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute init argument that your class does
not declare, then it calls "Carp::confess()". This is a great way to catch
small typos.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-StrictConstructor-%{version}
# avoid rpmlint wrong-script-interpreter warning
perl -MConfig -i -pe '$. == 1 && s~#!.*perl~$Config{startperl}~' t/*.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
