%global source0_hash 975485ab48503206040228e7a83daea66e67165ddd5e278de58c46f56afa4e14
Name:           perl-Module-Install-Contributors
Version:        0.001
Release:        1%{?dist}
Summary:        Add an x_contributors section to your META.yml
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/Module-Install-Contributors
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-Contributors-%{version}.tar.gz
Patch0:         Module-Install-Contributors-0.001-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
