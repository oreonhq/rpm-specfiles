%global source0_hash 60bd1369d4c347e127886a5813af13daf39b56ce818c9f8b2fc7d4bba0af7e11

Name: inksmoto
Version: 0.7.0
Release: 38%{?dist}
Summary: The new xmoto level editor for Inkscape

License: GPL-2.0-only
URL: http://xmoto.sourceforge.net/
Source0: http://download.tuxfamily.org/xmoto/svg2lvl/%{version}~rc1/inksmoto-%{version}.tar.gz       
BuildRequires: python3-devel
Requires: xmoto, inkscape, python3-lxml, python3-gobject
BuildArch: noarch

Patch0: inksmoto-0.7.0-pypath.patch
Patch1: inksmoto-python3.patch

%description
Inksmoto Level Editor is the new xmoto level editor. It uses Inkscape to
draw levels, then it allows you to save your drawing as a xmoto level
(.lvl file). It also allow you to edit xmoto level properties from 
within Inkscape such as make background block, strawberries, ...

Inksmoto Level Editor is written in Python, it's an Inkscape extension. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn extensions

%patch -P0 -p0
%patch -P1 -p1

%build
%py3_shebang_fix .

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
rm -f bezmisc.py
rm -f inkex.py
cp -p *.inx *.py %{buildroot}%{_datadir}/inkscape/extensions/
chmod 644 %{buildroot}%{_datadir}/inkscape/extensions/*
cp -pr inksmoto %{buildroot}%{_datadir}/inkscape/extensions/

%files
%{_datadir}/inkscape/extensions/*
%license COPYING
%doc AUTHORS INSTALL README

%changelog
%autochangelog
