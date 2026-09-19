%global source0_hash ab96b7950ecbf29b836fdfeebbe0aac22ca573e7183be7cb7d6d12df22ab58ca

Name:           perl-MooseX-Traits-Pluggable 
Summary:        A pluggable extension to MooseX::Traits 
Version:        0.12
Release:        33%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl 

Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/MooseX-Traits-Pluggable-%{version}.tar.gz 
URL:            https://metacpan.org/release/MooseX-Traits-Pluggable
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(Moose)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This module adds support for class precedence search for traits and some
extra attributes, described below.

See the MooseX::Traits man-page for more information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Traits-Pluggable-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes
%license  LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
