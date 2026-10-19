%global source0_hash d0e3bb6f3b4e75748680524a1d116f2bfb145618f8ceed55b279d15098a530f9
Name:          tesseract-tessdata
Version:       4.1.0
Release:        1%{?dist}
Summary:        Trained models for the Tesseract Open Source OCR Engine
BuildArch:     noarch
License:       Apache-2.0
URL:           https://github.com/tesseract-ocr/tessdata_fast
%if 0%{?commit:1}
Source0:        https://github.com/tesseract-ocr/tessdata_fast/archive/%{version}/tessdata_fast-%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
# oreon:deps

# /oreon:deps
%description
This package contains fast integer versions of trained models for the Tesseract
Open Source OCR Engine.

These models only work with the LSTM OCR engine of Tesseract 4.

%package        doc
Summary:        Documentation for %{name}
%description    doc
The %{name}-doc package contains the documentation for %{name}.

%package -n tesseract-osd
Summary:       Orientation & Script Detection Data for tesseract
BuildArch:     noarch
Requires:      tesseract
Requires:      %{name}-doc = %{version}-%{release}
%description -n tesseract-osd
Orientation & Script Detection data for the Tesseract Open Source OCR Engine.

%package -n tesseract-equ
Summary:       Equation traineddata for tesseract
BuildArch:     noarch
Requires:      tesseract
Requires:      %{name}-doc = %{version}-%{release}
%description -n tesseract-equ
Data for processing images of mathematics with the Tesseract Open Source OCR Engine.

# define lang_subpkg macro
# m: 3 letter macrolanguage code
# l: langcode used in Provides and Supplements tags
# n: language name
# -m and -n is needed for subpackages, -l is optional
#
%define lang_subpkg(l:m:n:) \
%define macrolang %{-m:%{-m*}}%{!-m:%{error:3 letter Language code not defined}} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package -n tesseract-langpack-%{macrolang}\
Summary:       %{langname} language data for %{name}\
BuildArch:     noarch\
Requires:      tesseract-common\
Requires:      %{name}-doc = %{version}-%{release}\
%{-l:Provides:      %{name}-langpack-%{-l*} = %{version}-%{release}\
Supplements:   (tesseract and langpacks-%{-l*})}\
\
%description -n tesseract-langpack-%{macrolang}\
This package contains the fast integer version of the %{langname} language \
trained models for the Tesseract Open Source OCR Engine.\
\
%package -n tesseract-script-%{pkgname}\
Summary:       %{scriptname} script data for %{name}\
BuildArch:     noarch\
Requires:      tesseract-common\
Requires:      %{name}-doc = %{version}-%{release}\
\
%description -n tesseract-script-%{pkgname}\
This package contains the fast integer version of the %{scriptname} script \
trained models for the Tesseract Open Source OCR Engine.\
\
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?commit:1}
%autosetup -p1 -n tessdata_fast-%{commit}
%else
%autosetup -p1 -n tessdata_fast-%{version}%{?pre:-%pre}
%endif

%build

%install
mkdir -p %{buildroot}/%{_datadir}/tesseract/tessdata/
cp -a * %{buildroot}/%{_datadir}/tesseract/tessdata/
rm -f %{buildroot}/%{_datadir}/tesseract/tessdata/LICENSE
rm -f %{buildroot}/%{_datadir}/tesseract/tessdata/README.md
rm -f %{buildroot}/%{_datadir}/tesseract/tessdata/configs
rm -f %{buildroot}/%{_datadir}/tesseract/tessdata/pdf.ttf
%oreon_autofiles tesseract-osd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tesseract-equ usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tesseract-tessdata-doc -f %{oreon_filedir}/tesseract-tessdata-doc.list
%files -n tesseract-osd -f %{oreon_filedir}/tesseract-osd.list
%files -n tesseract-equ -f %{oreon_filedir}/tesseract-equ.list
%files -n tesseract-langpack-afr -f %{oreon_filedir}/tesseract-langpack-afr.list
%files -n tesseract-langpack-amh -f %{oreon_filedir}/tesseract-langpack-amh.list
%files -n tesseract-langpack-ara -f %{oreon_filedir}/tesseract-langpack-ara.list
%files -n tesseract-langpack-asm -f %{oreon_filedir}/tesseract-langpack-asm.list
%files -n tesseract-langpack-aze -f %{oreon_filedir}/tesseract-langpack-aze.list
%files -n tesseract-langpack-aze_cyrl -f %{oreon_filedir}/tesseract-langpack-aze_cyrl.list
%files -n tesseract-langpack-bel -f %{oreon_filedir}/tesseract-langpack-bel.list
%files -n tesseract-langpack-ben -f %{oreon_filedir}/tesseract-langpack-ben.list
%files -n tesseract-langpack-bod -f %{oreon_filedir}/tesseract-langpack-bod.list
%files -n tesseract-langpack-bos -f %{oreon_filedir}/tesseract-langpack-bos.list
%files -n tesseract-langpack-bre -f %{oreon_filedir}/tesseract-langpack-bre.list
%files -n tesseract-langpack-bul -f %{oreon_filedir}/tesseract-langpack-bul.list
%files -n tesseract-langpack-cat -f %{oreon_filedir}/tesseract-langpack-cat.list
%files -n tesseract-langpack-ceb -f %{oreon_filedir}/tesseract-langpack-ceb.list
%files -n tesseract-langpack-ces -f %{oreon_filedir}/tesseract-langpack-ces.list
%files -n tesseract-langpack-chi_sim -f %{oreon_filedir}/tesseract-langpack-chi_sim.list
%files -n tesseract-langpack-chi_sim_vert -f %{oreon_filedir}/tesseract-langpack-chi_sim_vert.list
%files -n tesseract-langpack-chi_tra -f %{oreon_filedir}/tesseract-langpack-chi_tra.list
%files -n tesseract-langpack-chi_tra_vert -f %{oreon_filedir}/tesseract-langpack-chi_tra_vert.list
%files -n tesseract-langpack-chr -f %{oreon_filedir}/tesseract-langpack-chr.list
%files -n tesseract-langpack-cos -f %{oreon_filedir}/tesseract-langpack-cos.list
%files -n tesseract-langpack-cym -f %{oreon_filedir}/tesseract-langpack-cym.list
%files -n tesseract-langpack-dan -f %{oreon_filedir}/tesseract-langpack-dan.list
%files -n tesseract-langpack-deu -f %{oreon_filedir}/tesseract-langpack-deu.list
%files -n tesseract-langpack-div -f %{oreon_filedir}/tesseract-langpack-div.list
%files -n tesseract-langpack-dzo -f %{oreon_filedir}/tesseract-langpack-dzo.list
%files -n tesseract-langpack-ell -f %{oreon_filedir}/tesseract-langpack-ell.list
%files -n tesseract-langpack-eng -f %{oreon_filedir}/tesseract-langpack-eng.list
%files -n tesseract-langpack-enm -f %{oreon_filedir}/tesseract-langpack-enm.list
%files -n tesseract-langpack-epo -f %{oreon_filedir}/tesseract-langpack-epo.list
%files -n tesseract-langpack-est -f %{oreon_filedir}/tesseract-langpack-est.list
%files -n tesseract-langpack-eus -f %{oreon_filedir}/tesseract-langpack-eus.list
%files -n tesseract-langpack-fao -f %{oreon_filedir}/tesseract-langpack-fao.list
%files -n tesseract-langpack-fas -f %{oreon_filedir}/tesseract-langpack-fas.list
%files -n tesseract-langpack-fil -f %{oreon_filedir}/tesseract-langpack-fil.list
%files -n tesseract-langpack-fin -f %{oreon_filedir}/tesseract-langpack-fin.list
%files -n tesseract-langpack-fra -f %{oreon_filedir}/tesseract-langpack-fra.list
%files -n tesseract-langpack-frk -f %{oreon_filedir}/tesseract-langpack-frk.list
%files -n tesseract-langpack-frm -f %{oreon_filedir}/tesseract-langpack-frm.list
%files -n tesseract-langpack-fry -f %{oreon_filedir}/tesseract-langpack-fry.list
%files -n tesseract-langpack-gla -f %{oreon_filedir}/tesseract-langpack-gla.list
%files -n tesseract-langpack-gle -f %{oreon_filedir}/tesseract-langpack-gle.list
%files -n tesseract-langpack-glg -f %{oreon_filedir}/tesseract-langpack-glg.list
%files -n tesseract-langpack-grc -f %{oreon_filedir}/tesseract-langpack-grc.list
%files -n tesseract-langpack-guj -f %{oreon_filedir}/tesseract-langpack-guj.list
%files -n tesseract-langpack-hat -f %{oreon_filedir}/tesseract-langpack-hat.list
%files -n tesseract-langpack-heb -f %{oreon_filedir}/tesseract-langpack-heb.list
%files -n tesseract-langpack-hin -f %{oreon_filedir}/tesseract-langpack-hin.list
%files -n tesseract-langpack-hrv -f %{oreon_filedir}/tesseract-langpack-hrv.list
%files -n tesseract-langpack-hun -f %{oreon_filedir}/tesseract-langpack-hun.list
%files -n tesseract-langpack-hye -f %{oreon_filedir}/tesseract-langpack-hye.list
%files -n tesseract-langpack-iku -f %{oreon_filedir}/tesseract-langpack-iku.list
%files -n tesseract-langpack-ind -f %{oreon_filedir}/tesseract-langpack-ind.list
%files -n tesseract-langpack-isl -f %{oreon_filedir}/tesseract-langpack-isl.list
%files -n tesseract-langpack-ita -f %{oreon_filedir}/tesseract-langpack-ita.list
%files -n tesseract-langpack-ita_old -f %{oreon_filedir}/tesseract-langpack-ita_old.list
%files -n tesseract-langpack-jav -f %{oreon_filedir}/tesseract-langpack-jav.list
%files -n tesseract-langpack-jpn -f %{oreon_filedir}/tesseract-langpack-jpn.list
%files -n tesseract-langpack-jpn_vert -f %{oreon_filedir}/tesseract-langpack-jpn_vert.list
%files -n tesseract-langpack-kan -f %{oreon_filedir}/tesseract-langpack-kan.list
%files -n tesseract-langpack-kat -f %{oreon_filedir}/tesseract-langpack-kat.list
%files -n tesseract-langpack-kat_old -f %{oreon_filedir}/tesseract-langpack-kat_old.list
%files -n tesseract-langpack-kaz -f %{oreon_filedir}/tesseract-langpack-kaz.list
%files -n tesseract-langpack-khm -f %{oreon_filedir}/tesseract-langpack-khm.list
%files -n tesseract-langpack-kir -f %{oreon_filedir}/tesseract-langpack-kir.list
%files -n tesseract-langpack-kor -f %{oreon_filedir}/tesseract-langpack-kor.list
%files -n tesseract-langpack-kor_vert -f %{oreon_filedir}/tesseract-langpack-kor_vert.list
%files -n tesseract-langpack-kmr -f %{oreon_filedir}/tesseract-langpack-kmr.list
%files -n tesseract-langpack-lao -f %{oreon_filedir}/tesseract-langpack-lao.list
%files -n tesseract-langpack-lat -f %{oreon_filedir}/tesseract-langpack-lat.list
%files -n tesseract-langpack-lav -f %{oreon_filedir}/tesseract-langpack-lav.list
%files -n tesseract-langpack-lit -f %{oreon_filedir}/tesseract-langpack-lit.list
%files -n tesseract-langpack-ltz -f %{oreon_filedir}/tesseract-langpack-ltz.list
%files -n tesseract-langpack-mal -f %{oreon_filedir}/tesseract-langpack-mal.list
%files -n tesseract-langpack-mar -f %{oreon_filedir}/tesseract-langpack-mar.list
%files -n tesseract-langpack-mkd -f %{oreon_filedir}/tesseract-langpack-mkd.list
%files -n tesseract-langpack-mlt -f %{oreon_filedir}/tesseract-langpack-mlt.list
%files -n tesseract-langpack-mon -f %{oreon_filedir}/tesseract-langpack-mon.list
%files -n tesseract-langpack-mri -f %{oreon_filedir}/tesseract-langpack-mri.list
%files -n tesseract-langpack-msa -f %{oreon_filedir}/tesseract-langpack-msa.list
%files -n tesseract-langpack-mya -f %{oreon_filedir}/tesseract-langpack-mya.list
%files -n tesseract-langpack-nep -f %{oreon_filedir}/tesseract-langpack-nep.list
%files -n tesseract-langpack-nld -f %{oreon_filedir}/tesseract-langpack-nld.list
%files -n tesseract-langpack-nor -f %{oreon_filedir}/tesseract-langpack-nor.list
%files -n tesseract-langpack-oci -f %{oreon_filedir}/tesseract-langpack-oci.list
%files -n tesseract-langpack-ori -f %{oreon_filedir}/tesseract-langpack-ori.list
%files -n tesseract-langpack-pan -f %{oreon_filedir}/tesseract-langpack-pan.list
%files -n tesseract-langpack-pol -f %{oreon_filedir}/tesseract-langpack-pol.list
%files -n tesseract-langpack-por -f %{oreon_filedir}/tesseract-langpack-por.list
%files -n tesseract-langpack-pus -f %{oreon_filedir}/tesseract-langpack-pus.list
%files -n tesseract-langpack-que -f %{oreon_filedir}/tesseract-langpack-que.list
%files -n tesseract-langpack-ron -f %{oreon_filedir}/tesseract-langpack-ron.list
%files -n tesseract-langpack-rus -f %{oreon_filedir}/tesseract-langpack-rus.list
%files -n tesseract-langpack-san -f %{oreon_filedir}/tesseract-langpack-san.list
%files -n tesseract-langpack-sin -f %{oreon_filedir}/tesseract-langpack-sin.list
%files -n tesseract-langpack-slk -f %{oreon_filedir}/tesseract-langpack-slk.list
%files -n tesseract-langpack-slv -f %{oreon_filedir}/tesseract-langpack-slv.list
%files -n tesseract-langpack-snd -f %{oreon_filedir}/tesseract-langpack-snd.list
%files -n tesseract-langpack-spa -f %{oreon_filedir}/tesseract-langpack-spa.list
%files -n tesseract-langpack-spa_old -f %{oreon_filedir}/tesseract-langpack-spa_old.list
%files -n tesseract-langpack-sqi -f %{oreon_filedir}/tesseract-langpack-sqi.list
%files -n tesseract-langpack-srp -f %{oreon_filedir}/tesseract-langpack-srp.list
%files -n tesseract-langpack-srp_latn -f %{oreon_filedir}/tesseract-langpack-srp_latn.list
%files -n tesseract-langpack-sun -f %{oreon_filedir}/tesseract-langpack-sun.list
%files -n tesseract-langpack-swa -f %{oreon_filedir}/tesseract-langpack-swa.list
%files -n tesseract-langpack-swe -f %{oreon_filedir}/tesseract-langpack-swe.list
%files -n tesseract-langpack-syr -f %{oreon_filedir}/tesseract-langpack-syr.list
%files -n tesseract-langpack-tam -f %{oreon_filedir}/tesseract-langpack-tam.list
%files -n tesseract-langpack-tat -f %{oreon_filedir}/tesseract-langpack-tat.list
%files -n tesseract-langpack-tel -f %{oreon_filedir}/tesseract-langpack-tel.list
%files -n tesseract-langpack-tgk -f %{oreon_filedir}/tesseract-langpack-tgk.list
%files -n tesseract-langpack-tha -f %{oreon_filedir}/tesseract-langpack-tha.list
%files -n tesseract-langpack-tir -f %{oreon_filedir}/tesseract-langpack-tir.list
%files -n tesseract-langpack-ton -f %{oreon_filedir}/tesseract-langpack-ton.list
%files -n tesseract-langpack-tur -f %{oreon_filedir}/tesseract-langpack-tur.list
%files -n tesseract-langpack-uig -f %{oreon_filedir}/tesseract-langpack-uig.list
%files -n tesseract-langpack-ukr -f %{oreon_filedir}/tesseract-langpack-ukr.list
%files -n tesseract-langpack-urd -f %{oreon_filedir}/tesseract-langpack-urd.list
%files -n tesseract-langpack-uzb -f %{oreon_filedir}/tesseract-langpack-uzb.list
%files -n tesseract-langpack-uzb_cyrl -f %{oreon_filedir}/tesseract-langpack-uzb_cyrl.list
%files -n tesseract-langpack-vie -f %{oreon_filedir}/tesseract-langpack-vie.list
%files -n tesseract-langpack-yid -f %{oreon_filedir}/tesseract-langpack-yid.list
%files -n tesseract-langpack-yor -f %{oreon_filedir}/tesseract-langpack-yor.list
%files -n tesseract-script-arabic -f %{oreon_filedir}/tesseract-script-arabic.list
%files -n tesseract-script-armenian -f %{oreon_filedir}/tesseract-script-armenian.list
%files -n tesseract-script-bengali -f %{oreon_filedir}/tesseract-script-bengali.list
%files -n tesseract-script-canadian_aboriginal -f %{oreon_filedir}/tesseract-script-canadian_aboriginal.list
%files -n tesseract-script-cherokee -f %{oreon_filedir}/tesseract-script-cherokee.list
%files -n tesseract-script-cyrillic -f %{oreon_filedir}/tesseract-script-cyrillic.list
%files -n tesseract-script-devanagari -f %{oreon_filedir}/tesseract-script-devanagari.list
%files -n tesseract-script-ethiopic -f %{oreon_filedir}/tesseract-script-ethiopic.list
%files -n tesseract-script-fraktur -f %{oreon_filedir}/tesseract-script-fraktur.list
%files -n tesseract-script-georgian -f %{oreon_filedir}/tesseract-script-georgian.list
%files -n tesseract-script-greek -f %{oreon_filedir}/tesseract-script-greek.list
%files -n tesseract-script-gujarati -f %{oreon_filedir}/tesseract-script-gujarati.list
%files -n tesseract-script-gurmukhi -f %{oreon_filedir}/tesseract-script-gurmukhi.list
%files -n tesseract-script-hans -f %{oreon_filedir}/tesseract-script-hans.list
%files -n tesseract-script-hans_vert -f %{oreon_filedir}/tesseract-script-hans_vert.list
%files -n tesseract-script-hant -f %{oreon_filedir}/tesseract-script-hant.list
%files -n tesseract-script-hant_vert -f %{oreon_filedir}/tesseract-script-hant_vert.list
%files -n tesseract-script-hangul -f %{oreon_filedir}/tesseract-script-hangul.list
%files -n tesseract-script-hangul_vert -f %{oreon_filedir}/tesseract-script-hangul_vert.list
%files -n tesseract-script-hebrew -f %{oreon_filedir}/tesseract-script-hebrew.list
%files -n tesseract-script-japanese -f %{oreon_filedir}/tesseract-script-japanese.list
%files -n tesseract-script-japanese_vert -f %{oreon_filedir}/tesseract-script-japanese_vert.list
%files -n tesseract-script-kannada -f %{oreon_filedir}/tesseract-script-kannada.list
%files -n tesseract-script-khmer -f %{oreon_filedir}/tesseract-script-khmer.list
%files -n tesseract-script-lao -f %{oreon_filedir}/tesseract-script-lao.list
%files -n tesseract-script-latin -f %{oreon_filedir}/tesseract-script-latin.list
%files -n tesseract-script-malayalam -f %{oreon_filedir}/tesseract-script-malayalam.list
%files -n tesseract-script-myanmar -f %{oreon_filedir}/tesseract-script-myanmar.list
%files -n tesseract-script-oriya -f %{oreon_filedir}/tesseract-script-oriya.list
%files -n tesseract-script-sinhala -f %{oreon_filedir}/tesseract-script-sinhala.list
%files -n tesseract-script-syriac -f %{oreon_filedir}/tesseract-script-syriac.list
%files -n tesseract-script-tamil -f %{oreon_filedir}/tesseract-script-tamil.list
%files -n tesseract-script-telugu -f %{oreon_filedir}/tesseract-script-telugu.list
%files -n tesseract-script-thaana -f %{oreon_filedir}/tesseract-script-thaana.list
%files -n tesseract-script-thai -f %{oreon_filedir}/tesseract-script-thai.list
%files -n tesseract-script-tibetan -f %{oreon_filedir}/tesseract-script-tibetan.list
%files -n tesseract-script-vietnamese -f %{oreon_filedir}/tesseract-script-vietnamese.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.0-12
- Import
