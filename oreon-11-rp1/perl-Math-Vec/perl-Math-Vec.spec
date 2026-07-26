%global source0_hash 1de393ef44b5dd7d9312b84b81e267ac2911068fa7cd88d2df4d97b197faffaf

Name:           perl-Math-Vec
Version:        1.01
Release:        48%{?dist}
Summary:        Object-Oriented Vector Math Methods in Perl

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Vec
Source0:        https://cpan.metacpan.org/authors/id/E/EW/EWILHELM/Math-Vec-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
# Tests
BuildRequires:  perl(Test::More)

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Vec-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
PERL_INSTALL_ROOT=$RPM_BUILD_ROOT ./Build install
find $RPM_BUILD_ROOT -type f -name .packlist -delete
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
