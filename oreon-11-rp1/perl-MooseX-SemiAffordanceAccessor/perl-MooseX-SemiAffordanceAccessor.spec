%global source0_hash a5b85776bcdded168027a1ff664b41c5f65886721cdd543e3af9d53759a2b1d5

Name:           perl-MooseX-SemiAffordanceAccessor
Summary:        Name your accessors foo() and set_foo()
Version:        0.10
Release:        33%{?dist}
License:        Artistic-2.0

Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-SemiAffordanceAccessor-%{version}.tar.gz 
URL:            https://metacpan.org/release/MooseX-SemiAffordanceAccessor
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose) >= 1.16
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(Moose) >= 1.16

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This module does not provide any methods. Simply loading it changes the
default naming policy for the loading class so that accessors are
separated into get and set methods. The get methods have the same name
as the accessor, while set methods are prefixed with "set_".If you
define an attribute with a leading underscore, then the set method will
start with "_set_".If you explicitly set a "reader" or "writer" name
when creating an attribute, then that attribute's naming scheme is left
unchanged.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-SemiAffordanceAccessor-%{version}

# sigh
find lib/ -type f -exec perl -pi -e 's/0\.5504/0.55/' {} ';'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
