%global source0_hash ff982239cf0e582d3c93dfd4f9151b3328384c844fe567eddd207c878cee7894

Name:           perl-Kwiki-Users-Remote
Version:        0.04
Release:        56%{?dist}
Summary:        Automatically set Kwiki user name from HTTP authentication
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Users-Remote
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAN/Kwiki-Users-Remote-%{version}.tar.gz
Patch0:         Kwiki-Users-Remote-0.04-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Kwiki) >= 0.32
BuildRequires:  perl(Kwiki::Installer)
BuildRequires:  perl(Kwiki::User)
BuildRequires:  perl(Kwiki::UserName) >= 0.14
BuildRequires:  perl(Kwiki::Users)
BuildRequires:  perl(mixin)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Kwiki) >= 0.32
Requires:       perl(Kwiki::Installer)
Requires:       perl(Kwiki::UserName) >= 0.14

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Kwiki::UserName\\)$

%description
When using HTTP authentication for your Kwiki, use this module to
automatically set the user's name from the username they logged in with.
This name will appear in any Recent Changes listing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-Users-Remote-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
rm -f SIGNATURE
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
