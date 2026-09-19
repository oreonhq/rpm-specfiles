%global source0_hash 118d8601c12dd6a44f52423e68ca9083cc9f2bfe72da7a8c1acb22a80ae3550b

%{?mingw_package_header}

%global _basename opusfile

Name:          mingw-%{_basename}
Version:       0.12
Release:       17%{?dist}
Summary:       A high-level API for decoding and seeking within .opus files

License:       BSD-3-Clause
URL:           https://www.opus-codec.org/
Source0:       https://downloads.xiph.org/releases/opus/%{_basename}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1675383
Patch0:        opusfile-0.11-disable-cert-store-integration.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2163898
Patch1:        mingw-opusfile-0.12-CVE-2022-47021.patch

BuildArch:     noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libogg
BuildRequires: mingw32-openssl
BuildRequires: mingw32-opus

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libogg
BuildRequires: mingw64-openssl
BuildRequires: mingw64-opus

%description
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.

%package -n mingw32-%{_basename}
Summary: A high-level API for decoding and seeking within .opus files

%description -n mingw32-%{_basename}
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.
This is the MinGW version, built for the win32 target.

%package -n mingw64-%{_basename}
Summary: A high-level API for decoding and seeking within .opus files

%description -n mingw64-%{_basename}
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.
This is the MinGW version, built for the win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{_basename}-%{version}

%build
%{mingw_configure} --disable-static

%{mingw_make} %{?_smp_mflags} V=1

%install
# Unset dist_doc_DATA to prevent installing docs. Use files sections instead.
%{mingw_make} DESTDIR=%{buildroot} INSTALL='install -p' dist_doc_DATA= install 

# Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%files -n mingw32-%{_basename}
%doc AUTHORS README.md
%license COPYING
%{mingw32_bindir}/libopusfile-0.dll
%{mingw32_bindir}/libopusurl-0.dll
%{mingw32_libdir}/libopusfile.dll.a
%{mingw32_libdir}/libopusurl.dll.a
%{mingw32_libdir}/pkgconfig/opusfile.pc
%{mingw32_libdir}/pkgconfig/opusurl.pc
%{mingw32_includedir}/opus/opus*

%files -n mingw64-%{_basename}
%doc AUTHORS README.md
%license COPYING
%{mingw64_bindir}/libopusfile-0.dll
%{mingw64_bindir}/libopusurl-0.dll
%{mingw64_libdir}/libopusfile.dll.a
%{mingw64_libdir}/libopusurl.dll.a
%{mingw64_libdir}/pkgconfig/opusfile.pc
%{mingw64_libdir}/pkgconfig/opusurl.pc
%{mingw64_includedir}/opus/opus*

%changelog
%autochangelog
