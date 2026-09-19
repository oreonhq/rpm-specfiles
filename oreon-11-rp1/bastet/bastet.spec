%global source0_hash b89fd3a7401578b7787a80d19695001e812810fa0075c075e8add46070563e5a

Name:		bastet
Version:	0.43.2
Release:	15%{?dist}
Summary:	An evil falling bricks game

License:	GPL-3.0-or-later
URL:		https://github.com/fph/bastet
Source0:	https://github.com/fph/bastet/archive/%{version}.zip
Source1:	%{name}.desktop
# self-made icon
Source2:	%{name}.png
Patch0:		bastet-tr1.patch
Patch1:         bastet-fmt-str.patch

BuildRequires:  gcc-c++
BuildRequires:	boost-devel ncurses-devel desktop-file-utils
BuildRequires: make

%description
Bastet is a simple ncurses-based falling bricks like game. Unlike 
normal, however, Bastet does not choose your next brick at random. 
Instead, it uses a special algorithm designed to choose the worst 
brick possible. As you can imagine, playing Bastet can be a very 
frustrating experience!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1
%patch -P1 -p0

# remove reference to Tetris to match our guidelines
sed -e 's/Tetris(R)/any falling bricks game/g' -e 's/Tetris/falling bricks game/g' \
-e 's/tetris/falling bricks game/g' README > README.new
mv -f README.new README
# remove also any reference to Tetris in the bastet manpage
sed -e 's/Tetris(r)/any falling bricks game/g' -e 's/tetris/falling bricks game/g' \
bastet.6 > bastet.6.new
mv -f bastet.6.new bastet.6

%build

make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

# install the AppData file
%__mkdir_p %{buildroot}%{_datadir}/appdata
cp bastet.appdata.xml %{buildroot}%{_datadir}/appdata/

mkdir -p %{buildroot}%{_bindir}

install -p -m 755 bastet %{buildroot}%{_bindir}/bastet

# below the desktop file and icon stuff
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications	\
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2}				\
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# manpage
mkdir -p %{buildroot}%{_mandir}/man6/
      install -p -m 0644 %{name}.6 \
      %{buildroot}%{_mandir}/man6/%{name}.6

%files
%doc AUTHORS LICENSE NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*

%changelog
%autochangelog
