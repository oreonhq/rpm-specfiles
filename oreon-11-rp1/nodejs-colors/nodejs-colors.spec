%global source0_hash efb9e25c033cb639d7a99131f522aee8435fcdc54e2f89b7d0cf26f72d2f5889
%{?nodejs_find_provides_and_requires}
%global enable_tests 1
Name:           nodejs-colors
Version:        1.4.0
Release:        1%{?dist}
Summary:        Get colors in your Node.js console
License:        MIT
URL:            https://github.com/Marak/colors.js
Source0:        https://github.com/Marak/colors.js/archive/v%{version}/colors-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  npm
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir colors.js-%{version}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/colors
cp -pr package.json safe.js lib themes/ \
    %{buildroot}%{nodejs_sitelib}/colors
%nodejs_symlink_deps
%oreon_autofiles main
%if 0%{?enable_tests}
%check

%__nodejs tests/basic-test.js && %__nodejs tests/safe-test.js
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
