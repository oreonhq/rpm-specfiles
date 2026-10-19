%global source0_hash 7540fbb33bcfa5ddfce00d9035de034d0a36442bf8555e1afa0dbd34a3359364
%global srcname crypto
%global date 20250324
%global commit 9ac58405c2b91fb7cd230aed474dc7059f0fcad9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{?el8}
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}
%global common_description %{expand:
Crypto provides a simple implementation of the Rijndael (now AES) and DES
encryption algorithms as well as the SHA1 and SHA2 hashing algorithms. The
library is almost a verbatim copy of the code from OpenBSD and PuTTY for use by
the SDL-Hercules-390 emulator.}
Name:           sdl-crypto
Version:        1.0.0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Simple AES/DES encryption and SHA1/SHA2 hashing library
License:        LicenseRef-Fedora-Public-Domain AND MIT AND BSD-3-Clause
URL:            https://github.com/SDL-Hercules-390/%{srcname}
Source0:        https://github.com/SDL-Hercules-390/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Conflicts:      sha2-devel
Provides:       crypto-devel%{?_isa} = %{version}-%{release}
Obsoletes:      crypto-devel < 1.0.0-11
Provides:       crypto-static%{?_isa} = %{version}-%{release}
Obsoletes:      crypto-static < 1.0.0-11
%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-devel:g'

%build

%cmake
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/%{srcname}.LICENSE.txt .
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sdl-crypto-devel -f %{oreon_filedir}/sdl-crypto-devel.list

%changelog

%autochangelog
