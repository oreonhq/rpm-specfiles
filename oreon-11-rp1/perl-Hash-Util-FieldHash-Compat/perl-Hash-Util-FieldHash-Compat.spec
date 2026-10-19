%global source0_hash 642e46a75b537ba11420b30f8b03403c90a06a15458cd8009f339fe9e5f3741b
Name:		perl-Hash-Util-FieldHash-Compat
Version:	0.11
Release:        29%{?dist}
Summary:        Use Hash::Util::FieldHash or ties, depending on availability
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Hash-Util-FieldHash-Compat
Source0:        https://cpan.metacpan.org/modules/by-module/Hash/Hash-Util-FieldHash-Compat-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Hash::Util::FieldHash)
Provides:       perl(Hash::Util::FieldHash::Compat)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(Tie::RefHash::Weak)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
