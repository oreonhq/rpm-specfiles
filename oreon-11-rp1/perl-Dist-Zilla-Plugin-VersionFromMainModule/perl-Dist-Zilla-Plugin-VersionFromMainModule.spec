%global source0_hash 8bbb3d8d0e972d1d81c626a8a4edcc5e65e37e9f9fa35ba50d73228f8d3378ec

Name:           perl-Dist-Zilla-Plugin-VersionFromMainModule
Version:        0.04
Release:        24%{?dist}
Summary:        Set the distribution version from your main module's version
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-VersionFromMainModule
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Dist-Zilla-Plugin-VersionFromMainModule-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla::Role::ModuleMetadata)
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
# Tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Dist::Zilla::Role::ModuleMetadata)
Requires:       perl(Dist::Zilla::Role::VersionProvider)

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

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
