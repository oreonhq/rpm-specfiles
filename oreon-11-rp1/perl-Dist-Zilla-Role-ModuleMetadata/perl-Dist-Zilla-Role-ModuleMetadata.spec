%global source0_hash 5e211cbde5057b87f8e34061b662de4cee50373eb50ed5ecf2583e70a22ba21e

Name:           perl-Dist-Zilla-Role-ModuleMetadata
Version:        0.006
Release:        24%{?dist}
Summary:        Role for plugins that use Module::Metadata
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Role-ModuleMetadata
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Role-ModuleMetadata-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Module::Metadata) >= 1.000005
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
# Tests:
BuildRequires:  perl(Dist::Zilla) >= 5
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::Plugin)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
# Test::Warnings not used
BuildRequires:  perl(utf8)

%description
This role provides some common utilities for Dist::Zilla plugins which use
Module::Metadata and the information that it provides.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Role-ModuleMetadata-%{version}

%build
PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
