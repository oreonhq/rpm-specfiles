%global source0_hash fa65cc20a833cb4e944bb65932b666b3bae0af6e068c2fd5bdf971f6e97137e3

Name:           perl-latest
Version:        0.03
Release:        45%{?dist}
Summary:        Use the latest Perl features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/latest
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDYA/latest-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(version)
# Tests only
BuildRequires:  perl(Test::More)

%description
Shake out any obscure problems that might result from your code being used by a
program that requires the latest Perl version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n latest-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
