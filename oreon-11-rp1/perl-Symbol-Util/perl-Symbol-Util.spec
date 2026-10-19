%global source0_hash 55b661dd22f9ce9b9be5a7e0a3f5289ac00cd254c21e3d8603289a565ae6dc32
Name:           perl-Symbol-Util
Version:        0.0203
Release:        39%{?dist}
Summary:        Additional utilities for Perl symbols manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Symbol-Util
Source0:        https://cpan.metacpan.org/modules/by-module/Symbol/Symbol-Util-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Provides:       perl(Symbol::Util)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a set of additional functions useful for Perl symbols
manipulation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Symbol-Util-%{version}
chmod -c -x xt/cover.pl
chmod -c -x examples/delete_glob.pl

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
