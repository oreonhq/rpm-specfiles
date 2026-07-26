%global source0_hash 5808fffa0e66f571fd37f7a46cd4d99c0e897add86bbdc85a0666a18804bdc10

%global npm_name replace-require-self
%global enable_tests 1

Name:		nodejs-replace-require-self
Version:	1.1.1
Release:	22%{?dist}
Summary:	Require($THIS_PACKAGE) -> require('./')

License:	MIT
URL:		https://github.com/kemitchell/replace-require-self.js.git
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-devel

%description
Require($THIS_PACKAGE) -> require('./')

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/cli.js \
    %{buildroot}%{_bindir}/replace-require-self

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[102m -=#=- No test suite -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/replace-require-self

%changelog
%autochangelog
