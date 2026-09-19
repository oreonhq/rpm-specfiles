%global source0_hash 88383a38f50371c4f11031e0d45bfe73ffa6579fdab1c467586253a5491d24e7

Name:           perl-Net-IMAP-Client
Version:        0.9511
Release:        2%{?dist}
Summary:        IMAP client library for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IMAP-Client
Source0:        http://www.cpan.org/authors/id/G/GA/GANGLION/Net-IMAP-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(vars)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(overload)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::MIME::Header)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)

%description
Net::IMAP::Client provides methods to access an IMAP server. It aims to
provide a simple and clean API, while employing a rigorous parser for IMAP
responses in order to create Perl data structures from them. The code is
simple, clean and extensible.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IMAP-Client-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/boilerplate.t
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*
%doc Changes META.json README

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
