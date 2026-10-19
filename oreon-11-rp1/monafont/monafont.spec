%global source0_hash 26e608598edb2c9f1a662acd8bf4e06dc75910a69fc76698e4e062113a401978
%{!?_fontbasedir: %global _fontbasedir %{_datadir}/fonts}
%define		archivename		monafont
%define		projectname		mona
%define		fontname		%{projectname}
%define		family_ttf_s		sazanami
%define		family_ttf_s_dir	%{_fontbasedir}/%{family_ttf_s}
%define		family_ttf_v		vlgothic
%define		family_ttf_vp		vlgothic-p
%define		family_ttf_vp_dir	%{_fontbasedir}/vlgothic
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
%define		show_progress		0
%define	common_description	\
Mona Font is a Japanese proportional font which allows you to view \
Japanese text arts correctly.
Name:		%{archivename}
Version:	2.90
Release:        1%{?dist}
Summary:        Japanese font for text arts
License:	LicenseRef-Callaway-Public-Domain
URL:		http://monafont.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{fontname}.metainfo.xml
Source2:        %{fontname}-sazanami.metainfo.xml
Source3:        %{fontname}-vlgothic.metainfo.xml
Patch0:	monafont-2.90-perl512-split.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  //bin/bdftopcf
BuildRequires:  //bin/mkfontdir
BuildRequires:  //bin/perl
BuildRequires:  fontpackages-devel
BuildRequires:  glibc-all-langpacks
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  sazanami-gothic-fonts
BuildRequires:  vlgothic-p-fonts
# /oreon:deps
%description
%{common_description}

%package -n	%{name_bitmap}
Summary:	Bitmap Japanese font for text arts
License:	LicenseRef-Callaway-Public-Domain
BuildRequires:	perl-interpreter
BuildRequires:	%{_bindir}/bdftopcf
BuildRequires:	%{_bindir}/mkfontdir
Obsoletes:	%{old_name_bitmap} <= %{obsoletes_EVR}
Provides:	%{old_name_bitmap} = %{version}-%{release}
%description -n	%{name_bitmap}
%{common_description}

%package -n	%{name_ttf_s}
Summary:	True Type Japanese font for text arts based on Sazanami
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

make bdf
cd ttfsrc
cp -p name.src name.src.orig
sed -e 's|^Mona$|Mona-%{real_family_ttf_s}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{family_ttf_s_dir} -name sazanami-gothic.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_s}-%{sazanami_ver}
mv mona.ttf mona-%{real_family_ttf_s}.ttf
sed -e 's|^Mona$|Mona-%{real_family_ttf_v}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{family_ttf_vp_dir} -name VL-PGothic-Regular.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_v}-%{vlgothic_ver}
mv mona.ttf mona-%{real_family_ttf_v}.ttf
cd ..
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_bitmap_full}
make install \
	X11BINDIR=%{_bindir} \
	MKDIRHIER="mkdir -p" \
	X11FONTDIR=$RPM_BUILD_ROOT%{fontdir_bitmap_full} \
	GZIP_CMD="gzip -9" \
	install
install -cpm 644 fonts.alias.mona \
	$RPM_BUILD_ROOT%{fontdir_bitmap_full}/fonts.alias
mkdir -p $RPM_BUILD_ROOT%{catalog_dir}
pushd $RPM_BUILD_ROOT%{catalog_dir}
UPWARDDIR="../../.."
ln -sf ${UPWARDDIR}%{fontdir_bitmap_full} %{fontdir_bitmap}
if [ ! -f $UPWARDDIR%{fontdir_bitmap_full}/fonts.dir ] ; then
	echo "Perhaps symlink target is wrong"
	exit 1
fi
popd
cd ttfsrc
mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_s_full}
install -cpm 0644 mona-%{real_family_ttf_s}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_s_full}/
mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_v_full}
install -cpm 0644 mona-%{real_family_ttf_v}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_v_full}/
cd ..
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sazanami.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-vlgothic.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -n	%{name_bitmap}

if [ -x %{_bindir}/fc-cache ] ; then
	%{_bindir}/fc-cache %{fontdir_bitmap_full} || :
fi
%postun -n	%{name_bitmap}

if [ $1 -eq 0 -a -x %{_bindir}/fc-cache ] ; then
	%{_bindir}/fc-cache %{fontdir_bitmap_full} || :
fi
%files -f %{oreon_filedir}/main.list
%files -n mona-bitmap-fonts -f %{oreon_filedir}/mona-bitmap-fonts.list
%files -n mona-sazanami-fonts -f %{oreon_filedir}/mona-sazanami-fonts.list
%files -n mona-vlgothic-fonts -f %{oreon_filedir}/mona-vlgothic-fonts.list

%changelog

%autochangelog
