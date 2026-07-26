%global source0_hash d491fbd7f86b96999d749974726e64924d5a03fa6020fdf76325dea3bdab62bd

%global commit 98db2b43124e7d0873270675bc05f4f9f90f88e5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20170716

Name:		kscope
Summary: 	QT front-end to Cscope
Version:	1.9.4
Release:	46.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
# Source0:	http://download.sourceforge.net/kscope/%{name}-%{version}.tar.gz
Source0:	https://github.com/chaoys/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:	kscope.desktop
Patch0:		kscope-strings-conflict.patch
URL:		https://github.com/chaoys/kscope
BuildRequires:	desktop-file-utils, qt5-qtbase-devel, gettext, qscintilla-qt5-devel
BuildRequires:	glib2-devel
BuildRequires: make
Requires:	cscope, ctags, graphviz

%description
KScope is a QT5 front-end to Cscope. It provides a source-editing 
environment for large C projects, such as the Linux kernel.

KScope is by no means intended to be a replacement to any of the leading 
Linux/KDE IDEs, such as KDevelop. First of all, it is not an Integrated 
Development Environment: it does not provide the usual write/compile/debug 
cycle supported by most IDE's. Instead, KScope is focused on source 
editing and analysis. 

%package devel
Summary:	Development files for kscope
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for kscope.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .conflicts
sed -i 's|/usr/local|%{buildroot}%{_prefix}|g' config
for i in app/app.pro core/core.pro cscope/cscope.pro editor/editor.pro; do
	sed -i 's|/lib|/%{_lib}|g' $i
done

%build
%{qmake_qt5}
# not smp-safe
make

%install
make INSTALL_ROOT=%{buildroot}%{_prefix} install
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p app/images/kscope.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%ldconfig_scriptlets

%files
%doc COPYING
%{_bindir}/kscopeapp
%{_libdir}/libkscope_core.so.*
%{_libdir}/libkscope_cscope.so.*
%{_libdir}/libkscope_editor.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/kscope.png

%files devel
%{_libdir}/libkscope_core.so
%{_libdir}/libkscope_cscope.so
%{_libdir}/libkscope_editor.so

%changelog
%autochangelog
