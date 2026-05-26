# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 d59aff34164aa705b05155b86607f6b66918a433104f754a3fcf76216dd9f465
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global selinuxtype targeted
%global with_tests 1

Name: tpm2-abrmd
Version: 3.0.0
Release: 9%{?dist}
Summary: A system daemon implementing TPM2 Access Broker and Resource Manager

License: BSD-2-Clause
URL:     https://github.com/tpm2-software/tpm2-abrmd
Source0: https://github.com/tpm2-software/tpm2-abrmd/releases/download/%{version}/%{name}-%{version}.tar.gz

%{?systemd_requires}
BuildRequires: make
BuildRequires: systemd
BuildRequires: libtool
BuildRequires: autoconf-archive
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(tss2-mu)
BuildRequires: pkgconfig(tss2-sys)
# tpm2-abrmd depends on tpm2-tss-devel for tss2-mu/sys libs
BuildRequires: tpm2-tss-devel >= 2.4.0
%if 0%{?with_tests}
BuildRequires: pkgconfig(cmocka)
%endif

# tpm2-abrmd depends on the package that contains its SELinux policy module
Requires: (%{name}-selinux >= 2.0.0-1%{?dist} if selinux-policy-%{selinuxtype})
Requires(pre): tpm2-tss >= 2.4.0

%description
tpm2-abrmd is a system daemon implementing the TPM2 access broker (TAB) and
Resource Manager (RM) spec from the TCG.

%package devel
Summary: Headers, static libraries and package config files of tpm2-abrmd
Requires: %{name}%{_isa} = %{version}-%{release}
# tpm2-abrmd-devel depends on tpm2-tss-devel for tss2-mu/sys libs
Requires: tpm2-tss-devel%{?_isa} >= 2.4.0

%description devel
This package contains headers, static libraries and package config files
required to build applications that use tpm2-abrmd.


%prep
%oreon_verify_sources
%autosetup -p1 -n %{name}-%{version}

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

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/libtss2-tcti-tabrmd.so.*
%{_sbindir}/tpm2-abrmd
%{_datarootdir}/dbus-1/system.d/tpm2-abrmd.conf
%{_datarootdir}/dbus-1/system-services/com.intel.tss2.Tabrmd.service
%{_unitdir}/tpm2-abrmd.service
%{_mandir}/man3/Tss2_Tcti_Tabrmd_Init.3*
%{_mandir}/man7/tss2-tcti-tabrmd.7*
%{_mandir}/man8/tpm2-abrmd.8*

%files devel
%{_includedir}/tss2/tss2-tcti-tabrmd.h
%{_libdir}/libtss2-tcti-tabrmd.so
%{_libdir}/pkgconfig/tss2-tcti-tabrmd.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-9
- Prepare for Oreon 11 (RP1)
