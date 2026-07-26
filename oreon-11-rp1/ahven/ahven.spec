%global source0_hash 35187a3833c2fe62710f47e5bde3ee1c32fd964bcedf2ca65c3f324e82a8a1fa

Name:           ahven
Version:        2.9
Release:        4%{?dist}
Summary:        A unit testing framework for Ada 95
Summary(sv):    Ett enhetstestramverk för ada 95

License:        ISC
URL:            https://www.ahven-framework.com/
Source:         https://www.ahven-framework.com/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gnat make fedora-gnat-project-common
BuildRequires:  gprbuild
BuildRequires:  python3-sphinx
# Build only on architectures where gcc-gnat is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Ahven is a simple unit testing library (or a framework) for the Ada \
programming language. It is loosely modeled after Junit and some ideas are \
taken from Aunit.

%global common_description_sv \
Ahven är ett enkelt bibliotek (eller ramverk) för enhetstestning i \
programmeringsspråket ada. Det efterliknar Junit i stora drag, och några idéer \
är hämtade från Aunit.

%description %{common_description_en}

Features:
· Simple API
· Small size
· Junit-compatible test results in XML format, which allows integration with
  tools like Jenkins or Teamcity
· Strict coding style (enforced by Adacontrol)
· Plain Ada 95 code, no Ada 2005 features used, but can be compiled as Ada 2005
  or Ada 2012 code if needed
· Portable across different compilers and operating systems
· Permissive Open Source license (ISC)

%description -l sv %{common_description_sv}

Fördelar:
· Enkelt programmeringsgränssnitt
· Liten kodstorlek
· Junit-kompatibla testresultat i XML-form, vilket möjliggör samverkan med
  sådana verktyg som Jenkins eller Teamcity
· Stränga kodformateringsregler (upprätthållna av Adacontrol)
· Renodlad ada 95-kod som inte använder några ada 2005-finesser men kan
  kompileras som ada 2005 eller ada 2012 vid behov
· Portabelt mellan olika kompilatorer och operativsystem
· Medgörlig, fri licens (ISC)

%package devel
Summary:        Development files for Ahven
Summary(sv):    Filer för programmering med Ahven
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Ahven.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Ahven.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{Comfignat_make} all GNAT_BUILDER=gprbuild OS_VERSION=unix

%install
%{make_install}

# These files aren't needed in the package.
rm %{buildroot}%{_pkgdocdir}/html/{.buildinfo,objects.inv}

# Include these documentation files.
cp --preserve=timestamps README.md ROADMAP NEWS.txt %{buildroot}%{_pkgdocdir}

%check
%global GNAT_add_rpath x
# Disable the hardening hack only for the testsuite.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
%undefine _hardened_build

%{Comfignat_make} check GNAT_BUILDER=gprbuild OS_VERSION=unix

%files
%{_libdir}/*.so.*
%license LICENSE.txt

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}
%{_GNAT_project_dir}/*
%{_pkgdocdir}

%changelog
%autochangelog
