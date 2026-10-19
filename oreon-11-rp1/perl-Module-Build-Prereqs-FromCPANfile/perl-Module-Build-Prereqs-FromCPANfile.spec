%global source0_hash 94d17867bea8e04bf8a636bcbfb78c5d432cb8fbc0e046b88445c3983e089e29
Name:           perl-Module-Build-Prereqs-FromCPANfile
Version:        0.02
Release:        9%{?dist}
Summary:        Construct prereq parameters of Module::Build from cpanfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Build-Prereqs-FromCPANfile
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/Module-Build-Prereqs-FromCPANfile-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Module::Build) >= 0.4004
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This simple module reads cpanfile and converts its content into valid
prereq parameters for new() method of Module::Build.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Build-Prereqs-FromCPANfile-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
