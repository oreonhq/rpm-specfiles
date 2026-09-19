%global source0_hash e99b5da1f26fd26e0b828b6d445197e00353a0a56ac4b039824dbcedad8b5837

Name:           perl-Catalyst-Plugin-Email
Version:        0.09
Release:        30%{?dist}
Summary:        Send emails with Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-Plugin-Email
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Catalyst-Plugin-Email-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 2.99
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::MIME::Creator)
BuildRequires:  perl(Email::Send)
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Send emails with Catalyst and Email::Send and Email::MIME::Creator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Email-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
