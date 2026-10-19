%global source0_hash a1a16e60895c6b2fd151321db47f5d5373843116f1b98ed9749e6c25a6c44497
%global realversion 1.0-25.1
Name:           udpxy
Version:        1.0.25.1
Release:        1%{?dist}
Summary:        UDP-to-HTTP multicast traffic relay daemon
License:        GPL-3.0-or-later
URL:            https://github.com/pcherenkov/udpxy
Source0:        https://github.com/pcherenkov/%{name}/archive/%{realversion}.tar.gz
Source1:        udpxy.service
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
udpxy is a UDP-to-HTTP multicast traffic relay daemon:
it forwards UDP traffic from a given multicast subscription
to the requesting HTTP client.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{realversion}

sed -i 's|@cp $(UDPXREC)|@cp -a $(UDPXREC)|g' chipmunk/Makefile
sed -i 's|-Werror||' chipmunk/Makefile

%build

cd chipmunk
make %{?_smp_mflags} CPPFLAGS="%{optflags}" rdebug
%install
cd chipmunk
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%oreon_autofiles main

%post

%systemd_post udpxy.service
%preun

%systemd_preun udpxy.service
%postun

%systemd_postun_with_restart udpxy.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
