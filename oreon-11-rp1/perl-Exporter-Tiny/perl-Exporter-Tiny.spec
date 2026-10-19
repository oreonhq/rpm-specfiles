%global source0_hash 6499f09a6432cf87b133fb9580a8a9a9a6c566821346b1fdee95f7b64c0317b1
Name:		perl-Exporter-Tiny
Version:	1.006003
Release:        2%{?dist}
Summary:        An exporter with the features of Sub::Exporter but only core dependencies
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://exportertiny.github.io/
Source0:        https://cpan.metacpan.org/modules/by-module/Exporter/Exporter-Tiny-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Carp)
%{?perl_default_filter}
Provides:       perl(Exporter::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Exporter::Tiny supports many of Sub::Exporter's external-facing features
including renaming imported functions with the -as, -prefix and -suffix
options; explicit destinations with the into option; and alternative
installers with the installer option. But it's written in only about 40%%
as many lines of code and with zero non-core dependencies.

Its internal-facing interface is closer to Exporter.pm, with configuration
done through the @EXPORT, @EXPORT_OK and %%EXPORT_TAGS package variables.

Exporter::Tiny performs most of its internal duties (including resolution of
tag names to sub names, resolution of sub names to coderefs, and installation
of coderefs into the target package) as method calls, which means they can be
overridden to provide interesting behavior.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Exporter-Tiny-%{version}

# Remove bundled modules Test::Fatal, Test::Requires, Test::Simple and Try::Tiny
rm -rv ./inc/
sed -i -e '/^inc\//d' MANIFEST

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

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.006003-2
- Import
