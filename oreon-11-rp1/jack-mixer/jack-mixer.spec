%global source0_hash 0d68abe234256ec08dc7e728d2b5282956f103521620136825fd5326b4ab5238
Name:           jack-mixer
Version:        14
Release:        1%{?dist}
Summary:        JACK Audio Mixer
License:        GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            https://rdio.space/jackmixer/
Source0:        https://github.com/%{name}/jack_mixer/archive/release-%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    armv7hl
ExcludeArch:    i686
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(pygobject)
# /oreon:deps
%description
jack_mixer is an audio mixer for JACK with a look similar to its hardware
counterparts. Many features are available, here is a short list:

 - Mix any number of input channels (mono or stereo).
 - Control balance and faders with MIDI commands.
 - Handle session management with LASH.
 - Create as many outputs as necessary.
 - Quickly monitor inputs (PFL) and outputs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n jack_mixer-release-%{version}

%build

NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
%install
%make_install
rm %{buildroot}%{python3_sitelib}/jack_mixer_c.la
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}
desktop-file-validate %{buildroot}%{_datadir}/applications/jack_mixer.desktop
%py3_shebang_fix %{buildroot}%{_bindir}/jack_mixer.py
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
