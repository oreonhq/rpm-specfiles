%global source0_hash e43a0e08143a7df5f04ec1fa84964ad16bd271cd763d90c74b9d55fa1d5a5906

Name:           perl-Perl-Critic-Bangs
Version:        1.14
Release:        4%{?dist}
Summary:        Collection of handy Perl::Critic policies
License:        Artistic-2.0
URL:            https://metacpan.org/release/Perl-Critic-Bangs
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-Bangs-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Perl::Critic) >= 1.122
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
# Tests only:
BuildRequires:  perl(English)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(lib)
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Perl::Critic::PolicyFactory)
BuildRequires:  perl(Perl::Critic::PolicyParameter)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::UserProfile)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Perl::Critic) >= 1.122

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
The rules included with the Perl::Critic::Bangs group include:
  - Commented-out code is usually noise.  It should be removed.
  - Watch for comments like "XXX", "TODO", etc.
  - Tests should have a plan.
  - Variables like $user and $user2 are insufficiently distinguished.
  - Determining the class in a constructor by using "ref($proto) || $proto".
  - Adding modifiers to a regular expression made up entirely of a variable
  created with qr() is usually not doing what you expect.
  - Vague variables like $data or $info are not descriptive enough.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Bangs-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
# t/00_modules.t locates policies in MANIFEST
cp -a MANIFEST t %{buildroot}%{_libexecdir}/%{name}
# Remove tests that need modules in blib
rm %{buildroot}%{_libexecdir}/%{name}/t/93_version.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md TODO
%dir %{perl_vendorlib}/Perl
%dir %{perl_vendorlib}/Perl/Critic
%{perl_vendorlib}/Perl/Critic/Bangs.pm
%dir %{perl_vendorlib}/Perl/Critic/Policy
%{perl_vendorlib}/Perl/Critic/Policy/Bangs
%{_mandir}/man3/Perl::Critic::Bangs.*
%{_mandir}/man3/Perl::Critic::Policy::Bangs::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
