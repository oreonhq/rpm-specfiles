%global source0_hash 1e5be93e518372acf1d92d2f567d01a46fdb0b730487e544e6fb896c59cac77f
Name: trousers
Summary:        TCG's Software Stack v1.2
Version: 0.3.15
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
Url: http://trousers.sourceforge.net
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: tcsd.service
Patch1:  trousers-0.3.14-noinline.patch
Patch2: trousers-0.3.14-unlock-in-err-path.patch
Patch3: trousers-0.3.14-fix-indent-obj_policy.patch
Patch4: trousers-0.3.14-fix-indent-tspi_key.patch
%if ! 0%{?flatpak}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%endif
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd
# /oreon:deps
%description
TrouSerS is an implementation of the Trusted Computing Group's Software Stack
(TSS) specification. You can use TrouSerS to write applications that make use
of your TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's software
state using cryptographic hashes and more.

%package lib
Summary: TrouSerS libtspi library
Obsoletes: trousers < 0.3.13-4
%description lib
The libtspi library for use in Trusted Computing enabled applications.

%package static
Summary: TrouSerS TCG Device Driver Library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
The TCG Device Driver Library (TDDL) used by the TrouSerS tcsd as the
interface to the TPM's device driver. For more information about writing
applications to the TDDL interface, see the latest TSS spec at
https://www.trustedcomputinggroup.org/specs/TSS.

%package devel
Summary: TrouSerS header files and documentation
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
%description devel
Header files and man pages for use in creating Trusted Computing enabled
applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# fix man page paths
sed -i -e 's|/var/tpm|/var/lib/tpm|g' -e 's|/usr/local/var|/var|g' man/man5/tcsd.conf.5.in man/man8/tcsd.8.in

# Create a sysusers.d config file
cat >trousers.sysusers.conf <<EOF
u tss 59 'Account used for TPM access' - -
EOF

%build

chmod +x ./bootstrap.sh
./bootstrap.sh
%configure --with-gui=openssl
make -k %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_localstatedir}/lib/tpm
%make_install
find %{buildroot} -type f -name '*.la' -print -delete
mkdir -p %{buildroot}%{_unitdir}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -m0644 -D trousers.sysusers.conf %{buildroot}%{_sysusersdir}/trousers.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post tcsd.service
%preun

%systemd_preun tcsd.service
%postun

%systemd_postun_with_restart tcsd.service 
%files -f %{oreon_filedir}/main.list
%files -n trousers-lib -f %{oreon_filedir}/trousers-lib.list
%files -n trousers-static -f %{oreon_filedir}/trousers-static.list
%files -n trousers-devel -f %{oreon_filedir}/trousers-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.15-17
- Prepare for Oreon 11 (RP1)
