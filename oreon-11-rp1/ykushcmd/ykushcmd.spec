%global source0_hash eb6e2dbdf59419d3502fc16c0990aaf211372dc4dcd651a27a82a5884c9ed6af
Name:           ykushcmd
Version:        1.2.3
Release:        13%{?dist}
Summary:        YKUSH Boards Control Application
License:        Apache-2.0
URL:            https://github.com/Yepkit/ykush
Source0:        https://github.com/Yepkit/ykush/archive/%{version}/ykush-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  hidapi-devel
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  systemd-devel
# /oreon:deps
%description
Control application for Yepkit YKUSH Switchable USB Hub boards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ykush-%{version}
%oreon_prep
%build

make %{?_smp_mflags} CPP="%{__cxx} %{optflags} -I/usr/include/hidapi '-DDOCDIR=\"%{_pkgdocdir}\"'"
%install
mkdir -p %{buildroot}%{_bindir}
install bin/ykushcmd %{buildroot}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
