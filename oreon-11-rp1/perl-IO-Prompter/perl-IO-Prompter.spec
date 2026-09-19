%global source0_hash 29c8b2c30ebdb36fa90cb8a2d5d1b6c4637e98566fbc476262ba1c055fec2061

Name:           perl-IO-Prompter
Version:        0.005004
Release:        2%{?dist}
Summary:        Prompt for input, read it, clean it, return it

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://search.cpan.org/dist/IO-Prompter/
Source0:        https://www.cpan.org/modules/by-module/IO/IO-Prompter-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.010
BuildRequires:  perl(Carp)
BuildRequires:  perl(Contextual::Return)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(match::smart)

%description
IO::Prompter exports a single subroutine, prompt, that prints a prompt
(but only if the program's selected input and output streams are connected
to a terminal), then reads some input, then chomps it, and finally returns
an object representing that text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n IO-Prompter-%{version} -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
