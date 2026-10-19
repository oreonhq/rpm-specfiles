%global source0_hash 372931bda8556b310636a2f9020adc710f9bab66f47efe0ce90bff800ac2530c
%global source2_key_fpr 8C5F7146A1757A65E2422A94D70D1A666ACF2B21
Name:           nftables
Version:        1.1.6
Release:        1%{?dist}
Epoch:          1
Summary:        Netfilter Tables userspace utilities
License:        GPL-2.0-only
URL:            https://netfilter.org/projects/nftables/
Source0:        https://netfilter.org/projects/nftables//files/nftables-1.1.6.tar.xz
Source1:        nftables-1.1.6.tar.xz.sig
SOURCE2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
Source3:        nftables.service
Source4:        nftables.conf
Source5:        main.nft
Source6:        router.nft
Source7:        nat.nft
Patch01: 0001-build-fix-.-configure-with-non-bash-shell.patch
Patch02: 0002-doc-fix-typo-in-man-page.patch
Requires:	%{name}-services = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nftables = %{version}-%{release}
# /oreon:deps
%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
%description devel
Headers, man pages and other development files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-nftables}
BuildArch:	noarch
%description -n python3-nftables
The nftables python module provides an interface to libnftables via ctypes.

%package	services
Summary:	Systemd service for nftables
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch
%description	services
Manage an nftables-based firewall defined by ruleset snippets in /etc/nftables
and /etc/sysconfig/nftables.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -fi
%configure --disable-silent-rules --with-xtables --with-json
%make_build
cd py/
%pyproject_wheel
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnftables.a
rm -f $RPM_BUILD_ROOT/%{_datadir}/nftables/*.nft
chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man8/nft*
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp -a %{SOURCE3} $RPM_BUILD_ROOT/%{_unitdir}/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
cp -a %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/
cp %{SOURCE5} %{SOURCE6} %{SOURCE7} \
	$RPM_BUILD_ROOT/%{_sysconfdir}/nftables/
find $RPM_BUILD_ROOT/%{_sysconfdir} \
	\( -type d -exec chmod 0700 {} \; \) , \
	\( -type f -exec chmod 0600 {} \; \)
cd py/
%pyproject_install
%oreon_autofiles python3-nftables usr/lib/python3*/site-packages/nftables* usr/lib64/python3*/site-packages/nftables* usr/bin/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/nftables* usr/lib64/python3*/site-packages/nftables* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post services

if [ $1 -eq 1 ] && [[ ! -h /etc/systemd/system/multi-user.target.wants/nftables.service ]]; then
  %systemd_post nftables.service
fi
%preun services

%systemd_preun nftables.service
%postun services

%systemd_postun_with_restart nftables.service
%files
%files -n nftables-devel -f %{oreon_filedir}/nftables-devel.list
%files -n python3-nftables -f %{oreon_filedir}/python3-nftables.list
%files -n nftables-services -f %{oreon_filedir}/nftables-services.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-2
- Prepare for Oreon 11 (RP1)
