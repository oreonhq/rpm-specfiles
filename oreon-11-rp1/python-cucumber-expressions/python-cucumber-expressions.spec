%global source0_hash 2d16f1abf7c2a384f46ee87b8ef3a1017023aa83bc542fdac936aa586afb63a9
Name:           python-cucumber-expressions
Version:        20.1.0
Release:        1%{?dist}
Summary:        Cucumber Expressions - a simpler alternative to Regular Expressions
License:        MIT
URL:            https://github.com/cucumber/cucumber-expressions
Source0:        https://github.com/cucumber/cucumber-expressions/archive/v%{version}/cucumber-expressions-%{version}.tar.gz
Patch:          0001-Downstream-only-remove-the-upper-bound-on-the-versio.patch
BuildArch:      noarch
%global common_description %{expand:
Cucumber Expressions is an alternative to Regular Expressions with a more
intuitive syntax.}
# oreon:deps
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
# /oreon:deps
%description %{common_description}

%package -n python3-cucumber-expressions
Summary:        Cucumber Expressions - a simpler alternative to Regular Expressions
%description -n python3-cucumber-expressions %{common_description}

%build -p

cd python
%install -p
install -t '%{buildroot}%{_pkgdocdir}/general' -p -m 0644 -D \
    ARCHITECTURE.md CHANGELOG.md README.md
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 -D python/README.md
%oreon_autofiles python3-cucumber-expressions usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%prep
%oreon_prep
%check

%pytest python/tests -v
%files -f %{oreon_filedir}/main.list
%files -n python3-cucumber-expressions -f %{oreon_filedir}/python3-cucumber-expressions.list

%changelog

%autochangelog
