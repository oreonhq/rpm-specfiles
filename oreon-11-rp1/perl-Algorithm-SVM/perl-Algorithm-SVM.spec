%global source0_hash f72572df107eb45cd2ff6165c183164f38c7da98417d2242e334e6999fb7e422

Name:           perl-Algorithm-SVM
Version:        0.13
Release:        49%{?dist}
Summary:        Perl bindings for the libsvm Support Vector Machine library

# Note: The sources bundle a copy of libsvm which is BSD-licensed,
#    https://fedoraproject.org/wiki/Licensing/BSD#3ClauseBSD
# But this file gets dropped during %%prep (see Patch0)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-SVM

Source0:        https://cpan.metacpan.org/authors/id/L/LA/LAIRDM/Algorithm-SVM-%{version}.tar.gz

# https://rt.cpan.org/Public/Bug/Display.html?id=79106
Patch0:         Algorithm-SVM-0.13-Unbundle-libsvm.patch
Patch1:         Algorithm-SVM-0.13-Port-to-libsvm-3.0.patch

# https://rt.cpan.org/Public/Bug/Display.html?id=79754
Patch2:         Algorithm-SVM-0.13-Fix-build-on-32-bits-with-Perl-5.14.patch

BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  libsvm-devel

%{?perl_default_filter}

%description
Algorithm::SVM implements a Support Vector Machine for Perl. Support Vector
Machines provide a method for creating classification functions from a set
of labeled training data, from which predictions can be made for subsequent
data sets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-SVM-%{version}

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README sample.model sample.model.1
%{perl_vendorarch}/Algorithm/SVM*
%{perl_vendorarch}/auto/Algorithm/SVM
%{_mandir}/man3/Algorithm::SVM*

%changelog
%autochangelog
