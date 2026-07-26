%global source0_hash aa409b79a733f0c3550b144cce192a313f078c8ffaf037083ebb8a4beeab65a7

Name:           perl-Clownfish
Version:        0.6.3
Release:        28%{?dist}
Summary:        Apache Clownfish symbiotic object system
# The LICENSE file declares sinces 0.5.0 that portions of the libcmark libary
# from the CommonMark project are bundled. But I cannot find any of the code
# in the Clownfish. I believe the declaration concerns Clownfish-CFC sources
# instead.
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Clownfish
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/Clownfish-%{version}.tar.gz
# There is charmonizer.c which is becoming a separate project
# <git://git.apache.org/lucy-charmonizer.git>. However, lucy-charmonizer has
# not yet been released <http://lucy.apache.org/download.html>.
# A build-time dependency Clownfish::CFC::Perl::Build::Charmonic
# still relies on the local location. Provided charmonizer.c is used only
# at build time and upstream code is not ready for external lucy-charmonizer
# (upstream treats it like a build-time only copy library) I'm not going to
# unbudle the charmonizer.c now.
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Modules from buildlib are used when building
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clownfish::CFC::Perl::Build) >= 0.006003
BuildRequires:  perl(Clownfish::CFC::Perl::Build::Charmonic)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
# Module::Build not used (only when releasing a tar ball)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Generates perl binding, needs header files
BuildRequires:  perl-devel
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
# Generates perl binding, needs perl header files that are included from
# templates installed into _include directory.
Requires:       perl-devel%{?_isa}
Requires:       perl(DynaLoader)

%description
The Apache Clownfish "symbiotic" object system for C is designed to pair
with a "host" dynamic language environment, facilitating the development
of high performance host language extensions. Clownfish classes are
declared in header files with a .cfh extension. The Clownfish headers are
used by the Clownfish compiler to generate C header files and host
language bindings. Methods, functions and variables are defined in normal
C source files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Clownfish-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc CONTRIBUTING.md NOTICE README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Clownfish*
%{_mandir}/man3/*

%changelog
%autochangelog
