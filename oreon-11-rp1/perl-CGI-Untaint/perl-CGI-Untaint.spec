%global source0_hash 08e12a7ec938bc81899c02a6426777b9fe0e75da1161516416999d3052bc63b9

Name:           perl-CGI-Untaint
Version:        1.26
Release:        53%{?dist}
Summary:        Process CGI input parameters
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Untaint
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/CGI-Untaint-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL::require) >= 0.01
# Tests:
BuildRequires:  perl(CGI)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More) >= 0.11
Requires:  perl(UNIVERSAL::require) >= 0.01

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(UNIVERSAL::require\\)$

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Untaint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/CGI
%{_mandir}/man3/*.3*

%changelog
%autochangelog
