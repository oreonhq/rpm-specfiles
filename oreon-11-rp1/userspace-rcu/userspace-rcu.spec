%global source0_hash 850b192096eb11ebf2c70e8f97bc7da7479ee41da1bebeb44e3986908bac414f

%global source2_key_fpr 2A0B4ED915F2D3FA45F5B16217280A9781186ACF


Name:           userspace-rcu
Version:        0.15.6
Release:        1%{?dist}
Summary:        RCU (read-copy-update) implementation in user-space
License:        LGPL-2.1-or-later
URL:            https://liburcu.org

Source0:        https://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
Source1:        https://lttng.org/files/urcu/%{name}-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 2A0B4ED915F2D3FA45F5B16217280A9781186ACF > gpgkey-2A0B4ED915F2D3FA45F5B16217280A9781186ACF.gpg
Source2:        gpgkey-2A0B4ED915F2D3FA45F5B16217280A9781186ACF.gpg
Patch0:         regtest-without-bench.patch
BuildRequires:  gnupg2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  multilib-rpm-config
BuildRequires:  pkgconfig

%description
This data synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples copies
of a given data structure to live at the same time, and by monitoring
the data structure accesses to detect grace periods after which memory
reclamation is possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications
that use %{name}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Reinitialize libtool with the fedora version to remove Rpath
autoreconf -vif -W all,error

%configure --disable-static --enable-compiler-atomic-builtins
V=1 make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -type f -name "*.la" -delete
rm %{buildroot}/%{_docdir}/%{name}/LICENSE.md
# Replace arch-dependent header file with arch-independent stub (when needed).
%multilib_fix_c_header --file %{_includedir}/urcu/config.h
%multilib_fix_c_header --file %{_includedir}/urcu/arch.h
%multilib_fix_c_header --file %{_includedir}/urcu/uatomic.h

%check
make check
make regtest

%ldconfig_scriptlets


%files
%license LICENSE.md lgpl-relicensing.md
%doc ChangeLog README.md
%{_libdir}/liburcu-bp.so.8*
%{_libdir}/liburcu-cds.so.8*
%{_libdir}/liburcu-common.so.8*
%{_libdir}/liburcu-mb.so.8*
%{_libdir}/liburcu-memb.so.8*
%{_libdir}/liburcu-qsbr.so.8*
%{_libdir}/liburcu.so.8*

%files devel
%doc %{_pkgdocdir}/examples
%{_includedir}/*
%{_libdir}/liburcu-bp.so
%{_libdir}/liburcu-cds.so
%{_libdir}/liburcu-common.so
%{_libdir}/liburcu-mb.so
%{_libdir}/liburcu-memb.so
%{_libdir}/liburcu-qsbr.so
%{_libdir}/liburcu.so
%{_libdir}/pkgconfig/liburcu*.pc
%{_docdir}/%{name}/cds-api.md
%{_docdir}/%{name}/rcu-api.md
%{_docdir}/%{name}/solaris-build.md
%{_docdir}/%{name}/uatomic-api.md


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.6-1
- Import
