%global source0_hash 0bfbaaf3faf545048b81683b0eb5b333d041158282adee690437c8acf56654c7
%global toolchain clang
Summary:        Cryptographic library
Name:          bee2
Version:       2.2.4
Release:        1%{?dist}
License:       GPL-3.0-only and GPL-3.0-or-later
Url:           http://apmi.bsu.by/resources/tools.html
Source0:        https://github.com/agievich/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%global _descriptionlibs %{expand:
Bee2 is a cryptographic library which implements cryptographic
algorithm and protocols standardized in Belarus.
Bee2 fully supports the following Belarusian cryptography standards
(STB):
  STB 34.101.31 (belt): data encryption and integrity algorithms.
  STB 34.101.45 (bign): digital signature and key transport algorithms
                        over elliptic curves.
  STB 34.101.47 (brng): cryptographic algorithms of pseudorandom number
                        generation + one-time passwords.
  STB 34.101.60 (bels): secret sharing algorithms.
  STB 34.101.66 (bake): key establishment protocols over elliptic curves.
  STB 34.101.77 (bash): sponge-based algorithms.
For more details see apmi.bsu.by/resources/std.html
Bee2 partially supports cryptographic data formats defined in the
following standards:
  STB 34.101.78 (bpki): a PKI profile.
Additionally, Bee2 implements digital signature algorithms
standardized in Russia and Ukraine.}
# oreon:deps
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  doxygen
BuildRequires:  gzip
BuildRequires:  sed
# /oreon:deps
%description
Bee2 is a cryptographic library which implements cryptographic
algorithm and protocols standardized in Belarus.

%package  libs
Summary:  Libraries for applications that use bee2
%description	libs
%_descriptionlibs

%package  devel
Summary:  Files for development of applications which will use bee2
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
%_descriptionlibs

%package -n bee2cmd
Summary:  Command line interface to bee2 utilities
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
License:  GPL-3.0-only
%description -n bee2cmd
Command line interface to bee2 library offering utilities
to print version and build information, has files,
generate and manage passwords, generate and manage
private keys, manage CV-certificates, manage certificate
rings, sign files and verify signatures and provide
entropy sources.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n bee2-%{version}
# Generate MAN pages
sed -i 's/GENERATE_MAN           = NO/GENERATE_MAN           = YES/g' doc/bee2.doxy
# Link to shared library
sed -i 's/bee2_static/bee2/g' cmd/CMakeLists.txt
sed -i 's/bee2_static/bee2/g' test/CMakeLists.txt

%build

LDFLAGS="${LDFLAGS} -pie"
%cmake -DBUILD_DOC=ON\
       -DCMAKE_C_COMPILER=clang\
       -DBUILD_TESTS=ON\
       -DBUILD_PIC=ON\
       -DCMAKE_BUILD_TYPE=RELEASE
%cmake_build
%install
%cmake_install
for file in doc/man/man3/*.3; do
  gzip $file
done
mkdir -p %{buildroot}%{_mandir}/man3
install -m 644 doc/man/man3/*.3.gz %{buildroot}%{_mandir}/man3/
rm %{buildroot}%{_libdir}/libbee2_static.a
%oreon_autofiles bee2-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bee2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bee2cmd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n bee2-libs -f %{oreon_filedir}/bee2-libs.list
%files -n bee2-devel -f %{oreon_filedir}/bee2-devel.list
%files -n bee2cmd -f %{oreon_filedir}/bee2cmd.list

%changelog

%autochangelog
