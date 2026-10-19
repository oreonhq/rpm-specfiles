%global source0_hash d59aff34164aa705b05155b86607f6b66918a433104f754a3fcf76216dd9f465
%global selinuxtype targeted
%global with_tests 1
Name: tpm2-abrmd
Version: 3.0.0
Release:        1%{?dist}
Summary:        A system daemon implementing TPM2 Access Broker and Resource Manager
License: BSD-2-Clause
URL:     https://github.com/tpm2-software/tpm2-abrmd
Source0:        https://github.com/tpm2-software/tpm2-abrmd/releases/download/%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
%if 0%{?with_tests}
%endif
Requires: (%{name}-selinux >= 2.0.0-1%{?dist} if selinux-policy-%{selinuxtype})
Requires(pre): tpm2-tss >= 2.4.0
# oreon:deps
BuildRequires:  autoconf-archive
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-sys)
BuildRequires:  systemd
BuildRequires:  tpm2-tss-devel
# /oreon:deps
%description
tpm2-abrmd is a system daemon implementing the TPM2 access broker (TAB) and
Resource Manager (RM) spec from the TCG.

%package devel
Summary: Headers, static libraries and package config files of tpm2-abrmd
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: tpm2-tss-devel%{?_isa} >= 2.4.0
%description devel
This package contains headers, static libraries and package config files
required to build applications that use tpm2-abrmd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure --disable-static --disable-silent-rules \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemdpresetdir=%{_presetdir} \
           --with-dbuspolicydir=%{_datarootdir}/dbus-1/system.d/
%make_build
%install
%make_install
find %{buildroot}%{_libdir} -type f -name \*.la -delete
rm -f %{buildroot}/%{_presetdir}/tpm2-abrmd.preset
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if 0%{?with_tests}
%check

make check
%endif
%post

%systemd_post tpm2-abrmd.service
%preun

%systemd_preun tpm2-abrmd.service
%postun

%systemd_postun tpm2-abrmd.service
%files -f %{oreon_filedir}/main.list
%files -n tpm2-abrmd-devel -f %{oreon_filedir}/tpm2-abrmd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-9
- Prepare for Oreon 11 (RP1)
