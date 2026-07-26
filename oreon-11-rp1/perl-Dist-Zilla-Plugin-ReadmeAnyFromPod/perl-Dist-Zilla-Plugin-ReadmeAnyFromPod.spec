%global source0_hash d44f2799922f78b2a7961ed89123e11bdd77abfe85ba2040d82b80ad72ed13bc

Name:           perl-Dist-Zilla-Plugin-ReadmeAnyFromPod
Version:        0.163250
Release:        27%{?dist}
Summary:        Automatically convert POD to a README in any format for Dist::Zilla
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-ReadmeAnyFromPod
Source0:        https://cpan.metacpan.org/authors/id/R/RT/RTHOMPSON/Dist-Zilla-Plugin-ReadmeAnyFromPod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::AfterBuild)
BuildRequires:  perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::FileWatcher)
BuildRequires:  perl(Dist::Zilla::Role::PPI)
BuildRequires:  perl(Encode)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Has::Sugar)
BuildRequires:  perl(Path::Tiny) >= 0.004
BuildRequires:  perl(Pod::Markdown) >= 2.000
BuildRequires:  perl(Pod::Markdown::Github)
BuildRequires:  perl(Pod::Simple::HTML) >= 3.23
BuildRequires:  perl(Pod::Simple::Text) >= 3.23
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle::Easy)
# English not used
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
# Test::Kwalitee 1.21 not used
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Most)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Test::Requires)
# Test::Vars not used
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(Dist::Zilla::Plugin::PodWeaver)
Requires:       perl(Dist::Zilla::File::InMemory)
Requires:       perl(Dist::Zilla::Role::AfterBuild)
Requires:       perl(Dist::Zilla::Role::AfterRelease)
Requires:       perl(Dist::Zilla::Role::FileGatherer)
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Dist::Zilla::Role::FilePruner)
Requires:       perl(Dist::Zilla::Role::FileWatcher)
Requires:       perl(Dist::Zilla::Role::PPI)
Requires:       perl(Encode)
Requires:       perl(Pod::Markdown) >= 2.000
Requires:       perl(Pod::Markdown::Github)
Requires:       perl(Pod::Simple::HTML) >= 3.23
Requires:       perl(Pod::Simple::Text) >= 3.23
Requires:       perl(PPI::Document)

%description
This Perl module generates a README for your Dist::Zilla-powered distribution
from its main_module in any of several formats. The generated README can be
included in the build or created in the root of your dist for e.g. inclusion
into version control.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-ReadmeAnyFromPod-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
