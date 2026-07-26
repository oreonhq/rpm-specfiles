%global source0_hash 8b4f703136a0eb1226855ced051a0a2210bd794788122a9eee2eb97a5cddef96

Name:		perl-Data-Tumbler
Version:	0.010
Release:	32%{?dist}
Summary:	Dynamic generation of nested combinations
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Data-Tumbler
Source0:	https://cpan.metacpan.org/modules/by-module/Data/Data-Tumbler-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite (upstream wants Test::Most ≥ 0.33 but test suite works fine with Test::Most 0.11)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Most) >= 0.11
BuildRequires:	perl(Time::HiRes)

%description
The tumble() method calls a sequence of 'provider' code references, each of
which returns a hash. The first provider is called and then, for each hash item
it returns, the tumble() method recurses to call the next provider. The
recursion continues until there are no more providers to call, at which point
the consumer code reference is called. Effectively the providers create a tree
of combinations and the consumer is called at the leaves of the tree. If a
provider returns no items then that part of the tree is pruned. Further
providers, if any, are not called and the consumer is not called.

During a call to tumble() three values are passed down through the tree and
into the consumer: path, context, and payload. The path and context are derived
from the names and values of the hashes returned by the providers. Typically
the path defines the current "path" through the tree of combinations. The
providers are passed the current path, context, and payload. The payload is
cloned at each level of recursion so that any changes made to it by providers
are only visible within the scope of the generated sub-tree.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Tumbler-%{version}

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
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Tumbler.3*

%changelog
%autochangelog
