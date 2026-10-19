%global source0_hash d24a53448ba6ce491b383adcce772d6fddb94fbadbcdc5944f9c1a0cae7d2ea9
Name:           python-cucumber-tag-expressions
Version:        11.0.1
Release:        1%{?dist}
Summary:        Provides a tag-expression parser and evaluation logic for cucumber/behave
License:        MIT
URL:            https://github.com/cucumber/tag-expressions
Source0:        https://github.com/cucumber/tag-expressions/archive/v%{version}/tag-expressions-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Cucumber tag-expressions provide readable boolean expressions to select
features and scenarios marked with tags in Gherkin files in an easy way.}
# oreon:deps
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  tomcli
# /oreon:deps
%description %{common_description}

%package -n python3-cucumber-tag-expressions
Summary:        Provides a tag-expression parser and evaluation logic for cucumber/behave
%description -n python3-cucumber-tag-expressions %{common_description}

%prep

%autosetup -p1
# Python: Do not upper-bound (SemVer-bound) the version of uv_build; we must
# work with what we have, and compatibility across SemVer boundaries is quite
# good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' python/pyproject.toml

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
cd python
%install -p
install -t '%{buildroot}%{_pkgdocdir}/general' -p -m 0644 -D \
    ARCHITECTURE.md CHANGELOG.md README.md
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 -D python/README.md
%oreon_autofiles python3-cucumber-tag-expressions usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest python/tests -v
%files -f %{oreon_filedir}/main.list
%files -n python3-cucumber-tag-expressions -f %{oreon_filedir}/python3-cucumber-tag-expressions.list

%changelog

%autochangelog
