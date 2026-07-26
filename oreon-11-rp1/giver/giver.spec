%global source0_hash 0fe08f6c08896029b859bcf66720b50013a1e1a672141a782667db6c9d889b8d

# Like most mono packages, giver doesn't generate any debuginfo
%global debug_package %{nil}

Name:		giver
Summary: 	A simple file sharing desktop application
Version:	0.1.8
Release:	42%{?dist}
License:	MIT
Source0:	http://giver.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	Giver.exe.config
Patch0:		giver-0.1.8-fix-desktop-file.patch
# From: http://code.google.com/p/giver/issues/detail?id=2
Patch1:		giver-0.1.8-username_face.patch
# Sent a clean version of this patch to:
# http://code.google.com/p/giver/issues/detail?id=4
# This patch applies on top of the username_face patch.
Patch2:		giver-0.1.8-photoButtonFix2.patch
URL:		http://code.google.com/p/giver/
BuildRequires:  gcc
BuildRequires:	gnome-sharp-devel, gtk-sharp2-devel, notify-sharp-devel
# This really should be avahi-sharp-devel, but it is mispackaged
BuildRequires:  avahi-sharp
BuildRequires:	desktop-file-utils, intltool
BuildRequires: make
Requires:	notify-sharp gtk-sharp2 gnome-sharp avahi-sharp

# Mono available only on selected arches
ExclusiveArch:	%{mono_arches}

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

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.png

%changelog
%autochangelog
