%global source0_hash 222e4f99731faaba1a4601707bcf9412d957eb74c3c405db0c2b8ea41b179c7f
Name:           perl-Module-Install-Authority
Version:        0.03
Release:        1%{?dist}
Summary:        Add an x_authority key to META.yml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-Authority
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Module-Install-Authority-%{version}.tar.gz
Patch0:         Module-Install-Authority-0.03-Use-M-I-Authority-under-build-when-building.patch
Patch1:         Module-Install-Authority-0.03-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
