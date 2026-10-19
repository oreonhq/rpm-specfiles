%global source0_hash ba0c860626efbac6683f351dd718edb062065e919716d787b89e3d547c5d9493
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:           lxc
Version:        7.0.0
Release:        1%{?dist}
Summary:        Linux Resource Containers
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-only
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:        lxc-net
Patch0:         lxc-2.0.7-fix-init.patch
Patch1:         lxc-4.0.1-fix-lxc-net.patch
%if 0%{?with_seccomp}
%endif
%if 0%{?with_static_init}
%endif
Provides:       lxc-extra = %{version}-%{release}
Obsoletes:      lxc-extra < 1.1.5-3
Requires: lxc-libs%{?_isa} = %{version}-%{release}
Requires: lxcfs
Requires: openssl
Requires: rsync
# oreon:deps
BuildRequires:  cmake
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibc-headers
BuildRequires:  kernel-headers
BuildRequires:  libcap
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  pam
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  systemd-devel
# /oreon:deps
%description
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

%package           libs
Summary:           Runtime library files for %{name}
Requires:          rsync
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
Requires(post):    /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
%description    libs
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-libs package contains libraries for running %{name} applications.

%package        templates
Summary:        Templates for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       wget
%description    templates
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-templates package contains templates for creating containers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
        -D examples=true \
        -D man=true \
        -D tools=true \
        -D commands=true \
        -D capabilities=true \
        -D openssl=true \
        -D selinux=true \
%if 0%{?with_seccomp}
        -D seccomp=true \
%endif
        -D memfd-rexec=true \
        -D thread-safety=true \
        -D dbus=true \
        -D tests=false \
        -D init-script=systemd \
        -D systemd-unitdir=%{_unitdir} \
        -D distrosysconfdir=sysconfig \
        -D pam-cgroup=true \
        -D runtime-path=%{_rundir} \
        %{nil}
%meson_build
cd doc/api/ && doxygen
%install
%meson_install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_pkgdocdir}/api
cp -a AUTHORS README.md %{buildroot}%{_pkgdocdir}
cp -a doc/api/html/* %{buildroot}%{_pkgdocdir}/api/
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}
rm -r %{buildroot}%{_libdir}/liblxc.a
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-net
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post libs

%systemd_post %{name}-net.service
%systemd_post %{name}.service
%systemd_post lxc-monitord.service
%preun libs

%systemd_preun %{name}-net.service
%systemd_preun %{name}.service
%systemd_preun lxc-monitord.service
%postun libs

%systemd_postun %{name}-net.service
%systemd_postun %{name}.service
%systemd_postun lxc-monitord.service
%files -f %{oreon_filedir}/main.list
%files -n lxc-libs -f %{oreon_filedir}/lxc-libs.list
%files -n lxc-templates -f %{oreon_filedir}/lxc-templates.list
%files -n lxc-devel -f %{oreon_filedir}/lxc-devel.list
%files -n lxc-doc -f %{oreon_filedir}/lxc-doc.list

%changelog

%autochangelog
