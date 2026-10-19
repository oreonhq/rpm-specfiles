%global source0_hash 718e5519b0a403f7f766358bf66a85c008119c48189d1c2b7651fd0af9018e27
Name:             tntnet
Version:          3.0
Release:        15%{?dist}
Summary:        A web application server for web applications
Epoch:            1
License:          LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND Zlib
URL:              http://www.tntnet.org/
Source0:        http://www.tntnet.org/download/%{name}-%{version}.tar.gz
Source1:          %{name}.service
Patch0:           %{name}-%{version}-missing-call-to-setgroups-before-setuid.patch
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  cxxtools-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  systemd-units
BuildRequires:  zip
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{summary}

%package          devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:         cxxtools-devel%{?_isa} >= 3.0
%description devel
Development files for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# Create a sysusers.d config file
cat >tntnet.sysusers.conf <<EOF
u tntnet - 'User' %{_localstatedir}/lib/%{name} -
EOF

%build

%configure --disable-static
%make_build
%install
%make_install DESTDIR=%{buildroot} INSTALL="install -p"
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/doc/
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
install -m0644 -D tntnet.sysusers.conf %{buildroot}%{_sysusersdir}/tntnet.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

test/tntnet-test
%post

/sbin/ldconfig
%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
/sbin/ldconfig
%files -f %{oreon_filedir}/main.list
%files -n tntnet-devel -f %{oreon_filedir}/tntnet-devel.list

%changelog

%autochangelog
