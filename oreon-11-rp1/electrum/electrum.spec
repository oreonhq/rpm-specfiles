%global source0_hash 1f8398fe01751120ef97e20702649dddcf1d5e27ccec85cca133e4d207d41f09

Name:           electrum
Version:        4.5.8
Release:        9%{?dist}
Summary:        A lightweight Bitcoin Client

License:        MIT
URL:            https://electrum.org/
Source0:        https://download.electrum.org/%{version}/Electrum-sourceonly-%{version}.tar.gz
Source1:        https://download.electrum.org/%{version}/Electrum-sourceonly-%{version}.tar.gz.asc
#Wed Feb 01 2017, exported the upstream gpg key using the command:
#gpg2 --export --export-options export-minimal 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6 9EDAFF80E080659604F4A76B2EBB056FD847F8A7 0EEDCFD5CAFB459067349B23CA9EEEC43DF911DC > gpgkey-electrum.gpg
Source2:        gpgkey-%{name}.gpg
Source3:        %{name}.metainfo.xml
Source4:        %{name}.1

Patch0:         relax-protobuf-requirement.patch
Patch1:         fix-secp256k1.patch
Patch2:         relax-aiorpcx-requirements.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  gettext

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gnupg2
BuildRequires:  protobuf-compiler

Requires:       hicolor-icon-theme

# Unlucky rpm automatic dependency generation doesn't catch this dependency
Requires:       libsecp256k1

# Extra items are not tracked by runtime autodeps yet
Requires:       %{py3_dist cryptography}
Requires:       %{py3_dist pyqt5}

Recommends:     zbar
Recommends:     python3-trezor >= 0.13.0
Recommends:     python3-btchip >= 0.1.32

Conflicts:      python3-trezor < 0.11.2
Conflicts:      python3-btchip < 0.1.32

%description
Electrum is an easy to use Bitcoin client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0 -n Electrum-%{version}
rm -rf Electrum.egg-info
rm -rf packages

contrib/generate_payreqpb2.sh
contrib/build_locale.sh electrum/locale electrum/locale

%generate_buildrequires
%pyproject_buildrequires -x gui -x crypto

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

install -Dpm 644 %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -Dpm 644 %{SOURCE4} %{buildroot}%{_mandir}/man1/%{name}.1

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{pyproject_files}
%doc AUTHORS README.md RELEASE-NOTES
%license LICENCE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
