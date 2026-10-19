%global source1_hash 110535522396708cea37c72a802c5e7e81391139f5f7985631c93ef242b206a4
%global source0_hash 9aa0cc780dec156b8282844833b342ab7cb08c25d2cd9a1869cdd0df31deff48
Summary:        GNU data compression program
Name: gzip
Version: 1.15
Release:        1%{?dist}
License: GPL-3.0-or-later AND GFDL-1.3-only
Source0:        https://mirrors.kernel.org/gnu/gzip/gzip-%{version}.tar.xz
Source1:        https://www.gnu.org/licenses/fdl-1.3.txt
Patch0: 1790453516.patch
Source100: colorzgrep.csh
Source101: colorzgrep.sh
URL: https://www.gzip.org/
Requires: coreutils 
Conflicts: filesystem < 3
Provides: /bin/gunzip
Provides: /bin/gzip
Provides: /bin/zcat
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  less
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
The gzip package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a
very commonly used data compression program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch 0 -p1

cp %{SOURCE1} .
autoreconf

%build

export DEFS="NO_ASM"
export CPPFLAGS="-DHAVE_LSTAT"
export CC="%{__cc}"
export CPP="%{__cpp}"
export CXX="%{__cxx}"
%ifarch s390x
%configure
%else
%configure
%endif
make
%check

make check
%install
%makeinstall
gzip -9nf ${RPM_BUILD_ROOT}%{_infodir}/gzip.info*
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
rm -f ${RPM_BUILD_ROOT}%{_bindir}/uncompress
%global profiledir %{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE100} %{buildroot}%{profiledir}
install -p -m 644 %{SOURCE101} %{buildroot}%{profiledir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
