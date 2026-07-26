%global source0_hash c4a78588c194603222b0a6b426e61692189def0ce4a0581791873b8720f79e9e

Name:           perl-HTTP-Thin
Version:        0.006
Release:        27%{?dist}
Summary:        Thin Wrapper around HTTP::Tiny to play nice with HTTP::Message
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Thin
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/HTTP-Thin-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(Safe::Isa)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%description
HTTP::Thin is a thin wrapper around HTTP::Tiny adding the ability to pass
in HTTP::Request objects and get back HTTP::Response objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Thin-%{version}
perl -MConfig -i -pe 's/^#!.*perl/$Config{startperl}/' ex/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc CHANGES README ex
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
