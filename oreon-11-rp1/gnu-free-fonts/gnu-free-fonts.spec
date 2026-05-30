%global source0_hash 0d62e2e22655f841c3ac5fb8c8059a52fe2c09c695d9e8eda9903406e942657a

%global fontname gnu-free
%global fontconf 69-%{fontname}

Name:      %{fontname}-fonts
Version:   20120503
Release:   38%{?dist}
Summary:   Free UCS Outline Fonts

License:   GPL-3.0-or-later WITH Font-exception-2.0
URL:       http://www.gnu.org/software/freefont/ 
Source0:        http://ftp.gnu.org/gnu/freefont/freefont-src-%{version}.tar.gz
Source2:   %{fontconf}-mono.conf
Source3:   %{fontconf}-sans.conf
Source4:   %{fontconf}-serif.conf
Source5:   %{fontname}.metainfo.xml
Source6:   %{fontname}-mono.metainfo.xml
Source7:   %{fontname}-sans.metainfo.xml
Source8:   %{fontname}-serif.metainfo.xml

Patch0:    gnu-free-fonts-devanagari-rendering.patch
Patch1:    gnu-free-sans-square-dot-glyph-fix.patch
Patch2:    python3.patch
Patch3:    hints.patch

BuildArch: noarch
BuildRequires: make
BuildRequires: fontpackages-devel fontforge

%global common_desc \
Gnu FreeFont is a free family of scalable outline fonts, suitable for general \
use on computers and for desktop publishing. It is Unicode-encoded for \
compatibility with all modern operating systems. \
 \
Besides a full set of characters for writing systems based on the Latin \
alphabet, FreeFont contains large selection of characters from other writing \
systems some of which are hard to find elsewhere. \
 \
FreeFont also contains a large set of symbol characters, both technical and \
decorative. We are especially pleased with the Mathematical Operators range, \
with which most of the glyphs used in LaTeX can be displayed.

%description
%common_desc


%package common
Summary:  Common files for freefont (documentation…)
Requires: fontpackages-filesystem
Obsoletes: gnu-free-fonts-compat < 20120503

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-mono-fonts
Summary:  GNU FreeFont Monospaced Font
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-mono-fonts
%common_desc

This package contains the GNU FreeFont monospaced font.


%package -n %{fontname}-sans-fonts
Summary:  GNU FreeFont Sans-Serif Font
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This package contains the GNU FreeFont sans-serif font.


%package -n %{fontname}-serif-fonts
Summary:  GNU FreeFont Serif Font
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This package contains the GNU FreeFont serif font.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n freefont-%{version} -p1

# Following for loop should not be used on pyc files
# better remove pre-compiled buildutils.pyc file
rm tools/generate/*.pyc

%build
make

%install
pushd sfd
install -m 0755 -d %{buildroot}%{_fontdir}
install -p -m 644 *.ttf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf


for fconf in %{fontconf}-mono.conf \
                %{fontconf}-sans.conf \
                %{fontconf}-serif.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%_font_pkg -n mono -f %{fontconf}-mono.conf FreeMono*.ttf
%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
%_font_pkg -n sans -f %{fontconf}-sans.conf FreeSans*.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
%_font_pkg -n serif -f %{fontconf}-serif.conf FreeSerif*.ttf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%files common
%doc AUTHORS ChangeLog CREDITS README
%license COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20120503-38
- Prepare for Oreon 11 (RP1)
