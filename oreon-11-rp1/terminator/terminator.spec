%global source2_hash d0a1f6bf8125b97a894ac31329e32a53b03b6a90b09cd90be7317e179224f41d
%global source1_hash 4906de3e0a986d29d0258721fa3d41b99d7f8d59f7225b473883b5f5a152bbd3
%global source0_hash f0219cd8bd3db45d5173d850619145d55f9e864fe2106f6ceb9e736c575d0e03
Name:           terminator
Version:        2.1.5
Release:        4%{?dist}
Summary:        Store and run multiple GNOME terminals in one window
License:        GPL-2.0-only
URL:            https://github.com/gnome-terminator
Source0:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/terminator-%{version}.tar.gz
Source1:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/terminator-%{version}.tar.gz.asc
Source2:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/gpg-D11A7596F61705480C711598F2FAC7C7BAE930A5.asc
BuildArch:      noarch
Requires:       keybinder3
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       vte291
Patch0:         0000-terminator-fix-desktop-file.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-terminator = %{version}-%{release}
# /oreon:deps
%description
Multiple GNOME terminals in one window.  This is a project to produce
an efficient way of filling a large area of screen space with
terminals. This is done by splitting the window into a resizeable
grid of terminals. As such, you can  produce a very flexible
arrangements of terminals for different tasks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%pyproject_wheel 
%install
%pyproject_install
%find_lang %{name}
%oreon_autofiles main

%check

%py3_check_import terminatorlib
desktop-file-validate %{buildroot}%{_datadir}/applications/terminator.desktop
%files

%changelog

%autochangelog
