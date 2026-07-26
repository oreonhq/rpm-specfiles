%global source0_hash a8a4d5e986727206b1150f621c6f381078a16ffde7aa1a05d41846e74a2619fe

Name:           perl-DBIx-Class-TimeStamp
Version:        0.14
Release:        43%{?dist}
Summary:        DBIx::Class extension to update and create date and time based fields
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-TimeStamp
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-TimeStamp-%{version}.tar.gz
Patch0:         DBIx-Class-TimeStamp-0.14-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(DateTime) >= 0.55
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::DynamicDefault) >= 0.03
BuildRequires:  perl(DBIx::Class::InflateColumn::DateTime)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Warp)
# Optional tests only
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(DateTime) >= 0.55
Requires:       perl(DBIx::Class) >= 0.08009
Requires:       perl(DBIx::Class::DynamicDefault) >= 0.03
Requires:       perl(DBIx::Class::InflateColumn::DateTime)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DBIx::Class\\)$

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-TimeStamp-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
