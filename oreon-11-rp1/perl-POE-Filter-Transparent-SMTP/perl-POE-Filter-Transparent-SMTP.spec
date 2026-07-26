%global source0_hash d26ccb9a09e940847bd8fb61213954eb53fc18d4d305bfbdb923b38455d37088

Name:           perl-POE-Filter-Transparent-SMTP
Version:        0.2
Release:        51%{?dist}
Summary:        A POE filter for SMTP

# note license definition in Makefile.PL
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Filter-Transparent-SMTP
Source0:        https://cpan.metacpan.org/authors/id/U/UL/ULTRADM/POE-Filter-Transparent-SMTP-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(POE)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)

%description
POE data filter which aims to make SMTP data transparent 
just before going onto the wire as per RFC 821 Section 4.5.2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Filter-Transparent-SMTP-%{version}
chmod -x LICENSE

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
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
