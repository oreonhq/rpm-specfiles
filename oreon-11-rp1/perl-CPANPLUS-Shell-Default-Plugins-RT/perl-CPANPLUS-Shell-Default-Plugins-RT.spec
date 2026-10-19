%global source0_hash 3c7933065eec4247f7c9f0b6f475825fcf79671d8748b6225bc27884379a3569
Name:       perl-CPANPLUS-Shell-Default-Plugins-RT 
Version:    0.01 
Release:        46%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Check for rt.cpan.org tickets from within the CPANPLUS shell
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KANE/CPANPLUS-Shell-Default-Plugins-RT-%{version}.tar.gz
Url:        https://metacpan.org/release/CPANPLUS-Shell-Default-Plugins-RT
BuildArch:  noarch
Requires:      perl(CPANPLUS::Shell::Default)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This plugin allows you to query rt.cpan.org tickets for a given
distribution within the CPANPLUS shell.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPANPLUS-Shell-Default-Plugins-RT-%{version}

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
