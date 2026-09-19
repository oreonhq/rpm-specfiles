%global source0_hash 6afe0ab29955cdcad97dc67a2b0eb3c07f8d799fb78d9db7b6f84414cfb33e47

Name:           perl-MooseX-Extended
Version:        0.35
Release:        7%{?dist}
Summary:        Extend Moose with safe defaults and useful features
License:        Artistic-2.0
URL:            https://metacpan.org/dist/MooseX-Extended/
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/MooseX-Extended-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

BuildRequires:  perl(:VERSION) >= 5.20.0

BuildRequires:  perl(base)
BuildRequires:  perl(B::Hooks::AtRuntime) >= 8
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future::AsyncAwait) >= 0.58
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(Moose::Exception::Role::Class)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Role::WarnOnConflict)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Syntax::Keyword::MultiSub) >= 0.02
BuildRequires:  perl(Syntax::Keyword::Try) >= 0.027
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Compile) >= 3.1.0
BuildRequires:  perl(Test::Compile::Internal)
BuildRequires:  perl(true) >= 1.0.2
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Params)
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Common::String)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Type::Tiny) >= 1.012004
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(warnings)

%description
This class attempts to create a safer version of Moose that defaults to
read-only attributes and is easier to read and write.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Extended-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
