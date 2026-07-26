%global source0_hash 76dda8e1ad37a4c8bb676afe431eaa26e310e79968acf3f6386aedc319ac00f9

Name:           gkrellm-wifi
Version:        0.9.12
Release:        44%{?dist}
Summary:        Wireless monitor plugin for the GNU Krell Monitors
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.gkrellm.net/
# upsteam is dead, no URL
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
Patch1:         gkrellm-wifi-0.9.12-asm_h.patch
Patch2:         gkrellm-wifi-0.9.12-kernel-2.6.26.patch
Patch3:         gkrellm-wifi-0.9.12-bz650345.patch
BuildRequires:  gcc make
BuildRequires:  gkrellm-devel
Requires:       gkrellm >= 2.2, gkrellm < 3
# Unfortunate, but nescesarry this plugin used to be (wrongly) packaged in the
# same specfile as gkrellm itself, with the wrong namae gkrellm-wireless and
# causing it to have version 2.2.9 :(
Obsoletes:      gkrellm-wireless <= 2.2.9-3
Provides:       gkrellm-wireless = 2.2.9-4
ExcludeArch:    s390 s390x

%description
Plug-in for gkrellm (a system monitor) which monitors the wireless LAN cards in
your PC and displays a graph of the link quality percentage for each card.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -z .asm_h
%patch -P2 -p1
%patch -P3 -p1

%build
# -std=gnu17 because gkrellm-public-proto.h has incomplete callback prototpyes
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -std=gnu17 \
  `pkg-config gkrellm --cflags` -DG_LOG_DOMAIN=\\\"gkrellm-wifi\\\""

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins
install -m 755 %{name}.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%files
%doc AUTHORS ChangeLog NEWS README THEMING TODO
%license COPYING
%{_libdir}/gkrellm2/plugins/%{name}.so

%changelog
%autochangelog
