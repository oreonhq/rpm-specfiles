%global source0_hash 03a5adfed1b44280583ee4231ed529ccbc0f719ca368faa3aad3c024a8999082
Name:           perl-Catalyst-Plugin-Unicode
Version:        0.93
Release:        1%{?dist}
Summary:        Unicode aware Catalyst
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Unicode
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Unicode-%{version}.tar.gz
Patch0:         Catalyst-Plugin-Unicode-0.93-Define-POD-encoding.patch
BuildArch:      noarch
Requires:       perl(Catalyst::Runtime) >= 5.70
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
On request, decodes all params from UTF-8 octets into a sequence of logical
characters. On response, encodes body into UTF-8 octets.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Unicode-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build

PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

TEST_POD=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
