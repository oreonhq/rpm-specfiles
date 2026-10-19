%global source1_hash 7eb7606b396807a31c3841892289b672530ec74b54b9032c46728885ef84b537
%global source0_hash 9dedf22863cbc06954fa21fac849b0cc4ce30995b6dcde688309d24ff4741583
%global _privatelibs ^(%{_libdir}/%{name}/plugins.*/.*\\.so.*)$
%global _priv_debuginfo ^(.*lib.*[.]so-.*)$
%global __provides_exclude_from ^(%{_privatelibs}|%{_priv_debuginfo})$
%global __requires_exclude_from ^(%{_privatelibs}|%{_priv_debuginfo})$
%global latestversion 1.6.3
%global commit r12987
%global commitdate 20251209
%global postrelease .p1
%global namesuffix src
Name:           aubit4gl
Version:        %{latestversion}%{postrelease} 
Release:        1%{?dist}
Summary:        IBM Informix 4GL compatible compiler
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND GPL-1.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:            https://www.aubit.com
Source0:        https://downloads.sourceforge.net/%{name}/%{latestversion}/%{name}%{namesuffix}.%{latestversion}.tar.gz
Source1:        https://downloads.sourceforge.net/aubit4gl/Aubit4gl-manual/aubitmanpages.tar.bz2
Patch0:         https://downloads.sourceforge.net/aubit4gl/SRPM/%{name}-%{version}.patch
Requires: gcc
ExcludeArch: i686 s390x ppc64le
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  libtirpc-devel
BuildRequires:  ncurses-devel
BuildRequires:  procps-ng
BuildRequires:  rpcgen
# /oreon:deps
%description
Aubit 4GL compiler is software that translates IBM Informix 4GL source code
into C code, and compiles into executable programs.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}%{namesuffix}
%patch 0 -p1

%build

%configure LDFLAGS=-pie \
           --disable-prefix-check \
           --with-smtp=no \
           %if "%{getenv:INFORMIXDIR}" != ""
           --with-informix="%{getenv:INFORMIXDIR}" \
           %endif
           %if "%{getenv:INFORMIXC}" != ""
           --with-informixc="%{getenv:INFORMIXC}" \
           %endif
           --without-zlib \
           --enable-minimal=yes
%make_build -j1
%install
rm -rf %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
tar xvf %{SOURCE1} -C %{buildroot}%{_mandir}/man1
chmod -x %{_builddir}/%{name}%{namesuffix}/tools/examples/*/*.4gl
%make_install PREFIX=%{buildroot}%{_libdir}/%{name} \
              LIB_INSTALL_LINK=%{_builddir}/%{name}%{namesuffix} \
              BIN_INSTALL_LINK=%{_builddir}/%{name}%{namesuffix} \
              aubitrc=new
cp -p %{buildroot}%{_libdir}/%{name}/incl/*.h %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_libdir}/%{name}/incl
cp -d %{buildroot}%{_libdir}/%{name}/lib/lib%{name}.so* %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libdir}/%{name}/lib
mkdir -p %{buildroot}%{_sysconfdir}
install %{_builddir}/%{name}%{namesuffix}/etc/aubitrc %{buildroot}%{_sysconfdir}
sed -i -e "s|%{buildroot}||g" \
       -e "s|%{_builddir}/%{name}%{namesuffix}|%{_libdir}/%{name}|g" \
       -e "s|^\(AUBITETC=\).*|\1%{_sysconfdir}|g" \
       %{buildroot}%{_sysconfdir}/aubitrc
sed -i -e '1d' %{buildroot}%{_libdir}/%{name}/bin/report.pm 
sed -i -e '1d' %{buildroot}%{_libdir}/%{name}/bin/using.pm 
sed -i -e '1d;2i#!/usr/bin/bash' %{buildroot}%{_libdir}/%{name}/bin/aubit 
rm -f %{buildroot}%{_libdir}/%{name}/etc/import/default
rm -f %{buildroot}%{_libdir}/%{name}/tools/4glpc/settings/C
rm -f %{buildroot}%{_libdir}/%{name}/tools/4glpc/settings/C_INFORMIX
rm -f %{buildroot}%{_libdir}/%{name}/tools/4glpc/settings/EC
mkdir -p %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/4glpc %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/4glc %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/fcompile %{buildroot}%{_bindir}
install %{buildroot}%{_libdir}/%{name}/bin/amkmessage %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_libdir}/%{name}/bin
ln -sf libLEX_C.so %{buildroot}%{_libdir}/%{name}/plugins-%{latestversion}/libLEX_CS.so
rm -rf %{buildroot}%{_libdir}/%{name}/docs
rm -f %{buildroot}%{_libdir}/%{name}/README.txt
%oreon_autofiles aubit4gl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
make -C tools/test
%files -f %{oreon_filedir}/main.list
%files -n aubit4gl-devel -f %{oreon_filedir}/aubit4gl-devel.list

%changelog

%autochangelog
