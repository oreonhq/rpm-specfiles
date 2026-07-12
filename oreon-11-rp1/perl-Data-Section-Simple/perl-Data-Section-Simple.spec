%global source0_hash 0b3035ffdb909aa1f7ded6b608fa9d894421c82c097d51e7171170d67579a9cb

Name:		perl-Data-Section-Simple
Version:	0.07
Release:	34%{?dist}
Summary:	Read data from __DATA__
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Data-Section-Simple
Source0:	https://cpan.metacpan.org/modules/by-module/Data/Data-Section-Simple-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(warnings)
# Module
BuildRequires:	perl(base)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:	perl(Test::Pod) >= 1.41
%endif
# Dependencies
# (none)

Provides:       perl(Data::Section::Simple)
%description
Data::Section::Simple is a simple module to extract data from the __DATA__
section of the file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Section-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%if 0%{?fedora} || 0%{?rhel} > 6
make test RELEASE_TESTING=1
%else
make test
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Section::Simple.3*

%changelog
%autochangelog
