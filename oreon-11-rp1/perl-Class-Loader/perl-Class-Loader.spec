%global source0_hash 4fef2076ead60423454ff1f4e82859a9a9b9942b5fb8eee0c98b9c63c9f2b8e7

Summary:	Load modules and create objects on demand
Name:		perl-Class-Loader
Version:	2.03
Release:	53%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-Loader
Source0:	https://cpan.metacpan.org/modules/by-module/Class/Class-Loader-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Module
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test)
# Dependencies
# (none)

%description
Certain applications like to defer the decision to use a particular module till
runtime. This is possible in perl, and is a useful trick in situations where
the type of data is not known at compile time and the application doesn't wish
to pre-compile modules to handle all types of data it can work with. Loading
modules at runtime can also provide flexible interfaces for perl modules.
Modules can let the programmer decide what modules will be used by it instead
of hard-coding their names.

Class::Loader is an inheritable class that provides a method, _load(), to load
a module from disk and construct an object by calling its constructor. It also
provides a way to map modules' names and associated metadata with symbolic
names that can be used in place of module names at _load().

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Loader-%{version}

# Fix shellbangs
sed -i -e '/^#! *\/usr\/bin\/perl /d' lib/Class/*.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license ARTISTIC
%doc Changes
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Loader.3*

%changelog
%autochangelog
