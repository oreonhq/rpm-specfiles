%global source0_hash 406718f2a0c06065736437b44c9ee442fdede3a4e362ec25d6d50a0fc67d9ca0

Name:           perl-MooseX-Async
Version:        0.07
Release:        47%{?dist}
Summary:        Set of Metaclasses for MooseX::POE and it's siblings
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Async
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/MooseX-Async-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Moose) >= 0.56
BuildRequires:  perl(MooseX::AttributeHelpers) >= 0.13
BuildRequires:  perl(Test::More) >= 0.42
Requires:       perl(Moose) >= 0.56
Requires:       perl(MooseX::AttributeHelpers) >= 0.13

%{?perl_default_filter}

%description
MooseX::Async is a set of Metaclasses for MooseX::POE and it's siblings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Async-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
