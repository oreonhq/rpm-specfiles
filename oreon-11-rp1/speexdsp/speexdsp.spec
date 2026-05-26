Name:           speexdsp
Version:        1.2.1
Release:        10%{?dist}
Summary:        A voice compression format (DSP)

License:        BSD-3-Clause
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8c777343e4a6399569c72abc38a95b24db56882c83dbdb6c6424a5f4aeb54d3d
%global source0_file speexdsp-1.2.1.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  make
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts:      speex <= 1.2-0.21.rc1

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.

%package devel
Summary: 	Development package for %{name}
Requires: 	%{name}%{?_isa} = %{version}-%{release}
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts:      speex-devel <= 1.2-0.21.rc1

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}

This is the DSP package, see the speex package for the codec part.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/speexdsp-1.2.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8c777343e4a6399569c72abc38a95b24db56882c83dbdb6c6424a5f4aeb54d3d" || { echo "oreon: Source0 SHA256 mismatch for speexdsp-1.2.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%configure \
%ifarch aarch64
	--disable-neon \
%endif
	--disable-static

%make_build

%install
%make_install

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS TODO ChangeLog README NEWS doc/manual.pdf
%doc %{_docdir}/speexdsp/manual.pdf
%{_libdir}/libspeexdsp.so.1*

%files devel
%{_includedir}/speex/
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-10
- Prepare for Oreon 11 (RP1)
