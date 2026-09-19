%global source0_hash 222e4f99731faaba1a4601707bcf9412d957eb74c3c405db0c2b8ea41b179c7f

Name:           perl-Module-Install-Authority
Version:        0.03
Release:        33%{?dist}
Summary:        Add an x_authority key to META.yml
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-Authority
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Module-Install-Authority-%{version}.tar.gz
# Makefile.PL needs a module delivered by this package
Patch0:         Module-Install-Authority-0.03-Use-M-I-Authority-under-build-when-building.patch
Patch1:         Module-Install-Authority-0.03-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Base)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(YAML)

%description
If you upload a distribution which contains an x_authority key in the
META.yml then PAUSE will assign 'firstcome' permissions on any packages in
that distribution to the user given by the x_authority key (and assign co-
maintenance to the uploader).

This makes coordination (and maintenance sharing) much easier for large
CPAN distributions, or those maintained by a pool of people.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-Authority-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -rf inc
sed -i -e '/inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
