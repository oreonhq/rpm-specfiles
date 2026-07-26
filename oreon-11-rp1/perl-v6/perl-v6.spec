%global source0_hash f835eb72887b76692ca463936eab41d62a6b4de01a1674adf80b4e7f896ac2f4

# Inhibit python compilation
%global __python %{nil}

Name:           perl-v6
Version:        0.047
Release:        28%{?dist}
Summary:        Perl 6 implementation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/v6
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/v6-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Encode)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(utf8)
# YAML::Syck not used at tests
Requires:       perl(YAML::Syck)
Provides:       perl(Perlito6::AST) = %{version}
Provides:       perl(Perlito6::Emitter::Token) = %{version}
Provides:       perl(Perlito6::Grammar::Control) = %{version}
Provides:       perl(Perlito6::Go::Emitter) = %{version}
Provides:       perl(Perlito6::Java::Emitter) = %{version}
Provides:       perl(Perlito6::JavaScript::Emitter) = %{version}
Provides:       perl(Perlito6::Lisp::Emitter) = %{version}
Provides:       perl(Perlito6::Macro) = %{version}
Provides:       perl(Perlito6::Parrot::Emitter) = %{version}
Provides:       perl(Perlito6::Perl5::Emitter) = %{version}
Provides:       perl(Perlito6::Perl5::Prelude) = %{version}
Provides:       perl(Perlito6::Perl5::Runtime) = %{version}
Provides:       perl(Perlito6::Python::Emitter) = %{version}
Provides:       perl(Perlito6::Ruby::Emitter) = %{version}
Provides:       perl(Perlito6::Runtime) = %{version}

# Do not export private modules
%global __provides_exclude %{!?__provides_exclude:^$}
%global __provides_exclude %__provides_exclude|^perl\\(Apply\\)
%global __provides_exclude %__provides_exclude|^perl\\(ARRAY\\)
%global __provides_exclude %__provides_exclude|^perl\\(Bind\\)
%global __provides_exclude %__provides_exclude|^perl\\(Call\\)
%global __provides_exclude %__provides_exclude|^perl\\(CompUnit\\)
%global __provides_exclude %__provides_exclude|^perl\\(Decl\\)
%global __provides_exclude %__provides_exclude|^perl\\(Do\\)
%global __provides_exclude %__provides_exclude|^perl\\(For\\)
%global __provides_exclude %__provides_exclude|^perl\\(GLOBAL\\)
%global __provides_exclude %__provides_exclude|^perl\\(HASH\\)
%global __provides_exclude %__provides_exclude|^perl\\(If\\)
%global __provides_exclude %__provides_exclude|^perl\\(Index\\)
%global __provides_exclude %__provides_exclude|^perl\\(IO\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lit::Array\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lit::Block\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lit::Hash\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lookup\\)
%global __provides_exclude %__provides_exclude|^perl\\(Main\\)
%global __provides_exclude %__provides_exclude|^perl\\(Method\\)
%global __provides_exclude %__provides_exclude|^perl\\(Pair\\)
%global __provides_exclude %__provides_exclude|^perl\\(Perl5\\)
%global __provides_exclude %__provides_exclude|^perl\\(Proto\\)
%global __provides_exclude %__provides_exclude|^perl\\(Python\\)
%global __provides_exclude %__provides_exclude|^perl\\(Return\\)
%global __provides_exclude %__provides_exclude|^perl\\(Ruby\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::After\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Before\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Block\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Capture\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::CaptureResult\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::CharClass\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Concat\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Constant\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Dot\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::InterpolateVar\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::NamedCapture\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::NegateCharClass\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::NotBefore\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Or\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Quantifier\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::SpecialChar\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Subrule\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Var\\)
%global __provides_exclude %__provides_exclude|^perl\\(Sig\\)
%global __provides_exclude %__provides_exclude|^perl\\(Sub\\)
%global __provides_exclude %__provides_exclude|^perl\\(Use\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Bit\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Buf\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Int\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Num\\)
%global __provides_exclude %__provides_exclude|^perl\\(Var\\)
%global __provides_exclude %__provides_exclude|^perl\\(When\\)
%global __provides_exclude %__provides_exclude|^perl\\(While\\)

# Do not generate requires from Perlito/Python/Prelude.pm, because it
# contains "use v6" and generators process it as Perl version 6.0 instead
# of a Perl module
%global __requires_exclude_from %{?__requires_exclude_from:__requires_exclude_from|}^$
%global __requires_exclude_from %__requires_exclude_from|^%{perl_vendorlib}/Perlito6/Python/Prelude.pm

%description
The v6 module is a front-end to the "Perlito" compiler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n v6-%{version}
%fix_shbang_line scripts/perlito6
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
