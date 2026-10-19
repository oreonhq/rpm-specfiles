%global source0_hash e43a0e08143a7df5f04ec1fa84964ad16bd271cd763d90c74b9d55fa1d5a5906
Name:           perl-Perl-Critic-Bangs
Version:        1.14
Release:        1%{?dist}
Summary:        Collection of handy Perl::Critic policies
License:        Artistic-2.0
URL:            https://metacpan.org/release/Perl-Critic-Bangs
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-Bangs-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Critic) >= 1.122
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::PolicyFactory)
BuildRequires:  perl(Perl::Critic::PolicyParameter)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::UserProfile)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a MANIFEST t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/93_version.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Perl-Critic-Bangs-tests -f %{oreon_filedir}/perl-Perl-Critic-Bangs-tests.list

%changelog

%autochangelog
