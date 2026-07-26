%global source0_hash 4bb9ce4e7016c0138cf9c2375508595286efa1c8dc15b45baa4c47281c08243b

%global cpan_version v1.1.1

Name:           perl-URI-Encode
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        28%{?dist}
Summary:        Percent encoding/decoding for URIs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-Encode
Source0:        https://cpan.metacpan.org/modules/by-module/URI/URI-Encode-%{cpan_version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.38
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
# Dependencies
Requires:       perl(Encode) >= 2.12

# Drop under-specified dependencies
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Encode\\)$

%description
This module provides a method to encode strings (mainly URLs) into a format 
which can be pasted into a plain text emails, and that those links are 
'click-able' by the person reading that email.  This can be accomplished by NOT
encoding the reserved characters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-Encode-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/URI/
%{_mandir}/man3/URI::Encode.3*

%changelog
%autochangelog
