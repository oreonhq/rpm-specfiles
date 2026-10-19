%global source0_hash 03e084b994cbeffc8c3dd13303b2cb805f44d8f2c3b79f7690d7e3fc7f6215ad
%global apiversion 0.1
Name: libepubgen
Version: 0.1.1
Release:        1%{?dist}
Summary:        An EPUB generator library
License: MPL-2.0
URL: https://sourceforge.net/projects/libepubgen/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
%{name} is a library for generating EPUB documents. It is directly
pluggable into import filters based on librevenge.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch
%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make %{?_smp_mflags} check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libepubgen-devel -f %{oreon_filedir}/libepubgen-devel.list
%files -n libepubgen-doc -f %{oreon_filedir}/libepubgen-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.1-1
- Prepare for Oreon 11 (RP1)
