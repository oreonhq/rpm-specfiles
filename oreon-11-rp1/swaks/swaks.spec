%global source0_hash 0e531b4d164058802e7266b14f4dc1897099d096f930820de2f9b5eb08dcdbe8

%define to_utf8(f:) iconv -f %{-f:%{-f*}}%{!-f:iso-8859-1} -t utf-8 < %1 > %{1}. && touch -r %1 %{1}. && mv -f %{1}. %1

Name:       swaks
Version:    20240103.0
Release:    %autorelease
Summary:    Command-line SMTP transaction tester

License:    GPL-2.0-or-later
URL:        http://www.jetmore.org/john/code/swaks
Source0:    http://www.jetmore.org/john/code/swaks/swaks-%version.tar.gz

BuildArch:  noarch
BuildRequires: perl-generators
BuildRequires: perl-podlators

Requires:   perl(Authen::DigestMD5)
Requires:   perl(Authen::NTLM)
Requires:   perl(Authen::SASL)
Requires:   perl(Config)
Requires:   perl(Digest::SHA)
Requires:   perl(IO::Socket::IP)
Requires:   perl(Net::DNS)
Requires:   perl(Net::SSLeay)
Requires:   perl(Time::HiRes)

%description
Swiss Army Knife SMTP: A command line SMTP tester.  Swaks can test
various aspects of your SMTP server, including TLS and AUTH.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%to_utf8 doc/Changes.txt

%install
install -D -p -m 0755 swaks %buildroot/%_bindir/swaks
mkdir -p %buildroot/%_mandir/man1
/usr/bin/pod2man swaks > %buildroot/%_mandir/man1/swaks.1

%files
%_bindir/swaks
%_mandir/man1/*
%license LICENSE.txt
%doc README.txt doc/Changes.txt doc/recipes.txt doc/ref.txt

%changelog
%autochangelog
