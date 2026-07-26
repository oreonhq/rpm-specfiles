%global source0_hash 8747f643893914f8c44979f1716d0c1ec8a41394796555447944e860f1ff7c0b

Name:           perl-Class-Mix
Summary:        Dynamic class mixing
Version:        0.006
Release:        25%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Class-Mix-%{version}.tar.gz 
URL:            https://metacpan.org/release/Class-Mix
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(mro)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(mro)

%{?perl_default_filter}

%description
The mix_class function provided by this module dynamically generates
'anonymous' classes with specified inheritance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Mix-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
