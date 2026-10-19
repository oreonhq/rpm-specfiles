%global source1_hash 3bd65ab522517d46dedaee4e72f202de4b2dd0095a7d34761c97eae256ac5d06
%global source0_hash 136b2e34c5de8baea07ab8834b128cdf7e4f1f1afa0fad157dbf49da5eb323d8
Name:           electrum
Version:        4.8.2
Release:        1%{?dist}
Summary:        A lightweight Bitcoin Client
License:        MIT
URL:            https://electrum.org/
Source0:        https://download.electrum.org/%{version}/Electrum-sourceonly-%{version}.tar.gz
Source1:        https://download.electrum.org/%{version}/Electrum-sourceonly-%{version}.tar.gz.asc
Source2:        gpgkey-%{name}.gpg
Source3:        %{name}.metainfo.xml
Source4:        %{name}.1
Patch0:         relax-protobuf-requirement.patch
Patch1:         fix-secp256k1.patch
Patch2:         relax-aiorpcx-requirements.patch
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
Requires:       libsecp256k1
Requires:       %{py3_dist cryptography}
Requires:       %{py3_dist pyqt5}
Recommends:     zbar
Recommends:     python3-trezor >= 0.13.0
Recommends:     python3-btchip >= 0.1.32
Conflicts:      python3-trezor < 0.11.2
Conflicts:      python3-btchip < 0.1.32
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-electrum = %{version}-%{release}
# /oreon:deps
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

%build

%pyproject_wheel
%install
%pyproject_install
install -Dpm 644 %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -Dpm 644 %{SOURCE4} %{buildroot}%{_mandir}/man1/%{name}.1
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files

%changelog

%autochangelog
