%global source0_hash 4b44d4f2b38a370a2d98a78329fefc56a0cf93d1c1be70029217baae6628feea
Summary:        A voice compression format (codec)
Name:		speex
Version:	1.2.1
Release:        1%{?dist}
License:	BSD-3-clause AND TU-Berlin-1.0
URL:		https://www.speex.org/
Source0:        https://downloads.xiph.org/releases/speex/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(speexdsp)
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static --enable-binaries
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_docdir}/speex/manual.pdf
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n speex-devel -f %{oreon_filedir}/speex-devel.list
%files -n speex-tools -f %{oreon_filedir}/speex-tools.list

%changelog

%autochangelog
