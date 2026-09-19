%global source0_hash f0a3e61e49eb0ea9afa7e9653c03b28ad5bcca3378cf4885edb253740c4aec00

# Run optional tests
%{bcond_without perl_DBIx_Class_DateTime_Epoch_enables_optional_test}

Name:           perl-DBIx-Class-DateTime-Epoch
Summary:        Automatic inflation/deflation of epoch-based DateTime objects for DBIx::Class
Version:        0.10
Release:        38%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-DateTime-Epoch
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRICAS/DBIx-Class-DateTime-Epoch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(inc::Module::Install) >= 1.05
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DBIx::Class) >= 0.08103
# DBIx::Class::InflateColumn::DateTime loaded via __PACKAGE__->load_components()
BuildRequires:  perl(DBIx::Class::InflateColumn::DateTime)
# DBIx::Class::TimeStamp loaded via __PACKAGE__->load_components()
BuildRequires:  perl(DBIx::Class::TimeStamp) >= 0.07
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
# DateTime::Format::SQLite is loaded by DBICx::TestDatabase when SQLite database
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBICx::TestDatabase)
# DBIx::Class::Core loaded via __PACKAGE__->load_components()
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_DBIx_Class_DateTime_Epoch_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:       perl(DBIx::Class) >= 0.08103
# DBIx::Class::InflateColumn::DateTime loaded via __PACKAGE__->load_components()
Requires:       perl(DBIx::Class::InflateColumn::DateTime)
# DBIx::Class::TimeStamp loaded via __PACKAGE__->load_components()
Requires:       perl(DBIx::Class::TimeStamp) >= 0.07

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBIx::Class\\)$

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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
