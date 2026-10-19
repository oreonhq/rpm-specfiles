%global source0_hash 5eff09d35d39b18f9d593f0f464e2fb5be3ddf6c92fa9eb1e99c534126c62419
%global goipath github.com/AvengeMedia/%{name}/core
%bcond check 0
Name:           DankMaterialShell
Version:        1.6.2
Release:        1%{?dist}
Summary:        Desktop shell for Wayland compositors built on QuickShell
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-only AND ISC AND MIT AND MPL-2.0
URL:            https://danklinux.com/
Source0:        https://github.com/AvengeMedia/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%dnl dms-core go dependencies
%dnl Generated with the following:
%dnl $ tar xvf %{name}-%{version}.tar.bz2
%dnl $ cd %{name}-%{version}/core/
%dnl $ go_vendor_archive create %{name}-%{version}/core/ --output %{name}-%{version}-core-govendor.tar.bz2 --config %{S:2}
Source1:        %{name}-%{version}-core-govendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       accountsservice
Requires:       cups-pk-helper
Requires:       hicolor-icon-theme
Requires:       quickshell
Requires:       (adw-gtk3-theme if gtk3)
Requires:       cava
Requires:       cliphist
Requires:       danksearch
Requires:       dgop
Requires:       kf6-kimageformats
Requires:       khal
Requires:       matugen
Requires:       (qt5ct if qt5-qtbase)
Requires:       qt6ct
Requires:       qt6-qtmultimedia
Requires:       qt6-qtimageformats
Requires:       wl-clipboard
Recommends:     NetworkManager
Recommends:     ppd-service
Suggests:       tuned-ppd
Requires(posttrans): procps-ng
Obsoletes:      dms < %{version}-%{release}
Provides:       dms = %{version}-%{release}
Obsoletes:      dms-cli < %{version}-%{release}
Provides:       dms-cli = %{version}-%{release}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
DankMaterialShell is a complete desktop shell for Wayland compositors.
It replaces a variety of tools used to stitch together to make a desktop.

It features notifications, an app launcher, wallpaper customization, and is
fully customizable with plugins.

It includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
tar -xf %{S:1} -C core

%build

pushd core
export dms_buildtime=$(date -d "@${SOURCE_DATE_EPOCH}" +%%Y-%%m-%%d_%%H:%%M:%%S)
export GO_LDFLAGS="-X main.commit=fedora \
                   -X main.Version=%{version}-%{release} \
                   -X main.buildTime=${dms_buildtime}"
%global gomodulesmode GO111MODULE=on
mkdir -p %{_vpath_builddir}/bin
%gobuild -o %{_vpath_builddir}/bin/dms ./cmd/dms
popd
%install
install -Dm644 assets/systemd/dms.service %{buildroot}%{_userunitdir}/dms.service
install -Dm644 assets/dms-open.desktop %{buildroot}%{_datadir}/applications/dms-open.desktop
install -Dm644 assets/danklogo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/danklogo.svg
mkdir -p %{buildroot}%{_datadir}/quickshell/dms
cp -a quickshell/* %{buildroot}%{_datadir}/quickshell/dms/
echo "%{version}-%{release}" > %{buildroot}%{_datadir}/quickshell/dms/VERSION
mkdir -p %{buildroot}%{_bindir}
install -pm0755 core/%{_vpath_builddir}/bin/dms %{buildroot}%{_bindir}/dms
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
core/%{_vpath_builddir}/bin/dms completion bash > %{buildroot}%{bash_completions_dir}/dms
core/%{_vpath_builddir}/bin/dms completion fish > %{buildroot}%{fish_completions_dir}/dms.fish
core/%{_vpath_builddir}/bin/dms completion zsh > %{buildroot}%{zsh_completions_dir}/_dms
pushd core
%go_vendor_license_install -c %{S:2}
popd
%oreon_autofiles main

%check

pushd core
%dnl %go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
popd
%posttrans

pkill -USR1 -x dms || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
