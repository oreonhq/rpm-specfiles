%global source0_hash 469a66b6b54bb825efdc4cbaef1bbd45f87ddc6ce9f73ce7b1060f26b33ec6a9
%global  commit       ba331411f17702e01f6c2d7016eefebaa695871f
%global  shortcommit  %{sub %{commit} 1 7}
%global  commitdate   20210316
Name:           sonic
Version:        0.2.0^%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Library to speed up or slow down speech
License:        Apache-2.0
URL:            https://github.com/waywardgeek/sonic
Source0:        https://github.com/waywardgeek/%{name}/archive/%{commit}/%{name}-ba33141.tar.gz
Requires: libsonic%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Sonic is a simple algorithm for speeding up or slowing down speech.  However,
it's optimized for speed ups of over 2X, unlike previous algorithms for changing
speech rate.  The Sonic library is a very simple ANSI C library that is designed
to easily be integrated into streaming voice applications, like TTS back ends.

The primary motivation behind Sonic is to enable the blind and visually impaired
to improve their productivity with open source speech engines, like espeak.
Sonic can also be used by the sighted.  For example, Sonic can improve the
experience of listening to an audio book on an Android phone.

%package -n libsonic
Summary: Library package
%description -n libsonic
Sonic shared library package.

%package -n libsonic-devel
Summary:  Development files for sonic
Requires: libsonic%{?_isa} = %{version}-%{release}
%description -n libsonic-devel
Development files and libraries for sonic.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sonic-%{commit}
sed -i 's|LIBDIR=$(PREFIX)/lib|LIBDIR=%{_libdir}|g' Makefile

%build

%make_build
%install
%make_install
install -pDm0644 sonic.1 %{buildroot}%{_mandir}/man1/sonic.1
rm %{buildroot}/%{_libdir}/libsonic.a
%oreon_autofiles libsonic usr/*/lib*.so.*
%oreon_autofiles libsonic-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libsonic -f %{oreon_filedir}/libsonic.list
%files -n libsonic-devel -f %{oreon_filedir}/libsonic-devel.list

%changelog

%autochangelog
