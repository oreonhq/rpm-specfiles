%global source0_hash 59953c996aa057146d4ccb7697d846dad87c3e7c4e3b05eeea6f47f3837a64fc

Name:		jack-keyboard
Version:	2.7.2
Release:	15%{?dist}
Summary:	Virtual keyboard for JACK MIDI
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://sourceforge.net/projects/jack-keyboard/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Icon is derived from the image on the website:
Source1:	%{name}.png
# Upstreamable patch. Fix DSO linking
Patch0:		%{name}-dso-linking.patch
# cmake should look for gcc only
Patch1:		jack-keyboard-cproject.patch
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gtk2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lash-devel

%description
jack-keyboard is a virtual MIDI keyboard - a program that allows you to send
JACK MIDI events using your PC keyboard. It is somewhat similar to vkeybd,
except it uses JACK MIDI instead of ALSA, and the default keyboard mapping is
much better - it uses the same layout as trackers (like Impulse Tracker) did,
so you have two and half octaves under your fingers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .dso.linking
%patch -P1 -p1 -b .cproject

# Add GenericName to the desktop file
echo "GenericName=Virtual MIDI Keyboard" >> src/%{name}.desktop

# Fix man dir
sed -i 's|man/man1|%{_mandir}/man1|' CMakeLists.txt

%build
# TODO: Please submit an issue to upstream (rhbz#2380659)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

rm -fr $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/72x72/apps/
install -pm 644	%{SOURCE1} \
	$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/72x72/apps/

desktop-file-install						\
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications		\
	--add-category=X-Jack					\
	$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS NEWS README.md TODO
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/icons/hicolor/72x72/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
