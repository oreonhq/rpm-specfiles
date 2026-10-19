%global source0_hash aa409b79a733f0c3550b144cce192a313f078c8ffaf037083ebb8a4beeab65a7
Name:           perl-Clownfish
Version:        0.6.3
Release:        28%{?dist}
Summary:        Apache Clownfish symbiotic object system
License:        Apache-2.0
URL:            https://metacpan.org/release/Clownfish
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARMAN/Clownfish-%{version}.tar.gz
Requires:       perl-devel%{?_isa}
Requires:       perl(DynaLoader)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clownfish::CFC::Perl::Build)
BuildRequires:  perl(Clownfish::CFC::Perl::Build::Charmonic)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
