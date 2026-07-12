%global source0_hash 4e3bebec1bf82dbf850a94ae26a253644cf5806ec41afc74e43e1710a37321db

# Perform optinal tests
%bcond_without perl_podlinkcheck_enables_optional_test

Name:           perl-podlinkcheck
Version:        15
Release:        30%{?dist}
Summary:        Check Perl POD L<> link references
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/podlinkcheck
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/podlinkcheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# Config not used at tests
BuildRequires:  perl(constant::defer)
# File::Find::Iterator not used at tests
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
# FindBin not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::TextDomain)
# Pod::Find not used at tests
BuildRequires:  perl(Pod::Simple)
# Search::Dict not used at tests
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(vars)
# Recommended run-time:
# Sort::Key::Natural not used at tests
# Tests:
BuildRequires:  perl(Config)
# Data::Dumper not used
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
%if %{with perl_podlinkcheck_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Dumper)
# Devel::FindRef does not built with Perl 5.22
# Devel::StackTrace not used
%endif
Requires:       perl(Config)
Requires:       perl(File::Find::Iterator)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(File::Temp)
Requires:       perl(FindBin)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Run)
Requires:       perl(Pod::Find)
Requires:       perl(Search::Dict)
# Recommended:
Recommends:     perl(Sort::Key::Natural)
# We do not (build-)require CPAN, CPANPLUS on purpose
Suggests:       perl(CPAN)
Suggests:       perl(CPAN::SQLite)
Suggests:       perl(CPANPLUS::Backend)
Suggests:       perl(CPANPLUS::Configure)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(MyTestHelpers\\)
%global __provides_exclude %{?__provides_exclude:%{__requires_exclude}|}^perl\\(MyTestHelpers\\)

Provides:       perl(App::PodLinkCheck::ParseLinks)
Provides:       perl(App::PodLinkCheck::ParseSections)
Provides:       perl(podlinkcheck)
%description
PodLinkCheck parses Perl POD from a script, module or documentation
and checks that L<> links within it refer to a known program, module,
or man page.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Config)
Requires:       perl(Scalar::Util)
%if %{with perl_podlinkcheck_enables_optional_test}
Requires:       perl(Data::Dumper)
Requires:       perl(File::HomeDir)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n podlinkcheck-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license COPYING
%doc Changes
%{_bindir}/podlinkcheck
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/PodLinkCheck
%{perl_vendorlib}/App/PodLinkCheck.pm
%{_mandir}/man1/podlinkcheck.*
%{_mandir}/man3/App::PodLinkCheck.*
%{_mandir}/man3/App::PodLinkCheck::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
