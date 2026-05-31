%global source0_hash e58ab3fd7b8ff5f4dd0d17f11848817e7d83c0a6918145ac81de03b5dccf8f49

Name:             powertop
Version:          2.15
Release:          12%{?dist}
Summary:          Power consumption monitor

License:          gpl-2.0-only AND lgpl-2.1-only AND isc
URL:              http://01.org/powertop/
Source0:        http://github.com/fenrus75/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:          powertop.service

# Sent upstream
Patch0:           powertop-2.7-always-create-params.patch
BuildRequires:    make
BuildRequires:    gettext-devel
BuildRequires:    ncurses-devel
BuildRequires:    pciutils-devel
BuildRequires:    zlib-devel
BuildRequires:    libnl3-devel
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    systemd
BuildRequires:    autoconf-archive
BuildRequires:    gcc
BuildRequires:    gcc-c++
Requires(post):   systemd, coreutils
Requires(preun):  systemd
Requires(postun): systemd
# For "xset dpms force off" during calibration
Recommends:       xset
Provides:         bundled(kernel-event-lib)

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
# workaround for rhbz#1826935
autoreconf -fi || autoreconf -fi
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -Dd %{buildroot}%{_localstatedir}/cache/powertop
touch %{buildroot}%{_localstatedir}/cache/powertop/{saved_parameters.powertop,saved_results.powertop}
%find_lang %{name}

# Systemd
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/powertop.service

%preun
%systemd_preun powertop.service

%postun
%systemd_postun_with_restart powertop.service

%post
%systemd_post powertop.service
# Hack for powertop not to show warnings on first start
touch %{_localstatedir}/cache/powertop/{saved_parameters.powertop,saved_results.powertop} &> /dev/null || :

%files -f %{name}.lang
%doc COPYING README.md README.traceevent CONTRIBUTE.md TODO
%dir %{_localstatedir}/cache/powertop
%ghost %{_localstatedir}/cache/powertop/saved_parameters.powertop
%ghost %{_localstatedir}/cache/powertop/saved_results.powertop
%{_sbindir}/powertop
%{_mandir}/man8/powertop.8*
%{_unitdir}/powertop.service
%{_datadir}/bash-completion/completions/powertop

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15-12
- Import
