%global source0_hash 3c5e08329106f9cee3ab444b81331c5935f83084a151d88505e7a465da540f41
Name:           perl-FreezeThaw
Version:        0.5001
Release:        48%{?dist}
Summary:        Convert Perl structures to strings and back
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/FreezeThaw
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILYAZ/modules/FreezeThaw-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(FreezeThaw)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(dumpvar.pl)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Converts data to/from stringified form, appropriate for
saving-to/reading-from permanent storage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n FreezeThaw-%{version}

# Fix permissions
find -type f -exec chmod -c -x {} \;

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
