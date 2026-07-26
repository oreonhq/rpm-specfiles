%global source0_hash 4b076736bb0566274e863d792edaf8bd0246e696f3195781113260b9ec8a1358

# Url to upstream GitHub repo.
%global git_url https://github.com/scummvm/%{name}

Name:		scummvm-tools
Version:	2.9.0
Release:	5%{?dist}
Summary:	Tools for scummVM / S.C.U.M.M scripting language
# All previous Lua versions are relicensed to MIT (https://www.lua.org/license.html)
# Automatically converted from old format: GPLv3+ and LGPLv2+ and MIT - review is highly recommended.
License:	GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND BSD-2-Clause
URL:		http://www.scummvm.org

Source0:	http://www.scummvm.org/frs/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch1:		configure.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	wxGTK-devel, libvorbis-devel, flac-devel, desktop-file-utils
BuildRequires:	zlib-devel bzip2-devel libmad-devel
BuildRequires:	libpng-devel freetype-devel boost-devel
Requires:	scummvm%{?_isa} >= %{version}
Provides:	bundled(lua) = 3.1

%description
This is a collection of various tools that may be useful to use in
conjunction with ScummVM.
Please note that although a tool may support a feature, certain ScummVM
versions may not. ScummVM 0.6.x does not support FLAC audio, for example.

Many games package together all their game data in a few big archive files.
The following tools can be used to extract these archives, and in some cases
are needed to make certain game versions usable with ScummVM.

The following tools can also be used to analyze the game scripts
(controlling the behavior of certain scenes and actors in a game).
These tools are most useful to developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
# The configure script shall ignore the parameter for the --host option
#passed by %%configure.
export CONFIGURE_NO_HOST=true

%configure --enable-verbose-build
%make_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%make_install
(cd ${RPM_BUILD_ROOT}%{_bindir} ; for i in `ls *|grep -v scummvm` ; do mv $i scummvm-$i ; done)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

%files
%license COPYING*
%doc README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
