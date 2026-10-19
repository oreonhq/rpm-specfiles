%global source0_hash 1e2a1b953eca1908a482d48c905e717cfc6012bd47a57d92567f5b34cef156ff
Name:           perl-Module-Install-Copyright
Version:        0.009
Release:        28%{?dist}
Summary:        Package a COPYRIGHT file with a distribution
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/Module-Install-Copyright
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-Copyright-%{version}.tar.gz
Patch0:         Module-Install-Copyright-0.009-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Install::Admin::RDF)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::Contributors)
BuildRequires:  perl(Module::Manifest)
BuildRequires:  perl(MooX::Struct)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(RDF::Trine::Namespace)
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This Module::Install plug-in extracts copyright and licensing information from
embedded POD and/or RDF meta-data included in the distribution, and outputs it
as a text file called COPYRIGHT which should roughly conform to the Debian
copyright file format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-Copyright-%{version}
%patch -P0 -p1
# Remove bundled modules.
# And remove inc/Module/Package/Dist/RDF.pm because it's
# a Module::Package::RDF plug-in that depends on this package. Fortunatelly,
# the inc/Module/Package/Dist/RDF.pm is not good for anything so the patch
# makes not to load it.
rm -rf ./inc
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
