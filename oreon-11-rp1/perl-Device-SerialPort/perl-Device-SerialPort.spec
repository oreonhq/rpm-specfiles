%global source0_hash d392567cb39b4ea606c0e0acafd8ed72320311b995336ece5fcefcf9b150e9d7

Name:           perl-Device-SerialPort
Version:        1.04
Release:        56%{?dist}
Summary:        Linux/POSIX emulation of Win32::SerialPort functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Device-SerialPort
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COOK/Device-SerialPort-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module provides an object-based user interface essentially identical
to the one provided by the Win32::SerialPort module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Device-SerialPort-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
                      TESTPORT=/dev/null
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
# Can't do serial port tests in mock/build system
#make test

%files
%doc Changes README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Device*
%{_bindir}/modemtest
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
