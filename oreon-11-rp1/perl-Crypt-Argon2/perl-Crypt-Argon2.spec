%global source0_hash 216721bcf9588513a6125ff0c17db9293998763653a4b158371bce7bd572577a

Name:		perl-Crypt-Argon2
Version:	0.030
Release:	2%{?dist}
Summary:	Perl interface to the Argon2 key derivation functions
License:	Apache-2.0

URL:		https://metacpan.org/release/Crypt-Argon2
Source0:	https://www.cpan.org/authors/id/L/LE/LEONT/Crypt-Argon2-%{version}.tar.gz

BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.006
BuildRequires:	perl(Dist::Build)
#BuildRequires:	perl(ExtUtils::CBuilder)
#BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Run-time:
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(XSLoader)
# Tests:
BuildRequires:	perl(Test::More) >= 0.90

%{?perl_default_filter}

%description
This module implements the Argon2 key derivation function, which is
suitable to convert any password into a cryptographic key. This is most
often used to for secure storage of passwords but can also be used to
derive a encryption key from a password. It offers variable time and memory
costs as well as output size.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Crypt-Argon2-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
#--optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*
%{_bindir}/argon2-calibrate
%{_mandir}/man1/argon2-calibrate.1*

%changelog
%autochangelog
