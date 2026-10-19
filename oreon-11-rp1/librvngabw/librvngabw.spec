%global source0_hash c6fb7d0227327111cbb17fe0ab25fd8db04f7c063a9e6e03eef71d3ab7c8c1bc
%global apiversion 0.0
Name: librvngabw
Version: 0.0.3
Release:        1%{?dist}
Summary:        An AbiWord document generator library
License: LGPL-2.1-or-later OR MPL-2.0
URL: https://sourceforge.net/projects/librvngabw/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
# /oreon:deps
%description
%{name} is a library for generating AbiWord documents. It is directly
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

%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n librvngabw-devel -f %{oreon_filedir}/librvngabw-devel.list
%files -n librvngabw-doc -f %{oreon_filedir}/librvngabw-doc.list

%changelog

%autochangelog
