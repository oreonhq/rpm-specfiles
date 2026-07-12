%global source0_hash 17d33add2260ac49791250ccd32da8bca8063bf6fcf406ddb12b3a0076578e98

Name:           perl-Perl-Critic-Pulp
Version:        100
Release:        2%{?dist}
Summary:        Some add-on perlcritic policies
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Perl-Critic-Pulp
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Perl-Critic-Pulp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Scripts in ./devel and ./xtools are not executed.
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::String) >= 1.02
BuildRequires:  perl(List::MoreUtils) >= 0.24
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Perl::Critic) >= 1.084
BuildRequires:  perl(Perl::Critic::Policy) >= 1.084
BuildRequires:  perl(Perl::Critic::Utils) >= 1.100
BuildRequires:  perl(Perl::Critic::Utils::PPI)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::MinimumVersion) >= 50
BuildRequires:  perl(Pod::ParseLink)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI) >= 1.220
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests only:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Test::More)
# Optional tests only:
# Devel::FindRef not needed
# Devel::StackTrace not needed
BuildRequires:  perl(Perl::MinimumVersion)
Requires:       perl(IO::String) >= 1.02
Requires:       perl(List::MoreUtils) >= 0.24
Requires:       perl(Perl::Critic) >= 1.084
Requires:       perl(Pod::MinimumVersion) >= 50
Requires:       perl(PPI::Document)
# This is plug-in into Test::More. Depend on it even if not mentioned in the
# code.
Requires:       perl(Test::More)

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(List::MoreUtils\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::Policy\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::Utils\\)\\s*$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::Utils\\) >= 0\\.21$
%global __requires_exclude %__requires_exclude|perl\\(Perl::Critic::PodParser::ProhibitVerbatimMarkup\\)\\s*$
# Filter private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Perl::MinimumVersion\\)\\s*$
# Filter private parsers 
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::PodParser::ProhibitVerbatimMarkup\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Policy::Documentation::ProhibitAdjacentLinks::Parser\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodMinimumVersionViolation\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitBadAproposMarkup\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitLinkToSelf\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitParagraphTwoDots\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::ProhibitUnbalancedParens\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::PodParser::RequireLinkedURLs\\)\\s*$
%global __provides_exclude %__provides_exclude|perl\\(Perl::Critic::Pulp::ProhibitDuplicateHashKeys::Qword\\)\\s*$
# Filter parsed, but never executed code in the tests
%global __requires_exclude %__requires_exclude|perl\\(constant\\) >= 1\.
%global __requires_exclude %__requires_exclude|perl\\(:VERSION\\) >= 5\.10\.0$
# Filter private modules in the tests
%global __requires_exclude %__requires_exclude|perl\\(MyTestHelpers\\)
%global __provides_exclude %__provides_exclude|perl\\(MyTestHelpers\\)

Provides:       perl(Perl::Critic::Policy::Modules::ProhibitModuleShebang)
Provides:       perl(Perl::Critic::Pulp)
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorlib}/Perl/
%{_mandir}/man3/Perl::Critic::Policy::CodeLayout::ProhibitFatCommaNewline.3*
%{_mandir}/man3/Perl::Critic::Policy::CodeLayout::ProhibitIfIfSameLine.3*
%{_mandir}/man3/Perl::Critic::Policy::CodeLayout::RequireFinalSemicolon.3*
%{_mandir}/man3/Perl::Critic::Policy::CodeLayout::RequireTrailingCommaAtNewline.3*
%{_mandir}/man3/Perl::Critic::Policy::Compatibility::ConstantLeadingUnderscore.3*
%{_mandir}/man3/Perl::Critic::Policy::Compatibility::ConstantPragmaHash.3*
%{_mandir}/man3/Perl::Critic::Policy::Compatibility::Gtk2Constants.3*
%{_mandir}/man3/Perl::Critic::Policy::Compatibility::PerlMinimumVersionAndWhy.3*
%{_mandir}/man3/Perl::Critic::Policy::Compatibility::PodMinimumVersion.3*
%{_mandir}/man3/Perl::Critic::Policy::Compatibility::ProhibitUnixDevNull.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitAdjacentLinks.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitBadAproposMarkup.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitDuplicateHeadings.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitDuplicateSeeAlso.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitLinkToSelf.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitParagraphEndComma.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitParagraphTwoDots.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitUnbalancedParens.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::ProhibitVerbatimMarkup.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::RequireEndBeforeLastPod.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::RequireFilenameMarkup.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::RequireFinalCut.3*
%{_mandir}/man3/Perl::Critic::Policy::Documentation::RequireLinkedURLs.3*
%{_mandir}/man3/Perl::Critic::Policy::Miscellanea::TextDomainPlaceholders.3*
%{_mandir}/man3/Perl::Critic::Policy::Miscellanea::TextDomainUnused.3*
%{_mandir}/man3/Perl::Critic::Policy::Modules::ProhibitModuleShebang.3*
%{_mandir}/man3/Perl::Critic::Policy::Modules::ProhibitPOSIXimport.3*
%{_mandir}/man3/Perl::Critic::Policy::Modules::ProhibitUseQuotedVersion.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ConstantBeforeLt.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::NotWithCompare.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitArrayAssignAref.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitBarewordDoubleColon.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitDuplicateHashKeys.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitEmptyCommas.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitFiletest_f.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitNullStatements.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::ProhibitUnknownBackslash.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::RequireNumericVersion.3*
%{_mandir}/man3/Perl::Critic::Policy::ValuesAndExpressions::UnexpandedSpecialLiteral.3*
%{_mandir}/man3/Perl::Critic::Pulp.3*
%{_mandir}/man3/Perl::Critic::Pulp::PodParser.3*
%{_mandir}/man3/Perl::Critic::Pulp::Utils.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
