%global source0_hash eb702a789998d4ea3d58b3ddf5b94fe6edff99663f0385613ce1646177f62846
%global commit f9032ddd26ffb33fd140e0b9d5ee72c445608077
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210927
Name:           lpf
Version:        0.3
Release:        15%{?dist}
Summary:        Local package factory - build non-redistributable rpms
License:        MIT
URL:            https://github.com/sergiomb2/lpf
Source0:        https://github.com/sergiomb2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         https://github.com/sergiomb2/lpf/commit/4f414697e6977da5fdeff7632ec3ea86ffdfbdfb.patch
Patch3:         0003-Remove-option-allowerasing-of-dnf-install.patch
Patch4:         0004-Use-relative-symbol-links.patch
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       inotify-tools
Requires:       polkit
Requires:       procps-ng
Requires:       rpmdevtools
Requires:       rpm-build
Requires:       sudo
Requires:       dnf
Requires:       zenity
Requires:      python3-gobject-base
# oreon:deps
BuildRequires:  appdata-tools
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
lpf (Local Package Factory) is designed to handle two separate
problems:
 - Packages built from sources which does not allow redistribution.
 - Packages requiring user to accept EULA-like terms.

It works by downloading sources, possibly requiring a user to accept
license terms and then building and installing rpm package(s) locally.
Besides being interactive the operation is similar to akmod and dkms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
#-n lpf-%%{commit}

# Create a sysusers.d config file
cat >lpf.sysusers.conf <<EOF
u pkg-build - 'lpf local package build user' /var/lib/lpf -
EOF

%build

%install
make DESTDIR=%{buildroot} install
desktop-file-validate %{buildroot}%{_datadir}/applications/lpf.desktop
install -m0644 -D lpf.sysusers.conf %{buildroot}%{_sysusersdir}/lpf.conf
%oreon_autofiles main

%check

appstream-util validate-relax --nonet appdata/lpf-gui.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
