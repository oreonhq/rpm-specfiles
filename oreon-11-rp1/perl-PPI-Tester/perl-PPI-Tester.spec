%global source0_hash cdc02e777d2b02a4a9f3644017232cc6e6d8215d10aca9ea1ea5c185137ca29f
Name:           perl-PPI-Tester
Version:        0.15
Release:        35%{?dist}
Summary:        A wxPerl-based interactive PPI debugger/tester
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI-Tester
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/PPI-Tester-%{version}.tar.gz
Patch0:         PPI-Tester-0.15-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
Requires:       perl(Wx::Frame)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  font(:lang=en)
BuildRequires:  make
BuildRequires:  perl(Devel::Dumpvar)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(Wx)
BuildRequires:  perl(Wx::Event)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
# /oreon:deps
%description
This package implements a wxWindows desktop application which provides
the ability to interactively test the PPI perl parser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PPI-Tester-%{version}
%patch -P0 -p1
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 || :
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
