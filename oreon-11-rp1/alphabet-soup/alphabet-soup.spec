%global source0_hash 195d90145958ede4a0638df4dec47c091ffce12e2d7270a95e974a6c5f7d59de

Name:           alphabet-soup
Version:        1.1
Release:        43%{?dist}
Summary:        Guide your worm through the soup to spell words
# Automatically converted from old format: Crystal Stacker - review is highly recommended.
License:        CrystalStacker
URL:            http://www.t3-i.com/asoup.htm
Source0:        http://www.t3-i.com/ncdgames/as11src.zip
Source1:        alphabet-soup.desktop
Source2:        alphabet-soup.png
Patch0:         alphabet-soup-1.1-linux.patch
Patch1:         alphabet-soup-1.1-rhbz699425.patch
BuildRequires:  gcc
BuildRequires:  alfont-devel dumb-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Guide your worm through the soup to spell words and earn points. Play the way
you like with several game mode selections. Words are chosen from one of three
included dictionaries, or import your own.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p1 -z .unix
%patch -P1 -p1
sed -i 's/\r//' readme.txt

%build
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -DALLEGRO_FIX_ALIASES"

%install
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

%files
%doc readme.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
%autochangelog
