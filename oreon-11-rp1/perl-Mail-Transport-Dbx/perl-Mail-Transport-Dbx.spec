%global source0_hash 95fd6bacf2afa0acb121eb9385d61ad4743c48240fbf5a74a731b3c1b5dfdf7d

Name:           perl-Mail-Transport-Dbx
Version:        0.07
Release:        57%{?dist}
Summary:        Parse Outlook Express mailboxes
# libdbx/libdbx.c:  GPLv2+
# README:           GPL+ or Artistic
License:        GPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Mail-Transport-Dbx
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Mail-Transport-Dbx-%{version}.tar.gz
# Declare POD encoding, CPAN RT#79031
Patch0:         Mail-Transport-Dbx-0.07-Declare-POD-encoding.patch
BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# ExtUtils::Constant || (File::Copy && File::Spec)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
# Optional tests:
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
# Bundles https://sourceforge.net/projects/ol2mbox/files/LibDBX/, bug #234861
Provides:  bundled(libdbx) = 1.0.3

%description
Mail::Transport::Dbx is a wrapper around libdbx to read Outlook Express
mailboxes (more commonly known as .dbx files). 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Transport-Dbx-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode $RPM_BUILD_ROOT%{_mandir}/man3/Mail::Transport::Dbx.3pm iso-8859-1

%check
make test

%files
%doc README
%{perl_vendorarch}/auto/Mail/
%{perl_vendorarch}/Mail/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
