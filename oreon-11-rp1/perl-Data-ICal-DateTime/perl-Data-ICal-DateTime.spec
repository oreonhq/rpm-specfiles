%global source0_hash 00ab08667d7b93b245afa33c7599c3b5ddae02685b86a3dc630cc2cce7263a43

Name:           perl-Data-ICal-DateTime
Version:        0.82
Release:        22%{?dist}
Summary:        Convenience methods for using Data::ICal with DateTime
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Data-ICal-DateTime/
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/Data-ICal-DateTime-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# runtime deps
BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::ICal)
BuildRequires:  perl(DateTime::Format::ICal)
BuildRequires:  perl(DateTime::Set)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test deps
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::ICal::Entry::Event)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

%{?perl_default_filter}

%description
Data::ICal::Datetime is a perl module which contains convenience methods
for using Data::ICal data with the DateTime perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-ICal-DateTime-%{version}
# Remove bundled modules
rm -r ./inc/*
%{__perl} -pi -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes examples
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
