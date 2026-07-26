%global source0_hash 94e7778a20710fdcd521526f4cf06731e4b2b1ab059bbccf29b7e69b45013055

Name:           perl-IO-Capture-Extended
Version:        0.13
Release:        32%{?dist}
Summary:        Extend functionality of IO::Capture
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Capture-Extended
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/IO-Capture-Extended-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Capture) >= 0.05
BuildRequires:  perl(IO::Capture::Stderr)
BuildRequires:  perl(IO::Capture::Stdout)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple) >= 0.44
Requires:       perl(IO::Capture) >= 0.05

%description
IO::Capture::Extended is a distribution consisting of two classes, each of
which is a collection of subroutines which are useful in extending the
functionality of CPAN modules IO::Capture::Stdout and IO::Capture::Stderr,
particularly when used in a testing context such as that provided by
Test::Simple, Test::More or other modules built on Test::Builder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Capture-Extended-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
