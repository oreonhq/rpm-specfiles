%global source0_hash ffc7a58cdde390a01580f4cfc78c446b0965bcb719bde2c68c5e0c27345a8dfc

Summary:        Tunnel IPv4 data through a DNS server
Name:           iodine
Version:        0.8.0
Release:        1%{?dist}
License:        ISC
URL:            https://code.kryo.se/iodine/
Source0:        https://github.com/yarrick/iodine/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcheck)
BuildRequires:  pkgconfig(systemd)

%description
iodine lets you tunnel IPv4 data through a DNS server, which is usable in
situations where internet access is firewalled but DNS queries are
allowed. iodine is the client, iodined is the server. Used as the backend
transport for NetworkManager-iodine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}

%build
make %{?_smp_mflags} prefix=%{_prefix} sbindir=%{_sbindir} mandir=%{_mandir}

%install
%make_install prefix=%{_prefix} sbindir=%{_sbindir} mandir=%{_mandir} docdir=%{_defaultdocdir}/iodine-unused
rm -rf %{buildroot}%{_defaultdocdir}/iodine-unused

%files
%license LICENSE
%doc README.md CHANGELOG
%{_sbindir}/iodine
%{_sbindir}/iodined
%{_mandir}/man8/iodine.8*

%changelog
%autochangelog
