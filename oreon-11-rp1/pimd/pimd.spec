%global source0_hash c77a9812751f114490a28a6839b16aac8b020c8d9fd6aa22bf3880c054e19f1d
Name:           pimd
Version:        2.3.2
Release:        29%{?dist}
Summary:        The original PIM-SM multicast routing daemon
License:        LicenseRef-Callaway-BSD
URL:            http://troglobit.com/pimd.html
Source0:        ftp://ftp.troglobit.com/pimd/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Patch0000:      0000-bin-path.patch
Provides:       bundled(libite) = 1.4.2
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
pimd is a lightweight, stand-alone PIM-SM/SSM multicast routing daemon
available under the free 3-clause BSD license. This is the restored
original version from University of Southern California, by Ahmed Helmy,
Rusty Eddy and Pavlin Ivanov Radoslavov.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
rm %{buildroot}/usr/share/doc/pimd/LICENSE
rm %{buildroot}/usr/share/doc/pimd/LICENSE.mrouted
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
