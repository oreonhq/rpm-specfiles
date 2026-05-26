Name: sound-theme-freedesktop
Version: 0.8
Release: %autorelease
Summary: freedesktop.org sound theme
Source0: http://people.freedesktop.org/~mccann/dist/sound-theme-freedesktop-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 cb518b20eef05ec2e82dda1fa89a292c1760dc023aba91b8aa69bafac85e8a14
%global source0_file sound-theme-freedesktop-0.8.tar.bz2
# oreon url source checksums end
# For details on the licenses used, see CREDITS
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later AND CC-BY-SA-3.0 AND CC-BY-3.0 AND CC-BY-4.0
Url: http://www.freedesktop.org/wiki/Specifications/sound-theme-spec
BuildArch: noarch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: gettext
BuildRequires: intltool >= 0.40
Requires(post): coreutils
Requires(postun): coreutils

%description
The default freedesktop.org sound theme following the XDG theming
specification.  (http://0pointer.de/public/sound-theme-spec.html).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sound-theme-freedesktop-0.8.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cb518b20eef05ec2e82dda1fa89a292c1760dc023aba91b8aa69bafac85e8a14" || { echo "oreon: Source0 SHA256 mismatch for sound-theme-freedesktop-0.8.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure

%install
%make_install

%post
touch --no-create %{_datadir}/sounds/freedesktop %{_datadir}/sounds

%postun
touch --no-create %{_datadir}/sounds/freedesktop %{_datadir}/sounds

%files
%doc README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-1
- Prepare for Oreon 11 (RP1)
