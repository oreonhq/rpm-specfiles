%global source2_hash 2f0ffb2588e8337ec05ab38d6671cad9409b567c21f0ad36989ff279bf43dc14
%global source0_hash cc8471b83f7ba7a754e1da0631cfa9c32b9217da93597afc1c3283e3a1ae4112
%global py_name Screenkey
Name:		screenkey
Version:	1.5
Release:        1%{?dist}
Summary:        A screencast tool to display your keys
License:	GPL-3.0-or-later
URL:		https://www.thregr.org/~wavexx/software/%{name}
Source0:        https://www.thregr.org/~wavexx/software/%{name}/releases/%{name}-%{version}.tar.gz
Source1:	%{URL}/releases/%{name}-%{version}.tar.gz.asc
Source2:	https://www.thregr.org/~wavexx/files/wavexx.asc
BuildArch:	noarch
Requires:   slop
Recommends: fontawesome-fonts
Recommends: libappindicator-gtk3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-screenkey = %{version}-%{release}
# /oreon:deps
%description
A screencast tool to display your keys, featuring:
* Several keyboard translation methods
* Key composition/input method support
* Configurable font/size/position
* Highlighting of recent keystrokes
* Improved backspace processing
* Normal/Emacs/Mac caps modes
* Multi-monitor support
* Dynamic recording control etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files

%changelog

%autochangelog
