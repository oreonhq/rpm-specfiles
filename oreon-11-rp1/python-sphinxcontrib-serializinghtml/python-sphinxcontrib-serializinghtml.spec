%bcond tests 1

Name:           python-sphinxcontrib-serializinghtml
Version:        2.0.0
Release:        %autorelease
Summary:        Sphinx extension for serialized HTML
License:        BSD-2-Clause
URL:            http://sphinx-doc.org/
Source:         %{pypi_source sphinxcontrib_serializinghtml}
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}-devel


%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).


%package -n     python%{python3_pkgversion}-sphinxcontrib-serializinghtml
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sphinxcontrib-serializinghtml
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).


%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -x test, -x standalone}


%prep
%autosetup -n sphinxcontrib_serializinghtml-%{version}
find -name '*.mo' -delete


%build
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done
%pyproject_wheel


%install
%pyproject_install

# Move language files to /usr/share
pushd %{buildroot}%{python3_sitelib}
for lang in `find sphinxcontrib/serializinghtml/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/serializinghtml/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/serializinghtml/locales
ln -s %{_datadir}/locale sphinxcontrib/serializinghtml/locales
popd


%find_lang sphinxcontrib.serializinghtml


%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-sphinxcontrib-serializinghtml -f sphinxcontrib.serializinghtml.lang
%license LICENCE.rst
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_serializinghtml-%{version}.dist-info/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
