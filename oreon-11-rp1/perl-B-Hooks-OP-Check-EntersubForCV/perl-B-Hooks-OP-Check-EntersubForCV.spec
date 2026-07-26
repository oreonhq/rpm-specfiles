%global source0_hash 70909763bfd9d1919890df0e662e99b2bd8db8fa4e585a1224a26ffb12a078cc

Name:           perl-B-Hooks-OP-Check-EntersubForCV
Version:        0.10
Release:        28%{?dist}
Summary:        Invoke callbacks on construction of entersub OPs for certain CVs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Hooks-OP-Check-EntersubForCV
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/B-Hooks-OP-Check-EntersubForCV-%{version}.tar.gz
# Remove unwanted build dependencies
Patch0:         B-Hooks-OP-Check-EntersubForCV-0.09-Disable-author-tests.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.19
BuildRequires:  perl(B::Utils) >= 0.19
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Invoke callbacks on construction of entersub OPs for certain CVs.

%package devel
Summary:        XS support for B::Hooks::OP::Check::EntersubForCV
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-devel%{?_isa}

%description devel
These are developmental files needed for using
B::Hooks::OP::Check::EntersubForCV Perl module from XS code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Hooks-OP-Check-EntersubForCV-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/B
%exclude %{perl_vendorarch}/B/Hooks/OP/Check/EntersubForCV/Install
%{_mandir}/man3/*

%files devel
%{perl_vendorarch}/B/Hooks/OP/Check/EntersubForCV/Install

%changelog
%autochangelog
