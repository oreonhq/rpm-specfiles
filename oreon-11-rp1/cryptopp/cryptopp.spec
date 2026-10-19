%global source11_hash d6ff2bd7d0ae85f89b80c61865eb3441da13b851b6117fbc438f5450f919b4c8
%global source10_hash 887519c86d8b2fdd5172287aa0c063e58e4989752454b0fd50136ed4b8513e93
%global source1_hash 681141926ec3032e210c459ae7f5e974e7bd8bb5d15b852775e17839a5fac85a
%global source0_hash ace1c7b010a409eba5e86c4fd5a8845c43a6ac39bb6110e64ca5d7fea08583f4
%define _lto_cflags %{nil}
Name:           cryptopp
Version:        8.8.0
Release:        1%{?dist}
Summary:        C++ class library of cryptographic schemes
License:        BSL-1.0
URL:            https://www.cryptopp.com
%define v_tag %(v=%{version}; echo ${v//./_})
%define v_file %(v=%{version}; echo ${v//./})
Source0:        https://github.com/weidai11/%{name}/releases/download/CRYPTOPP_%{v_tag}/%{name}%{v_file}.zip
Source1:        https://github.com/weidai11/cryptopp/releases/download/CRYPTOPP_%{v_tag}/cryptopp%{v_file}.zip.sig
Source2:        %{url}/signing.html#/keyring.gpg
Source10:       https://github.com/noloader/cryptopp-autotools/releases/download/CRYPTOPP_%{v_tag}/cryptopp-autotools%{v_file}.zip
Source11:       https://github.com/noloader/cryptopp-autotools/releases/download/CRYPTOPP_%{v_tag}/cryptopp-autotools%{v_file}.zip.sig
Patch0:         fix-autotools-version-info.patch
Patch1:         remove-adhoc.patch
Obsoletes:  %{name}-progs < 8.8.0-3
Obsoletes:  pycryptopp < 0.7
Provides:   pycryptopp = 0.7
# oreon:deps
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-common
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Crypto++ Library is a free C++ class library of cryptographic schemes.
See http://www.cryptopp.com/ for a list of supported algorithms.

One purpose of Crypto++ is to act as a repository of public domain
(not copyrighted) source code. Although the library is copyrighted as a
compilation, the individual files in it are in the public domain.

%package devel
Summary:        Header files and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-doc < 8.8.0-3
Provides:       %{name}-doc < 8.8.0-3
%description devel
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains the header files and development documentation
for %{name}.

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains static libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE11}' --data='%{SOURCE10}'

%autosetup -c -p1 -a 10
find . -type f -name "*.zip" -exec rm "{}" \;
dos2unix License.txt Readme.txt
find . -not -type d -exec file "{}" ";" -print0 | grep -z CRLF | cut -d':' -z -f1 | xargs -0 dos2unix

%build

autoreconf -vi
export CXXFLAGS="$(echo "%{optflags}" | sed -e 's/-O2//') -O3 -DNDEBUG"
%configure
%make_build all-am docs
%install
%make_install
rm %{buildroot}%{_bindir}/cryptest
rm -rf %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -p -m 0644 libcryptopp.pc %{buildroot}%{_libdir}/pkgconfig/libcryptopp.pc
%oreon_autofiles cryptopp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cryptopp-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./cryptest v
%files -f %{oreon_filedir}/main.list
%files -n cryptopp-devel -f %{oreon_filedir}/cryptopp-devel.list
%files -n cryptopp-static -f %{oreon_filedir}/cryptopp-static.list

%changelog

%autochangelog
