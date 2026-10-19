%global source0_hash 285ad62b670075708b9fcfe14c54baa599733bc274d10502a82e8eebba0b7c70
Name:           prrte
Version:        4.1.0
Release:        1%{?dist}
Summary:        PMIx Reference RunTime Environment (PRRTE)
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause
URL:            https://github.com/openpmix/%{name}
Source0:        https://github.com/openpmix/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hwloc-devel
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pmix-devel
BuildRequires:  pmix-tools
# /oreon:deps
%description
PRRTE is the PMIx Reference Run Time Environment.

The project is formally referred to in documentation by "PRRTE", and
the GitHub repository is "openpmix/%{name}".

However, we have found that most users do not like typing the two
consecutive "r"s in the name. Hence, all of the internal API symbols,
environment variables, MCA frameworks, and CLI executables all use the
abbreviated "prte" (one "r", not two) for convenience.

%package        libs
Summary:        Libraries for %{name}
%description    libs
Runtime libraries for %{name}.

%package        devel
Summary:        Development files for %{name}
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause AND MIT AND (MIT OR GPL-2.0-or-later) AND (OFL-1.1 OR MIT)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

# touch lexer sources to recompile them
find src -name \*.l -print -exec touch --no-create {} \;

# Remove “BSD with advertising” licensed qsort implementation, which was only
# needed to work around ancient Solaris bugs. The typedef keeps the translation
# unit from being empty.
echo '' > src/util/qsort.h
echo 'typedef int x;' > src/util/qsort.c

%build

%configure \
    --sysconfdir=%{_sysconfdir}/prte \
    --disable-static \
    --disable-silent-rules \
    --enable-shared \
    --with-sge
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_libdir}/openmpi/{bin,share/man}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/openmpi/bin
mv %{buildroot}%{_mandir}/* %{buildroot}%{_libdir}/openmpi/share/man/
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n prrte-libs -f %{oreon_filedir}/prrte-libs.list
%files -n prrte-devel -f %{oreon_filedir}/prrte-devel.list

%changelog

%autochangelog
