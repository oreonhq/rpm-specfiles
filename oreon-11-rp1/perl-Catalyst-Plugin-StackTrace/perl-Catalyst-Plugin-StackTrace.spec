%global source0_hash 329dacd0ba09d10a76087ab176f95db6ba3db26a2d0fe33eee2f5e46ced753ac

Name:           perl-Catalyst-Plugin-StackTrace
Version:        0.12
Release:        31%{?dist}
Summary:        Display a stack trace on the debug screen
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-StackTrace
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-StackTrace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst) >= 5.70
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(warnings)
Requires:       perl(Catalyst) >= 5.70
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)

%description
This plugin will enhance the standard Catalyst debug screen by including a
stack trace of your appliation up to the point where the error occurred.
Each stack frame is displayed along with the package name, line number,
file name, and code context surrounding the line number.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-StackTrace-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
