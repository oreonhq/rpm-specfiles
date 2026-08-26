%global source0_hash 6844080cc444109ce84e69882a15f7738c6c6acabcc3373267bbd3ae55f4daf2ebb17fa53740f327a48708039eaafcffa0dad89a8b5fe996ced38c92dc5c54fe

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-formatsextra
Epoch:          12
Version:        svn72250
Release:        4%{?dist}
Summary:        Additional formats

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash af2cbe945ac3495e94fbf69797c05d9a7cd8c3874148c54c602a4a152c669638cf7a861949a3cc2d08aa21f378b57beffddf2d13e3afc1157c74472c348f5405
%global source3_hash 298b2e796736f7598a83a2d4fee53f48e78d0c8b255cc09c686371a3a05a4d36736cef96d812281cfd3fe1024af433f32e117c1c60d7559809220ed8dd5e56a9
%global source4_hash 54da97daf172e3dae434e75425b80d1c617ddc9991f6ee804cd812e2c4bd70b49eb1a01318e243c10998870877d4f76e084b5ef0b0eaa89afa66f77a124a7c02
%global source5_hash 76ca0658f861a8562cbcd146f68fd3ff33d7c5f6aef6afcc7737d127b725fd3382537d23c748d86b9a5851b205c9374c6891ef181a20f3513b3ba9c9463fe10e
%global source6_hash 81af373d208f14c4d4ac7d624db3ff0ac63ad32796143e08cc93cc2dc184bde592fa083435a934ccad10a1f018e260bfc1ee844ead1b540242fa76ed9ad63473
%global source7_hash bd07f654ad56219136e2f9e7612b87892bf8c6d0c8f2e41434a7fabb8b159bc43f79444301383adf560f1985f64e639dd496dad6d3ea97ccbd85fcee4d7a36e0
%global source8_hash 31eb2aa643ec37d68d902f4de7be391e7da3af61bde93e78beb1e6df1c6367fcfe00f88e29c8cc878b9cd40f2e3a45f9e46bf24ca3a5608aeae09be491130fef
%global source9_hash 8fdc06f22bc9d25b61cb7b3b151919b7d2d6cf3d78f3cfe5a11284d9246acb858410ccab56996cd521eb98518be9c232a4c8e0f8ebbe52d7e93c510e3a0ac070
%global source10_hash 96f9d64c8f668f67afe20dad97d1cd3cfec19df3300204831fbfe0d245c1e15d8d0cea48bb94fb002cfa18db45d3ade730848908b0d77b867fff7557b0fb826f
%global source11_hash 2253d07d753a5c20c29c2ebb97446453d2c0912c9f26b2e3bd78676e7c3c2ee82953e188e62253c80da538546481da58602b5478b2b8ccb3a6f7554ee41d228b
%global source12_hash 7dce0f9b7781ca89ba93c1607acc0b440ffcf482a1927d0709aa0e914531e250a4f1ef24b64ee63008351c7b206fc092f9211966fb92bb6e0214f296da872677
%global source13_hash c337900dc35cf0e02667d0eed6ac28aafc5336fa39bd7cd90dcf910ab27ebb741abe0ad7b0182fa8018c945cf9d4951db062d1ecfa9a9758e6e9940a0af0b0b3
%global source14_hash 65d5b1c2f5b49f3ceba1fab6021ea4445aec25f302145586331468d727a9cfd992e444b0e53f3aae132308492f15d8f76c5c18cdcb405d9d06dcef6a443a4e23
%global source15_hash a4693b80da94c5644e85c43b93a73ca385097fd2b395856d497e5a138b54063d98d59a8957937d2e2e6ef8948f59d0b1cf74defe50de0b7c5c0fe3c1da83c9a6

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-formatsextra.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antomega.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/antomega.doc.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lambda.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mxedruli.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mxedruli.doc.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omega.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omega.doc.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/otibet.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/otibet.doc.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/passivetex.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psizzl.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psizzl.doc.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/startex.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/startex.doc.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-aleph
Requires:       texlive-antomega
Requires:       texlive-collection-basic
Requires:       texlive-collection-latex
Requires:       texlive-eplain
Requires:       texlive-hitex
Requires:       texlive-jadetex
Requires:       texlive-lambda
Requires:       texlive-lollipop
Requires:       texlive-mltex
Requires:       texlive-mxedruli
Requires:       texlive-omega
Requires:       texlive-omegaware
Requires:       texlive-otibet
Requires:       texlive-passivetex
Requires:       texlive-psizzl
Requires:       texlive-startex
Requires:       texlive-texsis
Requires:       texlive-xmltex

%description
Collected TeX `formats', i.e., large-scale macro packages designed to be dumped
into .fmt files -- excluding the most common ones, such as latex and context,
which have their own package(s). It also includes the Aleph engine and related
Omega formats and packages, and the HiTeX engine and related.

%package -n texlive-antomega
Summary:        Alternative language support for Omega/Lambda
Version:        svn21933
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-omega
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Provides:       tex(antomega.sty) = %{tl_version}
Provides:       tex(grhyph16.tex) = %{tl_version}
Provides:       tex(lgc0700.def) = %{tl_version}
Provides:       tex(lgrenc-antomega.def) = %{tl_version}
Provides:       tex(ograhyph4.tex) = %{tl_version}
Provides:       tex(ogrmhyph4.tex) = %{tl_version}
Provides:       tex(ogrphyph4.tex) = %{tl_version}
Provides:       tex(omega-english.ldf) = %{tl_version}
Provides:       tex(omega-french.ldf) = %{tl_version}
Provides:       tex(omega-german.ldf) = %{tl_version}
Provides:       tex(omega-greek.ldf) = %{tl_version}
Provides:       tex(omega-latin.ldf) = %{tl_version}
Provides:       tex(omega-latvian.ldf) = %{tl_version}
Provides:       tex(omega-polish.ldf) = %{tl_version}
Provides:       tex(omega-russian.ldf) = %{tl_version}
Provides:       tex(omega-spanish.ldf) = %{tl_version}
Provides:       tex(ruhyph16.tex) = %{tl_version}
Provides:       tex(t1enc-antomega.def) = %{tl_version}
Provides:       tex(t2aenc-antomega.def) = %{tl_version}
Provides:       tex(uni0100.def) = %{tl_version}
Provides:       tex(uni0370.def) = %{tl_version}
Provides:       tex(uni0400.def) = %{tl_version}
Provides:       tex(uni1f00.def) = %{tl_version}
Provides:       tex(ut1enc-antomega.def) = %{tl_version}

%description -n texlive-antomega
A language support package for Omega/Lambda. This replaces the original omega
package for use with Lambda, and provides extra facilities (including
Babel-like language switching, which eases porting of LaTeX documents to
Lambda).

%package -n texlive-lambda
Summary:        LaTeX for Omega and Aleph
Version:        svn45756
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(elhyph16.tex) = %{tl_version}
Provides:       tex(grcodes.tex) = %{tl_version}
Provides:       tex(grmhyph.tex) = %{tl_version}
Provides:       tex(lambda.tex) = %{tl_version}
Provides:       tex(lchenc.def) = %{tl_version}
Provides:       tex(ocherokee.sty) = %{tl_version}
Provides:       tex(odev.sty) = %{tl_version}
Provides:       tex(ojapan.sty) = %{tl_version}
Provides:       tex(omega.sty) = %{tl_version}
Provides:       tex(ut1enc.def) = %{tl_version}

%description -n texlive-lambda
LaTeX for Omega and Aleph

%package -n texlive-mxedruli
Summary:        A pair of fonts for different Georgian alphabets
Version:        svn71991
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mxedruli.sty) = %{tl_version}
Provides:       tex(xucuri.sty) = %{tl_version}

%description -n texlive-mxedruli
Two Georgian fonts, in both Metafont and Type 1 formats, which cover the
Mxedruli and the Xucuri alphabets.

%package -n texlive-omega
Summary:        A wide-character-set extension of TeX
Version:        svn33046
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(bghyph.tex) = %{tl_version}
Provides:       tex(grlccode.tex) = %{tl_version}
Provides:       tex(lthyph.tex) = %{tl_version}
Provides:       tex(omega.tex) = %{tl_version}
Provides:       tex(srhyph.tex) = %{tl_version}

%description -n texlive-omega
A development of TeX, which deals in multi-octet Unicode characters, to enable
native treatment of a wide range of languages without changing character-set.
Work on Omega has ceased (the TeX Live package contains only support files);
its compatible successor is aleph, which is itself also in major maintenance
mode only. Ongoing projects developing Omega (and Aleph) ideas include Omega-2
and LuaTeX.

%package -n texlive-otibet
Summary:        Support for Tibetan using Omega
Version:        svn45777
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(otibet.sty) = %{tl_version}
Provides:       tex(otibet.tex) = %{tl_version}

%description -n texlive-otibet
support for Tibetan using Omega

%package -n texlive-passivetex
Summary:        Support package for XML/SGML typesetting
Version:        svn69742
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(bm.sty)
Requires:       tex(color.sty)
# Ignoring dependency on elfonts.sty - not part of TeX Live
Requires:       tex(eucal.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pifont.sty)
Requires:       tex(rotating.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(times.sty)
Requires:       tex(tipa.sty)
Requires:       tex(tone.sty)
Requires:       tex(ulem.sty)
Requires:       tex(url.sty)
Requires:       tex(wasysym.sty)
Provides:       tex(dummyels.sty) = %{tl_version}
Provides:       tex(fotex.sty) = %{tl_version}
Provides:       tex(mlnames.sty) = %{tl_version}
Provides:       tex(teixml.sty) = %{tl_version}
Provides:       tex(teixmlslides.sty) = %{tl_version}
Provides:       tex(ucharacters.sty) = %{tl_version}
Provides:       tex(unicode.sty) = %{tl_version}

%description -n texlive-passivetex
Packages providing XML parsing, UTF-8 parsing, Unicode entities, and common
formatting object definitions for jadetex.

%package -n texlive-psizzl
Summary:        A TeX format for physics papers
Version:        svn69742
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(mypsizzl.tex) = %{tl_version}
Provides:       tex(psizzl.tex) = %{tl_version}

%description -n texlive-psizzl
PSIZZL is a TeX format for physics papers written at SLAC and used at several
other places. It dates from rather early in the development of TeX82; as a
result, some of the descriptions of limitations look rather quaint to modern
eyes.

%package -n texlive-startex
Summary:        An XML-inspired format for student use
Version:        svn69742
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(startex.tex) = %{tl_version}

%description -n texlive-startex
A TeX format designed to help students write short reports and essays. It
provides the user with a suitable set of commands for such a task. It is also
more robust than plain TeX and LaTeX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE3} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE4} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE5} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE6} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE7} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE8} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE9} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE10} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE11} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE12} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE13} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE14} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE15} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-antomega
%license lppl1.3c.txt
%{_texmf_main}/omega/ocp/antomega/
%{_texmf_main}/omega/otp/antomega/
%{_texmf_main}/tex/lambda/antomega/
%doc %{_texmf_main}/doc/omega/antomega/

%files -n texlive-lambda
%license lppl1.3c.txt
%{_texmf_main}/tex/lambda/base/
%{_texmf_main}/tex/lambda/config/

%files -n texlive-mxedruli
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/public/mxedruli/
%{_texmf_main}/fonts/map/dvips/mxedruli/
%{_texmf_main}/fonts/source/public/mxedruli/
%{_texmf_main}/fonts/tfm/public/mxedruli/
%{_texmf_main}/fonts/type1/public/mxedruli/
%{_texmf_main}/tex/latex/mxedruli/
%doc %{_texmf_main}/doc/fonts/mxedruli/

%files -n texlive-omega
%license gpl2.txt
%{_texmf_main}/dvips/omega/
%{_texmf_main}/fonts/afm/public/omega/
%{_texmf_main}/fonts/map/dvips/omega/
%{_texmf_main}/fonts/ofm/public/omega/
%{_texmf_main}/fonts/ovf/public/omega/
%{_texmf_main}/fonts/ovp/public/omega/
%{_texmf_main}/fonts/tfm/public/omega/
%{_texmf_main}/fonts/type1/public/omega/
%{_texmf_main}/omega/ocp/char2uni/
%{_texmf_main}/omega/ocp/misc/
%{_texmf_main}/omega/ocp/omega/
%{_texmf_main}/omega/ocp/uni2char/
%{_texmf_main}/omega/otp/char2uni/
%{_texmf_main}/omega/otp/misc/
%{_texmf_main}/omega/otp/omega/
%{_texmf_main}/omega/otp/uni2char/
%{_texmf_main}/tex/generic/encodings/
%{_texmf_main}/tex/generic/omegahyph/
%{_texmf_main}/tex/plain/omega/
%doc %{_texmf_main}/doc/omega/base/

%files -n texlive-otibet
%license lppl1.3c.txt
%{_texmf_main}/fonts/ofm/public/otibet/
%{_texmf_main}/fonts/ovf/public/otibet/
%{_texmf_main}/fonts/ovp/public/otibet/
%{_texmf_main}/fonts/source/public/otibet/
%{_texmf_main}/fonts/tfm/public/otibet/
%{_texmf_main}/omega/ocp/otibet/
%{_texmf_main}/omega/otp/otibet/
%{_texmf_main}/tex/latex/otibet/
%doc %{_texmf_main}/doc/latex/otibet/

%files -n texlive-passivetex
%license mit.txt
%{_texmf_main}/tex/xmltex/passivetex/

%files -n texlive-psizzl
%license lppl1.3c.txt
%{_texmf_main}/tex/psizzl/base/
%{_texmf_main}/tex/psizzl/config/
%doc %{_texmf_main}/doc/otherformats/psizzl/

%files -n texlive-startex
%license pd.txt
%{_texmf_main}/makeindex/startex/
%{_texmf_main}/tex/startex/
%doc %{_texmf_main}/doc/otherformats/startex/

%changelog
%autochangelog
