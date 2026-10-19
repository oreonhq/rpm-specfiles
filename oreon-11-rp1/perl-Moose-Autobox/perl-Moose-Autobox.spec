%global source0_hash 92401da4cf484eb7188ec196b68186efa782a102b451ea156cd8b8772e687055
Name:       perl-Moose-Autobox 
Version:    0.16
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 
Summary:        Autoboxed wrappers for native Perl datatypes
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Moose-Autobox-%{version}.tar.gz
Url:        https://metacpan.org/release/Moose-Autobox
BuildArch:  noarch
%{?perl_default_filter}
Provides:       perl(Moose::Autobox)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Syntax::Keyword::Junction::All)
BuildRequires:  perl(Syntax::Keyword::Junction::Any)
BuildRequires:  perl(Syntax::Keyword::Junction::None)
BuildRequires:  perl(Syntax::Keyword::Junction::One)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autobox)
BuildRequires:  perl(metaclass)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Moose::Autobox provides an implementation of SCALAR, ARRAY, HASH & CODE
for use with autobox. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Moose-Autobox-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
