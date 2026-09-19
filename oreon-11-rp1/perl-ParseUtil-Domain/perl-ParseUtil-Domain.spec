%global source0_hash 69af103ceae7766c94d420053d82a64ebb91ee8e204c72bf67a57158ff9cd32b

Name:           perl-ParseUtil-Domain
Summary:        Utility for parsing a domain name into its components
Version:        2.427
Release:        25%{?dist}

# - ParseUtil::Domain is GPL+ or Artistic (the "Perl" license)
# - data/effective_tld_names.txt is MPL-2.0
# - ParseUtil::Domain::ConfigData is automatically generated during the build,
#   based on the contents of data/effective_tld_names.txt
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MPL-2.0

URL:            https://metacpan.org/release/ParseUtil-Domain
Source0:        https://cpan.metacpan.org/authors/id/H/HE/HEYTRAV/ParseUtil-Domain-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(autobox)
BuildRequires:  perl(autobox::Core)
BuildRequires:  perl(Carp) >= 1.17
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Mock::Quick)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Net::IDN::Encode) >= 2.003
BuildRequires:  perl(Net::IDN::Nameprep) >= 1.101
BuildRequires:  perl(Net::IDN::Punycode) >= 1.100
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Regexp::Assemble::Compressed)
#BuildRequires:  perl(Smart::Comments) - not used
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Routine)
BuildRequires:  perl(Test::Routine::Util)
#BuildRequires:  perl(Unicode::CharName) >= 1.07 - not used
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed

%{?perl_default_filter}

%description
A tool for parsing domain names. This module makes use of the data provided
by the Public Suffix List (http://publicsuffix.org/list/) to parse TLDs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ParseUtil-Domain-%{version}

# Remove incorrect executable bits
chmod -x lib/ParseUtil/Domain.pm \
         data/effective_tld_names.txt

# Add perl shebang to script
sed -i -e '1i#!%{__perl}' bin/suffix-regex.pl bin/punyconvert

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} %{buildroot}/*

%check
TEST_AUTHOR=1 make test

%files
%doc data/effective_tld_names.txt
%{_bindir}/punyconvert
%{_bindir}/suffix-regex.pl
%{_mandir}/man1/punyconvert.1*
%{_mandir}/man3/ParseUtil::Domain*3pm*
%{perl_vendorlib}/ParseUtil*

%changelog
%autochangelog
