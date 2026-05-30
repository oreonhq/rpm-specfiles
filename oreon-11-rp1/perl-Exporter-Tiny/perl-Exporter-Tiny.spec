%global source0_hash 6499f09a6432cf87b133fb9580a8a9a9a6c566821346b1fdee95f7b64c0317b1

Name:		perl-Exporter-Tiny
Version:	1.006003
Release:	2%{?dist}
Summary:	An exporter with the features of Sub::Exporter but only core dependencies
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://exportertiny.github.io/
Source0:        https://cpan.metacpan.org/modules/by-module/Exporter/Exporter-Tiny-%{version}.tar.gz


BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
# If we don't have at least 5.37.2 then we'll need Lexical::Var
BuildRequires:	perl(:VERSION) >= 5.37.2
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.47
# Optional Tests
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Warnings)
# Dependencies
Requires:	perl(Carp)

# Avoid doc-file dependency on perl(base)
%{?perl_default_filter}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%check
make test

%files
%license COPYRIGHT LICENSE
%doc Changes CREDITS examples/ NEWS README TODO
%{perl_vendorlib}/Exporter/
%{_mandir}/man3/Exporter::Tiny.3*
%{_mandir}/man3/Exporter::Tiny::Manual::Etc.3*
%{_mandir}/man3/Exporter::Tiny::Manual::Exporting.3*
%{_mandir}/man3/Exporter::Tiny::Manual::Importing.3*
%{_mandir}/man3/Exporter::Tiny::Manual::QuickStart.3*
%{_mandir}/man3/Exporter::Shiny.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.006003-2
- Import
