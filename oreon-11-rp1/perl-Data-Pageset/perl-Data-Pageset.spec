%global source0_hash bbe3c2348364f6a6ddc75c07c2fb2c5c8b5f3d7ac164a973a63526e80fe8b48a

Name:           perl-Data-Pageset
Version:        1.06
Release:        28%{?dist}
Summary:        Page numbering and page sets
# lib/Data/Pageset.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Data-Pageset
Source0:        https://cpan.metacpan.org/authors/id/L/LL/LLAP/Data-Pageset-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Page)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%{?perl_default_filter}

%description
The object produced by Data::Pageset can be used to create page navigation,
it inherits from Data::Page and has access to all methods from this object.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Pageset-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
