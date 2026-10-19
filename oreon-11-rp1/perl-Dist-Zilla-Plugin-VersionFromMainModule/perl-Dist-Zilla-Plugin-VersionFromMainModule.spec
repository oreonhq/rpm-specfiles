%global source0_hash 8bbb3d8d0e972d1d81c626a8a4edcc5e65e37e9f9fa35ba50d73228f8d3378ec
Name:           perl-Dist-Zilla-Plugin-VersionFromMainModule
Version:        0.04
Release:        1%{?dist}
Summary:        Set the distribution version from your main module's version
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-VersionFromMainModule
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Dist-Zilla-Plugin-VersionFromMainModule-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla::Role::ModuleMetadata)
Requires:       perl(Dist::Zilla::Role::VersionProvider)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Dist::Zilla::Role::ModuleMetadata)
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Dist::Zilla plugin sets the distribution version from the $VERSION
variable found in the distribution's main module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-VersionFromMainModule-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
