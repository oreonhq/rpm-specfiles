%global source0_hash none
%global source1_hash none
%global source2_hash none
%global source3_hash none
%global source4_hash none
%global source5_hash none
%global source6_hash none
%global source7_hash none
%global source8_hash none
%global source9_hash none
%global source10_hash none
%global source11_hash none
%global source12_hash none
%global source13_hash none
%global source14_hash none
%global source15_hash none
%global source16_hash none
%global source17_hash none
%global source18_hash none
%global source19_hash none
%global source20_hash none
%global source21_hash none
%global source22_hash none
%global source23_hash none
%global source24_hash none
%global source25_hash none
%global source26_hash none
%global source27_hash none
%global source28_hash none
%global source29_hash none
%global source30_hash none
%global source31_hash none
%global source32_hash none
%global source33_hash none
%global source34_hash none
%global source35_hash none
%global source36_hash none
%global source37_hash none
%global source38_hash none

%define buildall 0

%global _changelog_trimtime %(date +%s -d "1 year ago")

# build -flags subpkg
#define flags 1

Summary: Internationalization support for KDE3
Name: kde-i18n
Epoch: 1
Version: 3.5.10
Release: 46%{?dist}

# GFDL, with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
# Automatically converted from old format: GFDL - review is highly recommended.
License: LicenseRef-Callaway-GFDL 
Url: http://www.kde.org
BuildArch: noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Source0:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ar-%{version}.tar.bz2
Source1:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-bg-%{version}.tar.bz2
Source2:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-bn-%{version}.tar.bz2
Source3:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ca-%{version}.tar.bz2
Source4:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-cs-%{version}.tar.bz2
Source5:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-da-%{version}.tar.bz2
Source6:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-de-%{version}.tar.bz2
Source7:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-el-%{version}.tar.bz2
Source8:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-en_GB-%{version}.tar.bz2
Source9:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-es-%{version}.tar.bz2
Source10:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-et-%{version}.tar.bz2
Source11:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-fi-%{version}.tar.bz2
Source12:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-fr-%{version}.tar.bz2
Source13:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-he-%{version}.tar.bz2
Source14:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-hi-%{version}.tar.bz2
Source15:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-hu-%{version}.tar.bz2
Source16:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-is-%{version}.tar.bz2
Source17:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-it-%{version}.tar.bz2
Source18:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ja-%{version}.tar.bz2
Source19:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-nb-%{version}.tar.bz2
Source20:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-nl-%{version}.tar.bz2
Source21:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-nn-%{version}.tar.bz2
Source22:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-pa-%{version}.tar.bz2
Source23:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-pl-%{version}.tar.bz2
Source24:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-pt-%{version}.tar.bz2
Source25:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-pt_BR-%{version}.tar.bz2
Source26:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ro-%{version}.tar.bz2
Source27:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ru-%{version}.tar.bz2
Source28:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-sk-%{version}.tar.bz2
Source29:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-sl-%{version}.tar.bz2
Source30:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-sr-%{version}.tar.bz2
Source31:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-sv-%{version}.tar.bz2
Source32:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ta-%{version}.tar.bz2
Source33:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-tr-%{version}.tar.bz2
Source34:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-uk-%{version}.tar.bz2
Source35:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-zh_CN-%{version}.tar.bz2
Source36:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-zh_TW-%{version}.tar.bz2
Source37:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-lt-%{version}.tar.bz2
Source38:        https://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-ko-%{version}.tar.bz2
Source1000: subdirs-kde-i18n

BuildRequires: findutils
BuildRequires: gettext
BuildRequires: kdelibs3-devel
BuildRequires: make

Requires: kde-filesystem

%description
%{summary}.

%package flags
Summary: Geopolitical flags
Requires: %{name} = %{epoch}:%{version}-%{release}
%description flags
%{summary}.

%package Afrikaans
Summary: Afrikaans(af) language support for KDE3
Provides: %{name}-af = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Afrikaans
%{summary}.

%package Arabic 
Summary: Arabic(ar) language support for KDE3
Provides: %{name}-ar = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Arabic
%{summary}.

%package Azerbaijani
Summary: Azerbaijani(az) language support for KDE3
Provides: %{name}-az = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Azerbaijani
%{summary}.

%package Belarusian
Summary: Belarusian(be) language support for KDE3
Provides: %{name}-be = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Belarusian
%{summary}.

%package Bulgarian
Summary: Bulgarian(bg) language support for KDE3
Provides: %{name}-bg = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Bulgarian
%{summary}.

%package Bengali
Summary: Bengali(bn) language support for KDE3
Provides: %{name}-bn = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Bengali
%{summary}.

%package Tibetan
Summary: Tibetan(bo) language support for KDE3
Provides: %{name}-bo = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Tibetan
%{summary}.

%package Breton
Summary: Breton(br) language support for KDE3
Provides: %{name}-br = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Breton
%{summary}.

%package Bosnian
Summary: Bosnian(bs) language support for KDE3
Provides: %{name}-bs = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Bosnian
%{summary}.

%package Catalan
Summary: Catalan(ca) language support for KDE3
Provides: %{name}-ca = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Catalan
%{summary}.

%package Czech
Summary: Czech(cs) language support for KDE3
Provides: %{name}-cs = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Czech
%{summary}.

%package Cymraeg
Summary: Cymraeg language support for KDE3
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Cymraeg
%{summary}.

%package Welsh
Summary: Welsh(cy) language support for KDE3
Provides: %{name}-cy = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Welsh
%{summary}.

%package Danish
Summary: Danish(da) language support for KDE3
Provides: %{name}-da = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Danish
%{summary}.

%package German
Summary: German(de) language support for KDE3
Provides: %{name}-de = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description German
%{summary}.

%package Greek
Summary: Greek(el) language support for KDE3
Provides: %{name}-el = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Greek
%{summary}.

%package British
Summary: British(en_GB) English support for KDE3
Provides: %{name}-en_GB = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description British
%{summary}.

%package Esperanto
Summary: Esperanto(eo) support for KDE3
Provides: %{name}-eo = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Esperanto
%{summary}.

%package Spanish
Summary: Spanish(es) language support for KDE3
Provides: %{name}-es = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Spanish
%{summary}.

%package Estonian
Summary: Estonian(et) language support for KDE3
Provides: %{name}-et = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Estonian
%{summary}.

%package Basque
Summary: Basque(eu) language support for KDE3
Provides: %{name}-eu = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Basque
%{summary}.

%package Farsi
Summary: Farsi(fa) language support for KDE3
Provides: %{name}-fa = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Farsi
%{summary}.

%package Finnish
Summary: Finnish(fi) language support for KDE3
Provides: %{name}-fi = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Finnish
%{summary}.

%package Faroese
Summary: Faroese(fo) language support for KDE3
Provides: %{name}-fo = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Faroese
%{summary}.

%package French
Summary: French(fr) language support for KDE3
Provides: %{name}-fr = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description French
%{summary}.

%package Frisian
Summary: Frisian(fy) language support for KDE3
Provides: %{name}-fy = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Frisian
%{summary}.

%package Irish
Summary: Irish(ga) language support for KDE3
Obsoletes: kde-i18n-Gaeilge =< 3.5.10-45
Provides: %{name}-ga = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Irish
%{summary}.

%package Galician
Summary: Galician(gl) language support for KDE3
Provides: %{name}-gl = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Galician
%{summary}.

%package Hebrew
Summary: Hebrew(he) language support for KDE3
Provides: %{name}-he = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Hebrew
%{summary}.

%package Hindi
Summary: Hindi(hi) language support for KDE3
Provides: %{name}-hi = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Hindi
%{summary}.

%package Croatian
Summary: Croatian(hr) language support for KDE3
Provides: %{name}-hr = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Croatian
%{summary}.

%package Hungarian
Summary: Hungarian(hu) language support for KDE3
Provides: %{name}-hu = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Hungarian
%{summary}.

%package Indonesian
Summary: Indonesian(id) language support for KDE3
Provides: %{name}-id = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Indonesian
%{summary}.

%package Icelandic
Summary: Icelandic(is) language support for KDE3
Provides: %{name}-is = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Icelandic
%{summary}.

%package Italian
Summary: Italian(it) language support for KDE3
Provides: %{name}-it = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Italian
%{summary}.

%package Japanese
Summary: Japanese(ja) language support for KDE3
Provides: %{name}-ja = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Japanese
%{summary}.

%package Korean
Summary: Korean(ko) language support for KDE3
Provides: %{name}-ko = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Korean
%{summary}.

%package Kurdish
Summary: Kurdish(ku) language support for KDE3
Provides: %{name}-ku = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Kurdish
%{summary}.

%package Lao
Summary: Lao(lo) language support for KDE3
Provides: %{name}-lo = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Lao
%{summary}.

%package Lithuanian
Summary: Lithuanian(lt) language support for KDE3
Provides: %{name}-lt = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Lithuanian
%{summary}.

%package Latvian
Summary: Latvian(lv) language support for KDE3
Provides: %{name}-lv = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Latvian
%{summary}.

%package Maori
Summary: Maori(mi) language support for KDE3
Provides: %{name}-mi = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Maori
%{summary}.

%package Macedonian
Summary: Macedonian(mk) language support for KDE3
Provides: %{name}-mk = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Macedonian
%{summary}.

%package Maltese
Summary: Maltese(mt) language support for KDE3
Provides: %{name}-mt = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Maltese
%{summary}.

%package Dutch
Summary: Dutch(nl) language support for KDE3
Provides: %{name}-nl = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Dutch
%{summary}.

%package Norwegian
Summary: Norwegian(no) (Bokmaal) language support for KDE3
Provides: %{name}-no = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Norwegian
%{summary}.

%package Norwegian-Nynorsk
Summary: Norwegian(nn) (Nynorsk) language support for KDE3
Provides: %{name}-nn = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Norwegian-Nynorsk
%{summary}.

%package Occitan
Summary: Occitan(oc) language support for KDE3
Provides: %{name}-oc = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Occitan
%{summary}.

%package Polish
Summary: Polish(pl) language support for KDE3
Provides: %{name}-pl = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Polish
%{summary}.

%package Portuguese
Summary: Portuguese(pt) language support for KDE3
Provides: %{name}-pt = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Portuguese
%{summary}.

%package Punjabi
Summary: Punjabi(pa) language support for KDE3
Provides: %{name}-pa = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Punjabi
%{summary}.

%package Brazil
Summary: Brazil(pt_BR) Portuguese language support for KDE3
Provides: %{name}-pt_BR = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Brazil
%{summary}.

%package Romanian
Summary: Romanian(ro) language support for KDE3
Provides: %{name}-ro = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Romanian
%{summary}.

%package Russian
Summary: Russian(ru) language support for KDE3
Provides: %{name}-ru = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Russian
%{summary}.

%package Slovak
Summary: Slovak(sk) language support for KDE3
Provides: %{name}-sk = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Slovak
%{summary}.

%package Slovenian
Summary: Slovenian(sl) language support for KDE3
Provides: %{name}-sl = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Slovenian
%{summary}.

%package Serbian
Summary: Serbian(sr) language support for KDE3
Provides: %{name}-sr = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Serbian
%{summary}.

%package Swedish
Summary: Swedish(sv) language support for KDE3
Provides: %{name}-sv = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Swedish
%{summary}.

%package Tamil
Summary: Tamil(ta) language support for KDE3
Provides: %{name}-ta = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Tamil
%{summary}.

%package Tajik
Summary: Tajik(tg) language support for KDE3
Provides: %{name}-tg = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Tajik
%{summary}.

%package Thai
Summary: Thai(th) language support for KDE3
Provides: %{name}-th = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Thai
%{summary}.

%package Turkish
Summary: Turkish(tr) language support for KDE3
Provides: %{name}-tr = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Turkish
%{summary}.

%package Ukrainian
Summary: Ukrainian(uk) language support for KDE3
Provides: %{name}-uk = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Ukrainian
%{summary}.

%package Venda
Summary: Venda(ven) language support for KDE3
Provides: %{name}-ven = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Venda
%{summary}.

%package Vietnamese
Summary: Vietnamese(vi) language support for KDE3
Provides: %{name}-vi = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Vietnamese
%{summary}.

%package Walloon
Summary: Walloon(wa) language support for KDE3
Provides: %{name}-wa = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Walloon
%{summary}.

%package Xhosa
Summary: Xhosa(xh) (a Bantu language) support for KDE3
Provides: %{name}-xh = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Xhosa
%{summary}.

%package Chinese
Summary: Chinese(zh_CN) (Simplified Chinese) language support for KDE3
Provides: %{name}-zh_CN = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Chinese
%{summary}.

%package Chinese-Big5
Summary: Chinese(zh_TW) (Big5) language support for KDE3
Provides: %{name}-tz_TW = %{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description Chinese-Big5
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%(test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; })
%(test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; })
%(test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; })
%(test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; })
%(test "%{source7_hash}" = "none" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source7_hash}" || { echo "oreon: Source7 hash mismatch" >&2; exit 1; }; })
%(test "%{source8_hash}" = "none" || { f="%{SOURCE8}"; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source8_hash}" || { echo "oreon: Source8 hash mismatch" >&2; exit 1; }; })
%(test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; })
%(test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; })
%(test "%{source11_hash}" = "none" || { f="%{SOURCE11}"; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source11_hash}" || { echo "oreon: Source11 hash mismatch" >&2; exit 1; }; })
%(test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; })
%(test "%{source13_hash}" = "none" || { f="%{SOURCE13}"; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source13_hash}" || { echo "oreon: Source13 hash mismatch" >&2; exit 1; }; })
%(test "%{source14_hash}" = "none" || { f="%{SOURCE14}"; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source14_hash}" || { echo "oreon: Source14 hash mismatch" >&2; exit 1; }; })
%(test "%{source15_hash}" = "none" || { f="%{SOURCE15}"; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source15_hash}" || { echo "oreon: Source15 hash mismatch" >&2; exit 1; }; })
%(test "%{source16_hash}" = "none" || { f="%{SOURCE16}"; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source16_hash}" || { echo "oreon: Source16 hash mismatch" >&2; exit 1; }; })
%(test "%{source17_hash}" = "none" || { f="%{SOURCE17}"; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source17_hash}" || { echo "oreon: Source17 hash mismatch" >&2; exit 1; }; })
%(test "%{source18_hash}" = "none" || { f="%{SOURCE18}"; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source18_hash}" || { echo "oreon: Source18 hash mismatch" >&2; exit 1; }; })
%(test "%{source19_hash}" = "none" || { f="%{SOURCE19}"; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source19_hash}" || { echo "oreon: Source19 hash mismatch" >&2; exit 1; }; })
%(test "%{source20_hash}" = "none" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source20_hash}" || { echo "oreon: Source20 hash mismatch" >&2; exit 1; }; })
%(test "%{source21_hash}" = "none" || { f="%{SOURCE21}"; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source21_hash}" || { echo "oreon: Source21 hash mismatch" >&2; exit 1; }; })
%(test "%{source22_hash}" = "none" || { f="%{SOURCE22}"; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source22_hash}" || { echo "oreon: Source22 hash mismatch" >&2; exit 1; }; })
%(test "%{source23_hash}" = "none" || { f="%{SOURCE23}"; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source23_hash}" || { echo "oreon: Source23 hash mismatch" >&2; exit 1; }; })
%(test "%{source24_hash}" = "none" || { f="%{SOURCE24}"; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source24_hash}" || { echo "oreon: Source24 hash mismatch" >&2; exit 1; }; })
%(test "%{source25_hash}" = "none" || { f="%{SOURCE25}"; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source25_hash}" || { echo "oreon: Source25 hash mismatch" >&2; exit 1; }; })
%(test "%{source26_hash}" = "none" || { f="%{SOURCE26}"; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source26_hash}" || { echo "oreon: Source26 hash mismatch" >&2; exit 1; }; })
%(test "%{source27_hash}" = "none" || { f="%{SOURCE27}"; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source27_hash}" || { echo "oreon: Source27 hash mismatch" >&2; exit 1; }; })
%(test "%{source28_hash}" = "none" || { f="%{SOURCE28}"; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source28_hash}" || { echo "oreon: Source28 hash mismatch" >&2; exit 1; }; })
%(test "%{source29_hash}" = "none" || { f="%{SOURCE29}"; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source29_hash}" || { echo "oreon: Source29 hash mismatch" >&2; exit 1; }; })
%(test "%{source30_hash}" = "none" || { f="%{SOURCE30}"; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source30_hash}" || { echo "oreon: Source30 hash mismatch" >&2; exit 1; }; })
%(test "%{source31_hash}" = "none" || { f="%{SOURCE31}"; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source31_hash}" || { echo "oreon: Source31 hash mismatch" >&2; exit 1; }; })
%(test "%{source32_hash}" = "none" || { f="%{SOURCE32}"; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source32_hash}" || { echo "oreon: Source32 hash mismatch" >&2; exit 1; }; })
%(test "%{source33_hash}" = "none" || { f="%{SOURCE33}"; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source33_hash}" || { echo "oreon: Source33 hash mismatch" >&2; exit 1; }; })
%(test "%{source34_hash}" = "none" || { f="%{SOURCE34}"; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source34_hash}" || { echo "oreon: Source34 hash mismatch" >&2; exit 1; }; })
%(test "%{source35_hash}" = "none" || { f="%{SOURCE35}"; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source35_hash}" || { echo "oreon: Source35 hash mismatch" >&2; exit 1; }; })
%(test "%{source36_hash}" = "none" || { f="%{SOURCE36}"; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source36_hash}" || { echo "oreon: Source36 hash mismatch" >&2; exit 1; }; })
%(test "%{source37_hash}" = "none" || { f="%{SOURCE37}"; test -f "$f" || { echo "oreon: missing Source37 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source37_hash}" || { echo "oreon: Source37 hash mismatch" >&2; exit 1; }; })
%(test "%{source38_hash}" = "none" || { f="%{SOURCE38}"; test -f "$f" || { echo "oreon: missing Source38 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source38_hash}" || { echo "oreon: Source38 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version} -c

for i in $(cat %{SOURCE1000}) ; do
  tar jxf %{_sourcedir}/%{name}-$i-%{version}.tar.bz2
done


%build
for i in $(cat %{SOURCE1000}) ; do
  pushd %{name}-$i-%{version}
%configure
  %make_build
  popd
done


%install
for i in $(cat %{SOURCE1000}) ; do
  %make_install -C %{name}-$i-%{version} datadir=%{_datadir}
done

# make symlinks relative
pushd %{buildroot}%{_docdir}/HTML
for lang in *; do
  if [ -d $lang ]; then
    pushd $lang
    for i in */*/*; do
      if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -sf ../../../docs/common $i
      fi
    done

    for i in */*; do
      if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -sf ../../docs/common $i
      fi
    done

    for i in *; do
      if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -sf ../docs/common $i
      fi
    done

    popd
  fi
done
popd   

rm -rf %{buildroot}%{_docdir}/kinfocenter

# remove zero-length file
for i in $(find %{buildroot}%{_docdir}/HTML -size 0) ; do
   rm -f $i
done

%if ! 0%{?flags}
# See http://fedoraproject.org/wiki/Languages
   rm -f %{buildroot}%{_datadir}/locale/*/flag.png
%endif

# FIXME: This blacklist is exceedingly long and does not cover files which don't
# conflict, yet are still obsolete. We should switch to a whitelist approach.

# remove .mo and entry.desktop files which conflict with KDE 4 kde-l10n
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/amor.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ark.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/audiocd_encoder_lame.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/audiocd_encoder_vorbis.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/audiorename_plugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/blinken.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/bovo.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/cervisia.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/cvsservice.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/display.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/dolphin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/drkonqi.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/filetypes.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/gwenview.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/htmlsearch.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/imagerename_plugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/irkick.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/joystick.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/juk.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabc_dir.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabc_file.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabc_ldapkio.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabc_net.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabcformat_binary.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kaccess.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kalgebra.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kalzium.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kanagram.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kappfinder.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kate.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kateexternaltoolsplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katefilebrowserplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katefiletemplates.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katefindinfilesplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katehelloworld.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katehtmltools.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kateinsertcommand.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katekjswrapper.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katekonsoleplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katemailfilesplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katemake.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kateopenheader.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katepart4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katepybrowse.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katequickdocumentswitcherplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katesnippets.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katesymbolviewer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katetabbarextension.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katetextfilter.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katexmlcheck.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katexmltools.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/katomic.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kbattleship.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kblackbox.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kblankscrn.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kbounce.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kbruch.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kbstateapplet.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kbugbuster.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcachegrind.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcalc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcertpart.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcharselect.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcharselectapplet.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcm_krfb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcm_kwindesktop.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcm_phonon.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcm_phononxine.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcm_solid.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmaccess.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmaccessibility.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmaudiocd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmbackground.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmbell.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmcddb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmcgi.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmcolors.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmcomponentchooser.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmcrypto.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmcss.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmenergy.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmfonts.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmhtmlsearch.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmicons.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcminfo.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcminit.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcminput.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmioslaveinfo.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkamera.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkclock.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkded.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkdnssd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkeyboard.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkeys.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkio.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkonq.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkonqhtml.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkurifilt.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkvaio.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkwallet.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkwincompositing.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkwindecoration.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkwinrules.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkwm.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmlaunch.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmlirc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmlocale.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmnic.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmnotify.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmperformance.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmsamba.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmscreensaver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmshell.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmsmartcard.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmsmserver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmstyle.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmtaskbar.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmthinkpad.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmusb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmview1394.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmxinerama.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcolorchooser.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcron.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdat.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kde-menu.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdebugdialog.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdelibs4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdelibs_colors4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdelirc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdepasswd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdeqt.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdessh.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdesu.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdesud.mo
%if 0%{?fedora} > 12 || (0%{?oreon} >= 11)
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdevelop.mo
%endif
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdf.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdialog.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdmconfig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdmgreet.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/keditbookmarks.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfifteenapplet.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_avi.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_dds.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_drgeo.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_dvi.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_exr.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_flac.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_kig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_mp3.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_mpc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_mpeg.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_ogg.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_pnm.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_raw.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_rgb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_rpm.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_sid.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_theora.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_tiff.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_torrent.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_wav.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_xps.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfileaudiopreview4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfileshare.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfindpart.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfloppy.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfmclient.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfontinst.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfourinline.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kgamma.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kgeography.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kget.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kgoldrunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kgpg.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kgreet_classic.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kgreet_winbind.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/khangman.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/khelpcenter.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/khotkeys.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/khotnewstuff.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/khtmlkttsd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kinetd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kinfocenter.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_archive.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_audiocd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_finger.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_fish.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_floppy.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_help4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_imap4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_jabberdisco.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_ldap.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_man.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_mbox.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_nfs.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_nntp.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_pop3.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_remote.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_settings.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_sftp.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_sieve.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_smb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_smtp.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_svn.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_thumbnail.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_trash.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_zeroconf.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kioclient.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kioexec.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kiriki.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kiten.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kjots.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kjumpingcube.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/klaptopdaemon.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/klettres.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/klickety.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/klines.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/klipper.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/klock.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmag.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmahjongg.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmenuedit.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilo_asus.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilo_delli8k.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilo_generic.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilo_kvaio.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilo_powerbook.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilo_thinkpad.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmilod.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmimetypefinder.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmines.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmix.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmoon.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmousetool.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmouth.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmplot.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/knetattach.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/knetwalk.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/knetworkconf.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/knotify4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kolf.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kolourpaint4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kompare.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konqueror.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konquest.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konsole.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kopete.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpackage.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpartsaver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpasswdserver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpat.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpercentage.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kppp.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kppplogview.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kquitapp.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krandr.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krdb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krdc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kreadconfig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_bugzilla.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kreversi.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krfb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kruler.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krunner_bookmarksrunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krunner_calculatorrunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krunner_locationsrunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krunner_searchrunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/krunner_webshortcutsrunner.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kolourpaint.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksame.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksayit.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kscanplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kscd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kscreensaver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kshisen.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kshorturifilter.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksim.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksmserver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksnapshot.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kspaceduel.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksplashthemes.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksquares.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kstars.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kstart.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kstartperf.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kstyle_config.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kstyle_keramik_config.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kstyle_phase_config.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksudoku.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksysguard.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksystraycmd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksysv.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kteatime.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktexteditor_plugins.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kthememanager.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktimer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktip.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktouch.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktraderclient.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktron.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kttsd.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktuberling.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kturtle.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktux.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kuiserver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kuiviewer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kurifilter.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kuser.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwalletmanager.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kweather.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwin_art_clients.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwin_clients.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwin_effects.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwin_lib.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwordquiz.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kworldclock.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwrite.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwriteconfig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kxkb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kxsconfig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libKTTSD.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkblog.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkcal.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkcddb.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkcompactdisc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkdeedu.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkdegames.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkldap.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkmahjongg.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkmime.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkonq.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkpimidentities.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkpimutils.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkresources.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkscreensaver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libktnef.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkworkspace.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkxmlrpcclient.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libmailtransport.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libphonon.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libplasma.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libtaskmanager.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/lskat.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/marble.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/nepomukcoreservices.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/nepomukserver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/nsplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/oktetapart.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_chm.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_djvu.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_dvi.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_fictionbook.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_ghostview.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_kimgio.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_ooo.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_plucker.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_poppler.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_tiff.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular_xps.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/parley.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/phonon-xine.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/phonon_kde.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_battery.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_clock.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_desktop.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_devicenotifier.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_dig_clock.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_kget.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_knewsticker.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_launcher.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_pager.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_skapplet.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_applet_tasks.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasma_engine_dict.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/plasmaengineexplorer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/processcore.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/processui.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/secpolicy.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/solidcontrol.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/solidshell.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/soliduiserver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/spy.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/strigila_diff.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/superkaramba.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/svgpart.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/sweeper.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/systemsettings.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/timezones4.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/umbrello.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/useraccount.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdgantt.mo
rm -f %{buildroot}%{_datadir}/locale/*/entry.desktop

# keep these ones because we're shipping KDE 3 kdewebdev (because of Quanta)
# rm -f %%{buildroot}%%{_datadir}/locale/*/LC_MESSAGES/kfilereplace.mo
# rm -f %%{buildroot}%%{_datadir}/locale/*/LC_MESSAGES/kimagemapeditor.mo
# rm -f %%{buildroot}%%{_datadir}/locale/*/LC_MESSAGES/klinkstatus.mo

# remove docs which conflict with KDE 4 kde-l10n
rm -rf %{buildroot}%{_docdir}/HTML/*/amor
rm -rf %{buildroot}%{_docdir}/HTML/*/ark
rm -rf %{buildroot}%{_docdir}/HTML/*/blinken
rm -rf %{buildroot}%{_docdir}/HTML/*/bovo
rm -rf %{buildroot}%{_docdir}/HTML/*/cervisia
rm -rf %{buildroot}%{_docdir}/HTML/*/common
rm -rf %{buildroot}%{_docdir}/HTML/*/dolphin
rm -rf %{buildroot}%{_docdir}/HTML/*/gwenview
rm -rf %{buildroot}%{_docdir}/HTML/*/irkick
rm -rf %{buildroot}%{_docdir}/HTML/*/juk
rm -rf %{buildroot}%{_docdir}/HTML/*/kalgebra
rm -rf %{buildroot}%{_docdir}/HTML/*/kalzium
rm -rf %{buildroot}%{_docdir}/HTML/*/kamera
rm -rf %{buildroot}%{_docdir}/HTML/*/kanagram
rm -rf %{buildroot}%{_docdir}/HTML/*/kapptemplate
rm -rf %{buildroot}%{_docdir}/HTML/*/kate
rm -rf %{buildroot}%{_docdir}/HTML/*/kate-plugins
rm -rf %{buildroot}%{_docdir}/HTML/*/katomic
rm -rf %{buildroot}%{_docdir}/HTML/*/kbattleship
rm -rf %{buildroot}%{_docdir}/HTML/*/kblackbox
rm -rf %{buildroot}%{_docdir}/HTML/*/kbounce
rm -rf %{buildroot}%{_docdir}/HTML/*/kbruch
rm -rf %{buildroot}%{_docdir}/HTML/*/kbugbuster
rm -rf %{buildroot}%{_docdir}/HTML/*/kcachegrind
rm -rf %{buildroot}%{_docdir}/HTML/*/kcalc
rm -rf %{buildroot}%{_docdir}/HTML/*/kcharselect
rm -rf %{buildroot}%{_docdir}/HTML/*/kcmlirc
rm -rf %{buildroot}%{_docdir}/HTML/*/kcontrol
rm -rf %{buildroot}%{_docdir}/HTML/*/kcron
rm -rf %{buildroot}%{_docdir}/HTML/*/kdat
rm -rf %{buildroot}%{_docdir}/HTML/*/kdebugdialog
rm -rf %{buildroot}%{_docdir}/HTML/*/kdesu
rm -rf %{buildroot}%{_docdir}/HTML/*/kdesvn-build
rm -rf %{buildroot}%{_docdir}/HTML/*/kdf
rm -rf %{buildroot}%{_docdir}/HTML/*/kdm
rm -rf %{buildroot}%{_docdir}/HTML/*/kfind
rm -rf %{buildroot}%{_docdir}/HTML/*/kfloppy
rm -rf %{buildroot}%{_docdir}/HTML/*/kfourinline
rm -rf %{buildroot}%{_docdir}/HTML/*/kgamma
rm -rf %{buildroot}%{_docdir}/HTML/*/kgeography
rm -rf %{buildroot}%{_docdir}/HTML/*/kget
rm -rf %{buildroot}%{_docdir}/HTML/*/kgoldrunner
rm -rf %{buildroot}%{_docdir}/HTML/*/kgpg
rm -rf %{buildroot}%{_docdir}/HTML/*/khangman
rm -rf %{buildroot}%{_docdir}/HTML/*/khelpcenter
rm -rf %{buildroot}%{_docdir}/HTML/*/kig
rm -rf %{buildroot}%{_docdir}/HTML/*/kinfocenter
rm -rf %{buildroot}%{_docdir}/HTML/*/kiriki
rm -rf %{buildroot}%{_docdir}/HTML/*/kioslave
rm -rf %{buildroot}%{_docdir}/HTML/*/kiten
rm -rf %{buildroot}%{_docdir}/HTML/*/kjots
rm -rf %{buildroot}%{_docdir}/HTML/*/kjumpingcube
rm -rf %{buildroot}%{_docdir}/HTML/*/klettres
rm -rf %{buildroot}%{_docdir}/HTML/*/klickety
rm -rf %{buildroot}%{_docdir}/HTML/*/klines
rm -rf %{buildroot}%{_docdir}/HTML/*/klipper
rm -rf %{buildroot}%{_docdir}/HTML/*/kmag
rm -rf %{buildroot}%{_docdir}/HTML/*/kmahjongg
rm -rf %{buildroot}%{_docdir}/HTML/*/kmenuedit
rm -rf %{buildroot}%{_docdir}/HTML/*/kmines
rm -rf %{buildroot}%{_docdir}/HTML/*/kmix
rm -rf %{buildroot}%{_docdir}/HTML/*/kmoon
rm -rf %{buildroot}%{_docdir}/HTML/*/kmousetool
rm -rf %{buildroot}%{_docdir}/HTML/*/kmouth
rm -rf %{buildroot}%{_docdir}/HTML/*/kmplot
rm -rf %{buildroot}%{_docdir}/HTML/*/knetattach
rm -rf %{buildroot}%{_docdir}/HTML/*/knetwalk
rm -rf %{buildroot}%{_docdir}/HTML/*/knetworkconf
rm -rf %{buildroot}%{_docdir}/HTML/*/knewsticker
rm -rf %{buildroot}%{_docdir}/HTML/*/kolf
rm -rf %{buildroot}%{_docdir}/HTML/*/kolourpaint
rm -rf %{buildroot}%{_docdir}/HTML/*/kompare
rm -rf %{buildroot}%{_docdir}/HTML/*/konqueror
rm -rf %{buildroot}%{_docdir}/HTML/*/konquest
rm -rf %{buildroot}%{_docdir}/HTML/*/konsole
rm -rf %{buildroot}%{_docdir}/HTML/*/kopete
rm -rf %{buildroot}%{_docdir}/HTML/*/kpackage
rm -rf %{buildroot}%{_docdir}/HTML/*/kpat
rm -rf %{buildroot}%{_docdir}/HTML/*/kpercentage
rm -rf %{buildroot}%{_docdir}/HTML/*/kppp
rm -rf %{buildroot}%{_docdir}/HTML/*/krdc
rm -rf %{buildroot}%{_docdir}/HTML/*/kreversi
rm -rf %{buildroot}%{_docdir}/HTML/*/krfb
rm -rf %{buildroot}%{_docdir}/HTML/*/kruler
rm -rf %{buildroot}%{_docdir}/HTML/*/ksame
rm -rf %{buildroot}%{_docdir}/HTML/*/kscd
rm -rf %{buildroot}%{_docdir}/HTML/*/kshisen
rm -rf %{buildroot}%{_docdir}/HTML/*/ksim
rm -rf %{buildroot}%{_docdir}/HTML/*/ksnapshot
rm -rf %{buildroot}%{_docdir}/HTML/*/kspaceduel
rm -rf %{buildroot}%{_docdir}/HTML/*/ksquares
rm -rf %{buildroot}%{_docdir}/HTML/*/kstars
rm -rf %{buildroot}%{_docdir}/HTML/*/ksudoku
rm -rf %{buildroot}%{_docdir}/HTML/*/ksysguard
rm -rf %{buildroot}%{_docdir}/HTML/*/ksysv
rm -rf %{buildroot}%{_docdir}/HTML/*/kteatime
rm -rf %{buildroot}%{_docdir}/HTML/*/ktimer
rm -rf %{buildroot}%{_docdir}/HTML/*/ktouch
rm -rf %{buildroot}%{_docdir}/HTML/*/ktron
rm -rf %{buildroot}%{_docdir}/HTML/*/kttsd
rm -rf %{buildroot}%{_docdir}/HTML/*/ktuberling
rm -rf %{buildroot}%{_docdir}/HTML/*/kturtle
rm -rf %{buildroot}%{_docdir}/HTML/*/kuser
rm -rf %{buildroot}%{_docdir}/HTML/*/kwallet
rm -rf %{buildroot}%{_docdir}/HTML/*/kweather
rm -rf %{buildroot}%{_docdir}/HTML/*/kwordquiz
rm -rf %{buildroot}%{_docdir}/HTML/*/kworldclock
rm -rf %{buildroot}%{_docdir}/HTML/*/kwrite
rm -rf %{buildroot}%{_docdir}/HTML/*/kxkb
rm -rf %{buildroot}%{_docdir}/HTML/*/lskat
rm -rf %{buildroot}%{_docdir}/HTML/*/marble
rm -rf %{buildroot}%{_docdir}/HTML/*/okular
rm -rf %{buildroot}%{_docdir}/HTML/*/parley
rm -rf %{buildroot}%{_docdir}/HTML/*/plasma
rm -rf %{buildroot}%{_docdir}/HTML/*/sonnet
rm -rf %{buildroot}%{_docdir}/HTML/*/superkaramba
rm -rf %{buildroot}%{_docdir}/HTML/*/umbrello

# keep these ones because we're shipping KDE 3 kdewebdev (because of Quanta)
# rm -rf %%{buildroot}%%{_docdir}/HTML/*/kfilereplace
# rm -rf %%{buildroot}%%{_docdir}/HTML/*/kimagemapeditor
# rm -rf %%{buildroot}%%{_docdir}/HTML/*/klinkreplace
# rm -rf %%{buildroot}%%{_docdir}/HTML/*/xsldbg

# remove .mo files which conflict with KDE 4 extragear
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcoloredit.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kiconedit.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kaudiocreator.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmid.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/akregator_konqplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/autorefresh.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/babelfish.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/crashesplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/dirfilterplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/domtreeviewer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/fsview.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/imgalleryplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/khtmlsettingsplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konqsidebar_mediaplayer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konqsidebar_metabar.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konqsidebar_news.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/mf_konqplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/minitoolsplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/rellinks.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/searchbarplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/uachangerplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/validatorsplugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/webarchiver.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ksig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpovmodeler.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kuickshow.mo

# remove docs which conflict with KDE 4 extragear
rm -rf %{buildroot}%{_docdir}/HTML/*/kcoloredit
rm -rf %{buildroot}%{_docdir}/HTML/*/kiconedit
rm -rf %{buildroot}%{_docdir}/HTML/*/kaudiocreator
rm -rf %{buildroot}%{_docdir}/HTML/*/kmid
rm -rf %{buildroot}%{_docdir}/HTML/*/konq-plugins
rm -rf %{buildroot}%{_docdir}/HTML/*/ksig
rm -rf %{buildroot}%{_docdir}/HTML/*/kpovmodeler
rm -rf %{buildroot}%{_docdir}/HTML/*/kuickshow

# remove obsolete KDE 3 application data translations
rm -rf %{buildroot}%{_datadir}/apps

# on F10+, also get rid of kdepim stuff
rm -rf %{buildroot}%{_docdir}/HTML/*/akregator
rm -rf %{buildroot}%{_docdir}/HTML/*/kaddressbook
rm -rf %{buildroot}%{_docdir}/HTML/*/kalarm
rm -rf %{buildroot}%{_docdir}/HTML/*/karm
rm -rf %{buildroot}%{_docdir}/HTML/*/kleopatra
rm -rf %{buildroot}%{_docdir}/HTML/*/kmail
rm -rf %{buildroot}%{_docdir}/HTML/*/knode
rm -rf %{buildroot}%{_docdir}/HTML/*/knotes
rm -rf %{buildroot}%{_docdir}/HTML/*/konsolekalendar
rm -rf %{buildroot}%{_docdir}/HTML/*/kontact
rm -rf %{buildroot}%{_docdir}/HTML/*/korganizer
rm -rf %{buildroot}%{_docdir}/HTML/*/korn
rm -rf %{buildroot}%{_docdir}/HTML/*/kpilot
rm -rf %{buildroot}%{_docdir}/HTML/*/ktnef
rm -rf %{buildroot}%{_docdir}/HTML/*/kwatchgnupg
rm -rf %{buildroot}%{_docdir}/HTML/*/multisynk

rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/akregator.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kabc_slox.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kaddressbook.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kalarm.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkabconfig.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kcmkontactnt.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdepimresources.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kdepimwizards.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kfile_vcf.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kio_groupwise.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kitchensync.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kleopatra.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmail.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmail_text_calendar_plugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmail_text_vcard_plugin.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kmailcvt.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/knode.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/knotes.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/konsolekalendar.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kontact.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/korganizer.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/korn.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kpilot.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_birthday.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_featureplan.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_groupware.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_groupwise.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_kolab.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_remote.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_scalix.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_tvanytime.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kres_xmlrpc.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/ktnef.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/kwatchgnupg.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkdepim.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkholidays.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkleopatra.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkpgp.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libksieve.mo
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/libkicker.mo


%files
# This space intentionally left blank

%if 0%{?flags}
%files flags
%{_datadir}/locale/*/*.png
%endif

%if %{buildall}
%files Afrikaans
%lang(af) %{_datadir}/locale/af/LC_MESSAGES/*
%lang(af) %{_datadir}/locale/af/charset
%lang(af) %{_docdir}/HTML/af/
%endif

%files Arabic 
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*
%lang(ar) %{_datadir}/locale/ar/charset

%if %{buildall}
%files Azerbaijani
%lang(az) %{_datadir}/locale/az/LC_MESSAGES/*
%lang(az) %{_datadir}/locale/az/charset
%endif

%if %{buildall}
%files Belarusian
%lang(be) %{_datadir}/locale/be/LC_MESSAGES/*
%lang(be) %{_datadir}/locale/be/charset
%endif

%files Bulgarian
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/*
%lang(bg) %{_datadir}/locale/bg/charset

%files Bengali
%lang(bn) %{_datadir}/locale/bn/LC_MESSAGES/*
%lang(bn) %{_datadir}/locale/bn/charset

%if %{buildall}
%files Tibetan
%lang(bo) %{_datadir}/locale/bo/LC_MESSAGES/*
%lang(bo) %{_datadir}/locale/bo/charset
%endif

%if %{buildall}
%files Breton
%lang(br) %{_datadir}/locale/br/LC_MESSAGES/*
%lang(br) %{_datadir}/locale/br/charset
%endif

%if %{buildall}
%files Bosnian
%lang(bs) %{_datadir}/locale/bs/LC_MESSAGES/*
%lang(bs) %{_datadir}/locale/bs/charset
%endif

%files Catalan
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*
%lang(ca) %{_datadir}/locale/ca/charset
%lang(ca) %{_docdir}/HTML/ca/

%files Czech
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*
%lang(cs) %{_datadir}/locale/cs/charset
%lang(cs) %{_docdir}/HTML/cs/

%if %{buildall}
%files Welsh
%lang(cy) %{_datadir}/locale/cy/LC_MESSAGES/*
%lang(cy) %{_datadir}/locale/cy/charset
%endif

%files Danish
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*
%lang(da) %{_datadir}/locale/da/charset
%lang(da) %{_datadir}/locale/da/da.compendium
%lang(da) %{_docdir}/HTML/da/

%files German
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(de) %{_datadir}/locale/de/charset
%lang(de) %{_docdir}/HTML/de/

%files Greek
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
%lang(el) %{_datadir}/locale/el/charset

%files British
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/*
%lang(en_GB) %{_datadir}/locale/en_GB/charset
%lang(en_GB) %{_docdir}/HTML/en_GB/

%if %{buildall}
%files Esperanto
%lang(eo) %{_datadir}/locale/eo/LC_MESSAGES/*
%lang(eo) %{_datadir}/locale/eo/charset
%endif

%files Spanish
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/charset
%lang(es) %{_docdir}/HTML/es/

%files Estonian
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*
%lang(et) %{_datadir}/locale/et/charset
%lang(et) %{_docdir}/HTML/et/

%if %{buildall}
%files Basque
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/*
%lang(eu) %{_datadir}/locale/eu/charset
%endif

%if %{buildall}
%files Farsi
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*
%lang(fa) %{_datadir}/locale/fa/charset
%endif

%files Finnish
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*
%lang(fi) %{_datadir}/locale/fi/charset
%lang(fi) %{_docdir}/HTML/fi/

%if %{buildall}
%files Faroese
%lang(fo) %{_datadir}/locale/fo/LC_MESSAGES/*
%lang(fo) %{_datadir}/locale/fo/charset
%endif

%files French
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/charset
%lang(fr) %{_datadir}/locale/fr/nbsp_gui_fr.txt
%lang(fr) %{_datadir}/locale/fr/relecture_*
%lang(fr) %{_docdir}/HTML/fr/

%if %{buildall}
%files Frisian
%lang(fy) %{_datadir}/locale/fy/LC_MESSAGES/*
%lang(fy) %{_datadir}/locale/fy/charset
%endif

%if %{buildall}
%files Irish
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/*
%lang(ga) %{_datadir}/locale/ga/charset

%files Galician
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/*
%lang(gl) %{_datadir}/locale/gl/charset
%endif

%files Hebrew
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/*
%lang(he) %{_datadir}/locale/he/charset
%lang(he) %{_docdir}/HTML/he/

%files Hindi
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/*
%lang(hi) %{_datadir}/locale/hi/charset

%if %{buildall}
%files Croatian
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/*
%lang(hr) %{_datadir}/locale/hr/charset
%lang(hr) %{_docdir}/HTML/hr/
%endif

%files Hungarian
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*
%lang(hu) %{_datadir}/locale/hu/charset
%lang(hu) %{_docdir}/HTML/hu/

%if %{buildall}
%files Indonesian
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/*
%lang(id) %{_datadir}/locale/id/charset
%lang(id) %{_docdir}/HTML/id/
%endif

%files Icelandic
%lang(is) %{_datadir}/locale/is/LC_MESSAGES/*
%lang(is) %{_datadir}/locale/is/charset

%files Italian
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*
%lang(it) %{_datadir}/locale/it/charset
%lang(it) %{_docdir}/HTML/it/

%files Japanese
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*
%lang(ja) %{_datadir}/locale/ja/charset
%lang(ja) %{_docdir}/HTML/ja/

%files Korean
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*
%lang(ko) %{_datadir}/locale/ko/charset
%lang(ko) %{_docdir}/HTML/ko/

%if %{buildall}
%files Kurdish
%lang(ku) %{_datadir}/locale/ku/LC_MESSAGES/*
%lang(ku) %{_datadir}/locale/ku/charset
%lang(ku) %{_docdir}/HTML/ku/
%endif

%if %{buildall}
%files Lao
%lang(lo) %{_datadir}/locale/lo/LC_MESSAGES/*
%lang(lo) %{_datadir}/locale/lo/charset
%lang(lo) %{_docdir}/HTML/lo/
%endif

%files Lithuanian
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*
%lang(lt) %{_datadir}/locale/lt/charset

%if %{buildall}
%files Latvian
%lang(lv) %{_datadir}/locale/lv/LC_MESSAGES/*
%lang(lv) %{_datadir}/locale/lv/charset
%endif

%if %{buildall}
%files Maori
%lang(mi) %{_datadir}/locale/mi/LC_MESSAGES/*
%lang(mi) %{_datadir}/locale/mi/charset
%endif

%if %{buildall}
%files Macedonian
%lang(mk) %{_datadir}/locale/mk/LC_MESSAGES/*
%lang(mk) %{_datadir}/locale/mk/charset
%endif

%if %{buildall}
%files Maltese
%lang(mt) %{_datadir}/locale/mt/LC_MESSAGES/*
%lang(mt) %{_datadir}/locale/mt/charset
%endif

%files Dutch
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%lang(nl) %{_datadir}/locale/nl/charset
%lang(nl) %{_docdir}/HTML/nl/

%files Norwegian
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*
%lang(nb) %{_datadir}/locale/nb/charset
%lang(nb) %{_datadir}/locale/nb/README
#%lang(nb) %%{_docdir}/HTML/nb/

%files Norwegian-Nynorsk
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/*
%lang(nn) %{_datadir}/locale/nn/charset
#%lang(nn) %%{_docdir}/HTML/nn/

%if %{buildall}
%files Occitan
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/*
%lang(oc) %{_datadir}/locale/oc/charset
%endif

%files Punjabi
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/*
%lang(pa) %{_datadir}/locale/pa/charset

%files Polish
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*
%lang(pl) %{_datadir}/locale/pl/charset
%lang(pl) %{_docdir}/HTML/pl/

%files Portuguese
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%lang(pt) %{_datadir}/locale/pt/charset
%lang(pt) %{_docdir}/HTML/pt/

%files Brazil
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%lang(pt_BR) %{_datadir}/locale/pt_BR/charset
%lang(pt_BR) %{_docdir}/HTML/pt_BR/

%files Romanian
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/*
%lang(ro) %{_datadir}/locale/ro/charset
%lang(ro) %{_docdir}/HTML/ro/

%files Russian
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
%lang(ru) %{_datadir}/locale/ru/charset
%lang(ru) %{_docdir}/HTML/ru/

%files Slovak
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/*
%lang(sk) %{_datadir}/locale/sk/charset
%lang(sk) %{_docdir}/HTML/sk/

%files Slovenian
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/*
%lang(sl) %{_datadir}/locale/sl/charset
%lang(sl) %{_docdir}/HTML/sl/

%files Serbian
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/*
%lang(sr) %{_datadir}/locale/sr/charset
%lang(sr) %{_docdir}/HTML/sr/

%files Swedish
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*
%lang(sv) %{_datadir}/locale/sv/charset
%lang(sv) %{_docdir}/HTML/sv/

%files Tamil
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/*
%lang(ta) %{_datadir}/locale/ta/charset

%if %{buildall}
%files Tajik
%lang(tg) %{_datadir}/locale/tg/LC_MESSAGES/*
%lang(tg) %{_datadir}/locale/tg/charset
%endif

%if %{buildall}
%files Thai
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/*
%lang(th) %{_datadir}/locale/th/charset
%endif

%files Turkish
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*
%lang(tr) %{_datadir}/locale/tr/charset
%lang(tr) %{_docdir}/HTML/tr/

%files Ukrainian
%lang(uk) %{_docdir}/HTML/uk/
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
%lang(uk) %{_datadir}/locale/uk/charset

%if %{buildall}
%files Venda
%lang(ven) %{_datadir}/locale/ven/LC_MESSAGES/*
%lang(ven) %{_datadir}/locale/ven/charset
%endif

%if %{buildall}
%files Vietnamese
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/*
%lang(vi) %{_datadir}/locale/vi/charset
%endif

%if %{buildall}
%files Walloon
%lang(wa) %{_datadir}/locale/wa/LC_MESSAGES/*
%lang(wa) %{_datadir}/locale/wa/charset
%endif

%if %{buildall}
%files Xhosa
%lang(xh) %{_datadir}/locale/xh/LC_MESSAGES/*
%lang(xh) %{_datadir}/locale/xh/charset
%lang(xh) %{_docdir}/HTML/xh/
%endif

%files Chinese
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*
%lang(zh_CN) %{_datadir}/locale/zh_CN/charset
%lang(zh_CN) %{_docdir}/HTML/zh_CN/

%files Chinese-Big5
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
%lang(zh_TW) %{_datadir}/locale/zh_TW/charset
%lang(zh_TW) %{_docdir}/HTML/zh_TW/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.5.10-46
- Import
