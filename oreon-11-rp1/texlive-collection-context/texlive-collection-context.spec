%global source0_hash 8eed418d43e1f14d4bc867313bbfd5e2acaf6afbed4f7e376666db21e2bff2598190a00caee4b34998f86ccc8511c8ef9ea9b13a1c616ba87b0dd96ce6c9e982

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-context
Epoch:          12
Version:        svn75426
Release:        4%{?dist}
Summary:        ConTeXt and packages

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash b00de64b9050b88adda6efabedc45838944c5587158ee8cacc71e79664945294989b24d3e751fdb36b91fe12fecb91f859a45454206866300e4e7499ec884da1
%global source3_hash 8a0b6caddc510841d10e72dbe3ee76dae69606e5b88155ea85ec66b60edd581f0621c087bb857fb94eb9ee8a16690939e83dcb422d45dab397aaf92439e4549d
%global source4_hash aae09b844ae244839f82088ffbad9c777355696023fa95c24221b6ae0e4ac6dfce6a4d70efe9f09d5e5dc89e6e7a17d98282a77b90697ee6a3496ed0568734b4
%global source5_hash 62a63d54d0388a027cb6afa58141a6fc303fde6cc0f989348fe29fd10e825a03d86ff682f480723b223b606e296591cf03092c886cf13cde03463ff8012caca1
%global source6_hash 27b5dceae2d462c2e9c6aee0885163fd69b023b92b5f5f6dd52a30ab842c6e8eda8d690200e3a30bf3608d32e433d785aa8f90a6e83de25b485431e7c21efed1
%global source7_hash 3e5f06fcb75babfba4f3537cc303f85df5e4b593ebc79b81784618072e372df17c72932e339d126eb9d2586468534904b18ca39473f2b858c7637494c373399b
%global source8_hash dec8338854260467eb5d6542d4561e38a87183290e53e75c3fa188fc8f537a466ce4a5974f4f5644b9f2e62591cd4e8860f8e2b314c8918ae45e90e00c61ba4d
%global source9_hash 6a5d88d6091e95025e7a4f12a6e831e5bf462156afa06c7b49d35086f9b555ed8fc1ed9cde970146106f3efc29b70bf0699c1b5eadcf970c1f8978c46ad590bc
%global source10_hash 14a90656d706d68ce441301aa6bccf2033c36f9c8d8605ec9dedeeedb71a5670dae325a5a198b2ca25373eb2b495e57fff31b85089c6c0fb987738c76ac636b2
%global source11_hash d95b1df26033aaff0a9f6759268ac3e68bff02556001e3f9b2bae1db68aa13c839a87047a6ae0a296f8e5817398ba35b7cbacc4f194dd93cf72684904190e7e3
%global source12_hash c2534b543fd5444776a054f43fafa393040af5bcb67f869d61d200a4a1d0355f1d81c64adab683d15a6be806a21dfc9ad661995bbe51da3c0bfb841ade4b077f
%global source13_hash a9c2ea88b0e2514840c368ea7686894dda4b86c93ec8f34989238ffdf5704f1c1898d0ee5e0724035314d2d37803f1a1afdd445dd802a94f5ff4223148f81767
%global source14_hash 8021c3bb6bb1b03e77766ee6dfc7ab6b4a66bdaebe82be11e53878c16692f410ea21986122ec5752cbdd1b4c9a3046798eb899dcc34ebe4b21a5bcd93a3be73c
%global source15_hash 41a4a1e9dcb709ecf6e81f3104e5ab8fa61f0c931d80e59b2b7235bb5dbfab5cf3ffdff59d86c2e7b98096b56a138eeb7a93f1958276ca9640c93e3facb62b12
%global source16_hash cb761c8c0b2201be37c4612483047732a249ead5f3c86720ec88a696e48f42e1b003ca3490275f26df6b2f4d08d2a3dab17b818f0c5a98945b06a3ed70b18c9f
%global source17_hash cc254e29e0cf0d985b57cdab62edd685bf9335376729825ef651fc095b7239099c003f86d306154e6bb811b44d36625f8da3dcbf4b6f735bc9efb53037113594
%global source18_hash 09a2d99825566b7be6932ccec832095c137d01119cb8c5e7bb7cb15f9efbf63c8bb83d31ce55f097c0e79f7e5139c9e0362b42faa39e5491ec007756c7fcc539
%global source19_hash 696ac4949aca175b33f146982502eae04fefc11d13e0483fdad37edcf3c9bc337ce01aaa1b763bcd23b12fde1e7e2ba6c9c6700ec55fc197731f47892061ee95
%global source20_hash e4c689c745d06c61d6f693a9832001aa8c79d51664c2a5d6d0c6148a95b30870063f50eecca31ac0924193c6dab8c12cd5ccaca16eeaf5f83a99cef1a8889ec3
%global source21_hash f2c33244814da8e8838483038f507fe6b3e146f37691e55a37bb5355985d2af4c5fc423318133c4f13837a3e66a4fe72d5c14f6721bb5ee0417a59691b86d3f1
%global source22_hash 0b767274ee6b714400613485409889a9c429c9c30e6d339f87b95c633e42d1cec89ac2231e96857379dfecce923d15001177d2c0c8954a68c74570368f19f181
%global source23_hash 20d7845b6bf78dd7c26511185eb8c17e9c3dcdd1b49f5db607125066e2b469bdab5a4a5d7e228c5c464666b699f8a5e2964ae0c083fd887859b7513a18b2e26f
%global source24_hash eb10c183b9674f13abbf093fd9ee929ee56410ab1b64863ec6613933dc64e9a00983f860a2fc51b0124e698dcd5c67eb3721d9262130ae087d06331eb05932b1
%global source25_hash ac0c5ca04c6f13a2320c87dfda147acaf3015f0f86241ca6b6c5eb37fe9ab6cb4502ffd3421c01706a898ddc3c4790bf2dffabd5d86b2ed9e006b311c4620c31
%global source26_hash 083b1f0b70a74a3648501314fa993632534f476376fb80eb4444b0273866bf4a4d562e4bfffbd14ed79be0020361ab6cc5c40fde1f99544b76d6f33939781f19
%global source27_hash e7a410ec0d99f945dae91c041b396875a6350aa06333f5a5d2d7aa4c6bb62f926ec53a27a1c95a724ce7b320ddef11d6550b0b92a34c00ac63c7c0da96a35928
%global source28_hash 5668a801015f4462c7096016725cbeafc1a5779857c4ade883a02b7e4bf77224fae8566e1ce90cec24008f9b9a9b228bdee69fd162b0bedcb79bdda480863810
%global source29_hash f582dbb65e754d61fb1547b4ca92aec904dc729ad15493c07c347207f0f0de2821c5921cac445972778c45179e89e51366a2ec788453afe1485f194405a6ce52
%global source30_hash 12fab8b1e1aaf3f114351503f6d0aa8bcddaa0d6a2638918a2f8688e06390d2cfdce053ac1247b27e82c90328b7c5979b484ba53687320203b6055ac54c35e88
%global source31_hash 07ef8ce6ddd64b9e8d1f26dc950672ba880390d539ad52f880469133775d76d9fbe69541b9c4bfae2c50447f7cacb7058e7759b2e4f7adf33fc64dc7d0cf0f44
%global source32_hash f919d3f9e6ab25932cfaeadfc07f86ebdbe00d84dc21236e4775930fc3866cee69cf9a25d373e13655f4396a3c395ea6ea103a28ffb4f00a4e95b7ceaec155c9
%global source33_hash 8473c1ca7b48009055f5c33031ec60f80d84dc43396789b0c0c7e6d65bcf014a237088dca07211beae4bfb80377f55cf12a9f379995cff50f52143fc4bc81295
%global source34_hash d729fb634f821343c6265c7831815aa837dccc5c738eb8dedfe62c96764ce679d5706596f3910a5c8d6cf8826e2c95624f590ae7c39de0e1df2ec73bb549e544
%global source35_hash 684bdd78ca79a205d8234da3f42f2f2439755448f40d82a694981aad9c70b5923977c5ee91c4f04a88cfcc52be954020d9adf0120bbbc00321da722bad4bb4b8
%global source36_hash 12100c7aa3eb555cf9dbe72454a96e63feda52329a8a192ff86ba30477acab4ebaaf84c15a79f16d4e3f95cef02baf8146e5810b8c9e8e94c25ba1317bf4fc2c
%global source37_hash 0f49e22b9e1d465f46727a9e952e095eceab55e77a2559fe497cf14690377f77ca42aa23ce7eaca659e9b0983e5a950b36733eef49b0473fd33a8f783edb43b1
%global source38_hash 63ed91ff58f024dc7a460dfd70cb3fe5b06937f3cebd5e2dbbc53058eac37c4454926acf18b61dc772b9775b56b0ad5664bd1b9540c36e4d974f7173e8cdf112
%global source39_hash 1cc71a1bf46f5b39264894a7d17caeb74436cdc0254c1870a3399ac2b3d6256ff3b90250b901dcd60b393c438e7bf7083a5244c1d0caff30e008da0d3484c389
%global source40_hash 2e250c3f115911c56f9b8d46d358fdef289c624a5b24c9b4213bbf7818bf42c7b778df55d4bf181bce115b388915cedc90ef7cfa99ee6ad8dd621e7853fc7c29

Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/collection-context.tar.xz#/collection-context.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-animation.tar.xz#/context-animation.or11.tar.xz
Source3:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-animation.doc.tar.xz#/context-animation.doc.or11.tar.xz
Source4:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-calendar-examples.tar.xz#/context-calendar-examples.or11.tar.xz
Source5:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-calendar-examples.doc.tar.xz#/context-calendar-examples.doc.or11.tar.xz
Source6:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-chat.tar.xz#/context-chat.or11.tar.xz
Source7:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-chat.doc.tar.xz#/context-chat.doc.or11.tar.xz
Source8:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-collating-marks.tar.xz#/context-collating-marks.or11.tar.xz
Source9:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-collating-marks.doc.tar.xz#/context-collating-marks.doc.or11.tar.xz
Source10:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-cyrillicnumbers.tar.xz#/context-cyrillicnumbers.or11.tar.xz
Source11:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-cyrillicnumbers.doc.tar.xz#/context-cyrillicnumbers.doc.or11.tar.xz
Source12:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-filter.tar.xz#/context-filter.or11.tar.xz
Source13:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-filter.doc.tar.xz#/context-filter.doc.or11.tar.xz
Source14:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-gnuplot.tar.xz#/context-gnuplot.or11.tar.xz
Source15:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-gnuplot.doc.tar.xz#/context-gnuplot.doc.or11.tar.xz
Source16:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-handlecsv.tar.xz#/context-handlecsv.or11.tar.xz
Source17:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-handlecsv.doc.tar.xz#/context-handlecsv.doc.or11.tar.xz
Source18:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-letter.tar.xz#/context-letter.or11.tar.xz
Source19:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-letter.doc.tar.xz#/context-letter.doc.or11.tar.xz
Source20:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-mathsets.tar.xz#/context-mathsets.or11.tar.xz
Source21:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-mathsets.doc.tar.xz#/context-mathsets.doc.or11.tar.xz
Source22:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-notes-zh-cn.tar.xz#/context-notes-zh-cn.or11.tar.xz
Source23:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-notes-zh-cn.doc.tar.xz#/context-notes-zh-cn.doc.or11.tar.xz
Source24:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-pocketdiary.tar.xz#/context-pocketdiary.or11.tar.xz
Source25:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-pocketdiary.doc.tar.xz#/context-pocketdiary.doc.or11.tar.xz
Source26:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-simpleslides.tar.xz#/context-simpleslides.or11.tar.xz
Source27:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-simpleslides.doc.tar.xz#/context-simpleslides.doc.or11.tar.xz
Source28:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-squares.tar.xz#/context-squares.or11.tar.xz
Source29:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-squares.doc.tar.xz#/context-squares.doc.or11.tar.xz
Source30:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-sudoku.tar.xz#/context-sudoku.or11.tar.xz
Source31:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-sudoku.doc.tar.xz#/context-sudoku.doc.or11.tar.xz
Source32:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-transliterator.tar.xz#/context-transliterator.or11.tar.xz
Source33:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-transliterator.doc.tar.xz#/context-transliterator.doc.or11.tar.xz
Source34:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-typescripts.tar.xz#/context-typescripts.or11.tar.xz
Source35:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-typescripts.doc.tar.xz#/context-typescripts.doc.or11.tar.xz
Source36:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-vim.tar.xz#/context-vim.or11.tar.xz
Source37:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-vim.doc.tar.xz#/context-vim.doc.or11.tar.xz
Source38:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-visualcounter.tar.xz#/context-visualcounter.or11.tar.xz
Source39:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context-visualcounter.doc.tar.xz#/context-visualcounter.doc.or11.tar.xz
Source40:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jmn.tar.xz#/jmn.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-collection-basic
Requires:       texlive-context
Requires:       texlive-context-animation
Requires:       texlive-context-calendar-examples
Requires:       texlive-context-chat
Requires:       texlive-context-collating-marks
Requires:       texlive-context-cyrillicnumbers
Requires:       texlive-context-filter
Requires:       texlive-context-gnuplot
Requires:       texlive-context-handlecsv
Requires:       texlive-context-legacy
Requires:       texlive-context-letter
Requires:       texlive-context-mathsets
Requires:       texlive-context-notes-zh-cn
Requires:       texlive-context-pocketdiary
Requires:       texlive-context-simpleslides
Requires:       texlive-context-squares
Requires:       texlive-context-sudoku
Requires:       texlive-context-transliterator
Requires:       texlive-context-typescripts
Requires:       texlive-context-vim
Requires:       texlive-context-visualcounter
Requires:       texlive-jmn
Requires:       texlive-luajittex

%description
Hans Hagen's powerful ConTeXt system, https://pragma-ade.com. Also includes
third-party ConTeXt packages. TeX Live uses the ConTeXt repackaging as
distributed from https://github.com/gucci-on-fleek/context-packaging. See
https://contextgarden.net and https://pragma-ade.com for information about
ConTeXt.#

%package -n texlive-context-animation
Summary:        Generate fieldstack based animation with ConTeXt
Version:        svn75386
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-animation
The package is a port, to Context (mkvi), of the corresponding LaTeX package.

%package -n texlive-context-calendar-examples
Summary:        Collection of calendars based on the PocketDiary-module
Version:        svn66947
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-calendar-examples
The module contains examples for creating calendars based on the
PocketDiary-module in various page sizes. In this collection there are the
following examples: Year calendar with 1 day per page Year calendar with 1 week
per two facing pages Menu-Calendar for each week of the year Sun data and moon
data calendar for the whole year Photo calendar

%package -n texlive-context-chat
Summary:        Typeset messenger chats with ConTEXt
Version:        svn72010
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-chat
A simplified way to typeset a digital chat between characters.

%package -n texlive-context-collating-marks
Summary:        Environment to place collating marks on the spine of a section
Version:        svn68696
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-collating-marks
This module provides a possibility to place collating marks on the spines of
sections when using imposition. Placing collating marks is a method to make the
correct sequence of sections of a book block visible.

%package -n texlive-context-cyrillicnumbers
Summary:        Write numbers as cyrillic glyphs
Version:        svn47085
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-cyrillicnumbers
The package extends ConTeXt's system of number conversion, by adding numeration
using cyrillic letters.

%package -n texlive-context-filter
Summary:        Run external programs on the contents of a start-stop environment
Version:        svn62070
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-filter
The filter module provides a simple interface to run external programs on the
contents of a start-stop environment. Options are available to run the external
program only if the content of the environment has changed, to specify how the
program output should be read back, and to choose the name of the temporary
files that are created. The module is compatible with both MkII and MkIV.

%package -n texlive-context-gnuplot
Summary:        Inclusion of Gnuplot graphs in ConTeXt
Version:        svn75301
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-gnuplot
Enables simple creation and inclusion of graphs with Gnuplot. The package
writes a script into temporary file, runs Gnuplot and includes the resulting
graphic directly into the document. See the ConTeXt Garden package page for
further details.

%package -n texlive-context-handlecsv
Summary:        Data merging for automatic document creation
Version:        svn76721
License:        GPL-3.0-only
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(t-handlecsv.tex) = %{tl_version}

%description -n texlive-context-handlecsv
The package handles csv data merging for automatic document creation.

%package -n texlive-context-letter
Summary:        ConTeXt package for writing letters
Version:        svn60787
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-letter
A means of writing 'vanilla' letters and memos is provided, with support
covering ConTeXt Mkii and Mkiv. The design of letters may be amended by a wide
range of style specifications.

%package -n texlive-context-mathsets
Summary:        Set notation in ConTeXt
Version:        svn47085
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(t-mathsets.tex) = %{tl_version}

%description -n texlive-context-mathsets
Typeset good-looking set notation (e.g., {x|x \in Y}), as well as similar
things such as Dirac bra-ket notation, conditional probabilities, etc. The
package is at least inspired by braket.

%package -n texlive-context-notes-zh-cn
Summary:        A ConTeXt LMTX introduction for Chinese users
Version:        svn76286
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-context-notes-zh-cn-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-context-notes-zh-cn-doc <= 11:%{version}
Requires:       texlive-context

%description -n texlive-context-notes-zh-cn
An introductory tutorial on ConTeXt, in Chinese. The document covers ConTeXt
installation, fonts, layout design, cross-reference, project structure, metafun
and presentation design.

%package -n texlive-context-pocketdiary
Summary:        A personal organiser
Version:        svn73164
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-pocketdiary
PocketDiary is a calendar module, enabling to prepare various calendars from
day- to week, month- and year-calendars based on the ideas contained in
PocketMods, having 8 pages arranged on a A4 single-sided printed sheet of
paper. The module comes with different templates for notes etc. The module
provides sun and moon data calculations

%package -n texlive-context-simpleslides
Summary:        A module for preparing presentations
Version:        svn67070
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(s-simpleslides-BigNumber.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BlackBoard.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BottomSquares.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Boxed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BoxedTitle.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Ellipse.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Embossed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Framed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FramedTitle.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FuzzyFrame.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FuzzyTopic.tex) = %{tl_version}
Provides:       tex(s-simpleslides-HorizontalStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-NarrowStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-PlainCounter.tex) = %{tl_version}
Provides:       tex(s-simpleslides-RainbowStripe.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Rounded.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Shaded.tex) = %{tl_version}
Provides:       tex(s-simpleslides-SideSquares.tex) = %{tl_version}
Provides:       tex(s-simpleslides-SideToc.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Split.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Sunrise.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Swoosh.tex) = %{tl_version}
Provides:       tex(s-simpleslides-ThickStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-default.tex) = %{tl_version}

%description -n texlive-context-simpleslides
This ConTeXt module provides an easy-to-use interface for creating
presentations for use with a digital projector. The presentations are not
interactive (no buttons, hyperlinks or navigational tools such as tables of
contents). Graphics may be mixed with the text of slides. The module provides
several predefined styles, designed for academic presentation. Most styles are
configurable, and it is easy to design new styles.

%package -n texlive-context-squares
Summary:        Typesetting Magic and Latin squares
Version:        svn70128
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-squares
The package provides typesetting of magic and latin squares.

%package -n texlive-context-sudoku
Summary:        Sudokus for ConTeXt
Version:        svn76924
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-sudoku
A port of Peter Norvig's sudoku solver to Lua/ConTeXt. It provides four basic
commands for typesetting sudokus, as well as a command handler.

%package -n texlive-context-transliterator
Summary:        Transliterate text from 'other' alphabets
Version:        svn61127
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Provides:       tex(t-transliterator.tex) = %{tl_version}

%description -n texlive-context-transliterator
The package will read text in one alphabet, and provide a transliterated
version in another; this is useful for readers who cannot read the original
alphabet. The package can make allowance for hyphenation.

%package -n texlive-context-typescripts
Summary:        Small modules to load various fonts for use in ConTeXt
Version:        svn76524
License:        GPL-3.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-typescripts
The package provides files offering interfaces to 33 publicly available fonts
(or collections of fonts from the same foundry); each is available in a .mkii
and a .mkiv version.

%package -n texlive-context-vim
Summary:        Generate ConTeXt syntax highlighting code from vim
Version:        svn62071
License:        BSD-3-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context
Requires:       texlive-context-filter
Provides:       tex(t-vim.tex) = %{tl_version}

%description -n texlive-context-vim
ConTeXt has excellent pretty printing capabilities for many languages. The code
for pretty printing is written in TeX, and due to catcode juggling, such
verbatim typesetting is perhaps the trickiest part of TeX. This makes it
difficult for a "normal" user to define syntax highlighting rules for a new
language. This module takes the onus of defining syntax highlighting rules away
from the user and uses ViM editor to generate the syntax highlighting. There is
a helper 2context.vim script to do the syntax parsing in ViM.

%package -n texlive-context-visualcounter
Summary:        Visual display of ConTeXt counters
Version:        svn47085
License:        BSD-2-Clause
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-context

%description -n texlive-context-visualcounter
A typical document usually contains many counters: page numbers, section
numbers, itemizations, enumerations, theorems, and so on. This module provides
a visual display for such counters.

%package -n texlive-jmn
Summary:        Special fonts for ConTeXt
Version:        svn45751
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-jmn
special fonts for ConTeXt

%prep
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
tar -xf %{SOURCE26} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE27} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE28} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE29} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE30} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE31} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE32} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE33} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE34} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE35} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE36} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE37} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE38} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE39} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-context-animation
%license gpl3.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-calendar-examples
%license pd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-chat
%license gpl3.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-collating-marks
%license pd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-cyrillicnumbers
%license bsd.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-filter
%license bsd2.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-gnuplot
%license gpl2.txt
%{_texmf_main}/metapost/context/third/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-handlecsv
%license gpl3.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-letter
%license gpl2.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-mathsets
%license bsd2.txt
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-notes-zh-cn
%license fdl.txt
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-pocketdiary
%license pd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-simpleslides
%license gpl2.txt
%{_texmf_main}/scripts/context/lua/
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-squares
%license mit.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-sudoku
%license mit.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-transliterator
%license bsd.txt
%{_texmf_main}/scripts/context/lua/
%{_texmf_main}/tex/context/interface/
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-typescripts
%license gpl3.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-vim
%license bsd.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-context-visualcounter
%license bsd2.txt
%{_texmf_main}/tex/context/third/
%doc %{_texmf_main}/doc/context/third/

%files -n texlive-jmn
%license lppl1.3c.txt
%{_texmf_main}/fonts/afm/jmn/hans/
%{_texmf_main}/fonts/enc/dvips/jmn/
%{_texmf_main}/fonts/map/dvips/jmn/
%{_texmf_main}/fonts/tfm/jmn/hans/
%{_texmf_main}/fonts/type1/jmn/hans/

%changelog
%autochangelog
