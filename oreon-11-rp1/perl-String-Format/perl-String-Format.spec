%global source0_hash 9e417a8f8d9ea623beea2d13a47c0d5a696fc8602c0509b826cd45f97b76e778

Name:           perl-String-Format
Version:        1.18
Release:        23%{?dist}
Summary:        Sprintf-like string formatting capabilities with arbitrary format definitions

License:        GPL-2.0-only
URL:            https://metacpan.org/release/String-Format
Source0:        https://cpan.metacpan.org/modules/by-module/String/String-Format-%{version}.tar.gz

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.57
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Dependencies:
# (none)

Provides:       perl(String::Format)
%description
String::Format lets you define arbitrary printf-like format sequences
to be expanded. This module would be most useful in configuration
files and reporting tools, where the results of a query need to be
formatted in a particular way.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n String-Format-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}


%check
make test


%files
%license COPYING
%doc Changes README
%{perl_vendorlib}/String/
%{_mandir}/man3/String::Format.3*


%changelog
%autochangelog
