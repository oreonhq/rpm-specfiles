%global source0_hash f8a5bf5a28702dfb13c8093be5c41cab9c5fc1c5d247ab91e22e7dd72764cb5e
Name:           perl-MouseX-NativeTraits
Version:        1.09
Release:        1%{?dist}
Summary:        Extend your attribute interfaces for Mouse
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MouseX-NativeTraits
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/MouseX-NativeTraits-%{version}.tar.gz
Patch0:         MouseX-NativeTraits-1.09-Disable-author-tests.patch
BuildArch:      noarch
Requires:       perl(Mouse) >= 0.82
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mouse\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::TestTarget)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
While Mouse attributes provide a way to name your accessors, readers,
writers, clearers and predicates, MouseX::NativeTraits provides commonly
used attribute helper methods for more specific types of data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-NativeTraits-%{version}
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
