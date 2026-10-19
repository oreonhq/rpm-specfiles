%global source0_hash 4e6e76851dbf2606185972b53ec5decad68fe53b63a56e4df8b8b3c0a6c46800
%global _hardened_build 1
Name:           znc
Version:        1.10.1
Release:        2%{?dist}
Summary:        An advanced IRC bouncer
License:        Apache-2.0
URL:            https://znc.in
Source0:        https://%{name}.in/releases/archive/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/archive/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-5AE420CC0209989E.asc
Patch0:         0001-Use-system-wide-crypto-policy.patch
%{?systemd_requires}
# oreon:deps
BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  openssl11-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  tcl-devel
# /oreon:deps
%description
ZNC is an IRC bouncer with many advanced features like detaching,
multiple users, per channel playback buffer, SSL, IPv6, transparent
DCC bouncing, Perl and C++ module support to name a few.

%package devel
Summary:        Development files needed to compile ZNC modules
Requires:       %{name} = %{version}-%{release} pkgconfig
Requires:       openssl-devel c-ares-devel glibc-devel libicu-devel%{?_isa}
BuildRequires: pkgconfig
Requires:       gcc-c++ redhat-rpm-config
%description devel
All includes and program files you need to compile your own znc
modules.

%package modtcl
Summary:       TCL module for ZNC
BuildRequires: tcl-devel
Requires:      %{name} = %{version}-%{release}
Requires:      tcl
%description modtcl
%{summary}.

%if 0%{?with_modperl}
%package modperl
Summary:       Perl module for ZNC
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: swig
Requires:      %{name} = %{version}-%{release}
Requires:      perl-interpreter
Provides:      perl(ZNC::Module) = %{version}-%{release}
%description modperl
%{summary}.
%endif # 0%{?with_modperl}

%if 0%{?with_modpython}
%package modpython
Summary:       Python3 module for ZNC
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: swig
Requires:      %{name} = %{version}-%{release}
Requires:      python%{python3_pkgversion}
%description modpython
%{summary}.
%endif # 0%{?with_modpython}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify GPG signature
gpghome="$(mktemp -qd)" # Ensure we don't use any existing gpg keyrings
key="%{SOURCE2}"
gpg2 --dearmor --quiet --batch --yes $key >/dev/null
gpgv2 --homedir "$gpghome" --quiet --keyring $key.gpg %{SOURCE1} %{SOURCE0}
rm -rf "$gpghome" $key.gpg # Cleanup tmp gpg home dir and dearmored key

%autosetup -p1

# The manual page references /usr/local/; fix that
sed -ie 's!/usr/local/!/usr/!' man/znc.1

# Create a sysusers.d config file
cat >znc.sysusers.conf <<EOF
u znc - 'Account for ZNC to run as' /var/lib/znc -
EOF

%build

%ifarch aarch64
%global _smp_build_ncpus 1
%endif
%ifarch x86_64
%global _smp_build_ncpus 1
%endif
%cmake \
%if 0%{?with_modperl}
    -DWANT_PERL=1 \
%endif
%if 0%{?with_modpython}
    -DWANT_PYTHON=1 \
%endif
    -DWANT_SYSTEMD=1 \
    -DSYSTEMD_DIR=%{_unitdir} \
    -DWANT_IPV6=1 \
    -DWANT_CYRUS=1 \
    -DWANT_TCL=1
%cmake_build
%install
%cmake_install
install -d "%{buildroot}%{_sharedstatedir}/znc"
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/znc/
install -m0644 -D znc.sysusers.conf %{buildroot}%{_sysusersdir}/znc.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post znc.service
%postun

%systemd_postun_with_restart znc.service
%preun

%systemd_preun znc.service
%files -f %{oreon_filedir}/main.list
%files -n znc-devel -f %{oreon_filedir}/znc-devel.list
%files -n znc-modtcl -f %{oreon_filedir}/znc-modtcl.list

%changelog

%autochangelog
