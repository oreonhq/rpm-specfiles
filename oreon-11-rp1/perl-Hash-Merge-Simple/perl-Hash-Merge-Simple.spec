%global source0_hash c27f20895814a96e0c5bd0ca3315bf901d79706e3bab4ab0d946debc2c429c0b

Name:           perl-Hash-Merge-Simple
Version:        0.052
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Recursively merge two or more hashes, simply
URL:            https://metacpan.org/release/Hash-Merge-Simple
Source:         https://cpan.metacpan.org/modules/by-module/Hash/Hash-Merge-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Clone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Storable)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies
Requires:       perl(Clone)

%description
Hash::Merge::Simple will recursively merge two or more hashes and return
the result as a new hash reference. The merge function will descend and
merge hashes that exist under the same node in both the left and right
hash, but doesn't attempt to combine arrays, objects, scalars, or
anything else. The rightmost hash also takes precedence, replacing
whatever was in the left hash if a conflict occurs. This code was pretty
much taken straight from Catalyst::Utils, and modified to handle more
than 2 hashes at the same time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-Merge-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Hash/
%{_mandir}/man3/Hash::Merge::Simple.3*

%changelog
%autochangelog
