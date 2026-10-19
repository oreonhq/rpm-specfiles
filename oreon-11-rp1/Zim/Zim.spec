%global source0_hash 5561bed05a5fe4208da2ef8d5f8747ebc49e8cb32b46df2559cc73fb11fa65eb
Name:           Zim
Version:        0.77.2
Release:        1%{?dist}
Summary:        Desktop wiki & notekeeper
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            http://zim-wiki.org/
Source0:        http://www.zim-wiki.org/downloads/zim-%{version}.tar.gz
Patch:          0000-Disable-TestPlugins-test.patch
Patch:          https://github.com/zim-desktop-wiki/zim-desktop-wiki/pull/2859.patch
BuildArch:      noarch
Requires:       python3-gobject
Requires:       gtk3, python3-pyxdg
Recommends:     libappindicator-gtk3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-Zim = %{version}-%{release}
# /oreon:deps
%description
Zim is a WYSIWYG text editor written in Python which aims to bring the
concept of a wiki to your desktop. Every page is saved as a text file with
wiki markup. Pages can contain links to other pages, and are saved
automatically. Creating a new page is as easy as linking to a non-existing
page. Pages are ordered in a hierarchical structure that gives it the look
and feel of an outliner. This tool is intended to keep track of TODO lists
or to serve as a personal scratch book.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir zim-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%find_lang zim
cat zim.lang >> %{pyproject_files}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zim_wiki.Zim.desktop
%oreon_autofiles main

%check

LANG=en_US.UTF-8 xvfb-run ./test.py
%files

%changelog

%autochangelog
