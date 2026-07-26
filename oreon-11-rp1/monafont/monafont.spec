%global source0_hash 26e608598edb2c9f1a662acd8bf4e06dc75910a69fc76698e4e062113a401978

%{!?_fontbasedir: %global _fontbasedir %{_datadir}/fonts}

%define		archivename		monafont

%define		projectname		mona
%define		fontname		%{projectname}
%define		family_ttf_s		sazanami
%if 0%{?fedora} >= 38
%define		family_ttf_s_dir	%{_fontbasedir}/%{family_ttf_s}-gothic-fonts
%else
%define		family_ttf_s_dir	%{_fontbasedir}/%{family_ttf_s}
%endif
%define		family_ttf_v		vlgothic
%if 0%{?fedora} >= 37
%define		family_ttf_vp		vl-pgothic
%define		family_ttf_vp_dir	%{_fontbasedir}/%{family_ttf_vp}-fonts
%else
%define		family_ttf_vp		vlgothic-p
%define		family_ttf_vp_dir	%{_fontbasedir}/vlgothic
%endif
%define		real_family_ttf_s	sazanami
%define		real_family_ttf_v	VLGothic

%define		rpmname_suffix	fonts

%define		fontdir_bitmap	%{projectname}-bitmap
%define		fontdir_ttf_s		%{projectname}-%{family_ttf_s}
%define		fontdir_ttf_v		%{projectname}-%{family_ttf_v}

%define		name_bitmap		%{fontdir_bitmap}-%{rpmname_suffix}
%define		name_ttf_s		%{fontdir_ttf_s}-%{rpmname_suffix}
%define		name_ttf_v		%{fontdir_ttf_v}-%{rpmname_suffix}

%define		old_name_bitmap	mona-fonts-bitmap
%define		old_name_ttf_s	mona-fonts-sazanami
%define		old_name_ttf_v	mona-fonts-VLGothic

%define		fontdir_bitmap_full	%{_fontbasedir}/%{fontdir_bitmap}
%define		fontdir_ttf_s_full	%{_fontbasedir}/%{fontdir_ttf_s}
%define		fontdir_ttf_v_full	%{_fontbasedir}/%{fontdir_ttf_v}

%define		obsoletes_EVR		2.90-5.999
%define		sazanami_ver		20040629
%define		vlgothic_ver		20230918

%define		catalog_dir		%{_sysconfdir}/X11/fontpath.d

# misc
%define		show_progress		0

%define	common_description	\
Mona Font is a Japanese proportional font which allows you to view \
Japanese text arts correctly.

Name:		%{archivename}
Version:	2.90
Release:	44%{?dist}
Summary:	Japanese font for text arts

# monafont itself is under public domain
# Automatically converted from old format: Public Domain - review is highly recommended.
License:	LicenseRef-Callaway-Public-Domain
URL:		http://monafont.sourceforge.net/
Source0:	http://downloads.sourceforge.net/monafont/%{archivename}-%{version}.tar.bz2

# Appstream metainfo files
# https://bugzilla.redhat.com/show_bug.cgi?id=1165507
Source1:        %{fontname}.metainfo.xml
Source2:        %{fontname}-sazanami.metainfo.xml
Source3:        %{fontname}-vlgothic.metainfo.xml

# Need investigating, however
# it seems that the behavior of "split" changed between 5.10 -> 5.12
Patch0:	monafont-2.90-perl512-split.patch

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	fontpackages-devel
BuildRequires:	%{_bindir}/perl
BuildRequires:	glibc-all-langpacks

%description
%{common_description}

%package -n	%{name_bitmap}
Summary:	Bitmap Japanese font for text arts
# Automatically converted from old format: Public Domain - review is highly recommended.
License:	LicenseRef-Callaway-Public-Domain
# Write BuildRequires a bit verbosely
BuildRequires:	perl-interpreter
BuildRequires:	%{_bindir}/bdftopcf
BuildRequires:	%{_bindir}/mkfontdir
Obsoletes:	%{old_name_bitmap} <= %{obsoletes_EVR}
Provides:	%{old_name_bitmap} = %{version}-%{release}

%description -n	%{name_bitmap}
%{common_description}

%package -n	%{name_ttf_s}
Summary:	True Type Japanese font for text arts based on Sazanami
# monafont itself is Public Domain and this package borrows
# sazanami
# And the outline otf uses Kochi-substitute (later renamed to sazanami),
# which is under BSD
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
BuildRequires:	%{family_ttf_s}-gothic-fonts = 0.%{sazanami_ver}
Requires:	fontpackages-filesystem
Obsoletes:	%{old_name_ttf_s} <= %{obsoletes_EVR}
Provides:	%{old_name_ttf_s} = %{version}-%{release}

%description -n	%{name_ttf_s}
%{common_description}

This package contains True Type fonts generated generated from
%{name} source package which are based on Sazanami fonts.

%package -n	%{name_ttf_v}
Summary:	True Type Japanese font for text arts based on VLGothic
# monafont itself is Public Domain and this package borrows
# VLGothic (mplus and BSD)
# And the outline otf uses Kochi-substitute (later renamed to sazanami),
# which is under BSD
# Automatically converted from old format: mplus and BSD - review is highly recommended.
License:	mplus AND LicenseRef-Callaway-BSD
BuildRequires:	%{family_ttf_vp}-fonts = %{vlgothic_ver}
Requires:	fontpackages-filesystem
Obsoletes:	%{old_name_ttf_v} <= %{obsoletes_EVR}
Provides:	%{old_name_ttf_v} = %{version}-%{release}

%description -n	%{name_ttf_v}
%{common_description}

This package contains True Type fonts generated generated from
%{name} source package which are based on VLGothic fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .perl512

iconv -f EUC-JP -t UTF-8 README.euc > README
touch -r README.euc README
iconv -f SHIFT-JIS -t UTF-8 ttfsrc/README-ttf.txt > ttfsrc/README-ttf.txt.tmp
touch -r ttfsrc/README-ttf.txt ttfsrc/README-ttf.txt.tmp
mv -f ttfsrc/README-ttf.txt.tmp ttfsrc/README-ttf.txt

%if ! %{show_progress}
# In the build on koji, showing progress bar is rather dirty
grep -rl '\\rprogress' . | xargs sed -i.bar -e '/\\rprogress/s|print|# print|'
%endif

%build
## Not using parallel make

# 1. bitmap fonts
make bdf

# 2. ttf
cd ttfsrc
cp -p name.src name.src.orig

## 2.1 ttf based on sazanami
sed -e 's|^Mona$|Mona-%{real_family_ttf_s}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{family_ttf_s_dir} -name sazanami-gothic.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_s}-%{sazanami_ver}
mv mona.ttf mona-%{real_family_ttf_s}.ttf

## 2.2 ttf based on VLGothic
sed -e 's|^Mona$|Mona-%{real_family_ttf_v}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{family_ttf_vp_dir} -name VL-PGothic-Regular.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_v}-%{vlgothic_ver}
mv mona.ttf mona-%{real_family_ttf_v}.ttf

cd ..

%install
rm -rf $RPM_BUILD_ROOT

# 1. bitmap fonts
mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_bitmap_full}
make install \
	X11BINDIR=%{_bindir} \
	MKDIRHIER="mkdir -p" \
	X11FONTDIR=$RPM_BUILD_ROOT%{fontdir_bitmap_full} \
	GZIP_CMD="gzip -9" \
	install
install -cpm 644 fonts.alias.mona \
	$RPM_BUILD_ROOT%{fontdir_bitmap_full}/fonts.alias

## catalog symlink
mkdir -p $RPM_BUILD_ROOT%{catalog_dir}
pushd $RPM_BUILD_ROOT%{catalog_dir}

UPWARDDIR="../../.."
ln -sf ${UPWARDDIR}%{fontdir_bitmap_full} %{fontdir_bitmap}
if [ ! -f $UPWARDDIR%{fontdir_bitmap_full}/fonts.dir ] ; then
	echo "Perhaps symlink target is wrong"
	exit 1
fi
popd

# 2. ttf
cd ttfsrc

mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_s_full}
install -cpm 0644 mona-%{real_family_ttf_s}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_s_full}/

mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_v_full}
install -cpm 0644 mona-%{real_family_ttf_v}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_v_full}/

cd ..

# Add AppStream metadata
# https://bugzilla.redhat.com/show_bug.cgi?id=1165507
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sazanami.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-vlgothic.metainfo.xml

%post -n	%{name_bitmap}
if [ -x %{_bindir}/fc-cache ] ; then
	%{_bindir}/fc-cache %{fontdir_bitmap_full} || :
fi

%postun -n	%{name_bitmap}
if [ $1 -eq 0 -a -x %{_bindir}/fc-cache ] ; then
	%{_bindir}/fc-cache %{fontdir_bitmap_full} || :
fi

%files -n	%{name_bitmap}
%doc	README
%doc	README.ascii

%{catalog_dir}/%{fontdir_bitmap}
%dir				%{fontdir_bitmap_full}
%verify(not md5 size mtime)	%{fontdir_bitmap_full}/fonts.alias
%verify(not md5 size mtime)	%{fontdir_bitmap_full}/fonts.dir
%{fontdir_bitmap_full}/*.pcf.gz

%define	_font_pkg_name	%{name_ttf_s}
%define	_fontdir	%{fontdir_ttf_s_full}
%_font_pkg mona-%{real_family_ttf_s}.ttf
%doc	ttfsrc/README-ttf.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/appdata/%{fontname}-sazanami.metainfo.xml

%define	_font_pkg_name	%{name_ttf_v}
%define	_fontdir	%{fontdir_ttf_v_full}
%_font_pkg mona-%{real_family_ttf_v}.ttf
%doc	ttfsrc/README-ttf.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/appdata/%{fontname}-vlgothic.metainfo.xml

%changelog
%autochangelog
