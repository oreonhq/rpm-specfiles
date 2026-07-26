%global source0_hash 990d95f270f4c3fd8188111546ed70dbcc561092cf0749242594099cd59505a0

Name:           perl-Test-Able
Version:        0.11
Release:        42%{?dist}
Summary:        xUnit with Moose
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Able
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDV/Test-Able-%{version}.tar.gz
# Fix Moose enum warnings, CPAN RT#92396
Patch0:         Test-Able-0.11-Moose_enum.patch
# Adapt to Test-Simple-1.302019, bug #1338792, CPAN RT#65249
Patch1:         Test-Able-0.11-Adapt-to-Test-Simple-1.302019.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Builder)
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Moose) >= 0.94

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose\\)\\s*$

%description
An xUnit style testing framework inspired by Test::Class and built using
Moose. It can do all the important things Test::Class can do and more. The
prime advantages of using this module instead of Test::Class are
flexibility and power. Namely, Moose.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Able-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

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
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
