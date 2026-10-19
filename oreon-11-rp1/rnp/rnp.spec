%global source0_hash 423c8e32e1e591462f759adf8441b1c44bca96d9f5daff13b82e81a79f18ecfd
%bcond_without      tests
%bcond_with         licensecheck
%bcond_without      libsexpp
%bcond_with         openssl
%global libname     librnp
%global soname      0
Name:          rnp
Summary:        OpenPGP (RFC4880) tools
Version:       0.18.1
Release:        3%{?dist}
License:       BSD-2-Clause AND Apache-2.0 AND MIT
URL:           https://github.com/rnpgp/rnp
Source0:        https://github.com/%{name}gp/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz.asc
Source2:       %{name}-keyring.gpg
Source3:       %{name}-files-by-license.txt
ExcludeArch:    %{ix86}
%if %{with openssl}
%else
%endif
%if %{with licensecheck}
%endif
%if %{with libsexpp}
%global libsexpp_version 0.8.7
%endif
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  gtest-devel
BuildRequires:  json-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(sexpp)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
RNP is a set of OpenPGP (RFC4880) tools.

%package -n %{libname}
Summary:    Library for all OpenPGP functions
%if %{without libsexpp}
%global libsexpp_version 0.9.0
Provides:   bundled(libsexpp) = %{libsexpp_version}
%endif
%description -n %{libname}
%{libname} is the library used by RNP for all OpenPGP functions,
useful for developers to build against, different from GPGME.

%package -n %{libname}-devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{libname}%{?_isa} = %{version}-%{release}
%description -n %{libname}-devel
This package contains the header files and development libraries
for %{libname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%if %{with libsexpp}
rm -rf  src/libsexp
: check system version requirement
if ! grep -q 'sexpp>=%{libsexpp_version}' CMakeLists.txt; then
    echo fix %%libsexpp_version macro, defined %{libsexpp_version}, expected \
        $(grep 'sexpp>=' CMakeLists.txt | sed 's/.*sexp>=//;s/)//')
    exit 1
fi
%else
pushd src/libsexpp
: retrieve LICENSE
cp LICENSE.md ../../LICENSE-libsexp.md
: check bundled version
if ! grep -q %{libsexpp_version} version.txt; then
    echo fix %%libsexpp_version macro, defined %{libsexpp_version}, expected \
        $(cat version.txt)
    exit 1
fi
popd
%endif

%if %{with licensecheck}
LST=$(mktemp)

licensecheck -r . | sed -e 's:^./::' >$LST
grep -v UNKNOWN $LST | sed -e 's/.*: //' | sort -u | while read lic
do
	echo -e "\n$lic\n------------"
	grep ": $lic\$" $LST | sed -e "s/: $lic//"
done  | tee %{SOURCE3}
rm $LST
%endif

%build

%cmake . \
   -DINSTALL_STATIC_LIBS:BOOL=OFF \
%if %{with openssl}
   -DCRYPTO_BACKEND:STRING=openssl \
%else
   -DCRYPTO_BACKEND:STRING=botan \
%endif
%if %{with libsexpp}
   -DSYSTEM_LIBSEXPP:BOOL=ON \
%else
   -DSYSTEM_LIBSEXPP:BOOL=OFF \
%endif
   -DENABLE_COVERAGE:BOOL=OFF \
   -DENABLE_SANITIZERS:BOOL=OFF \
   -DENABLE_SANITIZERS:BOOL=OFF \
   -DENABLE_FUZZERS:BOOL=OFF \
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DDOWNLOAD_RUBYRNP:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

FILTER="s2k_iteration_tuning|test_key_add_userid|test_ffi_security_profile|EncryptElgamal|cli_tests"
%ctest --exclude-regex $FILTER
%endif
%files -f %{oreon_filedir}/main.list
%files -n librnp -f %{oreon_filedir}/librnp.list
%files -n librnp-devel -f %{oreon_filedir}/librnp-devel.list

%changelog

%autochangelog
