%global source0_hash 4df9d574f8f26db022bf06c1bda4708289451098c2e1563335df38d23b07326d

Name:           perl-MooX-Options
Version:        4.103
Release:        25%{?dist}
Summary:        Explicit Options eXtension for Object Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Options
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Options-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Record)
BuildRequires:  perl(Getopt::Long) >= 2.43
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.099
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::ConfigFromFile::Role)
BuildRequires:  perl(MooX::Locale::Passthrough)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.32
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 2
BuildRequires:  perl(Text::LineFold)
# Optional run-time:
BuildRequires:  perl(Term::Size::Any)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Mo) >= 0.36
BuildRequires:  perl(Mo::coerce)
BuildRequires:  perl(Mo::default)
BuildRequires:  perl(Mo::required)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Trap)
# Optional tests:
# English not used
BuildRequires:  perl(MooX::Cmd) >= 0.007
BuildRequires:  perl(MooX::Locale::TextDomain::OO)
BuildRequires:  perl(Locale::TextDomain::OO::Lexicon::Hash)
Requires:       perl(Data::Record)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Moo) >= 1.003
Requires:       perl(Moo::Role)
Requires:       perl(MooX::ConfigFromFile::Role)
Requires:       perl(MooX::Locale::TextDomain::OO)
Requires:       perl(MRO::Compat)
Requires:       perl(Path::Class) >= 0.32
Requires:       perl(Pod::Usage)
Requires:       perl(Regexp::Common)
Requires:       perl(Text::LineFold)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Getopt::Long::Descriptive|Moo::Role)\\)$

%description
Create a command line tool with your Mo, Moo, Moose objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Options-%{version}
chmod -c -x lib/MooX/Options.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes etc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
