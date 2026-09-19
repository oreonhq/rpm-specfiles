%global source0_hash none

# SPDX-License-Identifier: MIT

%global fontname naver-nanum

BuildArch: noarch

Version: 3.020
Release: 41.20140930%{?dist}
License: OFL-1.1
URL:     http://hangeul.naver.com

%global foundry           Naver
%global fontlicenses      COPYING

%global common_description %{expand:
Nanum fonts are collection of commonly-used Myeongjo and Gothic Korean \
font families, designed by Sandoll Communication and Fontrix. The \
publisher is Naver Corporation.
}

%global fontfamily1       Nanum Barun Gothic
%global fontsummary1      Nanum fonts Barun Gothic font faces
%global fontpkgheader1    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts1            NanumBarunGothic.ttf NanumBarunGothicBold.ttf NanumBarunGothicLight.ttf NanumBarunGothicUltraLight.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package consists of the Nanum fonts Barun Gothic font faces.
}

%global fontfamily2       Nanum Barun Pen
%global fontsummary2      Nanum fonts Barun Pen font faces
%global fontpkgheader2    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts2            NanumBarunpenR.ttf NanumBarunpenB.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package consists of the Nanum fonts Barun Pen font faces.
}

%global fontfamily3       Nanum Brush
%global fontsummary3      Nanum fonts Brush font faces
%global fontpkgheader3    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts3            NanumBrush.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package consists of the Nanum fonts Brush font faces.
}

%global fontfamily4       Nanum Gothic
%global fontsummary4      Nanum fonts Gothic font faces
%global fontpkgheader4    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts4            NanumGothic.ttf NanumGothicBold.ttf NanumGothicExtraBold.ttf NanumGothicLight.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package consists of the Nanum fonts Gothic font faces.
}

%global fontfamily5       Nanum Myeongjo
%global fontsummary5      Nanum fonts Myeongjo font faces
%global fontpkgheader5    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts5            NanumMyeongjo.ttf NanumMyeongjoBold.ttf NanumMyeongjoExtraBold.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package consists of the Nanum fonts Myeongjo font faces.
}

%global fontfamily6       Nanum Pen
%global fontsummary6      Nanum fonts Pen font faces
%global fontpkgheader6    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts6            NanumPen.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package consists of the Nanum fonts Pen font faces.
}

# Need to convert from Windows executable to tar ball to avoid to use p7zip
#Source:    http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
# wget http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
# 7z x NanumFontSetup_TTF_ALL_hangeulcamp.exe
# tar zcvf NanumFont.tar.gz -C \$WINDIR/Fonts/ .
Source0:  NanumFont.tar.gz
# License text was taken from the upstream web on May 13 2014:
# http://help.naver.com/ops/step2/faq.nhn?faqId=15879
Source1:  %{name}-license.txt
Source11: 66-%{fontpkgname1}.conf
Source12: 66-%{fontpkgname2}.conf
Source13: 66-%{fontpkgname3}.conf
Source14: 66-%{fontpkgname4}.conf
Source15: 66-%{fontpkgname5}.conf
Source16: 66-%{fontpkgname6}.conf

Name:     %{fontname}-fonts
Summary:  Nanum family of Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%autosetup -c
cp %{SOURCE1} COPYING

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
