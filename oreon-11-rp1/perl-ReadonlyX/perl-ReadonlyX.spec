%global source0_hash 81bb97dba93ac6b5ccbce04a42c3590eb04557d75018773ee18d5a30fcf48188

Name:           perl-ReadonlyX
Version:        1.04
Release:        25%{?dist}
Summary:        Faster facility for creating read-only scalars, arrays, hashes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/ReadonlyX/
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SANKO/ReadonlyX-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# runtime deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Storable)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# test deps
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
Requires:       perl(Storable)

%{?perl_default_filter}

%description
ReadonlyX is a near-drop-in replacement for Readonly, the popular facility
for creating non-modifiable variables. This is useful for configuration
files, headers, etc. It can also be useful as a development and debugging
tool for catching updates to variables that should not be changed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ReadonlyX-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/ReadonlyX*
%{_mandir}/man3/ReadonlyX*

%changelog
%autochangelog
