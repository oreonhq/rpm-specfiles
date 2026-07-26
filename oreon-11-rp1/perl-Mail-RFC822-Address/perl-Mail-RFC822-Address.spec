%global source0_hash 351ef4104ecb675ecae69008243fae8243d1a7e53c681eeb759e7b781684c8a7

Name:           perl-Mail-RFC822-Address
Version:        0.3
Release:        47%{?dist}
Summary:        Perl extension for validating email addresses according to RFC822
License:        MIT
URL:            https://metacpan.org/release/Mail-RFC822-Address
Source0:        https://cpan.metacpan.org/modules/by-module/Mail/Mail-RFC822-Address-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(Data::Dumper)

%description
Mail::RFC822::Address validates email addresses against the grammar 
described in RFC 822 using regular expressions. The only sure way to see 
if a supplied email address is genuine is to send an email to it and see 
if the user recieves it. This package only checks that the email address 
is syntactically valid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-RFC822-Address-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
