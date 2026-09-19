%global source0_hash 46bd9d735595317235b7feaf5ffc55e1491e54186c159277357daf97287d836b

Name:       perl-CPANPLUS-Shell-Default-Plugins-Changes 
Version:    0.02 
Release:    46%{?dist}
# lib/CPANPLUS/Shell/Default/Plugins/Changes.pm -> GPL+ or Artistic
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    View a module's Changes file from the CPANPLUS shell 
Source:     https://cpan.metacpan.org/authors/id/A/AR/ARJEN/CPANPLUS-Shell-Default-Plugins-Changes-%{version}.tar.gz 
Url:        https://metacpan.org/release/CPANPLUS-Shell-Default-Plugins-Changes
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time
BuildRequires: perl(CPANPLUS) >= 0.059
BuildRequires: perl(CPANPLUS::Error)
BuildRequires: perl(DirHandle)
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(lib)
BuildRequires: perl(Test::More)
# not automagically picked up, but useless w/o
Requires:      perl(CPANPLUS::Shell::Default)

%description
This plugin allows you to display the Changes (or Changelog, ChangeLog,
etc) file of a module to get an overview of what (according to the
maintainer) has changed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPANPLUS-Shell-Default-Plugins-Changes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
