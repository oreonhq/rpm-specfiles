%global source0_hash 35d815c49090d57b7051806ae1c4844879131791de1b861613c55a90a46b28ab

Name:           perl-UNIVERSAL-ref
Summary:        Turns ref() into a multimethod
Version:        0.14
Release:        49%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJORE/UNIVERSAL-ref-%{version}.tar.gz
# Restore compatibility with Perl 5.26.0, CPAN RT#118008
Patch0:         UNIVERSAL-ref-0.14-Fix-building-with-Perl-5.25.1.patch
URL:            https://metacpan.org/release/UNIVERSAL-ref

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(B::Utils)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

Requires:       perl(B::Utils)

%{?perl_default_filter}

%description
This module changes the behavior of the builtin function ref(). If
ref() is called on an object that has requested an overloaded ref,
the object's '->ref' method will be called and its return value
used instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n UNIVERSAL-ref-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
%autochangelog
