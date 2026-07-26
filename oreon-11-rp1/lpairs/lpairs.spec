%global source0_hash 57afe33d2a83229c3cff5efa6512fd2eeac4eacb92d37dd3070db6bbb024dc16

Name:           lpairs
Summary:        Classical memory game with cards
Version:        1.0.5
Release:        18%{?dist}
# Automatically converted from old format: GPLv2+ and CC-BY-SA and Freely redistributable without restriction - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Fedora-UltraPermissive
URL:            https://lgames.sourceforge.net/index.php?project=LPairs
Source0:        https://downloads.sourceforge.net/lgames/lpairs-%{version}.tar.gz
#there is a problem with data dir
#the author said it would be hard for him to fix it at autoconf level
Patch0:         lpairs-1.0.3-datadir.diff
Patch1:         lpairs-1.0.4-desktop.diff
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  SDL-devel
BuildRequires:  gettext
BuildRequires: make

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed
will be counted but there is no highscore chart or limit to this.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"

%configure inst_dir="%{_datadir}/%{name}"
make %{?_smp_mflags}

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} inst_dir="%{_datadir}/%{name}" install
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp lpairs.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        lpairs.desktop

%files -f %{name}.lang
%{_bindir}/lpairs
%{_datadir}/%{name}
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
