%global source0_hash 70909763bfd9d1919890df0e662e99b2bd8db8fa4e585a1224a26ffb12a078cc
Name:           perl-B-Hooks-OP-Check-EntersubForCV
Version:        0.10
Release:        1%{?dist}
Summary:        Invoke callbacks on construction of entersub OPs for certain CVs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Hooks-OP-Check-EntersubForCV
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/B-Hooks-OP-Check-EntersubForCV-%{version}.tar.gz
Patch0:         B-Hooks-OP-Check-EntersubForCV-0.09-Disable-author-tests.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(B::Utils)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-B-Hooks-OP-Check-EntersubForCV-devel -f %{oreon_filedir}/perl-B-Hooks-OP-Check-EntersubForCV-devel.list

%changelog

%autochangelog
