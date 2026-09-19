%global source0_hash 118d8601c12dd6a44f52423e68ca9083cc9f2bfe72da7a8c1acb22a80ae3550b

Name:          opusfile
Version:       0.12
%global soname_version 0
Release:       18%{?dist}
Summary:       A high-level API for decoding and seeking within .opus files
License:       BSD-3-Clause
URL:           https://www.opus-codec.org/
Source0:       https://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Propagate allocation failure from ogg_sync_buffer.
# https://github.com/xiph/opusfile/commit/0a4cd796df5b030cb866f3f4a5e41a4b92caddf5
#
# Fixes CVE-2022-47021.
# A potential bug of NPD
# https://github.com/xiph/opusfile/issues/36
Patch1:        https://github.com/xiph/opusfile/commit/0a4cd796df5b030cb866f3f4a5e41a4b92caddf5.patch#/CVE-2022-47021.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(opus)

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

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# The public API headers include ogg/ogg.h.
Requires: pkgconfig(ogg)

%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libopusfile.so.%{soname_version}{,.*}
%{_libdir}/libopusurl.so.%{soname_version}{,.*}

%files devel
%doc %{_docdir}/%{name}
%{_includedir}/opus/opus*
%{_libdir}/pkgconfig/opusfile.pc
%{_libdir}/pkgconfig/opusurl.pc
%{_libdir}/libopusfile.so
%{_libdir}/libopusurl.so

%changelog
%autochangelog
