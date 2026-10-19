%global source0_hash 29c8b2c30ebdb36fa90cb8a2d5d1b6c4637e98566fbc476262ba1c055fec2061
Name:           perl-IO-Prompter
Version:        0.005004
Release:        2%{?dist}
Summary:        Prompt for input, read it, clean it, return it
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://search.cpan.org/dist/IO-Prompter/
Source0:        https://www.cpan.org/modules/by-module/IO/IO-Prompter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Contextual::Return)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(lib)
BuildRequires:  perl(match::smart)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
IO::Prompter exports a single subroutine, prompt, that prints a prompt
(but only if the program's selected input and output streams are connected
to a terminal), then reads some input, then chomps it, and finally returns
an object representing that text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir IO-Prompter-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
