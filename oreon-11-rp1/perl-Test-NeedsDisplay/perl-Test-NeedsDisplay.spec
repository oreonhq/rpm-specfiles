%global source0_hash 60e93f6777a423c3b598ddafaf79d69c5f567ffc92f1b20229f51381df4344a9

Name:           perl-Test-NeedsDisplay
Version:        1.07
Release:        41%{?dist}
Summary:        Ensure that tests needing a display have one
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NeedsDisplay
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NeedsDisplay-%{version}.tar.gz
# Prevent from races by using free display numbers, bug #1248968,
# CPAN RT#106699
Patch0:         Test-NeedsDisplay-1.07-Use-non-conflicting-display-numbers.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.77
BuildRequires:  perl(Module::Install::External)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# xorg-x11-server-Xvfb for xvfb-run program required by Makefile.PL
BuildRequires:  xorg-x11-server-Xvfb
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(warnings)
# Optional tests:
# Pod::Simple 3.07 not used
# Test::CPAN::Meta 0.12 not used
# Test::MinimumVersion 0.008 not used
# Test::Pod 1.26 not used
# xeyes for xeyes (will pull in xorg-x11-apps on older distros)
BuildRequires:  xeyes
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Test::More) >= 0.47

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Test::More)\\)$

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
