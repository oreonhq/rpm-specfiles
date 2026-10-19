%global source0_hash 2465b0b662fdc5d4e3bebcdc9a79027713fb629ca2bff04a3c9251fdec42dd09
%global apiversion 0.10
Name: libwpd
Summary:        A library for import of WordPerfect documents
Version: 0.10.3
Release:        1%{?dist}
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0: %{name}-gcc11.patch
URL: http://libwpd.sf.net/
License: LGPL-2.1-or-later OR MPL-2.0
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
%{name} is a library for import of WordPerfect documents.

%package tools
Summary: Tools to transform WordPerfect documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform WordPerfect documents into other formats.
Currently supported: HTML, raw, text.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Files for developing with libwpd
%description devel
Includes and definitions for developing with libwpd.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch
%description doc
The %{name}-doc package contains API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in wpd2html wpd2raw wpd2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 wpd2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libwpd-tools -f %{oreon_filedir}/libwpd-tools.list
%files -n libwpd-devel -f %{oreon_filedir}/libwpd-devel.list
%files -n libwpd-doc -f %{oreon_filedir}/libwpd-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.3-1
- Prepare for Oreon 11 (RP1)
