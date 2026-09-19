%global source0_hash f2103cff3c48206a4030559bcc0da1046a63f44c52da4ebe5f78912e7fed05e4

Name:           perl-Bot-BasicBot
Version:        0.93
Release:        25%{?dist}
Summary:        Simple IRC bot base class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Bot-BasicBot
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Bot-BasicBot-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IRC::Utils)
BuildRequires:  perl(POE::Component::IRC::Plugin::Connector)
# POE::Component::IRC::State version from POE::Component::IRC in META.json
BuildRequires:  perl(POE::Component::IRC::State) >= 6.90
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Text::Wrap)
# Tests:
# IO::Socket not used
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# POE::Component::IRC::State version from POE::Component::IRC in META.json
Requires:       perl(POE::Component::IRC::State) >= 6.90

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(POE::Component::IRC::State\\)$

%description
Basic bot system designed to make it easy to do simple bots, optionally
forking longer processes (like searches) concurrently in the background.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Bot-BasicBot-%{version}
find examples -type f -exec chmod 644 {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
