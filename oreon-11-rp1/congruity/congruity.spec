%global source0_hash c5217861fd18c2c0fd1dfe8c8e6f66566a5f947930dd1b60cf261fffb8278586

Name:		congruity
Version:	21
Release:	16%{?dist}
Summary:	Applications to program Logitech Harmony universal remote controls

# Code is GPLv3+, icons are the other two licenses
License:	GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-1.0-or-later
URL:		https://sourceforge.net/projects/congruity
Source0:	https://downloads.sourceforge.net/congruity/%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
Requires:	python3-wxpython4
Requires:	python3-libconcord
# For mhgui
Requires:	python3-suds

%description
congruity is a GUI application for programming Logitech Harmony universal
remote controls. congruity builds upon the work of libconcord, which
provides the underlying communication.

congruity is configured to handle the configuration files downloaded
from the Logitech configuration website. After installing this package
you can just use the Logitech configuration website and congruity will
launch automatically when appropriate.

A tool called 'mhgui' is also included for configuring remotes that only
work through the myharmony.com website, which does not work with Linux.
This includes the Harmony 200 and Harmony 300. To use it, simply run
'mhgui' and follow the prompts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files congruity
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mhgui.desktop

%files -f %{pyproject_files}
%doc Changelog COPYING README.txt
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/mhgui.desktop
%{_mandir}/*/*

%changelog
%autochangelog
