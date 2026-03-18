Name:           perl-Config-IniFiles
Version:        3.000003
Release:        18%{?dist}
Summary:        A module for reading .ini-style configuration files
# LICENSE:                              GPL+ or Artistic
# lib/Config/IniFiles.pm:               GPL+ or Artistic
## Not distributed in a binary package
# t/30parameters-with-empty-values.t:   MIT
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-IniFiles
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Config-IniFiles-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.36
# Module::Build::Compat not used, we run Build.PL
BuildRequires:  perl(strict)
# Test::Run::CmdLine::Iface not used
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Scalar) >= 2.109
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildArch:      noarch
# Not autodetected. Found in lib/Config/IniFiles.pm:2761
Requires:       perl(IO::Scalar) >= 2.109
# Also not autodetected
Requires:       perl(List::Util) >= 1.33

# Filter under-specified requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::MoreUtils\\)$

%description
Config::IniFiles provides a way to have readable configuration files
outside your Perl script. Configurations can be imported (inherited,
stacked,...), sections can be grouped, and settings can be accessed
from a tied hash.

%prep
%setup -q -n Config-IniFiles-%{version}
# Normalize end-of-lines
sed -i -e 's/\r$//' Changes OLD-Changes.txt

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes OLD-Changes.txt README
%{perl_vendorlib}/Config/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.000003-18
- Prepare for Oreon 11 (RP1)
