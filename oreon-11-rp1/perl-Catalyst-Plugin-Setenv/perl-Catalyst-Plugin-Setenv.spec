%global source0_hash f8ece867a13da52d2ac6219f513249a913895cbc43d2bb4b2713aa41b5e7e005

Name:           perl-Catalyst-Plugin-Setenv
Version:        0.03
Release:        46%{?dist}
Summary:        Catalyst::Plugin::Setenv Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Setenv
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRAMBERG/Catalyst-Plugin-Setenv-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Runtime) >= 5.7
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
perl Build.PL ./Build ./Build test ./Build install

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Setenv-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
