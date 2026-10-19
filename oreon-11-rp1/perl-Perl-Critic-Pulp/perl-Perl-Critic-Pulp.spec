%global source0_hash 17d33add2260ac49791250ccd32da8bca8063bf6fcf406ddb12b3a0076578e98
Name:           perl-Perl-Critic-Pulp
Version:        100
Release:        2%{?dist}
Summary:        Some add-on perlcritic policies
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Perl-Critic-Pulp
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Perl-Critic-Pulp-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IO::String) >= 1.02
Requires:       perl(List::MoreUtils) >= 0.24
Requires:       perl(Perl::Critic) >= 1.084
Requires:       perl(Pod::MinimumVersion) >= 50
Requires:       perl(PPI::Document)
Requires:       perl(Test::More)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(List::MoreUtils\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::Policy\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::Utils\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::Utils\\) >= 0\\.21$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::PodParser::ProhibitVerbatimMarkup\\)\\s*$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Perl::MinimumVersion\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::PodParser::ProhibitVerbatimMarkup\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Policy::Documentation::ProhibitAdjacentLinks::Parser\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodMinimumVersionViolation\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitBadAproposMarkup\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitLinkToSelf\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitParagraphTwoDots\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitUnbalancedParens\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::RequireLinkedURLs\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::ProhibitDuplicateHashKeys::Qword\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(constant\\) >= 1\.
%global __requires_exclude %__requires_exclude|perl\\(:VERSION\\) >= 5\.10\.0$
%global __requires_exclude %__requires_exclude|perl\\(MyTestHelpers\\)
%global __provides_exclude %__provides_exclude|perl\\(MyTestHelpers\\)
Provides:       perl(Perl::Critic::Policy::Modules::ProhibitModuleShebang)
Provides:       perl(Perl::Critic::Pulp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Utils::PPI)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Perl::MinimumVersion)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::MinimumVersion)
BuildRequires:  perl(Pod::ParseLink)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a collection of add-on policies for Perl::Critic.  They're under
a "pulp" theme plus other themes according to their purpose (see "POLICY
THEMES" in Perl::Critic).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Data::Dumper)
Requires:       perl(PPI::Dumper)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-Critic-Pulp-%{version}
chmod +x t/*.t t/ProhibitModuleShebang/Script.pl

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Perl-Critic-Pulp-tests -f %{oreon_filedir}/perl-Perl-Critic-Pulp-tests.list

%changelog

%autochangelog
