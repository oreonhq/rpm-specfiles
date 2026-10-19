%global source0_hash 802aa6724cda1c3d7c95ace4858caa34b3a9999ff9b32fba94e3b612b5a1267a
Name:           perl-Crypt-RC4-XS
Version:        0.02
Release:        48%{?dist}
Summary:        Perl implementation of the RC4 encryption algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-RC4-XS
Source0:        https://cpan.metacpan.org/authors/id/O/OY/OYAMA/Crypt-RC4-XS-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module XS implementation of the RC4 algorithm, developed by RSA
Security, Inc. Here is the description from Wikipedia website:

In cryptography, RC4 (also known as ARC4 or ARCFOUR meaning Alleged RC4, see
below) is the most widely-used software stream cipher and is used in popular
protocols such as Secure Sockets Layer (SSL) (to protect Internet traffic)
and WEP (to secure wireless networks). While remarkable for its simplicity
and speed in software, RC4 is vulnerable to attacks when the beginning of the
output keystream is not discarded, or a single keystream is used twice; some
ways of using RC4 can lead to very insecure cryptosystems such as WEP.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-RC4-XS-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
