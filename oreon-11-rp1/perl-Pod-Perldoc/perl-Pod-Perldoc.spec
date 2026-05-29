%global source0_hash cc41e605b8e13c40a8ee6504ff46347b5ba7fbd92203b3bb055422051befc64d

# Optional features
# Run Tk tests
%bcond_with perl_Pod_Perldoc_enables_tk_test
# Support for groff
%bcond_without perl_enables_groff

%global base_version 3.28
Name:           perl-Pod-Perldoc
# let's overwrite the module from perl.srpm
Version:        3.28.01
Release:        522%{?dist}
Summary:        Look up Perl documentation in Pod format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Perldoc
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MALLEN/Pod-Perldoc-3.28.tar.gz
# Unbundled from perl 5.28.0-RC1
Patch0:         Pod-Perldoc-3.28-Upgrade-to-3.2801.patch
# 1/2 Fix searching for builtins in perlop POD, bug #1739463, CPAN RT#126015
Patch1:         Pod-Perldoc-3.28-Add-a-test-for-a-truncated-perldoc-f-tr-output.patch
# 1/2 Fix searching for builtins in perlop POD, bug #1739463, CPAN RT#126015
Patch2:         Pod-Perldoc-3.28-Search-for-X-in-the-whole-perlop-document.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
%if %{with perl_enables_groff}
# Pod::Perldoc::ToMan executes roff
BuildRequires:  groff-base
%endif
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
# File::Temp 0.22 not used by tests
# HTTP::Tiny not used by tests
# IO::Handle not used by tests
BuildRequires:  perl(IO::Select)
# IPC::Open3 not used by tests
BuildRequires:  perl(parent)
# POD2::Base is optional
# Pod::Checker is not needed if Pod::Simple::Checker is available
BuildRequires:  perl(Pod::Man) >= 2.18
BuildRequires:  perl(Pod::Simple::Checker)
BuildRequires:  perl(Pod::Simple::RTF) >= 3.16
BuildRequires:  perl(Pod::Simple::XMLOutStream) >= 3.16
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Pod::Text::Color)
BuildRequires:  perl(Pod::Text::Termcap)
# Symbol not used by tests
# Text::ParseWords not used by tests
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap}
%if !( 0%{?rhel} >= 7 ) || 0%{?oreon}
%if %{with perl_Pod_Perldoc_enables_tk_test}
BuildRequires:  perl(Tk)
# Tk::FcyEntry is optional
BuildRequires:  perl(Tk::Pod)
%endif
%endif
%endif
%if %{with perl_enables_groff}
# Pod::Perldoc::ToMan executes roff
Requires:       groff-base
%endif
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Tiny)
Requires:       perl(IO::Handle)
Requires:       perl(IPC::Open3)
# POD2::Base is optional
# Pod::Checker is not needed if Pod::Simple::Checker is available
Requires:       perl(Pod::Simple::Checker)
Requires:       perl(Pod::Simple::RTF) >= 3.16
Requires:       perl(Pod::Simple::XMLOutStream) >= 3.16
Requires:       perl(Text::ParseWords)
# Tk is optional
Requires:       perl(Symbol)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Pod::Man|Pod::Simple::XMLOutStream|Pod::Simple::RTF)\\)$

%description
perldoc looks up a piece of documentation in POD format that is embedded
in the perl installation tree or in a Perl script, and displays it via
"groff -man | $PAGER". This is primarily used for the documentation for
the Perl library modules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Pod-Perldoc-%{base_version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{_bindir}/perldoc
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.28.01-522
- Import
