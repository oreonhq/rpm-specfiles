%global source0_hash 032b71cb597edd92a0b270b916188281bc35be55296b263f6817b29adbcb1709
%global apiversion 0.1
Name: libetonyek
Version: 0.1.13
Release:        1%{?dist}
Summary:        A library for import of Apple iWork documents
License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libetonyek
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
Patch0: mdds3.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glm-devel
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
%{name} is library for import of Apple iWork documents. It supports
documents created by any version of Keynote, Pages or Numbers.

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
Summary: Tools to transform Apple iWork documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform Apple iWork documents into other formats. Currently
supported: CSV, HTML, SVG, text, and raw.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p0

%build

autoreconf -fiv
%configure --disable-silent-rules --disable-static --disable-werror --with-mdds=3.0
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in key2raw key2text key2xhtml numbers2csv numbers2raw numbers2text pages2html pages2raw pages2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 key2*.1 numbers2*.1 pages2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
if ! %make_build check; then
    cat src/test/*.log
    exit 1
fi
%files -f %{oreon_filedir}/main.list
%files -n libetonyek-devel -f %{oreon_filedir}/libetonyek-devel.list
%files -n libetonyek-doc -f %{oreon_filedir}/libetonyek-doc.list
%files -n libetonyek-tools -f %{oreon_filedir}/libetonyek-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.13-1
- Prepare for Oreon 11 (RP1)
