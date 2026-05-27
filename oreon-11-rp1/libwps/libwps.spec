%global source0_hash 365b968e270e85a8469c6b160aa6af5619a4e6c995dbb04c1ecc1b4dd13e80de

%global apiversion 0.4

Name:		libwps
Version:	0.4.14
Release:	%autorelease
Summary:	A library for import of Microsoft Works documents

License:	LGPL-2.1-or-later OR MPL-2.0
URL:		http://libwps.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(librevenge-generators-0.0)
BuildRequires:	pkgconfig(librevenge-stream-0.0)
BuildRequires:	make

%description
%{name} is a library for import of Microsoft Works text documents,
spreadsheets and (in a limited way) databases. Full list of supported
formats is available at
https://sourceforge.net/p/libwps/wiki/Home/#recognized-formats .

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools to transform Microsoft Works documents into other formats
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Microsoft Works documents into other formats.
Currently supported: CSV, HTML, raw, text

%package doc
Summary:	Documentation of %{name} API
BuildArch:	noarch

%description doc
The %{name}-doc package contains documentation files for %{name}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR="%{buildroot}" 
rm -f %{buildroot}%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in wks2csv wks2raw wks2text wps2html wps2raw wps2text; do
    help2man -S '%{name} %{version}' -N -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 wks2*.1 wps2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc CREDITS NEWS README
%license COPYING.LGPL COPYING.MPL
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files tools
%{_bindir}/wks2csv
%{_bindir}/wks2raw
%{_bindir}/wks2text
%{_bindir}/wps2html
%{_bindir}/wps2raw
%{_bindir}/wps2text
%{_mandir}/man1/wks2csv.1*
%{_mandir}/man1/wks2raw.1*
%{_mandir}/man1/wks2text.1*
%{_mandir}/man1/wps2html.1*
%{_mandir}/man1/wps2raw.1*
%{_mandir}/man1/wps2text.1*

%files doc
%license COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.14-1
- Prepare for Oreon 11 (RP1)
