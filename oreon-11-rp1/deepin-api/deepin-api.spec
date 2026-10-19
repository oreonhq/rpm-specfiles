%global source0_hash af28b1f73d58c1dd1dc06ddfb03a2ca96516f92066ec5a82858421981a616abd
%bcond check 1
%global goipath         github.com/linuxdeepin/dde-api
Version:                6.0.48
%global tag %{version}
%gometa -L -f
Name:           deepin-api
Release:        1%{?dist}
Summary:        Golang bindings for dde-daemon
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND ISC AND MIT AND (FTL OR GPL-2.0-or-later)
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/dde-api-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       deepin-desktop-base
Requires:       rfkill
# oreon:deps
BuildRequires:  deepin-gettext-tools
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Golang bindings for dde-daemon.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

sed -i 's|boot/grub/|boot/grub2/|' adjust-grub-theme/main.go
sed -i 's|cp out/bin|cp _build/bin|' Makefile

# add targets to print the binaries, so we can build/install them
# in Fedora style
cat <<EOF >> Makefile
print_binaries:
	@echo \${BINARIES}
EOF

%build

%global gomodulesmode GO111MODULE=on
for cmd in $(make print_binaries); do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%make_build ts-to-policy
%install
%go_vendor_license_install -c %{S:2}
make DESTDIR=%{buildroot} SYSTEMD_SERVICE_DIR="%{_unitdir}" GOBUILD_DIR=_build install-binary
install -pDm 0644 misc/sysusers/deepin-daemon.conf %{buildroot}%{_sysusersdir}/deepin-daemon.sysusers
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv -v %{buildroot}%{_prefix}/lib/%{name}/sound-theme-player \
      %{buildroot}%{_libexecdir}/%{name}
ln -s ../../libexec/%{name}/sound-theme-player \
      %{buildroot}%{_prefix}/lib/%{name}/sound-theme-player
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%post

%systemd_post deepin-shutdown-sound.service
%preun

%systemd_preun deepin-shutdown-sound.service
%postun

%systemd_postun_with_restart deepin-shutdown-sound.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
