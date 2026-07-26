%global source0_hash 12605c10fc4649a5b9e2bcda6960ec39e498ea25e060db4362c926de4594e590

Name:           perl-Diff-LibXDiff
Version:        0.05
Release:        27%{?dist}
Summary:        Calculate a diff with LibXDiff (via XS)
# License describes: libxdiff and (Diff-LibXDiff)
# Automatically converted from old format: LGPLv2+ and (GPL+ or Artistic) - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Diff-LibXDiff
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKRIMEN/Diff-LibXDiff-%{version}.tar.gz

# libxdiff license
Source1:        LICENSE-libxdiff-LGPL
# Diff-LibXDiff license (perl5 license)
Source2:        LICENSE-Diff-LibXDiff-GPL
Source3:        LICENSE-Diff-LibXDiff-Artistic

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Most)
Requires:       perl(Carp::Clan)
# The libxdiff packaged in Fedora doesn't work with this module
Provides:       bundled(libxdiff) = 0.23

%description
Diff::LibXDiff is a binding of LibXDiff to Perl via XS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Diff-LibXDiff-%{version}

# Install license files
install -pm 0644 %{S:1} LICENSE-libxdiff-LGPL
install -pm 0644 %{S:2} LICENSE-Diff-LibXDiff-GPL
install -pm 0644 %{S:3} LICENSE-Diff-LibXDiff-Artistic

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE-*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Diff*
%{_mandir}/man3/*

%changelog
%autochangelog
