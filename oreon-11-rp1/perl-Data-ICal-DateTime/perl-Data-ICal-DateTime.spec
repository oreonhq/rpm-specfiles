%global source0_hash 00ab08667d7b93b245afa33c7599c3b5ddae02685b86a3dc630cc2cce7263a43
Name:           perl-Data-ICal-DateTime
Version:        0.82
Release:        22%{?dist}
Summary:        Convenience methods for using Data::ICal with DateTime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-ICal-DateTime/
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/Data-ICal-DateTime-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::ICal)
BuildRequires:  perl(Data::ICal::Entry::Event)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::ICal)
BuildRequires:  perl(DateTime::Set)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
