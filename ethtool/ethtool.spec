%global appstream_id org.kernel.software.network.ethtool

Summary:        Settings tool for Ethernet NICs
Name:           ethtool
Epoch:          2
Version:        6.19
Release:        1%{?dist}
# {json_print,qsfp,sff-common}.{c,h} are GPL-2.0-or-later, rest is GPL-2.0-only
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://www.kernel.org/pub/software/network/%{name}/
Source0:        https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.sign
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/D2CB120AB45957B721CD9596F4554567B91DE934
BuildRequires:  gnupg2, xz
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  libmnl-devel
BuildRequires:  make
Conflicts:      filesystem < 3

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially of Ethernet devices.

%prep
xzcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
make check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{appstream_id}.metainfo.xml

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog* NEWS README
%{_sbindir}/%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man8/%{name}.8*
%{_metainfodir}/%{appstream_id}.metainfo.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.19-1
- Prepare for Oreon 11 (RP1)
