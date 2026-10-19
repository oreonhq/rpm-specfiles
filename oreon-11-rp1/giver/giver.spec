%global source0_hash 0fe08f6c08896029b859bcf66720b50013a1e1a672141a782667db6c9d889b8d
%global debug_package %{nil}
Name:		giver
Summary:        A simple file sharing desktop application
Version:	0.1.8
Release:        42%{?dist}
License:	MIT
Source0:        http://giver.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	Giver.exe.config
Patch0:		giver-0.1.8-fix-desktop-file.patch
Patch1:		giver-0.1.8-username_face.patch
Patch2:		giver-0.1.8-photoButtonFix2.patch
URL:		http://code.google.com/p/giver/
Requires:	notify-sharp gtk-sharp2 gnome-sharp avahi-sharp
ExclusiveArch:	%{mono_arches}
# oreon:deps
BuildRequires:  avahi-sharp
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnome-sharp-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  notify-sharp-devel
# /oreon:deps
%description
Giver is a simple file sharing desktop application. Other people running Giver 
on your network are automatically discovered and you can send files to them by 
simply dragging the files to their photo or icon shown in Giver. There is no 
knowledge or set up needed beyond what the person looks like or their name to 
use Giver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix-desktop
%patch -P1 -p1 -b .username_face
%patch -P2 -p1 -b .photoButtonFix

sed -i "s#gmcs#mcs#g" src/Makefile.*
sed -i "s#gmcs#mcs#g" configure*

%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/%{name}/
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
