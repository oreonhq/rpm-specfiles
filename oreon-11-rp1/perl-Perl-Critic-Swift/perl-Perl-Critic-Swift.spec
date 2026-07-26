%global source0_hash eb8a36c11ef75df2ac4428f5311168e3e8425a25f593c271d09de20700f8d89d

Name:           perl-Perl-Critic-Swift
Version:        1.0.3
Release:        45%{?dist}
Summary:        Set of additional policies for Perl::Critic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Swift
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-Swift-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(English)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(List::MoreUtils) >= 0.21
BuildRequires:  perl(Perl::Critic::Policy) >= 1.082
BuildRequires:  perl(Perl::Critic::Utils) >= 1.082
BuildRequires:  perl(version)
# Tests:
# Author tests are not executed
# File::Find not used
# File::Slurp not used
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.082
# PPI::Cache not used
# Test::Distribution not used
# Test::Kwalitee not used
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic) >= 1.01
# Test::Pod not used
# Test::Pod::Coverage not sued
# Test::Spelling not used
Requires:       perl(List::MoreUtils) >= 0.21
Requires:       perl(Perl::Critic::Policy) >= 1.082
Requires:       perl(Perl::Critic::Utils) >= 1.082

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\((List::MoreUtils|Perl::Critic::Policy|Perl::Critic::Utils)\\)*$
# Export not detected versions: $VERSION = qv('v%%{version}')
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Perl::Critic::[^=]*)$\)/\1 = %{version}

%description
Some Perl::Critic policies to make your code more clean. The included
policies are:

    * Perl::Critic::Policy::CodeLayout::RequireUseUTF8
    * Perl::Critic::Policy::Documentation::RequirePODUseEncodingUTF8

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Swift-v%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
