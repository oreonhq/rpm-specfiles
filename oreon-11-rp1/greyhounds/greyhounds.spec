%global source0_hash 233d7960034b0acf36701f2ccbe0a203cf6a09bc79f0915c719da69f2a751cdd

Name:           greyhounds
Version:        0.8
Release:        0.46.prealpha%{?dist}
Summary:        Greyhounds is a greyhounds racing and breeding game
Summary(pl):    Greyhounds to wyścigi i hodowla chartów
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://sourceforge.net/projects/byghound
Source0:        http://downloads.sourceforge.net/byghound/%{name}-%{version}-pre-alpha.tar.bz2
Source1:        %{name}.desktop
# Patch 0 should go upstrem
Patch0:		greyhound-am.patch
Patch1:		greyhound-in.patch
Patch2:		greyhound-save.patch
Patch3:		greyhound-gcc10.patch
Patch4:		greyhound-names.patch
Patch5:		greyhounds-configure-c99.patch
Patch6:		greyhounds-c99-headers.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils gtk2-devel ImageMagick
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Greyhounds is a greyhound racing and breeding game. Your goal is to
acquire fast and talented greyhounds and be successful with them in the
races; your two possibilities for doing so are breeding and trading.
Ultimately you should aim at winning the Champions' Trophy. You might
also consider establishing a record that lasts to the end of times a
worthy goal.

%description -l pl
Greyhounds to wyścigi i hodowla chartów. Twoim zadaniem jest zdobyć szybkie
i utalentowane charty i być zadowolonym z ich wyścigów; twoimi dwiema
możliwościami są hodowanie i handlowanie. Ostatecznie powinineś dążyć do
wygraia mistrzowskiego trofeum. Możesz również osiągać nowe rekordy
czasowe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-pre-alpha
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P4
%patch -P5 -p1
%patch -P6 -p1

# Create icons and make appropriate dir structure
mkdir icons
for size in 16 22 24 32 36 48; do
  mkdir -p icons/${size}x${size}/apps
  convert pixmaps/logo.xpm -resize ${size}x${size} icons/${size}x${size}/apps/%{name}.png
done

# Convert doc to UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 README > README.utf8
mv README.utf8 README

iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.utf8
mv AUTHORS.utf8 AUTHORS

%build

%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor
cp -pr icons/*x* $RPM_BUILD_ROOT%{_datadir}/icons/hicolor

# Desktop file
desktop-file-install                                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
