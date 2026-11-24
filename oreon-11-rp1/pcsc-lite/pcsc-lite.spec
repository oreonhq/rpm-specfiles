# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 23b1c644ab4f13269d3a9ff26734f473f622deff6ed60492171a9a25f603f078
%global source1_hash 3514d024fdc7ac6847329ace20c934917354b7663314e60084c9011b2c6ca797
%global source2_hash 204e5824015b70baa1da46a58aa3b2be53e67e03848e180006c82edca387c6da
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global source2_key_fpr F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E

%if 0%{?flatpak}
%global with_polkit 0
%else
%global with_polkit 1
%endif

Name:           pcsc-lite
Version:        2.5.4
Release:        1%{?dist}
Summary:        PC/SC Lite smart card framework and applications

License:        BSD-3-Clause AND BSD-2-Clause AND GPL-3.0-or-later
URL:            https://pcsclite.apdu.fr/
Source0:        https://pcsclite.apdu.fr/files/%{name}-%{version}.tar.xz
Source1:        https://pcsclite.apdu.fr/files/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E.gpg

BuildRequires: oreon-rpm-macros
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  perl-podlators
%if %{with_polkit}
BuildRequires:  polkit-devel
%endif
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  clang
BuildRequires:  python3-devel
BuildRequires:  flex
BuildRequires: libappstream-glib

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:       pcsc-ifd-handler
Requires:       %{name}-libs = %{version}-%{release}
%if %{with_polkit}
Requires:       polkit
%endif
Requires:       python3
Recommends:     pcsc-lite-ccid
Provides:       bundled(simclist) = 1.6

%description
The purpose of PC/SC Lite is to provide a Windows(R) SCard interface
in a very small form factor for communicating to smartcards and
readers.  PC/SC Lite uses the same winscard API as used under
Windows(R).  This package includes the PC/SC Lite daemon, a resource
manager that coordinates communications with smart card readers and
smart cards that are connected to the system, as well as other command
line tools.

%package        libs
Summary:        PC/SC Lite libraries

%description    libs
PC/SC Lite libraries.

%package        devel
Summary:        PC/SC Lite development files
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
PC/SC Lite development files.

%package        doc
Summary:        PC/SC Lite developer documentation
BuildArch:      noarch
Requires:       %{name}-libs = %{version}-%{release}

%description    doc
%{summary}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup

for file in ChangeLog; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
%meson -Dlibsystemd=true \
    -Dsystemdunit=system \
    -Dserial=true \
    -Dusbdropdir=%{_libdir}/pcsc/drivers \
%if ! %{with_polkit}
   -Dpolkit=false
%else
   -Dpolkit=true
%endif
%meson_build
%meson_build doc

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/reader.conf.d
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/pcscd

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%post
%systemd_post pcscd.socket pcscd.service
if [ $1 -eq 1 ] ; then
   if systemctl -q is-enabled pcscd.socket > /dev/null 2>&1 ; then
      systemctl start pcscd.socket > /dev/null 2>&1 || :
   fi
fi

%preun
%systemd_preun pcscd.socket pcscd.service

%postun
%systemd_postun_with_restart pcscd.socket pcscd.service

%ldconfig_scriptlets libs

%files
%doc AUTHORS ChangeLog HELP README SECURITY
%doc doc/README.polkit
%doc src/spy/setup_spy.sh
%dir %{_sysconfdir}/reader.conf.d/
%{_unitdir}/pcscd.service
%{_unitdir}/pcscd.socket
%{_sbindir}/pcscd
%dir %{_libdir}/pcsc/
%dir %{_libdir}/pcsc/drivers/
%{_mandir}/man5/reader.conf.5*
%{_mandir}/man8/pcscd.8*
%ghost %dir %{_localstatedir}/run/pcscd/
%if %{with_polkit}
%dir %{_datadir}/polkit-1/
%dir %{_datadir}/polkit-1/actions/
%{_datadir}/polkit-1/actions/org.debian.pcsc-lite.policy
%endif
%{_metainfodir}/fr.apdu.pcsclite.metainfo.xml
%{_sysconfdir}/default/pcscd

%files libs
%license COPYING
%{_libdir}/libpcsclite.so.*
%{_libdir}/libpcsclite_real.so.*
%{_sysusersdir}/pcscd-sysusers.conf

%files devel
%{_bindir}/pcsc-spy
%{_includedir}/PCSC/
%{_libdir}/libpcsclite.so
%{_libdir}/libpcsclite_real.so
%{_libdir}/libpcscspy.so*
%dir %{_libdir}/pkgconfig/
%{_libdir}/pkgconfig/libpcsclite.pc
%{_mandir}/man1/pcsc-spy.1*

%files doc
%doc %{_vpath_builddir}/doc/api/ doc/example/pcsc_demo.c

%changelog
%autochangelog
