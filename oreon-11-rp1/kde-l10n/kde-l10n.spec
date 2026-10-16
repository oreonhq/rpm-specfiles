Summary: Internationalization support for KDE Applications
Name:    kde-l10n
Version: 17.04.1
Release: 1%{?dist}

Url:     http://www.kde.org
License: LGPL-2.1-only
BuildArch: noarch
%define debug_package %{nil}

BuildRequires: gettext
BuildRequires: kde-filesystem
Requires: kde-filesystem

Conflicts: kde-i18n < 1:3.5.10-13

Source1: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ar-%{version}.tar.xz
Source2: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ast-%{version}.tar.xz
Source3: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-bg-%{version}.tar.xz
Source4: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-bs-%{version}.tar.xz
Source5: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ca-%{version}.tar.xz
Source6: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ca@valencia-%{version}.tar.xz
Source7: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-cs-%{version}.tar.xz
Source8: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-da-%{version}.tar.xz
Source9: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-de-%{version}.tar.xz
Source10: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-el-%{version}.tar.xz
Source11: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-en_GB-%{version}.tar.xz
Source12: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-eo-%{version}.tar.xz
Source13: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-es-%{version}.tar.xz
Source14: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-et-%{version}.tar.xz
Source15: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-eu-%{version}.tar.xz
Source16: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-fa-%{version}.tar.xz
Source17: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-fi-%{version}.tar.xz
Source18: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-fr-%{version}.tar.xz
Source19: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ga-%{version}.tar.xz
Source20: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-gl-%{version}.tar.xz
Source21: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-he-%{version}.tar.xz
Source22: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-hi-%{version}.tar.xz
Source23: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-hr-%{version}.tar.xz
Source24: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-hu-%{version}.tar.xz
Source25: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ia-%{version}.tar.xz
Source26: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-id-%{version}.tar.xz
Source27: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-is-%{version}.tar.xz
Source28: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-it-%{version}.tar.xz
Source29: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ja-%{version}.tar.xz
Source30: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-kk-%{version}.tar.xz
Source31: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-km-%{version}.tar.xz
Source32: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ko-%{version}.tar.xz
Source33: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-lt-%{version}.tar.xz
Source34: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-lv-%{version}.tar.xz
Source35: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-mr-%{version}.tar.xz
Source36: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-nb-%{version}.tar.xz
Source37: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-nds-%{version}.tar.xz
Source38: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-nl-%{version}.tar.xz
Source39: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-nn-%{version}.tar.xz
Source40: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-pa-%{version}.tar.xz
Source41: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-pl-%{version}.tar.xz
Source42: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-pt-%{version}.tar.xz
Source43: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-pt_BR-%{version}.tar.xz
Source44: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ro-%{version}.tar.xz
Source45: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ru-%{version}.tar.xz
Source46: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-sk-%{version}.tar.xz
Source47: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-sl-%{version}.tar.xz
Source48: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-sr-%{version}.tar.xz
Source49: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-sv-%{version}.tar.xz
Source50: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-tr-%{version}.tar.xz
Source51: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-ug-%{version}.tar.xz
Source52: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-uk-%{version}.tar.xz
Source53: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-wa-%{version}.tar.xz
Source54: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-zh_CN-%{version}.tar.xz
Source55: https://download.kde.org/Attic/applications/%{version}/src/kde-l10n/kde-l10n-zh_TW-%{version}.tar.xz
Source100: kde-l10n-hashes.txt
%description
Internationalization support for KDE.




%prep
( cd %{_sourcedir} && sha256sum -c kde-l10n-hashes.txt )
mkdir src
for f in %{_sourcedir}/kde-l10n-*-%{version}.tar.xz ; do
  tar xJf "$f" -C src
done

%install
cd src
for d in kde-l10n-*-17.04.1 ; do
  lang=${d#kde-l10n-}; lang=${lang%-17.04.1}
  find $d -name '*.po' | while read p ; do
    app=$(basename $p .po)
    out=%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
    mkdir -p $out
    msgfmt -o $out/$app.mo $p
  done
done

%files
%dir %{_datadir}/locale/


%package -n kde-l10n-ar
Summary: ar language support for KDE Applications
%description -n kde-l10n-ar
ar language support for KDE Applications.

%files -n kde-l10n-ar
%lang(ar) %{_datadir}/locale/ar/

%package -n kde-l10n-ast
Summary: ast language support for KDE Applications
%description -n kde-l10n-ast
ast language support for KDE Applications.

%files -n kde-l10n-ast
%lang(ast) %{_datadir}/locale/ast/

%package -n kde-l10n-bg
Summary: bg language support for KDE Applications
%description -n kde-l10n-bg
bg language support for KDE Applications.

%files -n kde-l10n-bg
%lang(bg) %{_datadir}/locale/bg/

%package -n kde-l10n-bs
Summary: bs language support for KDE Applications
%description -n kde-l10n-bs
bs language support for KDE Applications.

%files -n kde-l10n-bs
%lang(bs) %{_datadir}/locale/bs/

%package -n kde-l10n-ca
Summary: ca language support for KDE Applications
%description -n kde-l10n-ca
ca language support for KDE Applications.

%files -n kde-l10n-ca
%lang(ca) %{_datadir}/locale/ca/

%package -n kde-l10n-ca-valencia
Summary: Catalan (Valencia) language support for KDE Applications
%description -n kde-l10n-ca-valencia
Catalan (Valencia) language support for KDE Applications.

%files -n kde-l10n-ca-valencia
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/

%package -n kde-l10n-cs
Summary: cs language support for KDE Applications
%description -n kde-l10n-cs
cs language support for KDE Applications.

%files -n kde-l10n-cs
%lang(cs) %{_datadir}/locale/cs/

%package -n kde-l10n-da
Summary: da language support for KDE Applications
%description -n kde-l10n-da
da language support for KDE Applications.

%files -n kde-l10n-da
%lang(da) %{_datadir}/locale/da/

%package -n kde-l10n-de
Summary: de language support for KDE Applications
%description -n kde-l10n-de
de language support for KDE Applications.

%files -n kde-l10n-de
%lang(de) %{_datadir}/locale/de/

%package -n kde-l10n-el
Summary: el language support for KDE Applications
%description -n kde-l10n-el
el language support for KDE Applications.

%files -n kde-l10n-el
%lang(el) %{_datadir}/locale/el/

%package -n kde-l10n-en_GB
Summary: British English language support for KDE Applications
%description -n kde-l10n-en_GB
British English language support for KDE Applications.

%files -n kde-l10n-en_GB
%lang(en_GB) %{_datadir}/locale/en_GB/

%package -n kde-l10n-eo
Summary: eo language support for KDE Applications
%description -n kde-l10n-eo
eo language support for KDE Applications.

%files -n kde-l10n-eo
%lang(eo) %{_datadir}/locale/eo/

%package -n kde-l10n-es
Summary: es language support for KDE Applications
%description -n kde-l10n-es
es language support for KDE Applications.

%files -n kde-l10n-es
%lang(es) %{_datadir}/locale/es/

%package -n kde-l10n-et
Summary: et language support for KDE Applications
%description -n kde-l10n-et
et language support for KDE Applications.

%files -n kde-l10n-et
%lang(et) %{_datadir}/locale/et/

%package -n kde-l10n-eu
Summary: eu language support for KDE Applications
%description -n kde-l10n-eu
eu language support for KDE Applications.

%files -n kde-l10n-eu
%lang(eu) %{_datadir}/locale/eu/

%package -n kde-l10n-fa
Summary: fa language support for KDE Applications
%description -n kde-l10n-fa
fa language support for KDE Applications.

%files -n kde-l10n-fa
%lang(fa) %{_datadir}/locale/fa/

%package -n kde-l10n-fi
Summary: fi language support for KDE Applications
%description -n kde-l10n-fi
fi language support for KDE Applications.

%files -n kde-l10n-fi
%lang(fi) %{_datadir}/locale/fi/

%package -n kde-l10n-fr
Summary: fr language support for KDE Applications
%description -n kde-l10n-fr
fr language support for KDE Applications.

%files -n kde-l10n-fr
%lang(fr) %{_datadir}/locale/fr/

%package -n kde-l10n-ga
Summary: ga language support for KDE Applications
%description -n kde-l10n-ga
ga language support for KDE Applications.

%files -n kde-l10n-ga
%lang(ga) %{_datadir}/locale/ga/

%package -n kde-l10n-gl
Summary: gl language support for KDE Applications
%description -n kde-l10n-gl
gl language support for KDE Applications.

%files -n kde-l10n-gl
%lang(gl) %{_datadir}/locale/gl/

%package -n kde-l10n-he
Summary: he language support for KDE Applications
%description -n kde-l10n-he
he language support for KDE Applications.

%files -n kde-l10n-he
%lang(he) %{_datadir}/locale/he/

%package -n kde-l10n-hi
Summary: hi language support for KDE Applications
%description -n kde-l10n-hi
hi language support for KDE Applications.

%files -n kde-l10n-hi
%lang(hi) %{_datadir}/locale/hi/

%package -n kde-l10n-hr
Summary: hr language support for KDE Applications
%description -n kde-l10n-hr
hr language support for KDE Applications.

%files -n kde-l10n-hr
%lang(hr) %{_datadir}/locale/hr/

%package -n kde-l10n-hu
Summary: hu language support for KDE Applications
%description -n kde-l10n-hu
hu language support for KDE Applications.

%files -n kde-l10n-hu
%lang(hu) %{_datadir}/locale/hu/

%package -n kde-l10n-ia
Summary: ia language support for KDE Applications
%description -n kde-l10n-ia
ia language support for KDE Applications.

%files -n kde-l10n-ia
%lang(ia) %{_datadir}/locale/ia/

%package -n kde-l10n-id
Summary: id language support for KDE Applications
%description -n kde-l10n-id
id language support for KDE Applications.

%files -n kde-l10n-id
%lang(id) %{_datadir}/locale/id/

%package -n kde-l10n-is
Summary: is language support for KDE Applications
%description -n kde-l10n-is
is language support for KDE Applications.

%files -n kde-l10n-is
%lang(is) %{_datadir}/locale/is/

%package -n kde-l10n-it
Summary: it language support for KDE Applications
%description -n kde-l10n-it
it language support for KDE Applications.

%files -n kde-l10n-it
%lang(it) %{_datadir}/locale/it/

%package -n kde-l10n-ja
Summary: ja language support for KDE Applications
%description -n kde-l10n-ja
ja language support for KDE Applications.

%files -n kde-l10n-ja
%lang(ja) %{_datadir}/locale/ja/

%package -n kde-l10n-kk
Summary: kk language support for KDE Applications
%description -n kde-l10n-kk
kk language support for KDE Applications.

%files -n kde-l10n-kk
%lang(kk) %{_datadir}/locale/kk/

%package -n kde-l10n-km
Summary: km language support for KDE Applications
%description -n kde-l10n-km
km language support for KDE Applications.

%files -n kde-l10n-km
%lang(km) %{_datadir}/locale/km/

%package -n kde-l10n-ko
Summary: ko language support for KDE Applications
%description -n kde-l10n-ko
ko language support for KDE Applications.

%files -n kde-l10n-ko
%lang(ko) %{_datadir}/locale/ko/

%package -n kde-l10n-lt
Summary: lt language support for KDE Applications
%description -n kde-l10n-lt
lt language support for KDE Applications.

%files -n kde-l10n-lt
%lang(lt) %{_datadir}/locale/lt/

%package -n kde-l10n-lv
Summary: lv language support for KDE Applications
%description -n kde-l10n-lv
lv language support for KDE Applications.

%files -n kde-l10n-lv
%lang(lv) %{_datadir}/locale/lv/

%package -n kde-l10n-mr
Summary: mr language support for KDE Applications
%description -n kde-l10n-mr
mr language support for KDE Applications.

%files -n kde-l10n-mr
%lang(mr) %{_datadir}/locale/mr/

%package -n kde-l10n-nb
Summary: nb language support for KDE Applications
%description -n kde-l10n-nb
nb language support for KDE Applications.

%files -n kde-l10n-nb
%lang(nb) %{_datadir}/locale/nb/

%package -n kde-l10n-nds
Summary: nds language support for KDE Applications
%description -n kde-l10n-nds
nds language support for KDE Applications.

%files -n kde-l10n-nds
%lang(nds) %{_datadir}/locale/nds/

%package -n kde-l10n-nl
Summary: nl language support for KDE Applications
%description -n kde-l10n-nl
nl language support for KDE Applications.

%files -n kde-l10n-nl
%lang(nl) %{_datadir}/locale/nl/

%package -n kde-l10n-nn
Summary: nn language support for KDE Applications
%description -n kde-l10n-nn
nn language support for KDE Applications.

%files -n kde-l10n-nn
%lang(nn) %{_datadir}/locale/nn/

%package -n kde-l10n-pa
Summary: pa language support for KDE Applications
%description -n kde-l10n-pa
pa language support for KDE Applications.

%files -n kde-l10n-pa
%lang(pa) %{_datadir}/locale/pa/

%package -n kde-l10n-pl
Summary: pl language support for KDE Applications
%description -n kde-l10n-pl
pl language support for KDE Applications.

%files -n kde-l10n-pl
%lang(pl) %{_datadir}/locale/pl/

%package -n kde-l10n-pt
Summary: pt language support for KDE Applications
%description -n kde-l10n-pt
pt language support for KDE Applications.

%files -n kde-l10n-pt
%lang(pt) %{_datadir}/locale/pt/

%package -n kde-l10n-pt_BR
Summary: Brazilian Portuguese language support for KDE Applications
%description -n kde-l10n-pt_BR
Brazilian Portuguese language support for KDE Applications.

%files -n kde-l10n-pt_BR
%lang(pt_BR) %{_datadir}/locale/pt_BR/

%package -n kde-l10n-ro
Summary: ro language support for KDE Applications
%description -n kde-l10n-ro
ro language support for KDE Applications.

%files -n kde-l10n-ro
%lang(ro) %{_datadir}/locale/ro/

%package -n kde-l10n-ru
Summary: ru language support for KDE Applications
%description -n kde-l10n-ru
ru language support for KDE Applications.

%files -n kde-l10n-ru
%lang(ru) %{_datadir}/locale/ru/

%package -n kde-l10n-sk
Summary: sk language support for KDE Applications
%description -n kde-l10n-sk
sk language support for KDE Applications.

%files -n kde-l10n-sk
%lang(sk) %{_datadir}/locale/sk/

%package -n kde-l10n-sl
Summary: sl language support for KDE Applications
%description -n kde-l10n-sl
sl language support for KDE Applications.

%files -n kde-l10n-sl
%lang(sl) %{_datadir}/locale/sl/

%package -n kde-l10n-sr
Summary: sr language support for KDE Applications
%description -n kde-l10n-sr
sr language support for KDE Applications.

%files -n kde-l10n-sr
%lang(sr) %{_datadir}/locale/sr/

%package -n kde-l10n-sv
Summary: sv language support for KDE Applications
%description -n kde-l10n-sv
sv language support for KDE Applications.

%files -n kde-l10n-sv
%lang(sv) %{_datadir}/locale/sv/

%package -n kde-l10n-tr
Summary: tr language support for KDE Applications
%description -n kde-l10n-tr
tr language support for KDE Applications.

%files -n kde-l10n-tr
%lang(tr) %{_datadir}/locale/tr/

%package -n kde-l10n-ug
Summary: ug language support for KDE Applications
%description -n kde-l10n-ug
ug language support for KDE Applications.

%files -n kde-l10n-ug
%lang(ug) %{_datadir}/locale/ug/

%package -n kde-l10n-uk
Summary: uk language support for KDE Applications
%description -n kde-l10n-uk
uk language support for KDE Applications.

%files -n kde-l10n-uk
%lang(uk) %{_datadir}/locale/uk/

%package -n kde-l10n-wa
Summary: wa language support for KDE Applications
%description -n kde-l10n-wa
wa language support for KDE Applications.

%files -n kde-l10n-wa
%lang(wa) %{_datadir}/locale/wa/

%package -n kde-l10n-zh_CN
Summary: Simplified Chinese language support for KDE Applications
%description -n kde-l10n-zh_CN
Simplified Chinese language support for KDE Applications.

%files -n kde-l10n-zh_CN
%lang(zh_CN) %{_datadir}/locale/zh_CN/

%package -n kde-l10n-zh_TW
Summary: Traditional Chinese language support for KDE Applications
%description -n kde-l10n-zh_TW
Traditional Chinese language support for KDE Applications.

%files -n kde-l10n-zh_TW
%lang(zh_TW) %{_datadir}/locale/zh_TW/

%changelog
* Thu Oct 15 2026 Oreon Packaging Team <packaging@oreonhq.com> - 17.04.1-1
- Import
