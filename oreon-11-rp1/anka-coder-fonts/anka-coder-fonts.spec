%global source0_hash 6a133aaad52a10617197f8b74c9f58a84190319690f27cb39bf3e759ae6c2e1e

%global fontname anka-coder
%global fontconf 65-%{fontname}
%global hgrev 4348cf4ec395

%global common_desc \
The Anka/Coder family is a mono spaced, courier-width (60% of height; em size \
2048x1229) font that contains characters from 437, 866, 1251, 1252 and some \
other code pages and can be used for source code, terminal windows etc. \
There are 3 font sets (regular. italic, bold, bold-italic each): 1. \
Anka/Coder (em size 2048x1229) 2. Anka/Coder Condensed (condensed by \
12.5%; em size 2048x1075) 3. Anka/Coder Narrow (condensed by 25%; em \
size 2048x922)

Name:           %{fontname}-fonts
Version:        1.100
Release:        0.27.20130409hg%{hgrev}%{?dist}
Summary:        A mono spaced, courier-width font

License:        OFL-1.1
URL:            http://code.google.com/p/anka-coder-fonts/

# Generated from an hg clone since sfd sources were available
# hg clone https://code.google.com/p/anka-coder-fonts/
# tar -cvzf anka-coder-fonts-20130409-hg.tar.gz --exclude="\.hg" anka-coder-fonts/
Source0:        anka-coder-fonts-20130409-hg.tar.gz
Source1:        %{name}-norm.conf
Source2:        %{name}-condensed.conf
Source3:        %{name}-narrow.conf
Source4:        %{fontname}.metainfo.xml
Source5:        %{fontname}-condensed.metainfo.xml
Source6:        %{fontname}-narrow.metainfo.xml
Source7:        %{fontname}-norm.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Requires:       fontpackages-filesystem

%description
%common_desc

%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-norm-fonts
Summary:        Normal version of %{name}
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-norm-fonts
%common_desc

"Anka/Coder Norm" simply supplements the family. 

%_font_pkg -n norm -f %{fontconf}-norm.conf AnkaCoder-b.ttf AnkaCoder-bi.ttf AnkaCoder-i.ttf AnkaCoder-r.ttf
%doc AnkaCoder-b-sample.pdf AnkaCoder-bi-sample.pdf AnkaCoder-i-sample.pdf AnkaCoder-r-sample.pdf
%{_datadir}/appdata/%{fontname}-norm.metainfo.xml

# Repeat for every font family ➅
%package -n %{fontname}-condensed-fonts
Summary:        Condensed version of %{name}
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-condensed-fonts
%common_desc

"Anka/Coder Condensed" can be used for both printing and screen 
viewing of source code, also as for displaying terminal windows.

%_font_pkg -n condensed -f %{fontconf}-condensed.conf AnkaCoder-C87*.ttf
%doc AnkaCoder-C87-b-sample.pdf AnkaCoder-C87-bi-sample.pdf AnkaCoder-C87-i-sample.pdf AnkaCoder-C87-r-sample.pdf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml

%package -n %{fontname}-narrow-fonts
Summary:        Narrow version of %{name}
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-narrow-fonts
%common_desc

"Anka/Coder Narrow" was developed for printing of source code; it \
is too tight for screen resolution.

%_font_pkg -n narrow -f %{fontconf}-narrow.conf AnkaCoder-C75*.ttf
%doc AnkaCoder-C75-b-sample.pdf AnkaCoder-C75-bi-sample.pdf AnkaCoder-C75-i-sample.pdf AnkaCoder-C75-r-sample.pdf
%{_datadir}/appdata/%{fontname}-narrow.metainfo.xml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}

%build
for family in "AnkaCoder" "AnkaCoder Condensed" "AnkaCoder Narrow"
do
pushd "$family"
fontforge -lang=ff -script "-" *.sfd <<EOF
i = 1 
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5) 
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
EOF
mv *.ttf ../ -v
mv *.pdf ../ -v
popd
done

sed -i 's/\r//' AnkaCoder/OFL.txt

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-norm.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-narrow.conf

mkdir -p %{buildroot}/%{_datadir}/appdata/
cp %{SOURCE4} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE5} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE6} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE7} %{buildroot}/%{_datadir}/appdata/  -v

for fconf in %{fontconf}-norm.conf \
             %{fontconf}-condensed.conf \
             %{fontconf}-narrow.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%files common
%license AnkaCoder/OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
%autochangelog
