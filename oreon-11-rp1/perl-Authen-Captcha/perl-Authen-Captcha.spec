%global source0_hash 798cc6ad6a6afa53f792ca427a8e474a31f578ba60928e93d86bf0899b0fd739

Name:           perl-Authen-Captcha
Version:        1.024
Release:        35%{?dist}
Summary:        Perl extension for creating captchas
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only

URL:            https://metacpan.org/release/Authen-Captcha
Source0:        https://cpan.metacpan.org/authors/id/L/LK/LKUNDRAK/Authen-Captcha-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(GD)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Random)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  sed

%{?perl_default_filter}

%description
Authen::Captcha provides an object oriented interface to captcha file
creations. Captcha stands for Completely Automated Public Turning test to
tell Computers and Humans Apart.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-Captcha-%{version}

%build
sed -i 's/\r//' license.txt
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes license.txt README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
