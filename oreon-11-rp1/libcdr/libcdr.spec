%global source0_hash f7bb6abdd7f226820f288a93dd8d07759833c0250d9e202af90f9b312c4665a3
%global apiversion 0.1
Name: libcdr
Version: 0.1.9
Release:        1%{?dist}
Summary:        A library for import of CorelDRAW drawings
License: MPL-2.0 AND LicenseRef-Fedora-Public-Domain
URL: http://wiki.documentfoundation.org/DLP/Libraries/libcdr
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Libcdr is library providing ability to interpret and import CorelDRAW
drawings into various applications. You can find it being used in
libreoffice.

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
Summary: Tools to transform CorelDRAW drawings into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform CorelDRAW drawings into other formats.
Currently supported: XHTML, text, raw.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-silent-rules --disable-static --disable-werror
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
for tool in cdr2raw cmx2raw cdr2xhtml cmx2xhtml cdr2text cmx2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 cdr2*.1 cmx2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libcdr-devel -f %{oreon_filedir}/libcdr-devel.list
%files -n libcdr-doc -f %{oreon_filedir}/libcdr-doc.list
%files -n libcdr-tools -f %{oreon_filedir}/libcdr-tools.list

%changelog

%autochangelog
