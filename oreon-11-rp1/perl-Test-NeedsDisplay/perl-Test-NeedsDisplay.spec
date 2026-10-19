%global source0_hash 60e93f6777a423c3b598ddafaf79d69c5f567ffc92f1b20229f51381df4344a9
Name:           perl-Test-NeedsDisplay
Version:        1.07
Release:        41%{?dist}
Summary:        Ensure that tests needing a display have one
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NeedsDisplay
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NeedsDisplay-%{version}.tar.gz
Patch0:         Test-NeedsDisplay-1.07-Use-non-conflicting-display-numbers.patch
BuildArch:      noarch
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Test::More) >= 0.47
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Install::External)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  xeyes
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
When testing GUI applications, sometimes applications or modules absolutely
insist on a display, even just to load a module without actually showing
any objects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-NeedsDisplay-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf ./inc
sed -i -e '/^inc\//d' MANIFEST

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
