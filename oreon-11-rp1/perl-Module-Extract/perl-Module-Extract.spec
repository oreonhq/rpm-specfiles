%global source0_hash 691a9cb10255388ded9317fed1acf01f7c5470a55637b1847a420fdda0af5929

Name:           perl-Module-Extract
Version:        0.01
Release:        48%{?dist}
Summary:        Base class for working with Perl distributions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Extract
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Extract-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Archive::Extract) >= 0.12
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.42
Requires:       perl(Archive::Extract) >= 0.12

%description
Module::Extract is a convenience base class for creating module that work
with Perl distributions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Extract-%{version}

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
