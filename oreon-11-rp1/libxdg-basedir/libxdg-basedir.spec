%global source0_hash 1c2b0032a539033313b5be2e48ddd0ae94c84faf21d93956d53562eef4614868

Name:           libxdg-basedir
Version:        1.2.0
Release:        38%{?dist}
Summary:        Implementation of the XDG Base Directory Specifications

License:        MIT
URL:            https://github.com/devnev/libxdg-basedir
Source0:        https://github.com/devnev/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         libxdg-basedir-leak.patch
Patch1:         libxdg-basedir-valgrind-libtool.patch
Patch2:         libxdg-basedir-basedir-bounds-error.patch 
Patch3:         libxdg-basedir-home-undef.patch
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  libtool

%description
The XDG Base Directory Specification defines where should user files 
be looked for by defining one or more base directories relative in 
with they should be located.

This library implements functions to list the directories according 
to the specification and provides a few higher-level functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires: make

%description    doc
The %{name}-doc package contains doxygen generated files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%configure --disable-static
make %{?_smp_mflags}
make doxygen-run

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
%ifarch %{valgrind_arches}
make check USE_VALGRIND=1
%else
make check
%endif
#env -i make check USE_VALGRIND=1
# Check that we get NULL for all things rooted in ENV{HOME} when running
# with HOME unset
env -i ./tests/testdump | grep null > grep.NULL
env -i ./tests/testdump | grep HOME | grep -v DIRS > grep.HOME
diff -u grep.NULL grep.HOME

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc doc/html/

%changelog
%autochangelog
