# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 cf0c1b1eb29705c02d97c2913648009c0be42ce93ec24b36c696bf2d4f5ebd7e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-File-MMagic
Version:        1.30
Release:        37%{?dist}
Summary:        A Perl module emulating the file(1) command
# MMagic.pm and COPYING files contain identical license texts of App-s2p
# license, BSD license, and ASL 1.0 license.
License:        App-s2p AND Apache-1.0 AND Spencer-94
URL:            https://metacpan.org/release/File-MMagic
Source0:        https://cpan.metacpan.org/authors/id/K/KN/KNOK/File-MMagic-1.30.tar.gz

Patch0:         File-MMagic-1.30-rt109673.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
%if 0%{?fedora} > 34 || 0%{?rhel} > 8 || 0%{?oreon}
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
%oreon_verify_sources
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
