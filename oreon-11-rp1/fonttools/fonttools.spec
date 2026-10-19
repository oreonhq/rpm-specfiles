%global source0_hash dcb2ff59d87e63a9c0f0d618210cbac976540b348c04fbcf5b45497561fa8015
%bcond tests 1
%bcond graphite_extra %[ %{undefined rhel} || %{defined epel} ]
%bcond pathops_extra 0
%bcond plot_extra %[ %{undefined rhel} || %{defined epel} ]
%bcond repacker_extra %[ 0%{?fedora} > 41 ]
%bcond symfont_extra %{undefined rhel}
%bcond ufo_extra %[ %{undefined rhel} || %{defined epel} ]
%bcond unicode_extra %[ %{undefined rhel} || %{defined epel} ]
%bcond woff_extra %[ %{undefined rhel} || %{defined epel} ]
%bcond interpolatable_extra 1
%global desc %{expand:
fontTools is a library for manipulating fonts, written in Python. The project
includes the TTX tool, that can convert TrueType and OpenType fonts to and from
an XML text format, which is also called TTX. It supports TrueType, OpenType,
AFM and to an extent Type 1 and some Mac-specific formats.}
Name:           fonttools
Version:        4.66.1
Release:        1%{?dist}
Summary:        Tools to manipulate font files
License:        MIT
URL:            https://github.com/fonttools/fonttools/
Source0:        https://github.com/fonttools/fonttools//archive/refs/tags/4.66.1/fonttools-4.62.1.tar.gz#/fonttools-4.62.1.tar.gz
Requires:       python3-fonttools = %{version}-%{release}
Provides:       ttx = %{version}-%{release}
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fonttools = %{version}-%{release}
# /oreon:deps
%description %{desc}

%package -n python3-fonttools
Summary:        Python 3 fonttools library
Obsoletes: python3-ufolib <= 2.1.1-11
%description -n python3-fonttools %{desc}

# Cannot package “all” extra unless dependencies for all individual extras
# become satisfiable.
%if %{with graphite_extra}
%endif
%if %{with interpolatable_extra}
%endif
%if %{with pathops_extra}
%endif
%if %{with plot_extra}
%endif
%if %{with repacker_extra}
%endif
%if %{with symfont_extra}
%endif
%if %{with ufo_extra}
%endif
%if %{with unicode_extra}
%endif
%if %{with woff_extra}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Remove shebang
sed -r -i '1{/^#!/d}' Lib/fontTools/mtiLib/__init__.py

%build

export FONTTOOLS_WITH_CYTHON=1
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fonttools usr/lib/python3*/site-packages/fonttools* usr/lib64/python3*/site-packages/fonttools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fonttools* usr/lib64/python3*/site-packages/fonttools* usr/bin/*

%check

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
k="${k-}${k+ and }not (InterpolatableTest and test_designspace)"
k="${k-}${k+ and }not (InterpolatableTest and test_interpolatable_ufo)"
k="${k-}${k+ and }not (InterpolatableTest and test_sparse_designspace)"
k="${k-}${k+ and }not (InterpolatableTest and test_sparse_interpolatable_ufos)"
%endif
k="${k-}${k+ and }not (test_ttcompile_timestamp_calcs)"
%pytest ${ignore-} -k "${k-}" -rs -v
%endif
%files
%files -n python3-fonttools -f %{oreon_filedir}/python3-fonttools.list

%changelog

%autochangelog
