%global source0_hash 5afe822af5c4edbf67daaf45eec61d538f49eef6b19524de64897c6b95828caf

%global mingw_build_ucrt64 1

%{?mingw_package_header}

# Steps:
# - Perform (scratch) build with bootstrap=1
# - Update the standard-dlls-xxx files as documented below, and rebuild with bootstrap=0
%global bootstrap 0

Name:           mingw-crt
Version:        13.0.0
Release:        3%{?dist}
Summary:        MinGW Windows cross-compiler runtime

License:        LicenseRef-Fedora-Public-Domain AND ZPL-2.1
URL:            http://mingw-w64.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2


# Note about standard dlls
# ------------------------------------------------------------
#
# We want to be able to build & install mingw32 libraries without
# necessarily needing to install wine.  (And certainly not needing to
# install Windows!)  There is no requirement to have wine installed in
# order to use the mingw toolchain to develop software (i.e. to
# compile more stuff on top of it), so why require that?
#
# So for expediency, this base package provides the "missing" DLLs
# from Windows.  Another way to do it would be to exclude these
# proprietary DLLs in our find-requires checking script - essentially
# it comes out the same either way.
#
# (rpm -ql mingw32-crt | grep '\.a$' | while read f ; do i686-w64-mingw32-dlltool   -I $f 2>/dev/null ; done) | sort | uniq | tr A-Z a-z > standard-dlls-mingw32
Source1:       standard-dlls-mingw32
# (rpm -ql mingw64-crt | grep '\.a$' | while read f ; do x86_64-w64-mingw32-dlltool -I $f 2>/dev/null ; done) | sort | uniq | tr A-Z a-z > standard-dlls-mingw64
Source2:       standard-dlls-mingw64
# (rpm -ql ucrt64-crt | grep '\.a$' | while read f ; do x86_64-w64-mingw32ucrt-dlltool -I $f 2>/dev/null ; done) | sort | uniq | tr A-Z a-z > standard-dlls-ucrt64
Source3:       standard-dlls-ucrt64

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-gcc

BuildRequires:  ucrt64-filesystem >= 133
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-headers
BuildRequires:  ucrt64-gcc

%description
MinGW Windows cross-compiler runtime, base libraries.


%package -n mingw32-crt
Summary:        MinGW Windows cross-compiler runtime for the win32 target
Requires:       mingw32-filesystem >= 133
%if 0%{?bootstrap:1}
Provides:       %(sed "s/\(.*\)/mingw32(\1) /g" %{SOURCE1} | tr "\n" " ")
Provides:       mingw32(mscoree.dll)
%endif

%description -n mingw32-crt
MinGW Windows cross-compiler runtime, base libraries for the win32 target.

%package -n mingw64-crt
Summary:        MinGW Windows cross-compiler runtime for the win64 target
Requires:       mingw64-filesystem >= 133
%if 0%{?bootstrap:1}
Provides:       %(sed "s/\(.*\)/mingw64(\1) /g" %{SOURCE2} | tr "\n" " ")
Provides:       mingw64(mscoree.dll)
%endif

%description -n mingw64-crt
MinGW Windows cross-compiler runtime, base libraries for the win64 target.

%package -n ucrt64-crt
Summary:        MinGW Windows cross-compiler runtime for the win64 target
Requires:       ucrt64-filesystem >= 133
%if 0%{?bootstrap:1}
Provides:       %(sed "s/\(.*\)/ucrt64(\1) /g" %{SOURCE3} | tr "\n" " ")
Provides:       ucrt64(mscoree.dll)
%endif

%description -n ucrt64-crt
MinGW Windows cross-compiler runtime, base libraries for the win64 target.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n mingw-w64-v%{version}


%build
pushd mingw-w64-crt
    # Filter out -fstack-protector and -lssp from LDFLAGS as libssp is not yet potentially built with the bootstrap gcc
    MINGW32_LDFLAGS="`echo %{mingw32_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    MINGW64_LDFLAGS="`echo %{mingw64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    UCRT64_LDFLAGS="`echo %{ucrt64_ldflags} | sed 's|-fstack-protector||' | sed 's|-lssp||'`"
    MINGW32_CONFIGURE_ARGS="--with-default-msvcrt=msvcrt"
    MINGW64_CONFIGURE_ARGS="--disable-lib32 --with-default-msvcrt=msvcrt"
    UCRT64_CONFIGURE_ARGS="--disable-lib32 --with-default-msvcrt=ucrt"
    %mingw_configure
    %mingw_make_build
popd


%install
pushd mingw-w64-crt
    %mingw_make_install
popd

# Dunno what to do with these files
rm -rf %{buildroot}%{mingw32_includedir}/*.c
rm -rf %{buildroot}%{mingw64_includedir}/*.c
rm -rf %{buildroot}%{ucrt64_includedir}/*.c


%files -n mingw32-crt
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw32_libdir}/*

%files -n mingw64-crt
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw64_libdir}/*

%files -n ucrt64-crt
%license COPYING DISCLAIMER DISCLAIMER.PD
%{ucrt64_libdir}/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.0-3
- Prepare for Oreon 11 (RP1)
