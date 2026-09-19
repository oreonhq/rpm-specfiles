%global source0_hash 975485ab48503206040228e7a83daea66e67165ddd5e278de58c46f56afa4e14

Name:           perl-Module-Install-Contributors
Version:        0.001
Release:        28%{?dist}
Summary:        Add an x_contributors section to your META.yml
# CONTRIBUTING: CC-SA-BY
# COPYRIGHT:    Public Domain
# other files:  GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA and Public Domain - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/Module-Install-Contributors
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-Contributors-%{version}.tar.gz
# To boostrap this package without bundling
Patch0:         Module-Install-Contributors-0.001-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
# Modules from ./lib are also used from the patched Makefile.PL.
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)

%description
This is a plugin for Module::Install. It adds an x_contributors section to
your META.yml file. This is an array of strings, which should normally be in
"Name <email>" format, that is passed to contributors() function in
a Makefile.PL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-Contributors-%{version}
%patch -P0 -p1
# Remove bundled modules.
# And remove inc/Module/Package/Dist/RDF.pm becaus it's a Module::Package::RDF
# plug-in that depends on package transitively. Fortunatelly, the
# inc/Module/Package/Dist/RDF.pm is not good for anything so the patch makes
# not to load it.
rm -r ./inc
sed -i -e '/^inc/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
