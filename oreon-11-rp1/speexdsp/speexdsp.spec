%global source0_hash 8c777343e4a6399569c72abc38a95b24db56882c83dbdb6c6424a5f4aeb54d3d
Name:           speexdsp
Version:        1.2.1
Release:        1%{?dist}
Summary:        A voice compression format (DSP)
License:        BSD-3-Clause
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{name}-%{version}.tar.gz
Conflicts:      speex <= 1.2-0.21.rc1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
Conflicts:      speex-devel <= 1.2-0.21.rc1
%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}

This is the DSP package, see the speex package for the codec part.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
%ifarch aarch64
	--disable-neon \
%endif
	--disable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n speexdsp-devel -f %{oreon_filedir}/speexdsp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-10
- Prepare for Oreon 11 (RP1)
