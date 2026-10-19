%global source0_hash 3671095f5a10bee8a755052a30576952c5b16d8b0f2ba9f2fb998338c18cb119
%global apiversion 0.1
Name: libmspub
Version: 0.1.5
Release:        1%{?dist}
Summary:        A library for import of Microsoft Publisher documents
License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libmspub
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
Patch0: gcc10.patch
Patch1: includes.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

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

%package tools
Summary: Tools to transform Microsoft Publisher documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform Microsoft Publisher documents into other formats.
Currently supported: XHTML, raw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="%{optflags} -std=c++20"
%configure --disable-static --disable-silent-rules
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
 export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
 for tool in pub2raw pub2xhtml; do
     help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
 done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 pub2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmspub-devel -f %{oreon_filedir}/libmspub-devel.list
%files -n libmspub-doc -f %{oreon_filedir}/libmspub-doc.list
%files -n libmspub-tools -f %{oreon_filedir}/libmspub-tools.list

%changelog

%autochangelog
