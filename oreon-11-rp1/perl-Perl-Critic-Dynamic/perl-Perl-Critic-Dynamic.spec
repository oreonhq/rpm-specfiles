%global source0_hash 4a4f05706abc46ae9c2f037f5d3fe01d987283214929bd01489f8ef9ed0f3df4

Name:           perl-Perl-Critic-Dynamic
Version:        0.05
Release:        40%{?dist}
Summary:        Non-static policies for Perl::Critic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Dynamic
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Perl-Critic-Dynamic-%{version}.tar.gz
# Adapt to changes in CGI-4.14, bug #1209554, CPAN RT#103382
Patch0:         Perl-Critic-Dynamic-0.05-test_AUTOLOAD_on_private_module.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.36
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Symdump) >= 2.07
BuildRequires:  perl(English)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.108
BuildRequires:  perl(Perl::Critic::Utils) >= 1.108
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Storable) >= 2.16
# Tests only:
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic::Policy)
Requires:       perl(Devel::Symdump) >= 2.07
Requires:       perl(Perl::Critic::Policy) >= 1.108
Requires:       perl(Perl::Critic::Utils) >= 1.108
Requires:       perl(Storable) >= 2.16

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Symdump\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Perl::Critic::(Policy|Utils)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Storable\\)$

%description
Perl::Critic is primarily used as a static source code analyzer, which means
that it never compiles or executes any of the code that it examines. But
since Perl is a dynamic language, there are certain types of problems that
cannot be discovered until the code is actually compiled.

This distribution includes Perl::Critic::DynamicPolicy, which can be used as
a base class for Policies that wish to compile the code they analyze. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Dynamic-%{version}
%patch -P0 -p0

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
