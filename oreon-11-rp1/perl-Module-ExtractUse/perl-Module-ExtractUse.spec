%global source0_hash 8ee24e8742ab9da79228be187dda319b4d5f50a91a1ecf87d494213b5bb30dd1
Name:           perl-Module-ExtractUse
Version:        0.345
Release:        9%{?dist}
Summary:        Find out which modules are used
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-ExtractUse
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-ExtractUse-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pod::Strip)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::ExtractUse is basically a Parse::RecDescent grammar to parse Perl
code. It tries very hard to find all modules (whether pragmas, Core, or
from CPAN) used by the parsed code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-ExtractUse-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
./Build test --test_files="xt/*.t"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
