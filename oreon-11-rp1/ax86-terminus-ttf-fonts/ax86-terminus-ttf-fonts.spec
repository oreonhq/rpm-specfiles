%global source0_hash 0ead921d98d99a4590ffe6cd66dc037fc0a2ceea1c735d866ba73fe058257577

Version: 4.49.3
Release: 6%{?dist}

URL: https://files.ax86.net/terminus-ttf

%global foundry  AX86
%global fontlicense  OFL-1.1
%global fontlicenses  COPYING

%global fontfamily  Terminus (TTF)
%global fontsummary  Terminus TTF is a monospace TrueType Font
%global fontdescription  %{expand:Terminus TTF is a TrueType 
version of Terminus Font, a fixed-width bitmap font optimized for 
long work with computers. If the application you want to use the font 
with supports the original Terminus Font, you should really use that one 
instead of this TTF version — it will most likely be a more pleasant 
experience for you. 

There are applications that neither support the original Terminus Font
nor use bitmaps embedded in TrueType fonts. They completely rely on the 
automatically generated scalable outlines.

When Terminus TTF is used with such applications, it will probably look
a little bit weird and not exactly like the original Terminus Font 
(since the generated outlines do not exactly match the bitmaps); you will 
see whether you like it or not. Because the outlines are scalable, it 
should not matter which size you use, but anything bigger than 32 px 
(24 pt) will probably not look very nice. 

It should also be noted that you need to render Terminus TTF in monochrome
black/white if the outlines are used; otherwise, they will look smeary.}

%global fonts  *.ttf
%global fontconfs  %{SOURCE10}

Source0: %{url}/files/%{version}/terminus-ttf-%{version}.zip 
Source10: 60-%{fontpkgname}.conf

BuildRequires:  fontforge

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n terminus-ttf-%{version}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
