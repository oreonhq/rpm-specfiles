%global source0_hash 3c7933065eec4247f7c9f0b6f475825fcf79671d8748b6225bc27884379a3569

Name:       perl-CPANPLUS-Shell-Default-Plugins-RT 
Version:    0.01 
Release:    46%{?dist}
# see README 
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Check for rt.cpan.org tickets from within the CPANPLUS shell 
Source:     https://cpan.metacpan.org/authors/id/K/KA/KANE/CPANPLUS-Shell-Default-Plugins-RT-%{version}.tar.gz 
Url:        https://metacpan.org/release/CPANPLUS-Shell-Default-Plugins-RT
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(strict)
# Run-time
BuildRequires: perl(CPANPLUS) >= 0.059
BuildRequires: perl(CPANPLUS::Error)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Params::Check) >= 0.23
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(lib)
BuildRequires: perl(Test::More)
# not automagically picked up...
Requires:      perl(CPANPLUS::Shell::Default)

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

%check
make test

%files
%doc README 
%{perl_vendorlib}/*

%changelog
%autochangelog
