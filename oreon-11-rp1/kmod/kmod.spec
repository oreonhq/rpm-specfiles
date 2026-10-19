%global source0_hash 5a5d5073070cc7e0c7a7a3c6ec2a0e1780850c8b47b3e3892226b93ffcb9cb54
%bcond_with weak_modules
%bcond_with dist_conf
%bcond_without zlib
%bcond_without xz
%bcond_without zstd
Name:		kmod
Version:	34.2
Release:        4%{?dist}
Summary:        Linux kernel module management utilities
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND FSFUL AND FSFULLRWD AND LGPL-2.1-only AND LGPL-2.1-or-later AND X11
URL:		https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git
Source0:        https://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
Source1:	weak-modules
Source2:	depmod.conf.dist
Exclusiveos:	Linux
%if %{with zlib}
%endif
%if %{with xz}
%endif
%if %{with zstd}
%endif
Provides:	module-init-tools = 4.0-1
Obsoletes:	module-init-tools < 4.0-1
Provides:	/sbin/modprobe
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/modprobe
Provides:       /usr/sbin/modinfo
Provides:       /usr/sbin/insmod
Provides:       /usr/sbin/rmmod
Provides:       /usr/sbin/lsmod
Provides:       /usr/sbin/depmod
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  scdoc
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The kmod package provides various programs needed for automatic
loading and unloading of modules under 2.6, 3.x, and later kernels, as well
as other module management programs. Device drivers and filesystems are two
examples of loaded and unloaded modules.

%package libs
Summary:	Libraries to handle kernel module loading and unloading
%description libs
The kmod-libs package provides runtime libraries for any application that
wishes to load or unload Linux kernel modules from the running system.

%package devel
Summary:	Header files for kmod development
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The kmod-devel package provides header files used for development of
applications that wish to load or unload Linux kernel modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf --install
%configure \
  --with-openssl \
%if %{with zlib}
  --with-zlib \
%endif
%if %{with xz}
  --with-xz \
%endif
%if %{with zstd}
  --with-zstd \
%endif
  --enable-debug
%{make_build} V=1
%install
%{make_install}
pushd $RPM_BUILD_ROOT%{_mandir}/man5
ln -s modprobe.d.5.gz modprobe.conf.5.gz
popd
find %{buildroot} -type f -name "*.la" -delete
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/depmod.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d
%if %{with weak_modules}
install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/weak-modules
%endif
%if %{with dist_conf}
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/depmod.d/dist.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n kmod-libs -f %{oreon_filedir}/kmod-libs.list
%files -n kmod-devel -f %{oreon_filedir}/kmod-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 34.2-4
- Prepare for Oreon 11 (RP1)
