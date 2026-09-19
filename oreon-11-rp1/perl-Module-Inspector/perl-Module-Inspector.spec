%global source0_hash cca026875c338b46e6c9938ca8f0d88a88cebf39c3a18c9539e565a03a49ad65

Name:           perl-Module-Inspector
Version:        1.05
Release:        49%{?dist}
Summary:        Integrated API for inspecting Perl distributions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Inspector
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Inspector-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Find::Rule::VCS) >= 1.02
BuildRequires:  perl(Module::Extract) >= 0.01
BuildRequires:  perl(Module::Manifest) >= 0.01
BuildRequires:  perl(Module::Math::Depends) >= 0.02
BuildRequires:  perl(Params::Util) >= 0.17
BuildRequires:  perl(PPI) >= 1.118
BuildRequires:  perl(PPI::Document::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version) >= 0.74
BuildRequires:  perl(YAML::Tiny) >= 1.00
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(PPI::Document::File)

%description
An entire ecosystem of CPAN modules exist around the files and formats
relating to the CPAN itself. Parsers and object models for various
different types of files have been created over the years by various people
for various projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Inspector-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
