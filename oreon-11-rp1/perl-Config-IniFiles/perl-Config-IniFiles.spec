%global source0_hash 4f6f8eb0c4efbc9398a0f1ef0c97fb7704eee4ccd90af1a31dda32854aa81164
Name:           perl-Config-IniFiles
Version:        3.003000
Release:        1%{?dist}
Summary:        A module for reading .ini-style configuration files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-IniFiles
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Config-IniFiles-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IO::Scalar) >= 2.109
Requires:       perl(List::Util) >= 1.33
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::MoreUtils\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Config::IniFiles provides a way to have readable configuration files
outside your Perl script. Configurations can be imported (inherited,
stacked,...), sections can be grouped, and settings can be accessed
from a tied hash.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Config-IniFiles-%{version}
# Normalize end-of-lines
sed -i -e 's/\r$//' Changes OLD-Changes.txt

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
