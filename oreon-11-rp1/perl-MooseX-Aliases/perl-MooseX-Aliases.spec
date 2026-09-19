%global source0_hash c4850f972426c3447aaeed8dcb4033e84460ca51705ad3ea78b63af919fe0748

Name:           perl-MooseX-Aliases
Version:        0.11
Release:        34%{?dist}
Summary:        Easy aliasing of methods and attributes in Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Aliases
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Aliases-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module
BuildRequires:  perl(Moose) >= 2.0000
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Script) >= 1.05
# Dependencies
# (none)

%description
The MooseX::Aliases module will allow you to quickly alias methods in
Moose. It provides an alias parameter for has() to generate aliased
accessors as well as the standard ones. Attributes can also be initialized
in the constructor via their aliased names.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Aliases-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::Aliases.3*
%{_mandir}/man3/MooseX::Aliases::Meta::Trait::Attribute.3*
%{_mandir}/man3/MooseX::Aliases::Meta::Trait::Method.3*

%changelog
%autochangelog
