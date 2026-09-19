%global source0_hash baeb7fd7bf905be74631c88760fd8a2980ceea95627993399581643ef6377274

Name:           perl-Catalyst-Plugin-Session-Store-FastMmap
Version:        0.16
Release:        39%{?dist}
Summary:        FastMmap session storage backend
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-FastMmap
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-Store-FastMmap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Cache::FastMmap) >= 1.29
BuildRequires:  perl(Catalyst::ClassData)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Runtime) >= 5.80000
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Cache::FastMmap) >= 1.29
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)

%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage plugin
for Catalyst that uses an mmap'ed file to act as a shared memory
interprocess cache. It is based on Cache::FastMmap.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-Store-FastMmap-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
