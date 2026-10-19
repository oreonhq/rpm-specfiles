%global source1_hash 4466c59174263f6f38a8142fd852c9799d3becca22ea6f6a28cbc47d6a2dd5be
%global source0_hash 645cfc3ff6c599fe91d7c7f895bc59acf816d8f37be96dc639aeee9b0251a09b
%{?nodejs_find_provides_and_requires}
%global packagename linefix
%global enable_tests 1
Name:		nodejs-linefix
Version:	0.1.1
Release:        22%{?dist}
Summary:        Recursively repair line endings
License:	MIT
URL:		https://github.com/jhoff/linefix
Source0:        https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/jhoff/linefix/master/LICENSE.txt
BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  npm
# /oreon:deps
%description
Recursively repair line endings

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n package
cp -p %{SOURCE1} .

# fix script interpreter not to use env
sed -i '1!b;s/env node/node/' bin/fix.js

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json bin/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/fix.js %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/fix.js
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/fix.js \
    %{buildroot}%{_bindir}/%{packagename}
%nodejs_symlink_deps
%oreon_autofiles main

%check

%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[103m -=#=- No test suite -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
