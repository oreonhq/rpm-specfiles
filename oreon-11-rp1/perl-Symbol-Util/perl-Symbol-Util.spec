%global source0_hash 55b661dd22f9ce9b9be5a7e0a3f5289ac00cd254c21e3d8603289a565ae6dc32

Name:           perl-Symbol-Util
Version:        0.0203
Release:        39%{?dist}
Summary:        Additional utilities for Perl symbols manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Symbol-Util
Source0:        https://cpan.metacpan.org/modules/by-module/Symbol/Symbol-Util-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(Carp)

Provides:       perl(Symbol::Util)
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

%check
./Build test

%files
%license LICENSE
%doc Changes examples/ README xt/
%{perl_vendorlib}/Symbol/
%{_mandir}/man3/Symbol::Util.3*

%changelog
%autochangelog
