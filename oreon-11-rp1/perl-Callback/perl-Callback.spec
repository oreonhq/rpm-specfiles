%global source0_hash 8d430c74986862f4ea5e7121aaf40be72437fa2df5242c57671f35871a0d7a4d

Name:           perl-Callback
Version:        1.07
Release:        48%{?dist}
Summary:        Object interface for function callbacks
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Callback
Source0:        https://cpan.metacpan.org/modules/by-module/Callback/Callback-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Storable)

%description
Callback provides a standard interface to register callbacks. Those
callbacks can be either purely functional (i.e. a function call with
arguments) or object-oriented (a method call on an object).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Callback-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
