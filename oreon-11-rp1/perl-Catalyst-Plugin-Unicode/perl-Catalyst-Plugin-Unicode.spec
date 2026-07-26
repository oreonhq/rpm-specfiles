%global source0_hash 03a5adfed1b44280583ee4231ed529ccbc0f719ca368faa3aad3c024a8999082

Name:           perl-Catalyst-Plugin-Unicode
Version:        0.93
Release:        45%{?dist}
Summary:        Unicode aware Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Unicode
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Unicode-%{version}.tar.gz
# Define POD encoding, CPAN RT#87666
Patch0:         Catalyst-Plugin-Unicode-0.93-Define-POD-encoding.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
# This is a Catalyst plugin
BuildRequires:  perl(Catalyst::Runtime) >= 5.70
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
# Catalyst::Engine::HTTP not used
# Catalyst::Test not used
BuildRequires:  perl(FindBin)
# Getopt::Long not used
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(lib)
BuildRequires:  perl(ok)
# Pod::Usage not used
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# This is a Catalyst plugin
Requires:       perl(Catalyst::Runtime) >= 5.70

%{?perl_default_filter}

%description
On request, decodes all params from UTF-8 octets into a sequence of logical
characters. On response, encodes body into UTF-8 octets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Unicode-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
