%global source0_hash 7c3c89e779baa83afaf0dc9599c20f90b3e613ea3ece0328931257ab7cc24a99
Name:           perl-Module-Package
Version:        0.30
Release:        1%{?dist}
Summary:        Postmodern Perl Module Packaging
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Package
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Package-%{version}.tar.gz
Patch0:         Module-Package-0.30-Fix-building-on-Perl-without-.-in-INC.patch
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(File::Path)
Provides:       perl(Module::Package)
Provides:       perl(Module::Package::Plugin)
Provides:       perl(inc::Module::Package)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::ManifestSkip)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module is a drop-in replacement for Module::Install. It does everything
Module::Install does, but just a bit better.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Package-%{version}
%patch -P0 -p1
# XXX: Do not unbundle ./inc/ because of bootstrap

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-39
- Prepare for Oreon 11 (RP1)
