%global source0_hash b2c010ed9cd711d8ea9bcb7c0965a7ec9a0fab509fca8b3cde114a72d1809135

Name:           perl-B-Hooks-OP-Check-StashChange
Version:        0.06
Release:        52%{?dist}
Summary:        Invoke callbacks when the stash code is being compiled in changes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Hooks-OP-Check-StashChange
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/B-Hooks-OP-Check-StashChange-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ExtraTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.14
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
Register callbacks when an opcode is being compiled in a different namespace
than the previous one.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Hooks-OP-Check-StashChange-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
%autochangelog
