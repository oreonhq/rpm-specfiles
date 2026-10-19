%global source0_hash c8352b6653c3194af1f869107655df3f98ab18b560e8bce86eabac08d73c72eb
Name:           2ping
Version:        4.6.1
Release:        1%{?dist}
Summary:        Bi-directional ping utility
License:        GPL-2.0-or-later
URL:            https://www.finnie.org/software/2ping
Source0:        https://www.finnie.org/software/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-2ping = %{version}-%{release}
# /oreon:deps
%package -n       python3-2ping+full
Summary:        Metapackage for python3-2ping full extras
Requires:       python3-2ping = %{version}-%{release}
Provides:       python3dist(2ping[full]) = %{version}-%{release}

%description -n python3-2ping+full
Metapackage for python3-2ping full extras.

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN,
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -Dp -m 0644 2ping.service %{buildroot}/%{_unitdir}/2ping.service
install -Dp -m 0644 doc/2ping.1 %{buildroot}/%{_mandir}/man1/2ping.1
install -Dp -m 0644 doc/2ping.1 %{buildroot}/%{_mandir}/man1/2ping6.1
%oreon_autofiles main

%check

%pyproject_check_import
%{__python3} -mpytest
%post

%systemd_post 2ping.service
%preun

%systemd_preun 2ping.service
%postun

%systemd_postun 2ping.service
%files

%changelog

%autochangelog
