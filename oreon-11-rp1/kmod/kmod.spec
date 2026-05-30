%global source0_hash 5a5d5073070cc7e0c7a7a3c6ec2a0e1780850c8b47b3e3892226b93ffcb9cb54

# Fedora does not support CONFIG_MODVERSIONS. Without kabi support
# weak-modules is useless at best, and can be actively harmful.
# Since RHEL *does* support this and offers kabi support,
# turn it on there by default.
%if 0%{?rhel}
%bcond_without weak_modules
%bcond_without dist_conf
%else
%bcond_with weak_modules
%bcond_with dist_conf
%endif

%bcond_without zlib
%bcond_without xz
%bcond_without zstd

Name:		kmod
Version:	34.2
Release:	4%{?dist}
Summary:	Linux kernel module management utilities

# https://docs.fedoraproject.org/en-US/legal/license-field/#_no_effective_license_analysis
# GPL-2.0-or-later:
#   build-aux/compile
#   build-aux/depcomp
#   build-aux/ltmain.sh
#   build-aux/ltmain.sh
#   build-aux/missing
#   build-aux/py-compile
#   build-aux/test-driver
#   m4/attributes.m4
#   m4/features.m4
#   tools
# GPL-3.0-or-later:
#   build-aux/config.guess
#   build-aux/config.sub
#   build-aux/git-version-gen
#   libkmod/docs/gtk-doc.make
#   m4/gtk-doc.m4
# FSFUL:
#   configure
# FSFULLRWD:
#   aclocal.m4
#   libkmod/docs/Makefile.in
#   m4/libtool.m4
#   m4/lt~obsolete.m4
#   m4/ltoptions.m4
#   m4/ltsugar.m4
#   m4/ltversion.m4
#   Makefile.in
# LGPL-2.1-only:
#   libkmod/python/kmod/error.py
#   libkmod/python/kmod/__init__.py
#   libkmod/python/kmod/version.py
#   libkmod/python/kmod/version.py.in
# LGPL-2.1-or-later:
#   config.h.in (no explicit license, the one in COPYING is assumed)
#   libkmod
#   man (no explicit license, the one in COPYING is assumed)
#   shared
#   shell-completion/bash/kmod
#   testsuite
# X11:
#   build-aux/install-sh
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND FSFUL AND FSFULLRWD AND LGPL-2.1-only AND LGPL-2.1-or-later AND X11
URL:		https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git
Source0:        https://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
Source1:	weak-modules
Source2:	depmod.conf.dist
Exclusiveos:	Linux

BuildRequires:  gcc
BuildRequires:	chrpath
%if %{with zlib}
BuildRequires:	zlib-devel
%endif
%if %{with xz}
BuildRequires:	xz-devel
%endif
BuildRequires:  scdoc gtk-doc
BuildRequires:  openssl-devel
BuildRequires:  make automake libtool
%if %{with zstd}
BuildRequires:  libzstd-devel
%endif

Provides:	module-init-tools = 4.0-1
Obsoletes:	module-init-tools < 4.0-1
Provides:	/sbin/modprobe

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/modprobe
Provides:       /usr/sbin/modinfo
Provides:       /usr/sbin/insmod
Provides:       /usr/sbin/rmmod
Provides:       /usr/sbin/lsmod
Provides:       /usr/sbin/depmod
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

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
%endif

%files
%dir %{_sysconfdir}/depmod.d
%dir %{_sysconfdir}/modprobe.d
%dir %{_prefix}/lib/modprobe.d
%{_bindir}/kmod
%{_sbindir}/modprobe
%{_sbindir}/modinfo
%{_sbindir}/insmod
%{_sbindir}/rmmod
%{_sbindir}/lsmod
%{_sbindir}/depmod
%if %{with weak_modules}
%{_sbindir}/weak-modules
%endif
%{_datadir}/bash-completion/
%{_datadir}/fish/vendor_functions.d/*
%{_datadir}/zsh/site-functions/*
%if %{with dist_conf}
%{_sysconfdir}/depmod.d/dist.conf
%endif
%{_datadir}/pkgconfig/kmod.pc
%attr(0644,root,root) %{_mandir}/man5/mod*.d*.5*
%attr(0644,root,root) %{_mandir}/man5/depmod.d.5*
%{_mandir}/man5/modprobe.conf.5*
%attr(0644,root,root) %{_mandir}/man8/*.8*
%doc NEWS README.md

%files libs
%license COPYING
%{_libdir}/libkmod.so.*

%files devel
%{_includedir}/libkmod.h
%{_libdir}/pkgconfig/libkmod.pc
%{_libdir}/libkmod.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 34.2-4
- Prepare for Oreon 11 (RP1)
