%global source0_hash bf952d141e57cc416b6279d37cf44382fd62d0388d18c0ae665f3bd3fb94d878

Name:           perl-Catalyst-Plugin-PageCache
Version:        0.32
Release:        29%{?dist}
Summary:        Cache the output of entire pages
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-PageCache
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VERISSIMO/Catalyst-Plugin-PageCache-%{version}.tar.gz
# Define POD encoding, CPAN RT#87667
Patch0:         Catalyst-Plugin-PageCache-0.31-Define-POD-encoding.patch
Patch1:         Catalyst-Plugin-PageCache-0.32-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cache::Cache) >= 1.04
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Catalyst::Plugin::Cache) >= 0.10
BuildRequires:  perl(Catalyst::Plugin::I18N)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(Catalyst::Runtime)
Requires:       perl(Class::Accessor::Fast)

%description
Many dynamic websites perform heavy processing on most pages, yet this
information may rarely change from request to request. Using the PageCache
plugin, you can cache the full output of different pages so they are served
to your visitors as fast as possible. This method of caching is very useful
for withstanding a Slashdotting, for example.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-PageCache-%{version}
%patch -P0 -p1
%patch -P1 -p1
iconv -f iso-8859-1 -t utf-8 README >README.conv && mv README.conv README

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=yep make test

%files
%doc Changes README
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
