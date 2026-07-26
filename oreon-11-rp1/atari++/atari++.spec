%global source0_hash 2db193554b355d747e41f0e10b15fd50c910ddb9e4e33d1c925f780b0c1ef484

Name:           atari++
Version:        1.85
Release:        11%{?dist}
Summary:        Unix based emulator of the Atari 8-bit computers

# Automatically converted from old format: TPL - review is highly recommended.
License:        TPL-1.0
URL:            http://www.xl-project.com/
Source0:        http://www.xl-project.com/download/%{name}_%{version}.tar.gz
Source1:        http://www.xl-project.com/download/os++doc.pdf
Source2:        http://www.xl-project.com/download/basic++doc.pdf
Source3:        http://www.xl-project.com/download/system.atr
Source4:        %{name}.desktop
# borrowed from atari800 project
Source5:        atari2.svg
# be verbose during compile
Patch1:         %{name}-verbose.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  zlib-devel
BuildRequires:  ncurses-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make

%description
The Atari++ Emulator is a Unix based emulator of the Atari 8-bit
computers, namely the Atari 400 and 800, the Atari 400XL, 800XL and 130XE,
and the Atari 5200 game console. The emulator is auto-configurable and
will compile on a variety of systems (Linux, Solaris, Irix).
Atari++ 1.30 and up contain a built-in ROM emulation that tries to mimic
the AtariXL operating system closely.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

# fix encoding
f=README.History
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

# fix permissions for sources
chmod a-x *.cpp *.hpp

# additional docs
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
%configure
%{make_build} OPTIMIZER="%{build_cflags} -DDEBUG_LEVEL=0 -DCHECK_LEVEL=0" LDFLAGS="%{build_ldflags} -lSDL"

%install
make install DESTDIR=%{buildroot}

# remove installed docs
rm -rf %{buildroot}%{_docdir}/%{name}

# install system disk into %%_datadir
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}

# install icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps

# desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications           \
        %{SOURCE4}

%files
%license COPYRIGHT README.licence
%doc CREDITS README.LEGAL README.History manual
%doc os++doc.pdf basic++doc.pdf
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/atari2.svg
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
