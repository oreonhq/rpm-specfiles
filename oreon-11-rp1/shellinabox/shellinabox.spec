%global source0_hash 2a8f94beb286d0851bb146f7a7c480a8740f59b959cbd274e21a8fcbf0a7f307
%global username shellinabox
Name:           shellinabox
Version:        2.21
Release:        1%{?dist}
Summary:        Web based AJAX terminal emulator
License:        GPL-2.0-only
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        shellinaboxd.sysconfig
Source2:        shellinaboxd.service
Source3:        shellinaboxd.init
Patch0:         %{name}-ssh-options.patch
Patch1:         %{name}-gcc11.patch
Patch2: shellinabox-configure-c99.patch
Requires:       openssl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Shell In A Box implements a web server that can export arbitrary command line
tools to a web based terminal emulator. This emulator is accessible to any
JavaScript and CSS enabled web browser and does not require any additional
browser plugins.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# Create a sysusers.d config file
cat >shellinabox.sysusers.conf <<EOF
u shellinabox - 'Shellinabox' %{_sharedstatedir}/shellinabox -
EOF

%build

autoreconf -vif
%configure --disable-runtime-loading
make %{?_smp_mflags}
chmod 644 %{name}/*
%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
install -p -m 755 -D shellinaboxd %{buildroot}%{_sbindir}/shellinaboxd
install -p -m 644 -D shellinaboxd.1 %{buildroot}%{_mandir}/man1/shellinaboxd.1
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/shellinaboxd
install -p -m 644 shellinabox/white-on-black.css %{buildroot}%{_datadir}/%{name}
install -p -m 644 shellinabox/color.css %{buildroot}%{_datadir}/%{name}
install -p -m 644 shellinabox/monochrome.css %{buildroot}%{_datadir}/%{name}
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_initrddir}/shellinaboxd
install -m0644 -D shellinabox.sysusers.conf %{buildroot}%{_sysusersdir}/shellinabox.conf
%oreon_autofiles main

%pre

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
