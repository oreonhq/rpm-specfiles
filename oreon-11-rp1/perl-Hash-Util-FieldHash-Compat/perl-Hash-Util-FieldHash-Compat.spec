%global source0_hash 642e46a75b537ba11420b30f8b03403c90a06a15458cd8009f339fe9e5f3741b

Name:		perl-Hash-Util-FieldHash-Compat
Version:	0.11
Release:	29%{?dist}
Summary:	Use Hash::Util::FieldHash or ties, depending on availability
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Hash-Util-FieldHash-Compat
Source0:	https://cpan.metacpan.org/modules/by-module/Hash/Hash-Util-FieldHash-Compat-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(parent)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Tie::Hash)
BuildRequires:	perl(Tie::RefHash)
BuildRequires:	perl(Tie::RefHash::Weak) >= 0.08
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

# We actually have this everywhere, so use it
BuildRequires:	perl(Hash::Util::FieldHash)
Requires:	perl(Hash::Util::FieldHash)

Provides:       perl(Hash::Util::FieldHash::Compat)
%description
Under older perls this module provides a drop in compatible API to
Hash::Util::FieldHash using perltie. When Hash::Util::FieldHash is
available, it will use that instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Hash-Util-FieldHash-Compat-%{version}

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
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Hash/
%{_mandir}/man3/Hash::Util::FieldHash::Compat.3*
%{_mandir}/man3/Hash::Util::FieldHash::Compat::Heavy.3*

%changelog
%autochangelog
