%global source0_hash 37d66bfe205d7916824a46ad6290b8fb170fc602c16f8dc8169576f2ad682949
Name:           perl-Path-IsDev
Version:        1.001003
Release:        26%{?dist}
Summary:        Determine if a given Path resembles a development source tree
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Path-IsDev
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Path-IsDev-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(File::HomeDir)
Requires:       perl(Module::Runtime)
Requires:       perl(Path::Tiny)
Requires:       perl(Scalar::Util)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Class::Tiny\\)\\s*$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is more or less a bunch of heuristics for determining if a
given path is a development tree root of some kind.

This has many useful applications, notably ones that require behaviors for
"installed" modules to be different to those that are still "in
development"

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Path-IsDev-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
