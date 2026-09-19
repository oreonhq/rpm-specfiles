%global source0_hash none

# SPDX-License-Identifier: MIT

%global fontname    baekmuk-ttf
%global archivename %{fontname}-%{version}

BuildArch: noarch
BuildRequires: mkfontdir
BuildRequires: ttmkfdir >= 3.0.6

Version: 2.2
Release: 67%{?dist}
License: Baekmuk
URL:     http://kldp.net/projects/baekmuk/

%global foundry           Baekmuk
%global fontlicense       Baekmuk
%global fontlicenses      COPYRIGHT COPYRIGHT.ko
%global fontdocs          README

%global common_description %{expand:
This package provides the free Korean TrueType fonts.
}

%global fontfamily1       Baekmuk Batang
%global fontsummary1      Korean Baekmuk TrueType Batang typeface
%global fontpkgheader1    %{expand:
Obsoletes:      %{name}-batang < 2.2-13
Provides:       %{name}-batang = %{version}-%{release}
Obsoletes:      %{fontname}-batang-fonts < 2.2-60
Provides:       %{fontname}-batang-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts1            ttf/batang.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

Batang is Korean TrueType font in Serif typeface.
}

%global fontfamily2       Baekmuk Dotum
%global fontsummary2      Korean Baekmuk TrueType Dotum typeface
%global fontpkgheader2    %{expand:
Obsoletes:      %{name}-dotum < 2.2-13
Provides:       %{name}-dotum = %{version}-%{release}
Obsoletes:      %{fontname}-dotum-fonts < 2.2-60
Provides:       %{fontname}-dotum-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts2            ttf/dotum.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

Dotum is Korean TrueType font in San-serif typeface.
}

%global fontfamily3       Baekmuk Gulim
%global fontsummary3      Korean Baekmuk TrueType Gulim typeface
%global fontpkgheader3    %{expand:
Obsoletes:      %{name}-gulim < 2.2-13
Provides:       %{name}-gulim = %{version}-%{release}
Obsoletes:      %{fontname}-gulim-fonts < 2.2-60
Provides:       %{fontname}-gulim-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts3            ttf/gulim.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

Gulim is Korean TrueType font in Monospace typeface.
}

%global fontfamily4       Baekmuk Headline
%global fontsummary4      Korean Baekmuk TrueType Headline typeface
%global fontpkgheader4    %{expand:
Obsoletes:      %{name}-hline < 2.2-13
Provides:       %{name}-hline = %{version}-%{release}
Obsoletes:      %{fontname}-hline-fonts < 2.2-60
Provides:       %{fontname}-hline-fonts = %{version}-%{release}
Obsoletes:      %{name}-common < 2.2-60
Provides:       %{name}-common = %{version}-%{release}
}
%global fonts4            ttf/hline.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

Headline is Korean TrueType font in Black face.
}

Source0:  http://kldp.net/baekmuk/release/865-%{archivename}.tar.gz#/%{archivename}.tar.gz
Source11: 68-%{fontpkgname1}.conf
Source12: 68-%{fontpkgname2}.conf
Source13: 68-%{fontpkgname3}.conf
Source14: 68-%{fontpkgname4}.conf

Name:     %{fontname}-fonts
Summary:  Free Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%autosetup -n %{archivename}

# convert Korean copyright file to utf8
%{_bindir}/iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko

%build
%fontbuild -a

%install
%fontinstall -a

for fontdir in `echo %{fontdir1} %{fontdir2} %{fontdir3} %{fontdir4}`; do
    %__install -d -m 0755 %{buildroot}$fontdir

    # fonts.{scale,dir}
    %{_bindir}/ttmkfdir -d %{buildroot}$fontdir \
      -o %{buildroot}$fontdir/fonts.scale
      %{_bindir}/mkfontdir %{buildroot}$fontdir
done

%check
%fontcheck -a

%fontfiles -z 1
%verify(not md5 size mtime) %{fontdir1}/fonts.dir
%verify(not md5 size mtime) %{fontdir1}/fonts.scale

%fontfiles -z 2
%verify(not md5 size mtime) %{fontdir2}/fonts.dir
%verify(not md5 size mtime) %{fontdir2}/fonts.scale

%fontfiles -z 3
%verify(not md5 size mtime) %{fontdir3}/fonts.dir
%verify(not md5 size mtime) %{fontdir3}/fonts.scale

%fontfiles -z 4
%verify(not md5 size mtime) %{fontdir4}/fonts.dir
%verify(not md5 size mtime) %{fontdir4}/fonts.scale

%changelog
%autochangelog
