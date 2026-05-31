%global source0_hash 411f5d96d445d1d73bb5d52133377b4248ec79db5c793ce7dbe59e074b4dd1ad

%bcond_without tests

Name:           python-sphinxcontrib-devhelp
Version:        2.0.0
Release:        %autorelease
Summary:        Sphinx extension for Devhelp documents
License:        BSD-2-Clause
URL:            http://sphinx-doc.org/
Source:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib-devhelp/sphinxcontrib-devhelp-2.0.0.tar.gz
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}-devel


%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.


%package -n     python%{python3_pkgversion}-sphinxcontrib-devhelp
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sphinxcontrib-devhelp
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.


%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -x test, -x standalone}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n sphinxcontrib_devhelp-%{version}
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
for lang in `find sphinxcontrib/devhelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/devhelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/devhelp/locales
ln -s %{_datadir}/locale sphinxcontrib/devhelp/locales
popd


%find_lang sphinxcontrib.devhelp


%check
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-sphinxcontrib-devhelp -f sphinxcontrib.devhelp.lang
%license LICENCE.rst
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_devhelp-%{version}.dist-info/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
