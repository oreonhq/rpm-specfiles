%global source0_hash 56ca15ddf96d39ab0bf8ee12d3daca13cea45af01bcd5a9732ffcc01664fdfa2

Name:           uhubctl
Version:        2.6.0
Release:        5%{?dist}
Summary:        USB hub per-port power control

License:        GPL-2.0-only
URL:            https://github.com/mvp/%{name}
Source0:        https://github.com/mvp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
uhubctl is utility to control USB power per-port on smart USB hubs. Smart hub
is defined as one that implements per-port power switching.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build

%install
%make_install sbindir=%{_sbindir}

%check
%{buildroot}%{_sbindir}/%{name} --version

%files
%license COPYING LICENSE
%doc README.md
%{_sbindir}/%{name}

%changelog
%autochangelog
