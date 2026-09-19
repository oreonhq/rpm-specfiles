%global source0_hash eb702a789998d4ea3d58b3ddf5b94fe6edff99663f0385613ce1646177f62846

%global commit f9032ddd26ffb33fd140e0b9d5ee72c445608077
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210927
#%%global rel .%%{gitdate}.%%{shortcommit}

Name:           lpf
Version:        0.3
Release:        15%{?rel}%{?dist}
Summary:        Local package factory - build non-redistributable rpms

# Icon from iconarchive.com
License:        MIT
URL:            https://github.com/sergiomb2/lpf
#Source0:        %%{url}/archive/%%{commit}/lpf-%%{version}%%{?rel}.tar.gz
Source0:        %{url}/archive/v%{version}/lpf-%{version}%{?rel}.tar.gz
Patch1:         https://github.com/sergiomb2/lpf/commit/4f414697e6977da5fdeff7632ec3ea86ffdfbdfb.patch
Patch3:         0003-Remove-option-allowerasing-of-dnf-install.patch
Patch4:         0004-Use-relative-symbol-links.patch

BuildArch:      noarch

BuildRequires:  appdata-tools
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       hicolor-icon-theme
Requires:       inotify-tools
Requires:       polkit
Requires:       procps-ng
Requires:       rpmdevtools
Requires:       rpm-build
Requires:       sudo
Requires:       dnf
Requires:       zenity
#for lpf-gui
Requires:      python3-gobject-base

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

%check
appstream-util validate-relax --nonet appdata/lpf-gui.appdata.xml

%files
%doc README.md LICENSE
%{_bindir}/lpf
%{_bindir}/lpf-gui
%{_rpmconfigdir}/macros.d/macros.lpf
%{_datadir}/lpf
%{_datadir}/applications/lpf.desktop
%{_datadir}/applications/lpf-gui.desktop
%{_datadir}/applications/lpf-notify.desktop
%{_datadir}/icons/hicolor/*/apps/lpf*.png
%{_datadir}/appdata/lpf-gui.appdata.xml
%{_datadir}/man/man1/lpf*
%{_libexecdir}/lpf-kill-pgroup
%attr(440, root, root) %config(noreplace) %{_sysconfdir}/sudoers.d/pkg-build
%attr(2775, pkg-build, pkg-build)/var/lib/lpf
%{_sysusersdir}/lpf.conf

%changelog
%autochangelog
