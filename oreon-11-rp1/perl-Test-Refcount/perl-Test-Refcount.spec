%global source0_hash 0457c20a4956473d157c4faaff8814154bc93f6e2b543c2812a19ff8e3370eb2
Name:           perl-Test-Refcount
Version:        0.10
Release:        20%{?dist}
Summary:        Assert reference counts on objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Refcount
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Refcount-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Test::Refcount)
# oreon:deps
BuildRequires:  perl(B)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Perl garbage collector uses simple reference counting during the normal
execution of a program. This means that cycles or unweakened references in
other parts of code can keep an object around for longer than intended. To
help avoid this problem, the reference count of a new object from its class
constructor ought to be 1. This way, the caller can know the object will be
properly DESTROYed when it drops all of its references to it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Refcount-%{version}

%build

/usr/bin/perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
