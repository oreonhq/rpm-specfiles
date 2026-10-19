%global source0_hash 216721bcf9588513a6125ff0c17db9293998763653a4b158371bce7bd572577a
Name:		perl-Crypt-Argon2
Version:	0.030
Release:        1%{?dist}
Summary:        Perl interface to the Argon2 key derivation functions
License:	Apache-2.0
URL:		https://metacpan.org/release/Crypt-Argon2
Source0:        https://www.cpan.org/authors/id/L/LE/LEONT/Crypt-Argon2-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Build)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements the Argon2 key derivation function, which is
suitable to convert any password into a cryptographic key. This is most
often used to for secure storage of passwords but can also be used to
derive a encryption key from a password. It offers variable time and memory
costs as well as output size.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Crypt-Argon2-%{version}
%oreon_prep
%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
