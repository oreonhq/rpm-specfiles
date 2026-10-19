%global source0_hash 35187a3833c2fe62710f47e5bde3ee1c32fd964bcedf2ca65c3f324e82a8a1fa
Name:           ahven
Version:        2.9
Release:        1%{?dist}
Summary:        A unit testing framework for Ada 95
Summary(sv):    Ett enhetstestramverk för ada 95
License:        ISC
URL:            https://www.ahven-framework.com/
Source0:        https://www.ahven-framework.com/releases/%{name}-%{version}.tar.gz
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
Ahven is a simple unit testing library (or a framework) for the Ada \
programming language. It is loosely modeled after Junit and some ideas are \
taken from Aunit.
%global common_description_sv \
Ahven är ett enkelt bibliotek (eller ramverk) för enhetstestning i \
programmeringsspråket ada. Det efterliknar Junit i stora drag, och några idéer \
är hämtade från Aunit.
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  make
BuildRequires:  python3-sphinx
# /oreon:deps
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
rm %{buildroot}%{_pkgdocdir}/html/{.buildinfo,objects.inv}
cp --preserve=timestamps README.md ROADMAP NEWS.txt %{buildroot}%{_pkgdocdir}
%oreon_autofiles ahven-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%global GNAT_add_rpath x
%undefine _hardened_build
%{Comfignat_make} check GNAT_BUILDER=gprbuild OS_VERSION=unix
%files -f %{oreon_filedir}/main.list
%files -n ahven-devel -f %{oreon_filedir}/ahven-devel.list

%changelog

%autochangelog
