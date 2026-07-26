%global source0_hash 65472155f0d13ec204c49ce86c39d6eaeb044aef6e53b85ce05bdf906cc09853

%global pname   remote
%global __provides_exclude_from ^%{vdr_libdir}/.*\\.so.*$

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-%{pname}
Version:        0.7.0
Release:        45%{?dist}
Summary:        Extended remote control plugin for VDR
License:        GPL-1.0-or-later
URL:            http://www.escape-edv.de/endriss/vdr/
Source0:        http://www.escape-edv.de/endriss/vdr/%{name}-%{version}.tgz
Source1:        %{name}.conf
Source2:        %{name}-udev.rules
# Status query mail sent to upstream and Debian patchkit maintainer 2008-10-25
Patch0:         http://zap.tartarus.org/~ds/debian/dists/stable/main/source/vdr-plugin-remote_0.3.8-3.ds.diff.gz
Patch1:         vdr-remote-gcc11.patch
Patch2:         new-expresson-cLircRemote.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  gettext
BuildRequires:  systemd
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
# systemd >= 214-3 for the input group
Requires:       systemd >= 214-3

%description
This plugin extends VDR's remote control capabilities, adding support
for Linux input devices, keyboards (tty), TCP connections, and LIRC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pname}-%{version} -p1

patch -p1 -i debian/patches/02_no_abort.dpatch
sed -i \
    -e 's/0\.3\.8/%{version}/g' \
    -e 's/"Remote control"/trNOOP("Remote control")/' \
    debian/patches/04_constness.dpatch
patch -p1 -i debian/patches/04_constness.dpatch

for f in CONTRIBUTORS HISTORY ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done

%build
%make_build

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -Dpm 644 %{SOURCE2} \
    %{buildroot}/%{_udevrulesdir}/52-%{name}.rules
%find_lang %{name}

%pre
usermod -a -G input %{vdr_user} || :

%files -f %{name}.lang
%license COPYING
%doc CONTRIBUTORS FAQ HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%config(noreplace) %{_udevrulesdir}/*-%{name}.rules
%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion}

%changelog
%autochangelog
