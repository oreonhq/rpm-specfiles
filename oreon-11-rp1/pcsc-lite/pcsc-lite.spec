%global source1_hash 9efb84f3ea94142ea8b1729d2b97006bf33c4d1e0057033960791ab67e900785
%global source0_hash 60a08942d8c00a1d86a3bf4c64eddbf7a5569c7c54f6904e3f07801bb5316acd
%global source2_key_fpr F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E
%if 0%{?flatpak}
%global with_polkit 0
%else
%global with_polkit 1
%endif
Name:           pcsc-lite
Version:        2.5.2
Release:        1%{?dist}
Summary:        PC/SC Lite smart card framework and applications
License:        BSD-3-Clause AND BSD-2-Clause AND GPL-3.0-or-later
URL:            https://pcsclite.apdu.fr/
Source0:        https://pcsclite.apdu.fr/files/%{name}-%{version}.tar.xz
Source1:        https://pcsclite.apdu.fr/files/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E.gpg
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:       pcsc-ifd-handler
Requires:       %{name}-libs = %{version}-%{release}
Requires:       polkit
Requires:       python3
Recommends:     pcsc-lite-ccid
Provides:       bundled(simclist) = 1.6
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  perl-podlators
BuildRequires:  polkit-devel
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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

test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%setup -q

# Convert to utf-8
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n pcsc-lite-libs -f %{oreon_filedir}/pcsc-lite-libs.list
%files -n pcsc-lite-devel -f %{oreon_filedir}/pcsc-lite-devel.list
%files -n pcsc-lite-doc -f %{oreon_filedir}/pcsc-lite-doc.list

%changelog

%autochangelog
