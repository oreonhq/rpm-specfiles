%global source0_hash 00ba0bf08b9a5ff9300b1a5ef7041fff139c9543dad9bac6b4d09619aaba66b9b347417a3bca02a4c474a785315810742a18080cb918b9f9445b7775e9ff0321

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langcjk
Epoch:          12
Version:        svn65824
Release:        4%{?dist}
Summary:        Chinese/Japanese/Korean (base)

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 363f7fd337e5a34737608a2bc37521bb526ce726f5c9b5b4d08416e534448306002bc7af1be3f5e6fefcaba16ffc2260c4dea8a486d44dbccad577fb04d6da5b
%global source3_hash 2350e99bfd047ea514586894d20bd37dc778c74fd4c1848063ba7d53cb59ed5df36cd20fd51140ede8af7f32ed7efc44e1d4f3db4a0baaa7d1439941ed5297a9
%global source4_hash 9561381312a2e3fcd6a03da1082e9bdb5a2c30e241078adbb70d06060a21674fc8a40c5cb81ce87d31ff99c168d73e9b4074cb3a6114439d5a441dd0054cc682
%global source5_hash b13712912e479dab68cab9027042be8cb11047ebf9c034f532c857e83d28f19dfea5a1748685cfe1847c7372f2d0982f79736525694d937c88962c5262094585
%global source6_hash a8c6b2d4d0899b841ccc32b378855d61bdaa65d5f68fd408df3894d386bcde18f384410f34e6f33ee2a5ce770e1e663a05ab038d9b7483012a3cb414739c3705
%global source7_hash cb44aa3386cd79f05980e5402adcbbf9f8b67fa76bdd5b293063fe9810520edbdf243656cfb54fe17d6ca43d405e6b16e8012eda63bae3cb3d8fc0f7755e2551
%global source8_hash cb9383b6d3fe9ffd5926d10dddcb1ea758aabda232f015b22f61dc8a9b316193b30ca2d8e2b849b1c03d92e0073bba6d90cc5b3b50f47b28a745dff2f7229486
%global source9_hash 27a4c150b3b5e3fa23e0df55289154d44e3eaa55330544e426cdd3126f8ce0308abcc17fa5a011e12d83460616cad039cc483f08d7254b64d4dae933db6273d9
%global source10_hash ff08a32b6283fc7ca0454e0071ce1d90b7a6fbf8989ca3eb4cc1f804f002f920890b083e5aa81a9455f57659a4df52b6c4677096621d9dffefa37c318e79a0f9
%global source11_hash ef98234e6c6609dc9ea6f60027c3dad1f417d677d5177525945330122b9b513a90bd296ba86a1d96eadb52792b5d162264578118872d5a7b1794b4a1a7fe06a4
%global source12_hash 541f27a2119bd0694a9afe8dcf39649a6ae57ca66bfeb9493dd130b7815088463a258a5528e590ab78bdcd2ab1d92cc9fd559c9223a120b155d56609d3e9d762
%global source13_hash 10f6dda7da061830718627aa6f3dd570930899ee59928f5380fc6b91263e2f53ced551ba9c85db7b44273d5b15f0459f9fa89bf5aadcfe578a60f2acb93cd2fa
%global source14_hash a806538598cae0365968ab20936631a052dc65f9f6056c39197f7b1c7a5aad717a7a8b72ed2a1af347f8ce91f27d7dcd74b758db8f01fc7810a8d658990bcc28
%global source15_hash 5f65927546348815b07c93003a2b0922403d274bfa3d1665d4649c9dbc737df924958c2fd61c1d06cd5e7c1862aff392c8d1e9d827f4ae79e70d9b76467f651d
%global source16_hash 48f469ebeed1e7c43124ce4576636d9a13c4cfa6ce548734ef8dc8c449b048353a2fcb78019817ea47f5a72d830e6efafe2682e6c97b208491ae025a4aaa7bae
%global source17_hash 7e5d4e6a42ae1c41cb26109b036e125beb9111c0a5230ac9c1c7bbe91a4d0eec83ef94373c0fb8220b07a41d37af78d1f6966e0bb217661786a2678332e04c1c
%global source18_hash db0be3360dc3d6373866c9d27900f8dba9353bcf92d219f9f0b82532e2855210230a06b87d1ab6eef7e1f96c54e46884e6827395affb9375120b7cf8d2fbb99b
%global source19_hash 6a9958bc6ddf6d167b9d77a513d04f0077c9a8581109c51166410d60d5a243758da62b40bdf5cb1488a50b9ba76ca89261a2d31c3819d8b2738b4a7023ac3f90
%global source20_hash 40e4c9c5f2195021cde4859da7b137de0cdf0c96b83f7ddbf724c682e1dd07276cb83bf4004b2b7cb5f90b6033da54940b3c58aeb2ca231b9ce449ee32d3a3d8
%global source21_hash bd810a93bcb3849456c28a28456db65e75a74921412d93f22564c8f87342f4dab8edfbd531a530374a678ad3624bc593736116736b387b5d43960e8143af4a73
%global source22_hash 792911a9a80ed0613db8a1daab226f3e8ad747d6f695524a03882a12d9c6ebe6634d20c7e17851961aef0bcbde23dc59765abe0387a512e1790c0fd51292cfe2
%global source23_hash be4b89820c7a11dbcaab46f380efe28281d49498eef66040c65723bcf5600e9311db45dd47055f8ef8aa27406f02883add6fefb5d9817f3f65693a2221159574
%global source24_hash 552365f862e319bf2d649e5aba40ca4d252b2986782a1f1c4bc8f2902ffb2f2fe73973c183bd465588506a073c6bb919cfdac438fa9275e2bc9e7a6bdcd956c9
%global source25_hash e94ec8794d6f47d3de1c437a7171d2bb0d68c752ebcdf101790b77b32430ed440eb9d814f1821fcd6cc4d04a9b4ae412b989cb5b0a6c91dcc4b9610c611be785

Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/collection-langcjk.tar.xz#/collection-langcjk.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/adobemapping.tar.xz#/adobemapping.or11.tar.xz
Source3:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/c90.tar.xz#/c90.or11.tar.xz
Source4:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/c90.doc.tar.xz#/c90.doc.or11.tar.xz
Source5:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cjk.tar.xz#/cjk.or11.tar.xz
Source6:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cjk.doc.tar.xz#/cjk.doc.or11.tar.xz
Source7:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cjkpunct.tar.xz#/cjkpunct.or11.tar.xz
Source8:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/cjkpunct.doc.tar.xz#/cjkpunct.doc.or11.tar.xz
Source9:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/dnp.tar.xz#/dnp.or11.tar.xz
Source10:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/evangelion-jfm.tar.xz#/evangelion-jfm.or11.tar.xz
Source11:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/evangelion-jfm.doc.tar.xz#/evangelion-jfm.doc.or11.tar.xz
Source12:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/fixjfm.tar.xz#/fixjfm.or11.tar.xz
Source13:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/fixjfm.doc.tar.xz#/fixjfm.doc.or11.tar.xz
Source14:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/garuda-c90.tar.xz#/garuda-c90.or11.tar.xz
Source15:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/norasi-c90.tar.xz#/norasi-c90.or11.tar.xz
Source16:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxtatescale.tar.xz#/pxtatescale.or11.tar.xz
Source17:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/pxtatescale.doc.tar.xz#/pxtatescale.doc.or11.tar.xz
Source18:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xcjk2uni.tar.xz#/xcjk2uni.or11.tar.xz
Source19:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xcjk2uni.doc.tar.xz#/xcjk2uni.doc.or11.tar.xz
Source20:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xecjk.tar.xz#/xecjk.or11.tar.xz
Source21:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xecjk.doc.tar.xz#/xecjk.doc.or11.tar.xz
Source22:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zitie.tar.xz#/zitie.or11.tar.xz
Source23:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zitie.doc.tar.xz#/zitie.doc.or11.tar.xz
Source24:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zxjafont.tar.xz#/zxjafont.or11.tar.xz
Source25:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zxjafont.doc.tar.xz#/zxjafont.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-adobemapping
Requires:       texlive-c90
Requires:       texlive-cjk
Requires:       texlive-cjk-gs-integrate
Requires:       texlive-cjkpunct
Requires:       texlive-cjkutils
Requires:       texlive-collection-basic
Requires:       texlive-dnp
Requires:       texlive-evangelion-jfm
Requires:       texlive-fixjfm
Requires:       texlive-garuda-c90
Requires:       texlive-jfmutil
Requires:       texlive-norasi-c90
Requires:       texlive-pxtatescale
Requires:       texlive-xcjk2uni
Requires:       texlive-xecjk
Requires:       texlive-zitie
Requires:       texlive-zxjafont

%description
Packages supporting a combination of Chinese, Japanese, Korean, including
macros, fonts, documentation. Also Thai in the c90 encoding, since there is
some overlap in those fonts; standard Thai support is in collection-langother.
Additional packages for CJK are in their individual language collections.

%package -n texlive-adobemapping
Summary:        Adobe cmap and pdfmapping files
Version:        svn66552
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-adobemapping
The package comprises the collection of CMap and PDF mapping files made
available for distribution by Adobe.

%package -n texlive-c90
Summary:        C90 font encoding for Thai
Version:        svn60830
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-c90
part of the CJK package, ctan.org/pkg/cjk

%package -n texlive-cjk
Summary:        CJK language support
Version:        svn60865
License:        GPL-2.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-arphic
Requires:       texlive-cns
Requires:       texlive-garuda-c90
Requires:       texlive-norasi-c90
Requires:       texlive-uhc
Requires:       texlive-wadalab
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(ulem.sty)
Provides:       tex(CJK.sty) = %{tl_version}
Provides:       tex(CJKfntef.sty) = %{tl_version}
Provides:       tex(CJKnumb.sty) = %{tl_version}
Provides:       tex(CJKspace.sty) = %{tl_version}
Provides:       tex(CJKulem.sty) = %{tl_version}
Provides:       tex(CJKutf8.sty) = %{tl_version}
Provides:       tex(CJKvert.sty) = %{tl_version}
Provides:       tex(MULEenc.sty) = %{tl_version}
Provides:       tex(c90enc.def) = %{tl_version}
Provides:       tex(pinyin.ldf) = %{tl_version}
Provides:       tex(pinyin.sty) = %{tl_version}
Provides:       tex(pshan.sty) = %{tl_version}
Provides:       tex(ruby.sty) = %{tl_version}
Provides:       tex(thaicjk.ldf) = %{tl_version}

%description -n texlive-cjk
CJK is a macro package for LaTeX, providing simultaneous support for various
Asian scripts in many encodings (including Unicode): Chinese (both traditional
and simplified), Japanese, Korean and Thai. A special add-on feature is an
interface to the Emacs editor (cjk-enc.el) which gives simultaneous,
easy-to-use support to a bunch of other scripts in addition to the above --
Cyrillic, Greek, Latin-based scripts, Russian and Vietnamese are supported.

%package -n texlive-cjkpunct
Summary:        Adjust locations and kerning of CJK punctuation marks
Version:        svn41119
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(CJKpunct.sty) = %{tl_version}

%description -n texlive-cjkpunct
The package serves as a companion package for CJK.

%package -n texlive-dnp
Summary:        Subfont numbers for DNP font encoding
Version:        svn54074
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-dnp
part of the CJK package, ctan.org/pkg/cjk

%package -n texlive-evangelion-jfm
Summary:        A Japanese font metric supporting many advanced features
Version:        svn69751
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-evangelion-jfm
This package provides a Japanese Font Metric supporting vertical and horizontal
typesetting, 'linegap punctuations', 'extended fonts', and more interesting and
helpful features using traditional ('tc') and simplified ('sc') Chinese or
Japanese fonts under LuaTeX-ja. It also makes full use of the 'priority'
feature, meeting the standards, and allows easy customisation.

%package -n texlive-fixjfm
Summary:        Fix JFM (for *pTeX)
Version:        svn77677
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(fixjfm.sty) = %{tl_version}

%description -n texlive-fixjfm
This package fixes several bugs in the JFM format. Both LaTeX and plain TeX are
supported.

%package -n texlive-garuda-c90
Summary:        TeX support (from CJK) for the garuda font
Version:        svn60832
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fonts-tlwg

%description -n texlive-garuda-c90
TeX support (from CJK) for the garuda font

%package -n texlive-norasi-c90
Summary:        TeX support (from CJK) for the norasi font
Version:        svn60831
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-fonts-tlwg

%description -n texlive-norasi-c90
TeX support (from CJK) for the norasi font

%package -n texlive-pxtatescale
Summary:        Patch to graphics driver for scaling in vertical direction of pTeX
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(pxtatescale.sty) = %{tl_version}

%description -n texlive-pxtatescale
Patch for graphics driver 'dvipdfmx' to support correct scaling in vertical
direction of Japanese pTeX/upTeX.

%package -n texlive-xcjk2uni
Summary:        Convert CJK characters to Unicode, in pdfTeX
Version:        svn54958
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(xCJK2uni-UBg5plus.def) = %{tl_version}
Provides:       tex(xCJK2uni-UBig5.def) = %{tl_version}
Provides:       tex(xCJK2uni-UGB.def) = %{tl_version}
Provides:       tex(xCJK2uni-UGBK.def) = %{tl_version}
Provides:       tex(xCJK2uni-UJIS.def) = %{tl_version}
Provides:       tex(xCJK2uni-UKS.def) = %{tl_version}
Provides:       tex(xCJK2uni.sty) = %{tl_version}

%description -n texlive-xcjk2uni
The package provides commands to convert CJK characters to Unicode in non-UTF-8
encoding; it provides hooks to support hyperref in producing correct bookmarks.
The bundle also provides /ToUnicode mapping file(s) for a CJK subfont; these
can be used with the cmap package, allowing searches of, and cut-and-paste
operations on a PDF file generated by pdfTeX.

%package -n texlive-xecjk
Summary:        Support for CJK documents in XeLaTeX
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-ctex
Provides:       tex(xeCJK-listings.sty) = %{tl_version}
Provides:       tex(xeCJK.sty) = %{tl_version}
Provides:       tex(xeCJKfntef.sty) = %{tl_version}
Provides:       tex(xunicode-addon.sty) = %{tl_version}
Provides:       tex(xunicode-extra.def) = %{tl_version}

%description -n texlive-xecjk
A LaTeX package for typesetting CJK documents in the way users have become used
to, in the CJK package. The package requires a current version of xtemplate
(and hence of the current LaTeX3 development environment).

%package -n texlive-zitie
Summary:        Create CJK character calligraphy practicing sheets
Version:        svn77677
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(zitie.luatex.def) = %{tl_version}
Provides:       tex(zitie.sty) = %{tl_version}
Provides:       tex(zitie.xetex.def) = %{tl_version}

%description -n texlive-zitie
This is a LaTeX package for creating CJK character calligraphy practicing
sheets (copybooks). Currently, only XeTeX is supported.

%package -n texlive-zxjafont
Summary:        Set up Japanese font families for XeLaTeX
Version:        svn77677
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(keyval.sty)
Provides:       tex(zxjafont.sty) = %{tl_version}

%description -n texlive-zxjafont
Set up Japanese font families for XeLaTeX

%prep
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h_expected="%{source2_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h_expected="%{source3_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h_expected="%{source4_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h_expected="%{source5_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h_expected="%{source6_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
test "%{source7_hash}" = "none" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h_expected="%{source7_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source7_hash}" || { echo "oreon: Source7 hash mismatch" >&2; exit 1; }; }
test "%{source8_hash}" = "none" || { f="%{SOURCE8}"; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h_expected="%{source8_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source8_hash}" || { echo "oreon: Source8 hash mismatch" >&2; exit 1; }; }
test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h_expected="%{source9_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; }
test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h_expected="%{source10_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; }
test "%{source11_hash}" = "none" || { f="%{SOURCE11}"; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h_expected="%{source11_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source11_hash}" || { echo "oreon: Source11 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h_expected="%{source12_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
test "%{source13_hash}" = "none" || { f="%{SOURCE13}"; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h_expected="%{source13_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source13_hash}" || { echo "oreon: Source13 hash mismatch" >&2; exit 1; }; }
test "%{source14_hash}" = "none" || { f="%{SOURCE14}"; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h_expected="%{source14_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source14_hash}" || { echo "oreon: Source14 hash mismatch" >&2; exit 1; }; }
test "%{source15_hash}" = "none" || { f="%{SOURCE15}"; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h_expected="%{source15_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source15_hash}" || { echo "oreon: Source15 hash mismatch" >&2; exit 1; }; }
test "%{source16_hash}" = "none" || { f="%{SOURCE16}"; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h_expected="%{source16_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source16_hash}" || { echo "oreon: Source16 hash mismatch" >&2; exit 1; }; }
test "%{source17_hash}" = "none" || { f="%{SOURCE17}"; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h_expected="%{source17_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source17_hash}" || { echo "oreon: Source17 hash mismatch" >&2; exit 1; }; }
test "%{source18_hash}" = "none" || { f="%{SOURCE18}"; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h_expected="%{source18_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source18_hash}" || { echo "oreon: Source18 hash mismatch" >&2; exit 1; }; }
test "%{source19_hash}" = "none" || { f="%{SOURCE19}"; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h_expected="%{source19_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source19_hash}" || { echo "oreon: Source19 hash mismatch" >&2; exit 1; }; }
test "%{source20_hash}" = "none" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h_expected="%{source20_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source20_hash}" || { echo "oreon: Source20 hash mismatch" >&2; exit 1; }; }
test "%{source21_hash}" = "none" || { f="%{SOURCE21}"; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h_expected="%{source21_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source21_hash}" || { echo "oreon: Source21 hash mismatch" >&2; exit 1; }; }
test "%{source22_hash}" = "none" || { f="%{SOURCE22}"; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h_expected="%{source22_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source22_hash}" || { echo "oreon: Source22 hash mismatch" >&2; exit 1; }; }
test "%{source23_hash}" = "none" || { f="%{SOURCE23}"; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h_expected="%{source23_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source23_hash}" || { echo "oreon: Source23 hash mismatch" >&2; exit 1; }; }
test "%{source24_hash}" = "none" || { f="%{SOURCE24}"; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h_expected="%{source24_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source24_hash}" || { echo "oreon: Source24 hash mismatch" >&2; exit 1; }; }
test "%{source25_hash}" = "none" || { f="%{SOURCE25}"; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h_expected="%{source25_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source25_hash}" || { echo "oreon: Source25 hash mismatch" >&2; exit 1; }; }
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
tar -xf %{SOURCE16} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE17} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE18} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE19} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE20} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE21} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE22} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE23} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE24} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE25} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-adobemapping
%license bsd.txt
%{_texmf_main}/fonts/cmap/adobemapping/

%files -n texlive-c90
%license gpl2.txt
%{_texmf_main}/fonts/enc/dvips/c90/
%doc %{_texmf_main}/doc/fonts/enc/

%files -n texlive-cjk
%license gpl2.txt
%{_texmf_main}/tex/latex/cjk/
%doc %{_texmf_main}/doc/latex/cjk/

%files -n texlive-cjkpunct
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/cjkpunct/
%doc %{_texmf_main}/doc/latex/cjkpunct/

%files -n texlive-dnp
%license gpl2.txt
%{_texmf_main}/fonts/sfd/dnp/

%files -n texlive-evangelion-jfm
%license mit.txt
%{_texmf_main}/tex/luatex/evangelion-jfm/
%doc %{_texmf_main}/doc/luatex/evangelion-jfm/

%files -n texlive-fixjfm
%license knuth.txt
%{_texmf_main}/tex/generic/fixjfm/
%doc %{_texmf_main}/doc/generic/fixjfm/

%files -n texlive-garuda-c90
%license lppl1.3c.txt
%{_texmf_main}/dvips/garuda-c90/
%{_texmf_main}/fonts/map/dvips/garuda-c90/
%{_texmf_main}/fonts/tfm/public/garuda-c90/

%files -n texlive-norasi-c90
%license lppl1.3c.txt
%{_texmf_main}/dvips/norasi-c90/
%{_texmf_main}/fonts/map/dvips/norasi-c90/
%{_texmf_main}/fonts/tfm/public/norasi-c90/

%files -n texlive-pxtatescale
%license mit.txt
%{_texmf_main}/tex/latex/pxtatescale/
%doc %{_texmf_main}/doc/latex/pxtatescale/

%files -n texlive-xcjk2uni
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/xcjk2uni/
%doc %{_texmf_main}/doc/latex/xcjk2uni/

%files -n texlive-xecjk
%license lppl1.3c.txt
%{_texmf_main}/fonts/misc/xetex/fontmapping/
%{_texmf_main}/tex/xelatex/xecjk/
%doc %{_texmf_main}/doc/xelatex/xecjk/

%files -n texlive-zitie
%license lppl1.3c.txt
%{_texmf_main}/tex/xelatex/zitie/
%doc %{_texmf_main}/doc/xelatex/zitie/

%files -n texlive-zxjafont
%license mit.txt
%{_texmf_main}/tex/latex/zxjafont/
%doc %{_texmf_main}/doc/latex/zxjafont/

%changelog
%autochangelog
