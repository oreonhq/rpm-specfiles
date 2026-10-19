%global source0_hash 46bd9d735595317235b7feaf5ffc55e1491e54186c159277357daf97287d836b
Name:       perl-CPANPLUS-Shell-Default-Plugins-Changes 
Version:    0.02 
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        View a module's Changes file from the CPANPLUS shell
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARJEN/CPANPLUS-Shell-Default-Plugins-Changes-%{version}.tar.gz
Url:        https://metacpan.org/release/CPANPLUS-Shell-Default-Plugins-Changes
BuildArch:  noarch
Requires:      perl(CPANPLUS::Shell::Default)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
