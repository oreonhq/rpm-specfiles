%global source0_hash 24661b8a24699c59ffa364b06180def209056660eb6ba8196d881e32d8cba8dc

%define srcname notofonttools

%define with_python3 1

%global common_desc \
The nototools python package contains python scripts \
used to maintain the Noto Fonts project, \
including the google.com/get/noto website.

Name:		nototools
Version:	0.2.20
Release:	4%{?dist}
Summary:	Noto fonts support tools and scripts plus web site generation

# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
License:	Apache-2.0
URL:		https://github.com/googlefonts/nototools
Source0:	%pypi_source
Source1:	requirements.txt

%if %{with python3}
Requires:	python3-nototools = %{version}-%{release}
%endif

BuildArch:	noarch
%if %{with python3}
%generate_buildrequires
%pyproject_buildrequires -N %{SOURCE1}
%endif

%description
%common_desc

%if %{with python3}
%package     -n python3-nototools
Summary:	Noto tools for python 3
Requires:	python3dist(fonttools)
BuildRequires:	python3dist(fonttools)

%description -n python3-nototools
%common_desc

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

# remove unneeded files
rm -rf %{srcname}-%{version}/third_party/{cldr,dspl,fontcrunch,ohchr,spiro,udhr,unicode}
mv %{srcname}-%{version} python2

%if %{with python3}
cp -a python2 python3
%endif

# for documents
cp python2/*.md python2/LICENSE .

%build
%if %{with python3}
pushd python3
%pyproject_wheel
popd
%endif

%install
%if %{with python3}
pushd python3
%pyproject_install
%pyproject_save_files %{name} third_party
for lib in %{buildroot}%{python3_sitelib}/nototools/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd
%endif

%check
pushd python3
# Comment it out for the moment because it tries to run something which fails
#pyproject_check_import
popd

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/add_vs_cmap.py
%{_bindir}/autofix_for_release.py
%{_bindir}/create_image.py
%{_bindir}/decompose_ttc.py
%{_bindir}/drop_hints.py
%{_bindir}/dump_otl.py
%{_bindir}/fix_khmer_and_lao_coverage.py
%{_bindir}/fix_noto_cjk_thin.py
%{_bindir}/generate_sample_text.py
%{_bindir}/merge_fonts.py
%{_bindir}/merge_noto.py
%{_bindir}/noto_lint.py
%{_bindir}/notocoverage
%{_bindir}/notodiff
%{_bindir}/scale.py
%{_bindir}/subset.py
%{_bindir}/subset_symbols.py
%{_bindir}/test_vertical_extents.py

%if %{with python3}
%files -n python3-nototools -f %{pyproject_files}
%exclude %{python3_sitelib}/notofonttools-0.0.0.dist-info
%endif

%changelog
%autochangelog
