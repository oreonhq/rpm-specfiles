%global source0_hash cc41e605b8e13c40a8ee6504ff46347b5ba7fbd92203b3bb055422051befc64d
%bcond_with perl_Pod_Perldoc_enables_tk_test
%bcond_without perl_enables_groff
%global base_version 3.28
Name:           perl-Pod-Perldoc
Version:        3.28.01
Release:        522%{?dist}
Summary:        Look up Perl documentation in Pod format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Perldoc
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MALLEN/Pod-Perldoc-3.28.tar.gz
Patch0:         Pod-Perldoc-3.28-Upgrade-to-3.2801.patch
Patch1:         Pod-Perldoc-3.28-Add-a-test-for-a-truncated-perldoc-f-tr-output.patch
Patch2:         Pod-Perldoc-3.28-Search-for-X-in-the-whole-perlop-document.patch
BuildArch:      noarch
%if %{with perl_enables_groff}
%endif
%if !%{defined perl_bootstrap}
%if !( 0%{?rhel} >= 7 ) || (0%{?oreon} >= 11)
%if %{with perl_Pod_Perldoc_enables_tk_test}
%endif
%endif
%endif
%if %{with perl_enables_groff}
Requires:       groff-base
%endif
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Tiny)
Requires:       perl(IO::Handle)
Requires:       perl(IPC::Open3)
Requires:       perl(Pod::Simple::Checker)
Requires:       perl(Pod::Simple::RTF) >= 3.16
Requires:       perl(Pod::Simple::XMLOutStream) >= 3.16
Requires:       perl(Text::ParseWords)
Requires:       perl(Symbol)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Pod::Man|Pod::Simple::XMLOutStream|Pod::Simple::RTF)\\)$
Provides:       perl(Pod::Perldoc)
Provides:       perl(Pod::Perldoc::ToMan)
# oreon:deps
BuildRequires:  groff-base
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple::Checker)
BuildRequires:  perl(Pod::Simple::RTF)
BuildRequires:  perl(Pod::Simple::XMLOutStream)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Pod::Text::Color)
BuildRequires:  perl(Pod::Text::Termcap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
perldoc looks up a piece of documentation in POD format that is embedded
in the perl installation tree or in a Perl script, and displays it via
"groff -man | $PAGER". This is primarily used for the documentation for
the Perl library modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.28.01-522
- Import
