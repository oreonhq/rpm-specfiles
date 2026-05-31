%global source0_hash cf0c1b1eb29705c02d97c2913648009c0be42ce93ec24b36c696bf2d4f5ebd7e

Name:           perl-File-MMagic
Version:        1.30
Release:        37%{?dist}
Summary:        A Perl module emulating the file(1) command
# MMagic.pm and COPYING files contain identical license texts of App-s2p
# license, BSD license, and ASL 1.0 license.
License:        App-s2p AND Apache-1.0 AND Spencer-94
URL:            https://metacpan.org/release/File-MMagic
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-MMagic-%{version}.tar.gz



Patch0:         File-MMagic-1.30-rt109673.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
%if 0%{?fedora} > 34 || 0%{?rhel} > 8 || (0%{?oreon} >= 11)
BuildRequires:  glibc-gconv-extra
%endif
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Runtime

%description
This module attempts to guess a file's type from its contents like the file(1)
command.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-MMagic-%{version}

# Fix "Redundant argument in sprintf" warning (CPAN RT#109673)
%patch -P0

# Re-code README.ja as UTF-8
iconv -f ISO-2022-JP -t utf8 README.ja > README.ja.utf8 && mv README.ja.utf8 README.ja

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc ChangeLog README.en README.ja
%{perl_vendorlib}/File/
%{_mandir}/man3/File::MMagic.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30-37
- Import
