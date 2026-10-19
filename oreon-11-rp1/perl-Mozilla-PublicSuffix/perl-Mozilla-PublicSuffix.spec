%global source0_hash 6815e292161ba8192b434398db295e229b3e61574e6a61994e90f359a2c71b21
Name:           perl-Mozilla-PublicSuffix
Version:        1.0.7
Release:        1%{?dist}
Summary:        Get a domain name's public suffix via the Mozilla Public Suffix List
License:        MIT
URL:            https://metacpan.org/release/Mozilla-PublicSuffix
Source0:        https://cpan.metacpan.org/modules/by-module/Mozilla/Mozilla-PublicSuffix-v%{version}.tar.gz
Patch1:         Mozilla-PublicSuffix-unbundle.patch
BuildArch:      noarch
Requires:       publicsuffix-list
Provides:       perl(Mozilla::PublicSuffix)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::File)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::_idna)
BuildRequires:  perl(blib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  publicsuffix-list
# /oreon:deps
%description
This module provides a single function that returns the public suffix of a
domain name by referencing a parsed copy of Mozilla's Public Suffix List.
From the official website at http://publicsuffix.org/

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mozilla-PublicSuffix-v%{version}
%autopatch -p1

%build

perl Build.PL installdirs=vendor --config system_publicsuffix_list=/usr/share/publicsuffix/public_suffix_list.dat </dev/null
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.7-4
- Prepare for Oreon 11 (RP1)
