%global source0_hash d4cc9a06c170b898d12e4262581b16ae8adca32955956dbe1bb8c7d17662f0a2

Name:           perl-Pod-Weaver-Section-Contributors
Version:        0.009
Release:        26%{?dist}
Summary:        Section listing contributors
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Weaver-Section-Contributors
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KEEDI/Pod-Weaver-Section-Contributors-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# List::MoreUtils not used at tests
# Moose not used at tests
# Pod::Elemental::Element::Nested not used at tests
# Pod::Elemental::Element::Pod5::Verbatim not used at tests
# Pod::Weaver::Role::Section not used at tests
# Tests:
# File::Spec not used
# IO::Handle not used
# IPC::Open3 not used
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More) >= 0.94
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       perl(Pod::Weaver::Role::Section)

%description
This Pod::Weaver section adds a listing of the documents contributors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Weaver-Section-Contributors-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
