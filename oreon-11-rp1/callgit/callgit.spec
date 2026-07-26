%global source0_hash 57c1721de1c724e531af10a14a43cc8e72c83f85c28f172414b745cf8b65bc84

Name:		callgit
Version:	2.0
Release:	39%{dist}
Summary:	A tool for Ham Radio Operators to look up call-signs on the web
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		http://www.hamsoftware.org/

Source0:	http://www.hamsoftware.org/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:    Ham_Icon-1-48.png

BuildRequires: qt-devel
BuildRequires: desktop-file-utils
BuildRequires: make

%description
This program allows you to search for another Ham's name and address
without having a web browser up. It is very simple.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
%{qmake_qt4}
%make_build

%install
install -Dpm 755 callgit %{buildroot}/%{_bindir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/Ham_Icon-1-48.png 

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/Ham_Icon-1-48.png

%changelog
%autochangelog
