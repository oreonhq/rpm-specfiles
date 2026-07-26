%global source0_hash 79a9f61c27408b4fd1ed234dac246974ddeafa7fe635a18fe41ec7783130ae2a

Name:           perl-Path-Dispatcher
Version:        1.08
Release:        13%{?dist}
Summary:        Flexible and extensible dispatch
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Path-Dispatcher/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Path-Dispatcher-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(:VERSION) >= 5.8.1
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::TypeTiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
# test requirements
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Path::Dispatcher's basic operation is that of dispatch. Dispatch takes
a path and a list of rules, and it returns a list of matches. From there,
you can "run" the rules that matched. These phases are distinct so that,
if you need to, you can inspect which rules were matched without ever
running their code-blocks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Path-Dispatcher-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes CONTRIBUTING README
%license LICENSE
%{perl_vendorlib}/Path*
%{_mandir}/man3/Path*

%changelog
%autochangelog
