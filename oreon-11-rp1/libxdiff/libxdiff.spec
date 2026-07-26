%global source0_hash 667751e2e11971765a421d8d20e038ee2d4122d784ccf8da479cf6f578252159

# Matches 1.0 tag.
%global commit 9c6289c5a088bf24f18f0b7bf8acaaf643aa411d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		libxdiff
Version:	1.0
Release:	30%{?dist}
Summary:	Basic functionality to create difference/patches in binary and text
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://github.com/spotrh/libxdiff
Source0:	https://github.com/spotrh/libxdiff/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:		%{name}-1.0-big-endian.patch
BuildRequires:	gcc
BuildRequires: make

%description
The LibXDiff library implements basic and yet complete functionalities to 
create file differences/patches to both binary and text files. The library 
uses memory files as file abstraction to achieve both performance and 
portability. For binary files, LibXDiff implements both (with some 
modification) the algorithm described in File System Support for Delta 
Compression by Joshua P. MacDonald, and the algorithm described in 
Fingerprinting By Random Polynomials by Michael O. Rabin. While for text 
files it follows directives described in An O(ND) Difference Algorithm 
and Its Variations by Eugene W. Myers.

This is a merged fork of the forks of the original libxdiff (0.23) found 
in the git and libgit2 source code, converted into a shared library.

%package devel
Summary:	Development libraries and headers for libxdiff
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for libxdiff.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .big-endian

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README.md NEWS ChangeLog
%{_libdir}/libxdiff.so.*

%files devel
%{_includedir}/xdiff/
%{_libdir}/libxdiff.so
%{_libdir}/pkgconfig/libxdiff.pc

%changelog
%autochangelog
