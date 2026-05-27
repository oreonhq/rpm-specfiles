%global source0_hash 372931bda8556b310636a2f9020adc710f9bab66f47efe0ce90bff800ac2530c

Name:           nftables
Version:        1.1.6
Release:        2%{?dist}
# Upstream released a 0.100 version, then 0.4. Need Epoch to get back on track.
Epoch:          1
Summary:        Netfilter Tables userspace utilities

License:        GPL-2.0-only
URL:            https://netfilter.org/projects/nftables/
Source0:        https://netfilter.org/projects/nftables//files/nftables-1.1.6.tar.xz
Source1:        https://netfilter.org/projects/nftables//files/nftables-1.1.6.tar.xz.sig
SOURCE2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
Source3:        nftables.service
Source4:        nftables.conf
Source5:        main.nft
Source6:        router.nft
Source7:        nat.nft

Patch01: 0001-build-fix-.-configure-with-non-bash-shell.patch
Patch02: 0002-doc-fix-typo-in-man-page.patch

#BuildRequires: autogen
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: bison
BuildRequires: pkgconfig(libmnl) >= 1.0.4
BuildRequires: gmp-devel
BuildRequires: pkgconfig(libnftnl) >= 1.3.1
BuildRequires: systemd
BuildRequires: asciidoc
BuildRequires: pkgconfig(xtables) >= 1.6.1
BuildRequires: jansson-devel
BuildRequires: python3-devel
BuildRequires: readline-devel
BuildRequires: libedit-devel
BuildRequires: python3-setuptools
BuildRequires: gnupg2

# XXX: Drop this dependency in F45 or so
Requires:	%{name}-services = %{epoch}:%{version}-%{release}

%generate_buildrequires
cd py/
%pyproject_buildrequires

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

# Don't ship static lib (for now at least)
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnftables.a

# drop vendor-provided configs, they are not really useful
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
%pyproject_save_files nftables

%post services
# We want to keep nftables enabled on dist-upgrades
# So if it is not enabled run the normal systemd_post
if [ $1 -eq 1 ] && [[ ! -h /etc/systemd/system/multi-user.target.wants/nftables.service ]]; then
  %systemd_post nftables.service
fi

%preun services
%systemd_preun nftables.service

%postun services
%systemd_postun_with_restart nftables.service

%files
%license COPYING
%{_sbindir}/nft
%{_libdir}/libnftables.so.*
%{_mandir}/man5/libnftables-json.5*
%{_mandir}/man8/nft*
%{_docdir}/nftables/

%files devel
%{_libdir}/libnftables.so
%{_libdir}/pkgconfig/libnftables.pc
%{_includedir}/nftables/libnftables.h
%{_mandir}/man3/libnftables.3*

%files -n python3-nftables -f %{pyproject_files}

%files services
%config(noreplace) %{_sysconfdir}/nftables/
%config(noreplace) %{_sysconfdir}/sysconfig/nftables.conf
%{_unitdir}/nftables.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-2
- Prepare for Oreon 11 (RP1)
