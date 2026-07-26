%global source0_hash 58cbf7e333d3a4a40297abc43412b321da449c6816020e4fa6625ab079fc90a5

Name:           perl-Color-Library
Version:        0.021
Release:        36%{?dist}
Summary:        Easy-to-use and comprehensive named-color library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Color-Library
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/Color-Library-%{version}.tar.gz
# Fix POD syntax, CPAN RT#86023
Patch0:         Color-Library-0.021-pod-fixes.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
Requires:       perl(overload)

%description
Color::Library is an easy-to-use and comprehensive named-color
dictionary. Currently provides coverage for WWW (SVG, HTML, CSS) colors,
X11 colors, and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Color-Library-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
