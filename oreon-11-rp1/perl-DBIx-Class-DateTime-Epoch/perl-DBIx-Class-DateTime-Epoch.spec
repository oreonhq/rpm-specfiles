%global source0_hash f0a3e61e49eb0ea9afa7e9653c03b28ad5bcca3378cf4885edb253740c4aec00
%{bcond_without perl_DBIx_Class_DateTime_Epoch_enables_optional_test}
Name:           perl-DBIx-Class-DateTime-Epoch
Summary:        Automatic inflation/deflation of epoch-based DateTime objects for DBIx::Class
Version:        0.10
Release:        38%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-DateTime-Epoch
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRICAS/DBIx-Class-DateTime-Epoch-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_DBIx_Class_DateTime_Epoch_enables_optional_test}
%endif
Requires:       perl(DBIx::Class) >= 0.08103
Requires:       perl(DBIx::Class::InflateColumn::DateTime)
Requires:       perl(DBIx::Class::TimeStamp) >= 0.07
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBIx::Class\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(DBICx::TestDatabase)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::InflateColumn::DateTime)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::TimeStamp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module automatically inflates/deflates DateTime objects
corresponding to applicable columns. Columns may also be defined to
specify their nature, such as columns representing a creation time
(set at time of insertion) or a modification time (set at time of
every update).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-DateTime-Epoch-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
