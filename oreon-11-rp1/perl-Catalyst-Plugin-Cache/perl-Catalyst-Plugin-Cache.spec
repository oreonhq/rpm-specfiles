%global source0_hash 295fed449c9324b06578fd468e3391e04fbf64ad24376a004408d1bc6f5443e0

Name:           perl-Catalyst-Plugin-Cache
Version:        0.12
Release:        37%{?dist}
Summary:        Flexible caching support for Catalyst
# Automatically converted from old format: (GPL+ or Artistic) or MIT - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) OR LicenseRef-Callaway-MIT
URL:            https://metacpan.org/release/Catalyst-Plugin-Cache
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Cache-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst) >= 5.80000
BuildRequires:  perl(Catalyst::ClassData)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(warnings)
BuildRequires:  sed

%{?perl_default_filter}

%description
This plugin gives you access to a variety of systems for caching data. It
allows you to use a very simple configuration API, while maintaining the
possibility of flexibility when you need it later.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Cache-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
