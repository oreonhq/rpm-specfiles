%global source0_hash cf37e565b958a64f1e3086daeab82d7959566a372d01d40d3904cbca95cdf3d2
Name:             powertop
Version:          2.16
Release:        1%{?dist}
Summary:        Power consumption monitor
License:          gpl-2.0-only AND lgpl-2.1-only AND isc
URL:              http://01.org/powertop/
Source0:        http://github.com/fenrus75/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz#/powertop-%{version}.tar.gz
Source1:          powertop.service
Requires(post):   systemd, coreutils
Requires(preun):  systemd
Requires(postun): systemd
Recommends:       xset
Provides:         bundled(kernel-event-lib)
# oreon:deps
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pciutils-devel
BuildRequires:  pkgconfig(libtracefs)
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
PowerTOP is a tool that finds the software component(s) that make your
computer use more power than necessary while it is idle.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# https://www.gnu.org/software/gettext/manual/html_node/autopoint-Invocation.html
sed -i -e 's|AM_GNU_GETTEXT_VERSION|AM_GNU_GETTEXT_REQUIRE_VERSION|' configure.ac

echo "v%{version}" > version-long
echo '"v%{version}"' > version-short

%build

autoreconf -fi || autoreconf -fi
%configure
printf '#include <algorithm>\n#include <format>\n' > oreon-std.h
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags} -include %_builddir/powertop-%{version}/oreon-std.h" V=1
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -Dd %{buildroot}%{_localstatedir}/cache/powertop
touch %{buildroot}%{_localstatedir}/cache/powertop/{saved_parameters.powertop,saved_results.powertop}
%find_lang %{name}
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/powertop.service
%oreon_autofiles main

%preun

%systemd_preun powertop.service
%postun

%systemd_postun_with_restart powertop.service
%post

%systemd_post powertop.service
touch %{_localstatedir}/cache/powertop/{saved_parameters.powertop,saved_results.powertop} &> /dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
