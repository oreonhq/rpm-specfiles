%global source0_hash bbca92882e96c55bd1527670866d6bc7529ccb12786da55a2398b60a063378da
%global apiversion 0.0
Name: libstaroffice
Version: 0.0.8
Release:        1%{?dist}
Summary:        A library for import of binary StarOffice documents
License: LGPL-2.1-or-later OR MPL-2.0
URL: https://github.com/fosnola/libstaroffice/wiki
Source0:        https://github.com/fosnola/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
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
%{name} is a library for import of binary StarOffice documents.

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
Summary: Tools to transform StarOffice documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform StarOffice documents into other formats. Currently
supported: CSV, HTML, plain text, SVG, raw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --disable-silent-rules --enable-zip
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_docdir}/%{name}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in sd2raw sd2svg sd2text sdc2csv sdw2html; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 sd2*.1 sd?2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libstaroffice-devel -f %{oreon_filedir}/libstaroffice-devel.list
%files -n libstaroffice-doc -f %{oreon_filedir}/libstaroffice-doc.list
%files -n libstaroffice-tools -f %{oreon_filedir}/libstaroffice-tools.list

%changelog

%autochangelog
