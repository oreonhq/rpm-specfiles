%global source0_hash 4b23542491af010d44a5c7c861244738acc74ababae6b8838d354dfb19462b5e
Name:		perl-Readonly
Version:	2.05
Release:        1%{?dist}
Summary:        Facility for creating read-only scalars, arrays, hashes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Readonly
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SANKO/Readonly-%{version}.tar.gz
Patch0:		Readonly-2.05-interpreter.patch
BuildArch:	noarch
Requires:	perl(Carp)
Requires:	perl(Storable)
Provides:       perl(Readonly)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Readonly provides a facility for creating non-modifiable scalars,
arrays, and hashes. Any attempt to modify a Readonly variable throws
an exception.

Readonly:
* Creates scalars, arrays (not lists), and hashes
* Creates variables that look and work like native perl variables
* Creates global or lexical variables
* Works at run-time or compile-time
* Works with deep or shallow data structures
* Prevents reassignment of Readonly variables

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Readonly-%{version}

# Fix script interpreter for test suite since we're packaging it
%patch -P0

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.05-30
- Prepare for Oreon 11 (RP1)
