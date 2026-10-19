%global source0_hash 41bd1c75a375b85c337b59783f5deb93dbb443fb0a52d257f403df7bd653ee12
%{?mingw_package_header}
Name: mingw-libpsl
Version: 0.21.0
Release:        1%{?dist}
Summary:        MinGW port of C library for the Publix Suffix List
License: MIT
URL: https://rockdaboot.github.io/libpsl
Source0:        https://github.com/rockdaboot/libpsl/releases/download/libpsl-%{version}/libpsl-%{version}.tar.gz
BuildArch: noarch
Requires: publicsuffix-list-dafsa
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-icu
BuildRequires:  mingw32-libidn2
BuildRequires:  mingw32-libunistring
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-icu
BuildRequires:  mingw64-libidn2
BuildRequires:  mingw64-libunistring
BuildRequires:  mingw64-win-iconv
BuildRequires:  publicsuffix-list
BuildRequires:  python3
# /oreon:deps
%description
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%package -n mingw32-libpsl
Summary:        MinGW port of C library for the Publix Suffix List
Requires: publicsuffix-list
%description -n mingw32-libpsl
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%package -n mingw64-libpsl
Summary:        MinGW port of C library for the Publix Suffix List
Requires: publicsuffix-list
%description -n mingw64-libpsl
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libpsl-%{version}
rm -frv list
ln -sv %{_datadir}/publicsuffix list
sed -i -e "1s|#!.*|#!%{__python3}|" src/psl-make-dafsa

%build

%mingw_configure --disable-silent-rules                                             \
           --disable-static                                                         \
           --disable-man                                                            \
           --disable-gtk-doc                                                        \
           --enable-builtin=libicu                                                  \
           --enable-runtime=libidn2                                                 \
           --with-psl-distfile=%{_datadir}/publicsuffix/public_suffix_list.dafsa    \
           --with-psl-file=%{_datadir}/publicsuffix/effective_tld_names.dat         \
           --with-psl-testfile=%{_datadir}/publicsuffix/test_psl.txt
pushd build_win32
sed -i libtool \
    -e 's|^\(runpath_var=\).*$|\1|' \
    -e 's|^\(hardcode_libdir_flag_spec=\).*$|\1|'
popd
pushd build_win64
sed -i libtool \
    -e 's|^\(runpath_var=\).*$|\1|' \
    -e 's|^\(hardcode_libdir_flag_spec=\).*$|\1|'
popd
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT
install -m0755 src/psl-make-dafsa %{buildroot}%{mingw32_bindir}/
install -m0755 src/psl-make-dafsa %{buildroot}%{mingw64_bindir}/
find $RPM_BUILD_ROOT -name '*.la' -delete -print
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libpsl.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libpsl.a
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man
%oreon_autofiles mingw32-libpsl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libpsl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libpsl -f %{oreon_filedir}/mingw32-libpsl.list
%files -n mingw64-libpsl -f %{oreon_filedir}/mingw64-libpsl.list

%changelog

%autochangelog
