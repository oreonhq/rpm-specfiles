%global source0_hash 44c4cf65d011d38e278e8f4d8e03e17ed1cfb7c76c33916f890a1f46d17de43b
Name:           kmid2
Version:        2.4.0
Release:        34%{?dist}
Summary:        A MIDI/karaoke player for KDE
License:        GPLv2+ and CC-BY-SA
URL:            http://userbase.kde.org/KMid2
Source0:        http://downloads.sourceforge.net/project/%{name}/%{version}/kmid-%{version}.tar.bz2
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api}}
%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}
Requires:       oxygen-icon-theme
Requires:       drumstick0 >= 0.4
Requires:       %{name}-libs = %{version}-%{release}
Obsoletes:      kmid < 2.0-1
Provides:       kmid = %{version}-%{release}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  drumstick0-devel
BuildRequires:  gettext
BuildRequires:  kde-filesystem
BuildRequires:  kdelibs4-devel
BuildRequires:  make
# /oreon:deps
%description
KMid2 is a MIDI/karaoke file player, with configurable midi mapper, real
Session Management, drag & drop, customizable fonts, etc. It has a very
nice interface which let you easily follow the tune while changing the
color of the lyrics.
It supports output through external synthesizers, AWE, FM and GUS cards.
It also has a keyboard view to see the notes played by each instrument.

%package libs
Summary:        Runtime libraries for %{name}
License:        GPL-2.0-or-later
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api}}
%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}
%description libs
%{summary}.

%package devel
Summary:        Development files for %{name}
License:        GPL-2.0-or-later
Requires:       %{name}-libs = %{version}-%{release}
Obsoletes:      kmid-devel < 2.0-1
Provides:       kmid-devel = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kmid-%{version}
# zap bundled copy of drumstick to guarantee it's never used
rm -rf drumstick

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kmid.desktop
%find_lang kmid --with-kde
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kmid2-libs -f %{oreon_filedir}/kmid2-libs.list
%files -n kmid2-devel -f %{oreon_filedir}/kmid2-devel.list

%changelog

%autochangelog
