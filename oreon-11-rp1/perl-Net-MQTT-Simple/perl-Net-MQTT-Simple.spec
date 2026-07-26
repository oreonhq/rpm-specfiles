%global source0_hash 58539c1c2794d25872652d78a26c9fd26b627bdad1b9134a159869c1b2822aa7

Name:           perl-Net-MQTT-Simple
Version:        1.33
Release:        2%{?dist}
Summary:        Minimal MQTT version 3 interface

# Chosen from https://opensource.org/licenses/alphabetical
# as allowed by the original licence text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-MQTT-Simple
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/Net-MQTT-Simple-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module consists of only one file and has no dependencies except core
Perl modules, making it suitable for embedded installations where CPAN
installers are unavailable and resources are limited. Only basic MQTT
functionality is provided.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-MQTT-Simple-%{version}

%build
export PERL_MM_USE_DEFAULT=yes
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --no-online-tests
%make_build OPTIMIZE="%{optflags}"

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net/
%{_bindir}/mqtt-simple
%{_mandir}/man1/mqtt-simple.1*
%{_mandir}/man3/Net::MQTT::Simple*.3*

%changelog
%autochangelog
