%global source0_hash 7819ccdd18ee18b0e5ce660c084e4e04be3f2f34341302925581d21b53cac6bd

Name:           perl-Object-Tiny
Version:        1.09
Release:        22%{?dist}
Summary:        Class building as simple as it gets
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Tiny
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Object-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47

%{?perl_default_filter}

%description
To use Object::Tiny, just call it with a list of accessors to be created.
This will create a basic "new" constructor and a bunch of simple accessors,
and set the inheritance to be the child of Object::Tiny.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
