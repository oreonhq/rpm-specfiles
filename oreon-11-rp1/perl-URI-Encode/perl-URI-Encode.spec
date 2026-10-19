%global source0_hash 4bb9ce4e7016c0138cf9c2375508595286efa1c8dc15b45baa4c47281c08243b
%global cpan_version v1.1.1
Name:           perl-URI-Encode
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        1%{?dist}
Summary:        Percent encoding/decoding for URIs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-Encode
Source0:        https://cpan.metacpan.org/modules/by-module/URI/URI-Encode-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(Encode) >= 2.12
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Encode\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
