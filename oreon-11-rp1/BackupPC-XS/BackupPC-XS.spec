%global source0_hash 94d863083a466558f82f10b1b95db7742ea99ebce808214f20897b343dc32b18

Name:           BackupPC-XS
Version:        0.62
Release:        24%{?dist}
Summary:        Implementation of various BackupPC functions in a perl-callable module

License:        GPL-3.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Zlib
URL:            https://github.com/backuppc/backuppc-xs
Source0:        https://github.com/backuppc/backuppc-xs/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0:         BackupPC-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Testing requirement
BuildRequires:  perl(Test::More)

Provides:       bundled(zlib) = 1.2.3

%description
BackupPC::XS implements various BackupPC functions in a perl-callable
module.  This module is required for BackupPC V4+.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/BackupPC::XS.3pm*

%changelog
%autochangelog
