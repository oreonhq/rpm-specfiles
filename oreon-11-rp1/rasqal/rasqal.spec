%global source0_hash 6924c9ac6570bd241a9669f83b467c728a322470bf34f4b2da4f69492ccfd97c
Name:           rasqal
Version:        0.9.33
Release:        1%{?dist}
Summary:        RDF Query Library
License:        LGPL-2.1-or-later OR Apache-2.0
URL:            http://librdf.org/rasqal/
Source0:        http://download.librdf.org/source/%{name}-%{version}.tar.gz
Patch1: define-printf.patch
Patch2: rasqal-configure-c99-2.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(XML::DOM)
BuildRequires:  raptor2-devel
# /oreon:deps
%description
Rasqal is a library providing full support for querying Resource
Description Framework (RDF) including parsing query syntaxes, constructing
the queries, executing them and returning result formats.  It currently
handles the RDF Data Query Language (RDQL) and SPARQL Query language.

%package        devel
Summary:        Development files for the Rasqal RDF libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Libraries, includes etc to develop with the Rasqal RDF query language library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P1 -p1 -b .printf
%patch -P2 -p1

# hack to nuke rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif

%build

%configure \
  --with-digest-library=gcrypt\
  --disable-pcre \
  --disable-static\
  --enable-release
%make_build
%install
%make_install
rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion rasqal)" = "%{version}"
if [ -x %{_bindir}/rapper ]; then
%ifarch ppc64 s390x
make -k check ||:
%else
make -k check
%endif
else
echo "WARNING: %{_bindir}/rapper not present in buildroot, 'make check' skipped"
fi
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n rasqal-devel -f %{oreon_filedir}/rasqal-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.33-32
- Prepare for Oreon 11 (RP1)
