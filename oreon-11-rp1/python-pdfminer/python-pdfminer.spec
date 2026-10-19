%global source0_hash 39fb0259472276501d9f9d44e83057f1d5ee3eae20a8ad8b5304d1c25ee65433
Name:           python-pdfminer
Version:        20260107
Release:        1%{?dist}
Summary:        Tool for extracting information from PDF documents
License:        %{shrink:
                MIT AND
                LicenseRef-Fedora-Public-Domain AND
                APAFML AND
                BSD-3-Clause AND
                (Apache-2.0 AND MIT) AND
                Adobe-Glyph
                }
URL:            https://github.com/pdfminer/pdfminer.six
Source0:        pdfminer.six-%{version}-filtered.tar.zst
Source1:        get_source.sh
Source2:        dumppdf.1
Source3:        pdf2txt.1
BuildArch:      noarch
%global common_description %{expand:
Pdfminer.six is a community maintained fork of the original PDFMiner. It is a
tool for extracting information from PDF documents. It focuses on getting and
analyzing text data. Pdfminer.six extracts the text from a page directly from
the sourcecode of the PDF. It can also be used to get the exact location, font
or color of the text.
It is built in a modular way such that each component of pdfminer.six can be
replaced easily. You can implement your own interpreter or rendering device
that uses the power of pdfminer.six for other purposes than text analysis.
Check out the full documentation on Read the Docs
(https://pdfminersix.readthedocs.io/).
Features:
  • Written entirely in Python.
  • Parse, analyze, and convert PDF documents.
  • PDF-1.7 specification support. (well, almost).
  • CJK languages and vertical writing scripts support.
  • Various font types (Type1, TrueType, Type3, and CID) support.
  • Support for extracting images (JPG, JBIG2, Bitmaps).
  • Support for various compressions (ASCIIHexDecode, ASCII85Decode, LZWDecode,
    FlateDecode, RunLengthDecode, CCITTFaxDecode)
  • Support for RC4 and AES encryption.
  • Support for AcroForm interactive form extraction.
  • Table of contents extraction.
  • Tagged contents extraction.
  • Automatic layout analysis.}
# oreon:deps
BuildRequires:  adobe-mappings-cmap-devel
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n     python3-pdfminer
Summary:        Tool for extracting information from PDF documents
%py_provides python3-pdfminer-six
Provides:       bundled(python3dist(pymongo))
Provides:       bundled(python3dist(pyhanko))
Obsoletes:      python-pdfminer-doc < 20240706-4
%description -n python3-pdfminer %{common_description}

%prep

%autosetup -p1
# Unbundle cmap data; it will be replaced in %%build.
rm -vf cmaprsrc/* pdfminer/cmap/*

# Remove shebang line in non-script source
sed -r -i '1{/^#!/d}' pdfminer/psparser.py

# Copy the pyHanko license to the top-level directory so it is automatically
# included in the licenses in the installed dist-info directory.
cp -p docs/licenses/LICENSE.pyHanko ./

%build -p

for cmap in Japan1 Korea1 GB1 CNS1
do
  ln -s "%{adobe_mappings_rootpath}/${cmap}/cid2code.txt" \
      "cmaprsrc/cid2code_Adobe_${cmap}.txt"
done
mkdir -p pdfminer/cmap
%{python3} tools/conv_cmap.py -c B5=cp950 -c UniCNS-UTF8=utf-8 \
    pdfminer/cmap Adobe-CNS1 cmaprsrc/cid2code_Adobe_CNS1.txt
%{python3} tools/conv_cmap.py -c GBK-EUC=cp936 -c UniGB-UTF8=utf-8 \
    pdfminer/cmap Adobe-GB1 cmaprsrc/cid2code_Adobe_GB1.txt
%{python3} tools/conv_cmap.py -c RKSJ=cp932 -c EUC=euc-jp \
    -c UniJIS-UTF8=utf-8 \
    pdfminer/cmap Adobe-Japan1 cmaprsrc/cid2code_Adobe_Japan1.txt
%{python3} tools/conv_cmap.py -c KSC-EUC=euc-kr -c KSC-Johab=johab \
    -c KSCms-UHC=cp949 -c UniKS-UTF8=utf-8 \
    pdfminer/cmap Adobe-Korea1 cmaprsrc/cid2code_Adobe_Korea1.txt
echo '*pyproject*' >> .gitignore
git add -A
git commit -m 'Imitate upstream release %{version}'
git tag '%{version}'
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE2}' '%{SOURCE3}'
%py3_shebang_fix '%{buildroot}%{_bindir}'
for script in pdf2txt dumppdf
do
  ln -sf "${script}.py" "%{buildroot}%{_bindir}/${script}"
done
%oreon_autofiles python3-pdfminer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

k="${k-}${k+ and }not TestColorSpace"
k="${k-}${k+ and }not TestDumpImages"
k="${k-}${k+ and }not TestDumpPDF"
k="${k-}${k+ and }not TestExtractPages"
k="${k-}${k+ and }not TestExtractText"
k="${k-}${k+ and }not TestOpenFilename"
k="${k-}${k+ and }not TestPdf2Txt"
k="${k-}${k+ and }not TestPdfDocument"
k="${k-}${k+ and }not TestPdfPage"
k="${k-}${k+ and }not test_cmap_font_12"
k="${k-}${k+ and }not test_font_size"
k="${k-}${k+ and }not test_paint_path_quadrilaterals"
k="${k-}${k+ and }not test_pdf_with_empty_characters_horizontal"
k="${k-}${k+ and }not test_pdf_with_empty_characters_vertical"
k="${k-}${k+ and }not (TestPaintPath and test_linewidth)"
ignore="${ignore-} --ignore=tests/test_tools_dumppdf.py"
ignore="${ignore-} --ignore=tests/test_tools_pdf2txt.py"
%pytest -k "${k-}" ${ignore-}
%files -f %{oreon_filedir}/main.list
%files -n python3-pdfminer -f %{oreon_filedir}/python3-pdfminer.list

%changelog

%autochangelog
