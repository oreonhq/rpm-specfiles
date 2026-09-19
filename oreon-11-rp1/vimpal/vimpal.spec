%global source0_hash 58f7f604ec92bb09e1eea2768fbc455f899b821b029f5ff02b895b93c04f3521

Name:		vimpal		
Version:	1.5.0
Release:	27%{?dist}
Summary:	Separate application providing a file tree for VIM
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://vimpal.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}_%{version}.tar.gz
Source1:	vimpal.desktop
BuildRequires: make
BuildRequires:	qt-devel
BuildRequires:	desktop-file-utils
Requires:	vim-X11

%description
Simple and small application that can be used to select the files you want
to edit in Vim.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_%{version}
# I provide an icon without a name so generic
cp -p img/icon.png img/vimpal.png

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}/
install -pm 0755 vimpal %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -pm 0644 img/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}

%files
%doc README gpl.txt
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
