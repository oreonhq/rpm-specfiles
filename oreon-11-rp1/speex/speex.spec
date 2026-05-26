Summary:	A voice compression format (codec)
Name:		speex
Version:	1.2.0
Release:	21%{?dist}
License:	BSD-3-clause AND TU-Berlin-1.0
URL:		https://www.speex.org/
Source0:	https://downloads.xiph.org/releases/speex/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	gcc
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(speexdsp)
Patch0:		speex-1.2.0-guard-against-invalid-channel-numbers.patch
# oreon url source checksums begin
%global source0_sha256 eaae8af0ac742dc7d542c9439ac72f1f385ce838392dc849cae4536af9210094
%global source0_file speex-1.2.0.tar.gz
# oreon url source checksums end

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

%package devel
Summary: 	Development package for %{name}
Requires: 	%{name}%{?_isa} = %{version}-%{release}

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}

%package tools
Summary:	The tools package for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Speex is a patent-free compression format designed especially for
speech. This package contains tools files and user's manual for %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/speex-1.2.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "eaae8af0ac742dc7d542c9439ac72f1f385ce838392dc849cae4536af9210094" || { echo "oreon: Source0 SHA256 mismatch for speex-1.2.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p1 -b.CVE-2020-23903

%build
%configure --disable-static --enable-binaries
# Remove rpath from speexenc and speexdec
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_docdir}/speex/manual.pdf

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS TODO ChangeLog README NEWS
%{_libdir}/libspeex.so.1*

%files devel
%doc doc/manual.pdf
%{_includedir}/speex
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex.pc
%{_libdir}/libspeex.so
%exclude %{_libdir}/libspeex.la

%files tools
%{_bindir}/speexenc
%{_bindir}/speexdec
%{_mandir}/man1/speexenc.1*
%{_mandir}/man1/speexdec.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-21
- Prepare for Oreon 11 (RP1)
