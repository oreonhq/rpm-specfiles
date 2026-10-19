%global source0_hash 398b2468e7838d2274d1f62dbc112e7e043433812f7ae63ef29f5cb31dc6defd
%global commit 020a4c2b7612863600428e0e9f2491b923e54ac2
%global gittag 1.5
%global shortcommit %(c=%{commit0}; echo ${c:0:7})
Name:            libbinio
Version:         %{gittag}
Release:        1%{?dist}
Summary:        A software library for binary I/O classes in C++
URL:             http://adplug.github.io/libbinio
Source0:        https://github.com/adplug/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch0:          libbinio-1.4-includes.patch
License:         LGPL-2.1-or-later AND GFDL-1.1-or-later
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
This binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware
independent in the form that it transparently converts between the
different forms of machine-internal binary data representation.
It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%package devel
Summary:         Development files for libbinio
Requires:        %{name}%{?_isa} = %{version}-%{release}
BuildRequires:   texinfo
%description devel
This package contains development files for the libbinio binary
data stream class for C++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libbinio-devel -f %{oreon_filedir}/libbinio-devel.list

%changelog

%autochangelog
