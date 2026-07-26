%global source0_hash 98746f3c1f6f049491fec203d455bb8f8c9c6e250f041904dda5d78e21187f93

Name:           perl-XML-Filter-XInclude
Version:        1.0
Release:        50%{?dist}
Summary:        XInclude as a SAX Filter
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Filter-XInclude
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-Filter-XInclude-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# LWP::UserAgent not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::SAX::Base)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(XML::SAX) >= 0.05
BuildRequires:  perl(XML::SAX::Writer)
Requires:       perl(LWP::UserAgent)

%description
This module implements a simple SAX filter that provides XInclude support.
It does NOT support XPointer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Filter-XInclude-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
