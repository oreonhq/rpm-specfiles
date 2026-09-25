%global source0_hash 9aa0cc780dec156b8282844833b342ab7cb08c25d2cd9a1869cdd0df31deff48

Summary: GNU data compression program
Name: gzip
Version: 1.15
Release: 1%{?dist}
# info pages are under GFDL license
License: GPL-3.0-or-later AND GFDL-1.3-only
Source0:        https://mirrors.kernel.org/gnu/gzip/gzip-%{version}.tar.xz
Source1:        https://www.gnu.org/licenses/fdl-1.3.txt

# downstream solution for coloured z*grep (#1034839)
Source100: colorzgrep.csh
Source101: colorzgrep.sh


# Fixed in upstream code.
# http://thread.gmane.org/gmane.comp.gnu.gzip.bugs/378
URL: https://www.gzip.org/
# Requires should not be added for gzip wrappers (eg. zdiff, zgrep,
# zless) of another tools, because gzip "extends" the tools by its
# wrappers much more than it "requires" them.
Requires: coreutils 
BuildRequires: texinfo, gcc, autoconf, automake, less
BuildRequires: make
Conflicts: filesystem < 3
Provides: /bin/gunzip
Provides: /bin/gzip
Provides: /bin/zcat
# Gzip contains bundled Gnulib
# exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)

%description
The gzip package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a
very commonly used data compression program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

cp %{SOURCE1} .
autoreconf

%build
export DEFS="NO_ASM"
export CPPFLAGS="-DHAVE_LSTAT"
export CC="%{__cc}"
export CPP="%{__cpp}"
export CXX="%{__cxx}"
%ifarch s390x

#When the otpimizations are enabled, the huft test fails as of F44/gzip1.14
#export CFLAGS="$RPM_OPT_FLAGS -Dalignas=_Alignas -DDFLTCC_LEVEL_MASK=0x7e"
#use this in the next realease after gzip 1.13 export CFLAGS="$RPM_OPT_FLAGS -DDFLTCC_LEVEL_MASK=0x7e"
#%configure --enable-dfltcc

%configure
%else
%configure
%endif
make
%check
make check
#make gzip.info

%install
%makeinstall

gzip -9nf ${RPM_BUILD_ROOT}%{_infodir}/gzip.info*

# we don't ship it, so let's remove it from ${RPM_BUILD_ROOT}
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
# uncompress is a part of ncompress package
rm -f ${RPM_BUILD_ROOT}%{_bindir}/uncompress

# coloured z*grep (#1034839)
%global profiledir %{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE100} %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE101} %{buildroot}%{profiledir}

%files
%doc NEWS README AUTHORS ChangeLog THANKS TODO
%license COPYING fdl-1.3.txt
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/gzip.info*
%{profiledir}/*

%changelog
%autochangelog
