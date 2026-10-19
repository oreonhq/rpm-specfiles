%global source0_hash d18afd78893bd830ba2465c0ae6a33425460159003864ded3b5adcf51189cae9
Name:           perl-SQL-Abstract-Limit
Version:        0.143
Release:        1%{?dist}
Summary:        Portable LIMIT Emulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Abstract-Limit
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/SQL-Abstract-Limit-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?fedora} < 18 && 0%{?rhel} < 7 && 0%{?oreon} < 11
%endif
Requires:       perl(Class::DBI)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl-generators
# /oreon:deps
%description
Portable SQL LIMIT emulation, with support for multiple dialects and syntax 
models.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Abstract-Limit-%{version}

# Get rid of spurious exec bits
find . -type f -exec chmod -c -x {} ';'

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
