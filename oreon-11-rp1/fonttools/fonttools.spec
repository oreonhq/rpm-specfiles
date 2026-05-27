%global source0_hash 9207dc3e2a8e3212986b1cdbe0696f6cebcf1a1d6de93cce11c2d85afb2a35dc

%bcond tests 1

# Some extras are disabled in RHEL to avoid bringing in additional
# dependencies.
#
# Requires python-lz4:
%bcond graphite_extra %[ %{undefined rhel} || %{defined epel} ]
# Requires python-skia-pathops, not packaged:
%bcond pathops_extra 0
# Requires python-matplotlib:
%bcond plot_extra %[ %{undefined rhel} || %{defined epel} ]
# Requires python-uharfbuzz, currently only in F42+
%bcond repacker_extra %[ 0%{?fedora} > 41 ]
# Requires python-sympy (not yet in any EPEL):
%bcond symfont_extra %{undefined rhel}
# Required python-fs till 4.58.0 release
%bcond ufo_extra %[ %{undefined rhel} || %{defined epel} ]
# Requires python-unicodedata2 (depending on python version):
%bcond unicode_extra %[ %{undefined rhel} || %{defined epel} ]
# Requires python-brotli, python-zopfli:
%bcond woff_extra %[ %{undefined rhel} || %{defined epel} ]
# Requires scipy, munkres, pycairo
%bcond interpolatable_extra 1


%global desc %{expand:
fontTools is a library for manipulating fonts, written in Python. The project
includes the TTX tool, that can convert TrueType and OpenType fonts to and from
an XML text format, which is also called TTX. It supports TrueType, OpenType,
AFM and to an extent Type 1 and some Mac-specific formats.}

Name:           fonttools
Version:        4.62.1
Release:        1%{?dist}
Summary:        Tools to manipulate font files

# https://spdx.org/licenses/MIT.html
License:        MIT
URL:            https://github.com/fonttools/fonttools/
Source:        https://github.com/fonttools/fonttools//archive/4.62.1/fonttools-4.62.1.tar.gz

Requires:       python3-fonttools = %{version}-%{release}
Provides:       ttx = %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  gcc

%if %{with tests}
# A few additional requirements for specific tests, noted in requirements.txt:
BuildRequires:  %{py3_dist pytest}
# Not included in RHEL, but available in EPEL:
%if %{undefined rhel} || %{defined epel}
BuildRequires:  %{py3_dist pytest-randomly}
%endif
# For Tests/cu2qu/{ufo,cli}_test.py
# Not yet in EPEL10:
%if %{undefined rhel} || (%{defined epel} && !%{defined el10})
BuildRequires:  %{py3_dist ufoLib2}
%endif
# Not yet in any EPEL:
%if %{undefined rhel}
BuildRequires:  %{py3_dist ufo2ft}
%endif

# For Tests/pens/freetypePen_test.py
%if %{undefined rhel} || (%{defined epel} && !%{defined el10})
BuildRequires:  %{py3_dist freetype-py}
%global have_freetype_py 1
%endif

# For Tests/varLib/interpolatable_test.py
# Not yet in any EPEL:
%if %{undefined rhel}
BuildRequires:  %{py3_dist glyphsLib}
%endif
%endif

%description %{desc}

%package -n python3-fonttools
Summary:        Python 3 fonttools library

# From 3.31.0 and on, python3-fonttools incorporated the ufolib project under fontTools.ufoLib
# python-ufolib has been retired and fontTools.ufoLib should be used instead.
# See https://github.com/fonttools/fonttools/releases/tag/3.31.0 for further reference
Obsoletes: python3-ufolib <= 2.1.1-11

%description -n python3-fonttools %{desc}

# Cannot package “all” extra unless dependencies for all individual extras
# become satisfiable.
%if %{with graphite_extra}
%pyproject_extras_subpkg -n python3-fonttools graphite
%endif
%if %{with interpolatable_extra}
%pyproject_extras_subpkg -n python3-fonttools interpolatable
%endif
%pyproject_extras_subpkg -n python3-fonttools lxml
%if %{with pathops_extra}
%pyproject_extras_subpkg -n python3-fonttools pathops
%endif
%if %{with plot_extra}
%pyproject_extras_subpkg -n python3-fonttools plot
%endif
%if %{with repacker_extra}
%pyproject_extras_subpkg -n python3-fonttools repacker
%endif
%if %{with symfont_extra}
%pyproject_extras_subpkg -n python3-fonttools symfont
%endif
%pyproject_extras_subpkg -n python3-fonttools type1
%if %{with ufo_extra}
%pyproject_extras_subpkg -n python3-fonttools ufo
%endif
%if %{with unicode_extra}
%pyproject_extras_subpkg -n python3-fonttools unicode
%endif
%if %{with woff_extra}
%pyproject_extras_subpkg -n python3-fonttools woff
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# Remove shebang
sed -r -i '1{/^#!/d}' Lib/fontTools/mtiLib/__init__.py

%generate_buildrequires
export FONTTOOLS_WITH_CYTHON=1
# We use tox to get things like pytest, but we add extras manually since not
# all dependencies from requirements.txt might be satisfiable and not all
# extras might be packaged; plus, requirements.txt pins exact versions.
%{pyproject_buildrequires \
    %{?with_graphite_extra:-x graphite} \
    %{?with_interpolatable_extra:-x interpolatable} \
    -x lxml \
    %{?with_pathops_extra:-x pathops} \
    %{?with_plot_extra:-x plot} \
    %{?with_repacker_extra:-x repacker} \
    %{?with_symfont_extra:-x symfont} \
    -x type1 \
    %{?with_ufo_extra:-x ufo} \
    %{?with_unicode_extra:-x unicode} \
    %{?with_woff_extra:-x woff} \
    }

%build
export FONTTOOLS_WITH_CYTHON=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fontTools

%check
# - fontTools.misc.symfont requires python3dist(sympy), i.e., the symfont extra
# - fontTools.pens.freetypePen requires python3dist(freetype-py)
# - fontTools.pens.quartzPen only works on Darwin
# - fontTools.pens.reportLabPen requires python3dist(reportlab), and it is not
#   worth adding the BuildRequires just for the import check
# - fontTools.ttLib.removeOverlaps requires python3dist(skia-pathops), i.e., the
#   pathops extra
# - fontTools.ufoLib(.*) requires python3dist(fs), i.e., the ufo extra
# - fontTools.varLib.plot requires python3dist(matplotlib), i.e., the plot
#   extra
%{pyproject_check_import \
    %{?!with_symfont_extra:-e fontTools.misc.symfont} \
    %{?!have_freetype_pen:-e fontTools.pens.freetypePen} \
    -e fontTools.pens.quartzPen \
    -e fontTools.pens.reportLabPen \
    %{?!with_pathops_extra:-e fontTools.ttLib.removeOverlaps} \
    %{?!with_ufo_extra:-e fontTools.ufoLib*} \
    %{?!with_plot_extra:-e fontTools.varLib.plot} \
    %{?!with_interpolatable_extra:-e fontTools.varLib.interpolatable*} \
    %{nil}}

%if %{with tests}
%if %{without ufo_extra}
# These tests pertain to the interpolatable extra, but also require the ufo
# extra (even though the interpolatable extra as a whole does not):
k="${k-}${k+ and }not (InterpolatableTest and test_designspace)"
k="${k-}${k+ and }not (InterpolatableTest and test_interpolatable_ufo)"
k="${k-}${k+ and }not (InterpolatableTest and test_sparse_designspace)"
k="${k-}${k+ and }not (InterpolatableTest and test_sparse_interpolatable_ufos)"
%endif

# Below test is randomly failing on any arch, mostly the arch on which build runs
k="${k-}${k+ and }not (test_ttcompile_timestamp_calcs)"

%pytest ${ignore-} -k "${k-}" -rs -v
%endif

%files
%{_bindir}/pyftmerge
%{_bindir}/pyftsubset
%{_bindir}/ttx
%{_bindir}/fonttools
%{_mandir}/man1/ttx.1*

%files -n python3-fonttools -f %{pyproject_files}
%doc NEWS.rst README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.62.1-1
- Prepare for Oreon 11 (RP1)
