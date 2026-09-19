%global source0_hash 70b5e8bf4643d72966b4d58400504089134f7a29457549bcd091c23747015700

Name:           perl-Catalyst-Engine-Apache
Version:        1.16
Release:        42%{?dist}
Summary:        Catalyst Apache Engines
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Engine-Apache
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Catalyst-Engine-Apache-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Catalyst::Runtime)

%description
These classes provide mod_perl support for Catalyst.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Engine-Apache-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# remove MP13 and MP19 as they are not used in Fedora
find %{buildroot} -type f -name '*MP13.*' -exec rm -f {} \;
find %{buildroot} -type f -name '*MP19.*' -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
