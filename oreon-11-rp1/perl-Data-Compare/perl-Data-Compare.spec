%global source0_hash 53c9db3b93263c88aaa3c4072d819eaded024d7a36b38c0c37737d288d5afa8c

Name:           perl-Data-Compare
Version:        1.29
Release:        8%{?dist}
Summary:        Compare perl data structures
# Some of the metadata files suggest GPL2 rather than GPL (any version)
# but the module is actually licensed "same as perl"
# See "COPYRIGHT and LICENCE" in lib/Data/Compare.pm
# See also: https://github.com/DrHyde/perl-modules-Data-Compare/issues/15
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Compare
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Compare-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone) >= 0.43
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:  perl(JSON)
BuildRequires:  perl(Scalar::Properties)
BuildRequires:  perl(Test::Pod) >= 1.00
# Dependencies
# (none)

Provides:       perl(Data::Compare)
%description
This module compares arbitrary data structures to see if they are copies
of each other.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Compare-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG MAINTAINERS-NOTE
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Compare/
%dir %{perl_vendorlib}/Data/Compare/Plugins/
%doc %{perl_vendorlib}/Data/Compare/Plugins.pod
%{perl_vendorlib}/Data/Compare.pm
%{perl_vendorlib}/Data/Compare/Plugins/Scalar/
%{_mandir}/man3/Data::Compare.3*
%{_mandir}/man3/Data::Compare::Plugins.3*
%{_mandir}/man3/Data::Compare::Plugins::Scalar::Properties.3*

%changelog
%autochangelog
