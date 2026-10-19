%global source0_hash 23b32bb98260a0254c58e6e7b4f4582b78509ed08d83b366a85d77a946220d15
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%undefine _debugsource_packages
%endif
Name:           cloog
%global         tarball_name %{name}
Version:        0.18.4
Release:        24%{?dist}
Epoch:		1
Summary:        The Chunky Loop Generator
License:        GPL-2.0-or-later
URL:            http://www.cloog.org
Source0:        cloog-%{version}.tar.gz
Obsoletes: cloog-ppl < 0.18.3
Obsoletes: cloog-ppl-devel < 0.18.3
# oreon:deps
BuildRequires:  gmp-devel
BuildRequires:  isl-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package devel
Summary:        Development tools for the Chunky Loop Generator
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       isl-devel >= 0.15, gmp-devel >= 6.0.0
%description devel
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarball_name}-%{version}

%build

./autogen.sh
%configure \
    --with-isl=system \
    --with-isl-prefix=%{_prefix}
test -f doc/cloog.info && rm doc/cloog.info
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
CLOOG_CFLAGS="-fPIE"
%endif
make %{?_smp_mflags} AM_CFLAGS=${CLOOG_CFLAGS} LIBTOOL=%{_bindir}/libtool
make %{?_smp_mflags} AM_CFLAGS=${CLOOG_CFLAGS} LIBTOOL=%{_bindir}/libtool -C doc cloog.pdf
%install
%make_install INSTALL="%{__install} -p"
rm %{buildroot}%{_libdir}/*/*.cmake
mkdir -p %{buildroot}%{_docdir}/cloog-%{version}
%{__install} -m0644 -p README LICENSE ChangeLog doc/cloog.pdf %{buildroot}%{_docdir}/cloog-%{version}
%oreon_autofiles cloog-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cloog-devel -f %{oreon_filedir}/cloog-devel.list

%changelog

%autochangelog
