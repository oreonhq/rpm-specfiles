%global source0_hash 7398ce05f0f9786aa14b40daeb73290d99cc0b7f4969772330aa48016696d10f

Name:           sigrok-firmware
Version:        0.1.0
%global         checkout 20151211gitb2daf81
Release:        27.%{checkout}%{?dist}
Summary:        Firmware for some hardware supported by sigrok
License:        GPL-2.0-only AND LicenseRef-Fedora-Firmware
URL:            http://www.sigrok.org/
# $ git clone git://sigrok.org/sigrok-firmware
# $ cd sigrok-firmware
# $ git checkout b2daf81ca2e892b5b80ce4bc35ff5a846853b50b
# $ sh autogen.sh
# $ mkdir build
# $ cd build
# $ ../configure
# $ make dist
# $ mv %%{name}-%%{version}.tar.gz %%{name}-%%{version}-%%{checkout}.tar.gz
Source0:        %{name}-%{version}-%{checkout}.tar.gz
BuildArch:      noarch

BuildRequires:  make

%description
%{name} is a collection of firmware files required for some of the
devices libsigrok supports (logic analyzers, oscilloscopes, or others).

%{name} only contains firmware files which have an explicit
permission/license that allows at _least_ redistribution of the firmware.

%package        nonfree
Summary:        Components of %{name} with non-free licenses
License:        LicenseRef-Fedora-Firmware
Requires:       %{name}-filesystem = %{version}-%{release}

%description    nonfree
The %{name}-nonfree package contains firmwares available under non-free
licenses which permit redistribution.

%package        filesystem
Summary:        Directory structure for %{name}

%description    filesystem
This package provides directories required by packages containing sigrok
binary firmware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files filesystem
%doc README NEWS COPYING
%dir %{_datadir}/%{name}

%files nonfree
%doc asix-sigma/LICENSE.Sigma
%{_datadir}/%{name}/asix-sigma-*.fw
%doc sysclk-lwla/LICENSE.LWLA
%{_datadir}/%{name}/sysclk-lwla1016-*.rbf
%{_datadir}/%{name}/sysclk-lwla1034-*.rbf

%changelog
%autochangelog
