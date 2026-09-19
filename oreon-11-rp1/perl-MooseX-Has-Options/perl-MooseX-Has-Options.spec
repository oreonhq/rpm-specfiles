%global source0_hash 07c21cf8ed500b272020ff8da19f194728bb414e0012a2f0cc54ef2ef6222a68

Name:           perl-MooseX-Has-Options
Version:        0.003
Release:        36%{?dist}
Summary:        Succinct options for Moose
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Has-Options
Source0:        https://cpan.metacpan.org/authors/id/P/PS/PSHANGOV/MooseX-Has-Options-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Package::Stash) >= 0.18
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(warnings)
Requires:       perl(Package::Stash) >= 0.18

%{?perl_default_filter}

%description
This module provides a succinct syntax for declaring options for Moose
attributes. It hijacks the 'has' function imported by Moose and replaces it
with one that understands the options syntax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Has-Options-%{version}

# silence rpmlint
sed -i 's/\r//' Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
