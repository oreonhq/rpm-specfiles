Name:           perl-Mozilla-PublicSuffix
Version:        1.0.7
Release:        4%{?dist}
Summary:        Get a domain name's public suffix via the Mozilla Public Suffix List
License:        MIT
URL:            https://metacpan.org/release/Mozilla-PublicSuffix
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOMHUKINS/Mozilla-PublicSuffix-v1.0.7.tar.gz


# https://github.com/rsimoes/Mozilla-PublicSuffix/pull/6
Patch1:         Mozilla-PublicSuffix-unbundle.patch
# oreon url source checksums begin
%global source0_sha256 6815e292161ba8192b434398db295e229b3e61574e6a61994e90f359a2c71b21
%global source0_file Mozilla-PublicSuffix-v1.0.7.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::File)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(URI::_idna)
BuildRequires:  publicsuffix-list
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

Requires:       publicsuffix-list

%description
This module provides a single function that returns the public suffix of a
domain name by referencing a parsed copy of Mozilla's Public Suffix List.
From the official website at http://publicsuffix.org/

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Mozilla-PublicSuffix-v1.0.7.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6815e292161ba8192b434398db295e229b3e61574e6a61994e90f359a2c71b21" || { echo "oreon: Source0 SHA256 mismatch for Mozilla-PublicSuffix-v1.0.7.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Mozilla-PublicSuffix-v%{version}
%autopatch -p1

%build
perl Build.PL installdirs=vendor --config system_publicsuffix_list=/usr/share/publicsuffix/public_suffix_list.dat </dev/null
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.7-4
- Prepare for Oreon 11 (RP1)
