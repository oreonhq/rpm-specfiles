%global source0_hash 5723dd78f4ac0b4d262a05ea46af663ea00d8096b2e9c0a43515c210760e1e75

Name:           perl-Exception-Base
Version:        0.2501
Release:        31%{?dist}
Summary:        Lightweight exceptions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Exception-Base
Source0:        https://cpan.metacpan.org/modules/by-module/Exception/Exception-Base-%{version}.tar.gz
Source2:        to_string_changes_errors.t
Patch0:         Exception-Base-0.2501-smartmatch.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(Test::Unit::Lite)
# Test for https://bugzilla.redhat.com/show_bug.cgi?id=1273668
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Scalar::Util)
Requires:       perl(Symbol)

Provides:       perl(Exception::Base)
%description
This class implements a fully OO exception mechanism similar to
Exception::Class or Class::Throwable. It provides a simple interface
allowing programmers to declare exception classes. These classes can be
thrown and caught. Each uncaught exception prints full stack trace if the
default verbosity is increased for debugging purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Exception-Base-%{version}

# Fix FTBFS with Perl 5.38 onwards (rhbz#2222742)
# Smartmatch is deprecated, resulting warning causes test failures
# https://github.com/dex4er/perl-Exception-Base/issues/5
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

# to_string() appends 'undef' to array attribute
# https://bugzilla.redhat.com/show_bug.cgi?id=1273668
# https://github.com/dex4er/perl-Exception-Base/issues/3
# Fixed in 0.2501
make test TEST_FILES=%{SOURCE2}

%files
%license LICENSE
%doc Changes Incompatibilities README examples/
%{perl_vendorlib}/Exception/
%{_mandir}/man3/Exception::Base.3*

%changelog
%autochangelog
