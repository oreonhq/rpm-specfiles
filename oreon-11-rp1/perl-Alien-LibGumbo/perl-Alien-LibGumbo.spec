%global source0_hash 0fbe916ab11f680e5c28cd1ac800372323e2a0e06affc6c8b36279fc64d76517

Name:           perl-Alien-LibGumbo
Version:        0.05
Release:        14%{?dist}
Summary:        Gumbo parser library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-LibGumbo
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RUZ/Alien-LibGumbo-%{version}.tar.gz

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.010

BuildRequires:  perl(Alien::Base) >= 0.005
BuildRequires:  perl(Alien::Base::ModuleBuild)
BuildRequires:  perl(File::ShareDir) >= 1.03
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Class) >= 0.013

BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  gumbo-parser-devel

# Pull in %%{_libdir}/libgumbo.so.?
Requires:       gumbo-parser%{?_isa}

# This is an architecture-dependent package because it stores data about
# architecture-specific library, but it has no XS code, hence no debuginfo.
%global debug_package %%{nil}

%description
This distribution installs libgumbo:https://github.com/google/gumbo-parser
on your system for use by perl modules like HTML::Gumbo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-LibGumbo-%{version}
# Remove bundled gumbo tarball
rm -f gumbo-0.10.1.tar.gz
sed -i -e '/gumbo-0.10.1.tar.*/d' MANIFEST

%build
%{__perl} Build.PL --installdirs=vendor --install_path lib=%{perl_vendorarch}
./Build

%install

./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
%autochangelog
