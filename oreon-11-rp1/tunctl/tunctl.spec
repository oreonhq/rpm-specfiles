%global source0_hash aa2a6c4cc6bfacb11e0d9f62334a6638a0d435475c61230116f00b6af8b14fff

Name:           tunctl
Version:        1.5
Release:        36%{?dist}
Summary:        Create and remove virtual network interfaces

License:        GPL-1.0-or-later
URL:            http://tunctl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/tunctl/tunctl-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  docbook-utils

%description
tunctl is a tool to set up and maintain persistent TUN/TAP network
interfaces, enabling user applications access to the wire side of a
virtual nework interface. Such interfaces is useful for connecting VPN
software, virtualization, emulation and a number of other similar
applications to the network stack.

tunctl originates from the User Mode Linux project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} BIN_DIR=%{_sbindir} install

%files
%{_mandir}/man8/tunctl.8*
%{_sbindir}/tunctl
%doc ChangeLog

%changelog
%autochangelog
