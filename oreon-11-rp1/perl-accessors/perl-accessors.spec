%global source0_hash 3a8db00f38148f3afadbe5330dc5490d9933f9cae137e842ec225a4d3adb2d9f
Name:           perl-accessors
Version:        1.01
Release:        1%{?dist}
Summary:        Create accessor methods in caller's package
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/accessors
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/accessors-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(accessors)
Provides:       perl(accessors)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The accessors pragma lets you create simple accessors at compile-time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n accessors-%{version}

# A few of the .pm modules have bogus execute permission
find . -name '*.pm' | xargs chmod -c a-x

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.01-47
- Prepare for Oreon 11 (RP1)
