%global source0_hash bcea24e6486c9cdfcde0d7c6bbb8e1ac7148f79be36bde026f499f820dcfce7e

Name:           perl-Catalyst-Plugin-SubRequest
Summary:        Make subrequests to actions in Catalyst
Version:        0.21
Release:        33%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Plugin-SubRequest-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-SubRequest
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime) >= 5.90000
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(warnings)
BuildRequires:  sed

Requires:       perl(Catalyst::Runtime) >= 5.90000

%{?perl_default_filter}

%description
Make subrequests to actions in Catalyst. Uses the Catalyst dispatcher, so
it will work like an external url call.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-SubRequest-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
