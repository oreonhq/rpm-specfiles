%global source0_hash 81af0aff7d2086d8af24cea7202f7546130997982534691373485cd96744d05e

Version: 1.003
Release: 4%{?dist}
URL:     http://www.amirifont.org

%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          README.md README-Arabic.md Documentation-Arabic.html
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
Amiri is a revival of the beautiful typeface pioneered in early 20th
century by Bulaq Press in Cairo, also known as Amiria Press, after which
the font is named.
}

%global common_description_ar %{expand:
تميزت به مطبعة بولاق منذ أوائل القرن العشرين، والتي عرفت
أيضًا بالمطبعة الأميرية، ومن هنا أخذ الخط اسمه.
}

%global fontfamily0       Amiri
%global fontsummary0      A classical Arabic font in Naskh style
%global fontpkgheader0    %{expand:
Obsoletes: amiri-fonts-common < %{version}-%{release}
}
%global fonts0            Amiri-Regular.ttf Amiri-Italic.ttf Amiri-BoldItalic.ttf Amiri-Bold.ttf
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:%{common_description}

Amiri is a classical Arabic typeface in Naskh style for typesetting books
and other running text.
%{common_description_ar}

الخط الأميري خط نسخي موجه لطباعة الكتب والنصوص الطويلة.
الخط الأميري هو إحياء ومحاكاة للخط الطباعي الجميل الذي

}

%global fontfamily1       Amiri Quran
%global fontsummary1      Quran type of Amiri fonts
%global fonts1            AmiriQuran.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:%{common_description}

This package contains Quran type of Amiri fonts.

%{common_description_ar}

تحتوي هذه الحُزمة على النّمط القرآني من الخط الأميري.
}

%global fontfamily2       Amiri Quran Colored
%global fontsummary2      None
%global fonts2            AmiriQuranColored.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:%{common_description}
This package contains Quran Colored type of Amiri fonts.

%{common_description_ar}

تحتوي هذه الحزمة على نوع القرآن الملون من الخطوط الأميرية.
}

Source0:  https://github.com/alif-type/amiri/releases/download/%{version}/Amiri-%{version}.zip
Source10: 67-%{fontpkgname0}.conf
Source11: 67-%{fontpkgname1}.conf
Source12: 67-%{fontpkgname2}.conf

%fontpkg -a

%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Amiri-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
