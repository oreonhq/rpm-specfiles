%global source3_hash 357cb1abd314537cf3840419e852464256a890c3714f6fde51339d957210769f
%global source2_hash d5455d2e5990b16fc319e7493608abf297dac7321c8b4532ac7522cb85c04f5e
%global source1_hash 0e882e762db072ca759204259104500d129a28a85514e2c67555b29a244e3a6b
%global source0_hash 2db193554b355d747e41f0e10b15fd50c910ddb9e4e33d1c925f780b0c1ef484
Name:           atari++
Version:        1.85
Release:        1%{?dist}
Summary:        Unix based emulator of the Atari 8-bit computers
License:        TPL-1.0
URL:            http://www.xl-project.com/
Source0:        http://www.xl-project.com/download/%{name}_%{version}.tar.gz
Source1:        http://www.xl-project.com/download/os++doc.pdf
Source2:        http://www.xl-project.com/download/basic++doc.pdf
Source3:        http://www.xl-project.com/download/system.atr
Source4:        %{name}.desktop
Source5:        atari2.svg
Patch1:         %{name}-verbose.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
rm -rf %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications           \
        %{SOURCE4}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
