%global source0_hash ac3590f691a2904eb8c7dc8b757b8a29f125f592449e421459ae8fa928b399eb
%global apiversion 0.3
Name: libmwaw
Version: 0.3.23
Release:        1%{?dist}
Summary:        A library for import of many old Mac document formats
License: LGPL-2.1-or-later OR MPL-2.0
URL: http://sourceforge.net/projects/libmwaw/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
# /oreon:deps
%description
%{name} is a library for import of old Mac documents. It supports many
kinds of text documents, spreadsheets, databases, vector and bitmap
images. Supported are, for example, documents created by BeagleWorks,
ClarisWorks, MacPaint, MacWrite or Microsoft Word for Mac. A full list
of supported formats is available at
https://sourceforge.net/p/libmwaw/wiki/Home/ .

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
Summary: Tools to transform the supported formats into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform the supported document formats into other formats.
Supported output formats are CSV, HTML, SVG, plain text and raw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --disable-werror --disable-zip --enable-docs
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'convert Mac spreadsheet into CSV' -o mwaw2csv.1 ./src/conv/csv/.libs/mwaw2csv
help2man -N -n 'debug the conversion library' -o mwaw2raw.1 ./src/conv/raw/.libs/mwaw2raw
help2man -N -n 'convert Mac text document into HTML' -o mwaw2html.1 ./src/conv/html/.libs/mwaw2html
help2man -N -n 'convert Mac drawing into SVG' -o mwaw2svg.1 ./src/conv/svg/.libs/mwaw2svg
help2man -N -n 'convert Mac text document into plain text' -o mwaw2text.1 ./src/conv/text/.libs/mwaw2text
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_bindir}/mwawFile
rm -rf %{buildroot}/%{_docdir}/%{name}
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 mwaw2*.1 %{buildroot}/%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmwaw-devel -f %{oreon_filedir}/libmwaw-devel.list
%files -n libmwaw-doc -f %{oreon_filedir}/libmwaw-doc.list
%files -n libmwaw-tools -f %{oreon_filedir}/libmwaw-tools.list

%changelog

%autochangelog
