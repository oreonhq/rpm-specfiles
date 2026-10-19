%global source0_hash 19cb70e98584655e354d2d6a8e71cc5ca902dddc3ac44416712f9163d122b9e8
%global rpm_version 0.08
%global cpan_version 0.08
Name:           perl-DateTime-Format-MySQL
Version:        %{rpm_version}
Release:        1%{?dist}
Summary:        Parse and format MySQL dates and times
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-MySQL
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-MySQL-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(DateTime::Format::MySQL)
Provides:       perl(DateTime::Format::MySQL)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in order
to create DateTime objects, and it can take a DateTime object and produce a
string representing it in the MySQL format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Format-MySQL-%{cpan_version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
