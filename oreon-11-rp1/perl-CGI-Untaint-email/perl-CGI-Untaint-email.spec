%global source0_hash 1fe7c0dc294b57f5469cdb292ab3f92004ad8b4eaa6c6d2e074178de8a422528

Name:           perl-CGI-Untaint-email
Version:        0.03
Release:        53%{?dist}
Summary:        Validate an email address
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Untaint-email
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/CGI-Untaint-email-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.18
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Untaint) >= 0.07
BuildRequires:  perl(Email::Valid) >= 0.13
BuildRequires:  perl(Mail::Address) >= 1.40
BuildRequires:  perl(Test::More)
Requires:  perl(CGI::Untaint) >= 0.07

%description
CGI::Untaint::email input handler verifies that it is a valid RFC2822 mailbox
format. The resulting value will be a Mail::Address instance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Untaint-email-%{version}

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
