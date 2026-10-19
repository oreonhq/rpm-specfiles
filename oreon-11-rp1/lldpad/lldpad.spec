%global source0_hash 4213455d7fdf81f610ab1f712328f6bee737e21786ad8a1ab770166b51cc49ac
%global _default_patch_fuzz 2
%global _hardened_build 1
%global checkout 85e5583
Name:               lldpad
Version:            1.1.1
Release:        1%{?dist}
Summary:        Intel LLDP Agent
License:            GPL-2.0-only
URL:                http://open-lldp.org/
Source0:        https://github.com/intel/openlldp/archive/%{checkout}.tar.gz#/openlldp-%{checkout}.tar.gz
Requires:           readline
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  kernel-headers
BuildRequires:  libconfig-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  systemd
# /oreon:deps
%description
This package contains the Linux user space daemon and configuration tool for
Intel LLDP Agent with Enhanced Ethernet support for the Data Center.

%package            devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Provides:           dcbd-devel = %{version}-%{release}
Obsoletes:          dcbd-devel < 0.9.26
%description devel
The %{name}-devel package contains header files for developing applications
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir openlldp-85e55837a81d710e5baa7da47f7ed0d205c8ede5
%oreon_prep
%build

./bootstrap.sh
CFLAGS=${CFLAGS:-%optflags -Wno-error -fcommon}; export CFLAGS;
%configure --disable-static
sed -i -e 's! \\\$compiler_flags !&\\\$CFLAGS \\\$LDFLAGS !' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
rm -f %{buildroot}%{_libdir}/liblldp_clif.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post %{name}.service %{name}.socket
%preun

%systemd_preun %{name}.service %{name}.socket
%postun

%systemd_postun_with_restart %{name}.service %{name}.socket
%files -f %{oreon_filedir}/main.list
%files -n lldpad-devel -f %{oreon_filedir}/lldpad-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-16.git85e5583
- Import
