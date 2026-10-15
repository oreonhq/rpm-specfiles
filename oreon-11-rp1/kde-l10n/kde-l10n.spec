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

%description
Internationalization support for KDE.

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


%global l10n_hashes kde-l10n-ar-17.04.1.tar.xz:7bbcd32164fc1c9e553c9c11f31092aeea8e9b27d52ede386f861c84b6d67ba8 \\
kde-l10n-ast-17.04.1.tar.xz:14f3d6502c8fe2fe3102df81123e85436b639f17670f8d1925fa38be8cc89d19 \\
kde-l10n-bg-17.04.1.tar.xz:893ddd50f94efbe79db592923606785da3b66c546b703e7bbd5bc1b61230a191 \\
kde-l10n-bs-17.04.1.tar.xz:210088507785d3a6606d5b1fe20cf95e7897c98ba01bf61adbe55455de1d4091 \\
kde-l10n-ca-17.04.1.tar.xz:12fce2ea402a25e1f4205399be68241e235e9461c8e33b05a0c74f3dc7bf239b \\
kde-l10n-ca@valencia-17.04.1.tar.xz:8ee61d32450ec20004c87f317d37af1e254baaf487076ca0c177fe102fefd912 \\
kde-l10n-cs-17.04.1.tar.xz:acc4ae135e3bae247b03a8bacc4b3fefcdce387baa0e4cad8f14969b28c470da \\
kde-l10n-da-17.04.1.tar.xz:b5bae6e47a369f741d60163e78bf7a5b9f89dad7ee9b07e80fdff3d1d0f266f1 \\
kde-l10n-de-17.04.1.tar.xz:15a5108c9c9a3d36780fe0ad9c3af16db5e908c4214133015251d30cfcf4b35b \\
kde-l10n-el-17.04.1.tar.xz:4df7158b1a3568956611f8b0ef1c8edb086c5a634df9ead8e7fccb8aee5b7a93 \\
en_GB-17.04.1.tar.xz:7fb1136d2c684ce619bba9e47eb882acf9e4af33c49c9833b26e5121fcc70722 \\
kde-l10n-eo-17.04.1.tar.xz:65c6231aa7d2faa64d0dde93d4625af0651997913c31f5918955480f323e88bc \\
kde-l10n-es-17.04.1.tar.xz:a7bcf1a6b94f9382cb50281411129a9f1f6547d3863a43b5d42ca2ea694ddd03 \\
kde-l10n-et-17.04.1.tar.xz:3baac031d1ee1bb9adc32451be30ef47c56dedf42b4dbd7b7c5112b1341cb17c \\
kde-l10n-eu-17.04.1.tar.xz:d39683729c35be4d7a5ec0d38503dbc15d17d6a20877cf37caa785fdf8246001 \\
kde-l10n-fa-17.04.1.tar.xz:3933f7f0696cca459a6e4f658bce48977f8c8762cece197acd850e65c1901a1a \\
kde-l10n-fi-17.04.1.tar.xz:e1574734025314d1dc2c87d6930ea6acbdffee30d47c7fca39f9bdcfc580bfcb \\
kde-l10n-fr-17.04.1.tar.xz:468015a1a0195b9eaeee0e9f1ac782f8458145a9d0153d74ca1a1d263b97b973 \\
kde-l10n-ga-17.04.1.tar.xz:9cf35dad9289e47df9558ace6b88afd4b4cc7ecdc6cebcab776b05839040f793 \\
kde-l10n-gl-17.04.1.tar.xz:ede51207e6fa0f149a22fd907b000f67e1618131423abcbd44d794d40d9fe6dc \\
kde-l10n-he-17.04.1.tar.xz:9681dda9c6b53156f618c055ed44703569860c51fa19e8e9eb3530c3e198e8ea \\
kde-l10n-hi-17.04.1.tar.xz:90a9ea1ebdaeb3445b9c6bcddd34efa06afc6bc701f43144ae090cfd968eab85 \\
kde-l10n-hr-17.04.1.tar.xz:fe43b9e48a138e0598fc2cdd7ccc5a66c54e1a11a59b45a3be8d10de28963fc6 \\
kde-l10n-hu-17.04.1.tar.xz:4b740d81b708ee56f536a315310ea94526ddf9f69ebb6795601d6e7130ba6329 \\
kde-l10n-ia-17.04.1.tar.xz:c344d4f2f714361bbab2d1c52d6ed75239cc905c5de20589221d23711edc41eb \\
kde-l10n-id-17.04.1.tar.xz:9de258fd75aee4f5991537e768d723b458aeebbff722c54593435476516e609f \\
kde-l10n-is-17.04.1.tar.xz:685f1d413a37408a2c26cc333bf47cd23e472bfa9c4c3ba3478197f2c5d51321 \\
kde-l10n-it-17.04.1.tar.xz:523b73531ebf2928f1d694ce05db7fc142fd67b08ca6dc149fe08734da338b18 \\
kde-l10n-ja-17.04.1.tar.xz:4f0df9d222ade32b89bd9f5d1b763c89db9b8c6092788a1e912141949302be04 \\
kde-l10n-kk-17.04.1.tar.xz:bf21476a0b5058d626a702cef9901a8dc64dc8d3505b56dbcd2b96be03d0f524 \\
kde-l10n-km-17.04.1.tar.xz:c34b3263e6ebb158f18f819e18ece53e5f836dc5ad4f16abd2ab42a69335a407 \\
kde-l10n-ko-17.04.1.tar.xz:af362af1016b05c70e0bffe913c29e658daf8dfea6022d7b45ae6e9ab585cad9 \\
kde-l10n-lt-17.04.1.tar.xz:09c7643fe110627473262d2ef8ca7c17d4f49b9bd24757cbeee7407d41efb60c \\
kde-l10n-lv-17.04.1.tar.xz:821fea5332cc6ec9ad4ba25792481efe211f08f4a5142fb8fe13f70455da0a94 \\
kde-l10n-mr-17.04.1.tar.xz:248b88e4b458a575f2dd846c0a06227dfa3bf6ffa2778304670107cd6f77ec9f \\
kde-l10n-nb-17.04.1.tar.xz:835289e5eefab7eb9c4b982d12c88f523dd0b57612c8a6f99ef1ab28c434ecb1 \\
kde-l10n-nds-17.04.1.tar.xz:1a822a792467eddc084ef736421f365357ce6fc79f0f8f7782489cf96788944c \\
kde-l10n-nl-17.04.1.tar.xz:513bcb76e2f9ee1c8bdacbe37b88008bbec8f9e27f8ed8f36e851747c1787c3d \\
kde-l10n-nn-17.04.1.tar.xz:989c4d916a1d43dbf469c6eb8a9398413466a4a4898f96f892729db808a89099 \\
kde-l10n-pa-17.04.1.tar.xz:d887d831a9150b1b1501bdc1a06d8bcef4b5c924f90baa1ee1618b2cc5d7e1c1 \\
kde-l10n-pl-17.04.1.tar.xz:27bfe116bd5a4f3fbe1f5887d0c3d493fd608f87f633031c5e8233dbd4e47648 \\
kde-l10n-pt-17.04.1.tar.xz:f480638c68936b39d2a783d9b4caa5497e84fb0126d0bd59bc01d3e25be574a0 \\
pt_BR-17.04.1.tar.xz:5cb56cd90ae98c926f0af93a4c8e5a9e75927cf0825bcc51ed32795a46868669 \\
kde-l10n-ro-17.04.1.tar.xz:e71df3af002ef71bc736dba6ac11c4c983c184e3737aec51a356856eea9b286d \\
kde-l10n-ru-17.04.1.tar.xz:ccf5ee4eb9b9d0158b6388e957de92dbc9d4d5f486163189ba87fc0d8a7c8d05 \\
kde-l10n-sk-17.04.1.tar.xz:903a7f51606af43e05429697514a777e825d923fa44ea5454ae387d591cc09cb \\
kde-l10n-sl-17.04.1.tar.xz:2367101237ee2e69b5aa73abd6c3ef78c74e331fa3b89ddb6cc9eee43428f27e \\
kde-l10n-sr-17.04.1.tar.xz:28ea0e28e374b7c4bba85fb3e530566f223016d65e9b9df70895cc143c3ed1e4 \\
kde-l10n-sv-17.04.1.tar.xz:044afc38b3869151aef8e5228c6eb7a4c8c01522ecb9a4f396634a7621931732 \\
kde-l10n-tr-17.04.1.tar.xz:460a9f0d1097c8e52554aed83e5f5fdb00506ab9f3df6fb7981ebf89a5d36b4c \\
kde-l10n-ug-17.04.1.tar.xz:95cc33bf64ca54f0d15383c368cee1a4bb3dcb9ec2d68fddaa580164cef6a937 \\
kde-l10n-uk-17.04.1.tar.xz:522a33038ed0dc0265d9cfca96b57337a4c19d9c1e9e7131583c11a96f2308c7 \\
kde-l10n-wa-17.04.1.tar.xz:1a2496976d5e135681481ae2265effe54ccea9209714e5b78024803ce2f66209 \\
zh_CN-17.04.1.tar.xz:b0cf455e603d86ebea64818ba1e9c4be9392c06c33e6c7a8b69241256e80efad \\
zh_TW-17.04.1.tar.xz:78f75255ed7d03d7434e66656942d362e12a78e42f01b8985c782c98061eb030

%prep
for entry in %{l10n_hashes} ; do
  f=${entry%%:*}
  h=${entry#*:}
  test -f "%{_sourcedir}/$f" || { echo "oreon: missing source $f" >&2; exit 1; }
  got=$(sha256sum "%{_sourcedir}/$f" | awk '{print $1}')
  test "$got" = "$h" || { echo "oreon: source hash mismatch $f" >&2; exit 1; }
done
mkdir src
for s in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ; do
  tar xJf %{SOURCE$s} -C src
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
