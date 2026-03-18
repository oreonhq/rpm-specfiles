# Upstream actually uses a post-release snapshot of commit
# df4d68c09cdef73e023b8838a8bc7ca4dff1d1de “that addresses a missing include
# directive needed in more recent Visual Studio releases;” we should be able to
# get by with the release.
%global antl4_ver 4.13.2

Name:		adobe-afdko
Version:	4.0.3
Release:	3%{?dist}
Summary:	Adobe Font Development Kit for OpenType
# Everything is Apache-2.0 except:
#
# The following would affect the license of a python3-afdko subpackage, which
# we currently don’t have.
#
# - License of afdko-3.6.1/python/afdko/pdflib/pdfgen.py is said to be “same as
#   the Python license,” which would seem to suggest Python-2.0.1, but the
#   license text matches MIT-CMU.
# - Contents of python/afdko/resources/ are derived from adobe-mappings-cmap
#   and share its BSD-3-Clause license.
#
# The following do not affect the licenses of the binary RPMs.
#
# - ExternalAntlr4Cpp.cmake is BSD-3-Clause, as noted in LICENSE.md, but this
#   is a build-system file and does not affect the licenses of the binary RPMs
# - Various fonts and other test data files are OFL-1.1 (and/or
#   OFL-1.0-RFN/OFL-1.0-no-RFN?), but do not contribute to the licenses of the
#   binary RPMs
License:	Apache-2.0
URL:		https://github.com/adobe-type-tools/afdko
Source0:	%{url}/releases/download/%{version}/afdko-%{version}.tar.gz
Source1:	https://www.antlr.org/download/antlr4-cpp-runtime-%{antl4_ver}-source.zip
BuildRequires:	gcc g++
BuildRequires:	cmake
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	utf8cpp-devel
Provides: bundled(antlr4-project) = %{antl4_ver}
%description
Adobe Font Development Kit for OpenType (AFDKO).
The AFDKO is a set of tools for building OpenType font files
from PostScript and TrueType font data.

%prep
%autosetup -p1 -n afdko-%{version}

%build
%set_build_flags
export XFLAGS="${CFLAGS} ${LDFLAGS}"
%cmake \
  -DANTLR4_ZIP_REPOSITORY:PATH=%{SOURCE1}
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%doc docs/ README.md NEWS.md
%{_bindir}/detype1
%{_bindir}/makeotfexe
%{_bindir}/mergefonts
%{_bindir}/rotatefont
%{_bindir}/sfntdiff
%{_bindir}/sfntedit
%{_bindir}/spot
%{_bindir}/tx
%{_bindir}/type1

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.3-3
- Prepare for Oreon 11 (RP1)
