%global source0_hash 44a9e8f60a26bdc9e1d68667d4e0ff7487dc11d16b68b938dcf95cc78b868863
Name:           perl-MouseX-StrictConstructor
Version:        0.02
Release:        1%{?dist}
Summary:        Make your object constructors blow up on unknown attributes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-StrictConstructor
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-StrictConstructor-%{version}.tar.gz
Patch0:         MouseX-StrictConstructor-0.02-Disable-author-tests.patch
BuildArch:      noarch
Requires:       perl(Mouse) >= 0.62
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mouse\\)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute argument that your class does not
declare, then it dies. This is a great way to catch small typos.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-StrictConstructor-%{version}
%patch -P0 -p1
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
