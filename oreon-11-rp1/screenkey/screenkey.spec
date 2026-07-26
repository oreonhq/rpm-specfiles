%global source0_hash cc8471b83f7ba7a754e1da0631cfa9c32b9217da93597afc1c3283e3a1ae4112

%global py_name Screenkey
Name:		screenkey
Version:	1.5
Release:	17%{?dist}
Summary:	A screencast tool to display your keys
License:	GPL-3.0-or-later
URL:		https://www.thregr.org/~wavexx/software/%{name}
Source0:	%{URL}/releases/%{name}-%{version}.tar.gz
Source1:	%{URL}/releases/%{name}-%{version}.tar.gz.asc
Source2:	https://www.thregr.org/~wavexx/files/wavexx.asc

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-babel
BuildRequires:	desktop-file-utils

BuildRequires: gnupg2

Requires:   slop

Recommends: fontawesome-fonts
Recommends: libappindicator-gtk3

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

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{py_name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{pyproject_files}
%doc README.rst NEWS.rst
%license COPYING.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.thregr.%{name}.metainfo.xml

%changelog
%autochangelog
